#!/usr/bin/env python3
"""
editar_video.py — Gerador de pílulas de vídeo para análise de desempenho esportivo.

Cada clipe segue 3 etapas:
  1. Abertura em velocidade normal — bloco centralizado no topo com animação de slide
  2. Análise no momento-chave: câmera lenta ou freeze + grafismos (com tracking opcional)
  3. Replay completo em velocidade normal

Uso:
    python editar_video.py config.json
    python editar_video.py config.json --saida pasta_saida
    python editar_video.py config.json --clipe nome_do_clipe
"""

import json
import math
import os
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips
import moviepy.video.fx.all as vfx


# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTES
# ─────────────────────────────────────────────────────────────────────────────

_CORES_TIPO = {
    "acerto": {
        "primaria":   (0, 210, 0),
        "secundaria": (30, 100, 255),
    },
    "ajuste": {
        "primaria":   (255, 190, 0),
        "secundaria": (255, 130, 0),
    },
}

_TEXTO_FG        = (255, 255, 255)
_ESPESSURA       = 4
_SETA_SIZE       = 22
_DASH            = 20
_GAP             = 10
_MAX_DESL_FRAME  = 50   # pixels máximos por frame antes de rejeitar salto do tracker

_FONTES_TTF = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/calibrib.ttf",
]


# ─────────────────────────────────────────────────────────────────────────────
# UTILIDADES
# ─────────────────────────────────────────────────────────────────────────────

def ts(valor) -> float:
    """Converte 'HH:MM:SS.mmm' ou número para segundos float."""
    if isinstance(valor, (int, float)):
        return float(valor)
    partes = str(valor).strip().split(":")
    s = 0.0
    for p in partes:
        s = s * 60 + float(p)
    return s


def _carregar_fonte(tamanho: int) -> ImageFont.ImageFont:
    for caminho in _FONTES_TTF:
        if os.path.exists(caminho):
            try:
                return ImageFont.truetype(caminho, tamanho)
            except Exception:
                continue
    return ImageFont.load_default()


def _f2p(frame: np.ndarray) -> Image.Image:
    return Image.fromarray(frame.astype("uint8"), "RGB")


def _p2f(img: Image.Image) -> np.ndarray:
    return np.array(img.convert("RGB"))


def _smoothstep(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return x * x * (3.0 - 2.0 * x)


def _calcular_animacao(t: float, dur: float,
                       fade: float = 0.5) -> Tuple[int, float]:
    """
    Retorna (alfa 0-255, slide_pct 0.0-1.0).
    slide_pct=0 → bloco na posição final; slide_pct=1 → bloco acima da tela.
    """
    if dur <= 0 or t >= dur or t < 0:
        return (0, 1.0)
    if t < fade:
        p = _smoothstep(t / fade)
    elif t > dur - fade:
        p = _smoothstep((dur - t) / fade)
    else:
        p = 1.0
    return (int(255 * p), 1.0 - p)


# ─────────────────────────────────────────────────────────────────────────────
# PRIMITIVOS DE GRAFISMO
# ─────────────────────────────────────────────────────────────────────────────

def desenhar_circulo(frame: np.ndarray, x: int, y: int, raio: int,
                     cor: Tuple, espessura: int = _ESPESSURA) -> np.ndarray:
    img = _f2p(frame)
    ImageDraw.Draw(img).ellipse(
        [x - raio, y - raio, x + raio, y + raio],
        outline=cor, width=espessura,
    )
    return _p2f(img)


def _pontos_arrowhead(x1: float, y1: float, x2: float, y2: float,
                      tamanho: float = _SETA_SIZE) -> List[Tuple]:
    angulo = math.atan2(y2 - y1, x2 - x1)
    return [
        (x2, y2),
        (x2 - math.cos(angulo + 0.45) * tamanho,
         y2 - math.sin(angulo + 0.45) * tamanho),
        (x2 - math.cos(angulo - 0.45) * tamanho,
         y2 - math.sin(angulo - 0.45) * tamanho),
    ]


def desenhar_seta(frame: np.ndarray, x1: int, y1: int, x2: int, y2: int,
                  cor: Tuple, espessura: int = _ESPESSURA) -> np.ndarray:
    img = _f2p(frame)
    d = ImageDraw.Draw(img)
    d.line([(x1, y1), (x2, y2)], fill=cor, width=espessura)
    d.polygon(_pontos_arrowhead(x1, y1, x2, y2), fill=cor)
    return _p2f(img)


def desenhar_seta_tracejada(frame: np.ndarray, x1: int, y1: int,
                             x2: int, y2: int,
                             cor: Tuple, espessura: int = _ESPESSURA) -> np.ndarray:
    img = _f2p(frame)
    d = ImageDraw.Draw(img)
    dist = math.hypot(x2 - x1, y2 - y1)
    if dist == 0:
        return frame
    ux, uy = (x2 - x1) / dist, (y2 - y1) / dist
    pos, desenhando = 0.0, True
    while pos < dist:
        prox = min(pos + (_DASH if desenhando else _GAP), dist)
        if desenhando:
            d.line(
                [(x1 + ux * pos, y1 + uy * pos),
                 (x1 + ux * prox, y1 + uy * prox)],
                fill=cor, width=espessura,
            )
        pos, desenhando = prox, not desenhando
    d.polygon(_pontos_arrowhead(x1, y1, x2, y2), fill=cor)
    return _p2f(img)


def desenhar_zona(frame: np.ndarray, pontos: List, cor: Tuple,
                  alfa: int = 80) -> np.ndarray:
    img = _f2p(frame).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(overlay).polygon(
        [(p[0], p[1]) for p in pontos],
        fill=(*cor[:3], alfa),
    )
    return _p2f(Image.alpha_composite(img, overlay))


def _aplicar_grafismos_estaticos(frame: np.ndarray, grafismos: List,
                                  cor: Tuple) -> np.ndarray:
    for g in grafismos:
        tipo = g["tipo"]
        if tipo == "circulo":
            frame = desenhar_circulo(frame, g["x"], g["y"], g["raio"], cor)
        elif tipo == "seta":
            frame = desenhar_seta(frame, g["x1"], g["y1"], g["x2"], g["y2"], cor)
        elif tipo == "seta_tracejada":
            frame = desenhar_seta_tracejada(
                frame, g["x1"], g["y1"], g["x2"], g["y2"], cor,
            )
        elif tipo == "zona":
            frame = desenhar_zona(frame, g["pontos"], cor)
    return frame


# ─────────────────────────────────────────────────────────────────────────────
# BLOCO DE LEGENDA — TOPO CENTRALIZADO COM CANTOS ARREDONDADOS
# ─────────────────────────────────────────────────────────────────────────────

_BLOCO_MARGIN_TOP  = 30    # distância da borda superior do frame
_BLOCO_PAD_H       = 24    # padding horizontal interno
_BLOCO_PAD_V       = 18    # padding vertical interno
_BLOCO_CORNER      = 18    # raio dos cantos arredondados
_BLOCO_ACCENT_W    = 7     # largura da faixa colorida esquerda
_BADGE_RAIO        = 22    # raio do círculo badge


def _renderizar_bloco_topo(frame: np.ndarray, texto: str,
                            tipo: str, alfa: int,
                            slide_pct: float = 0.0,
                            mostrar_badge: bool = True) -> np.ndarray:
    """
    Desenha um bloco com cantos arredondados, centralizado no topo.
    slide_pct: 0.0 = posição final visível, 1.0 = acima da tela (oculto).
    alfa: 0-255 controla opacidade global do bloco.
    """
    if alfa <= 0:
        return frame

    h_frame, w_frame = frame.shape[:2]
    cor_primaria = _CORES_TIPO[tipo]["primaria"]
    font_size = 46 if mostrar_badge else 40
    fonte = _carregar_fonte(font_size)

    # Medir texto numa imagem temporária
    _tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bb = _tmp.textbbox((0, 0), texto, font=fonte)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]

    # Dimensões do bloco
    badge_space = (_BADGE_RAIO * 2 + 14) if mostrar_badge else 0
    bloco_h = max(th + _BLOCO_PAD_V * 2, _BADGE_RAIO * 2 + _BLOCO_PAD_V * 2, 76)
    conteudo_w = (_BLOCO_ACCENT_W + 16 + badge_space + tw
                  + _BLOCO_PAD_H * 2 + 20)
    bloco_w = min(conteudo_w, int(w_frame * 0.85))
    bloco_x = (w_frame - bloco_w) // 2

    # Posição vertical animada (slide de cima para baixo)
    y_final  = _BLOCO_MARGIN_TOP
    y_oculto = -bloco_h
    bloco_y  = int(y_oculto + (y_final - y_oculto) * (1.0 - slide_pct))

    # Overlay RGBA do mesmo tamanho do frame
    overlay = Image.new("RGBA", (w_frame, h_frame), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    bx, by, bx2, by2 = bloco_x, bloco_y, bloco_x + bloco_w, bloco_y + bloco_h
    r = _BLOCO_CORNER

    # Fundo principal — rounded rect escuro
    d.rounded_rectangle([bx, by, bx2, by2], radius=r, fill=(20, 20, 20, 230))

    # Faixa colorida esquerda (simula accent: rounded_rect estreito + rect para preencher o gap)
    accent_right = bx + _BLOCO_ACCENT_W + r
    d.rounded_rectangle(
        [bx, by, accent_right, by2],
        radius=r,
        fill=(*cor_primaria[:3], 230),
    )
    d.rectangle(
        [bx + r, by, accent_right, by2],
        fill=(*cor_primaria[:3], 230),
    )

    # Ponto de início do conteúdo (após accent)
    conteudo_x = bx + _BLOCO_ACCENT_W + r + 14

    # Badge circular com símbolo
    if mostrar_badge:
        badge_cx = conteudo_x + _BADGE_RAIO
        badge_cy = by + bloco_h // 2
        d.ellipse(
            [badge_cx - _BADGE_RAIO, badge_cy - _BADGE_RAIO,
             badge_cx + _BADGE_RAIO, badge_cy + _BADGE_RAIO],
            fill=(*cor_primaria[:3], 240),
        )
        simbolo = "✓" if tipo == "acerto" else "!"
        fonte_badge = _carregar_fonte(20)
        sbb = d.textbbox((0, 0), simbolo, font=fonte_badge)
        stw, sth = sbb[2] - sbb[0], sbb[3] - sbb[1]
        d.text(
            (badge_cx - stw // 2, badge_cy - sth // 2),
            simbolo, font=fonte_badge, fill=(255, 255, 255, 255),
        )
        texto_x = badge_cx + _BADGE_RAIO + 14
    else:
        texto_x = conteudo_x

    # Texto principal
    texto_y = by + (bloco_h - th) // 2
    d.text((texto_x, texto_y), texto, font=fonte, fill=(255, 255, 255, 255))

    # Aplicar alfa global ao overlay (fade)
    if alfa < 255:
        r_ch, g_ch, b_ch, a_ch = overlay.split()
        a_ch = a_ch.point(lambda v: int(v * alfa / 255))
        overlay = Image.merge("RGBA", (r_ch, g_ch, b_ch, a_ch))

    img = _f2p(frame).convert("RGBA")
    img = Image.alpha_composite(img, overlay)
    return _p2f(img.convert("RGB"))


# ─────────────────────────────────────────────────────────────────────────────
# CLOSURES DE OVERLAY
# ─────────────────────────────────────────────────────────────────────────────

def _fn_abertura(tipo: str, label: str, dur_label: float):
    """
    Legenda inicial: bloco no topo com animação de slide-down + fade.
    Assinatura: (get_frame, t) → frame
    """
    if label.upper().startswith(("ACERTO:", "AJUSTE:")):
        texto = label
    else:
        prefix = "ACERTO: " if tipo == "acerto" else "AJUSTE: "
        texto = prefix + label

    def fn(get_frame, t):
        frame = get_frame(t)
        if t > dur_label:
            return frame
        alfa, slide_pct = _calcular_animacao(t, dur_label, fade=0.5)
        return _renderizar_bloco_topo(frame, texto, tipo, alfa,
                                      slide_pct=slide_pct, mostrar_badge=True)

    return fn


def _fn_analise_estatico(grafismos: List, cor: Tuple,
                          legenda: str, tipo: str):
    """
    Legenda de análise estática (sem tracking): grafismos + bloco no topo.
    Assinatura: frame → frame  (para fl_image)
    """
    def fn(frame: np.ndarray) -> np.ndarray:
        frame = _aplicar_grafismos_estaticos(frame, grafismos, cor)
        if legenda:
            frame = _renderizar_bloco_topo(frame, legenda, tipo,
                                           alfa=240, slide_pct=0.0,
                                           mostrar_badge=False)
        return frame

    return fn


def _fn_analise_com_tracking(grafismos: List, cor: Tuple,
                               legenda: str, tipo: str,
                               tracked: Dict[int, Tuple[int, int]],
                               fps_source: float, vel_slow: float,
                               pos_inicial: Tuple[int, int]):
    """
    Legenda de análise com grafismos animados (tracking).
    seta_tracking: seta com dx/dy relativo ao centro do jogador rastreado.
    Assinatura: (get_frame, t) → frame  (para fl)
    """
    def fn(get_frame, t):
        frame = get_frame(t)

        # Mapeia tempo de output → frame do source
        k = int(t * vel_slow * fps_source)
        pos = tracked.get(k, pos_inicial)

        for g in grafismos:
            gtype = g["tipo"]
            if gtype == "circulo_tracking":
                frame = desenhar_circulo(frame, pos[0], pos[1], g["raio"], cor)
            elif gtype == "seta_tracking":
                x2 = pos[0] + int(g.get("dx", 0))
                y2 = pos[1] + int(g.get("dy", 0))
                frame = desenhar_seta(frame, pos[0], pos[1], x2, y2, cor)
            elif gtype == "seta_alvo":
                frame = desenhar_seta(
                    frame, pos[0], pos[1],
                    int(g["alvo_x"]), int(g["alvo_y"]),
                    cor,
                )
            elif gtype == "circulo":
                frame = desenhar_circulo(frame, g["x"], g["y"], g["raio"], cor)
            elif gtype == "seta":
                frame = desenhar_seta(
                    frame, g["x1"], g["y1"], g["x2"], g["y2"], cor,
                )
            elif gtype == "seta_tracejada":
                frame = desenhar_seta_tracejada(
                    frame, g["x1"], g["y1"], g["x2"], g["y2"], cor,
                )
            elif gtype == "zona":
                frame = desenhar_zona(frame, g["pontos"], cor)

        if legenda:
            frame = _renderizar_bloco_topo(frame, legenda, tipo,
                                           alfa=240, slide_pct=0.0,
                                           mostrar_badge=False)
        return frame

    return fn


def _fn_replay():
    """Badge 'REPLAY' no canto superior direito nos primeiros 2.5s."""
    def fn(get_frame, t):
        frame = get_frame(t)
        if t < 2.5:
            alfa, slide_pct = _calcular_animacao(t, 2.5, fade=0.3)
            if alfa > 0:
                h_frame, w_frame = frame.shape[:2]
                img = _f2p(frame).convert("RGBA")
                overlay = Image.new("RGBA", (w_frame, h_frame), (0, 0, 0, 0))
                d = ImageDraw.Draw(overlay)
                fonte = _carregar_fonte(30)
                bb = d.textbbox((0, 0), "REPLAY", font=fonte)
                tw, th = bb[2] - bb[0], bb[3] - bb[1]
                pad, margin = 10, 20
                rx = w_frame - tw - pad * 2 - margin
                ry = _BLOCO_MARGIN_TOP
                d.rounded_rectangle(
                    [rx - pad, ry - pad, rx + tw + pad, ry + th + pad],
                    radius=8, fill=(10, 10, 10, 200),
                )
                d.text((rx, ry), "REPLAY", font=fonte, fill=(255, 255, 255, 255))
                if alfa < 255:
                    r_ch, g_ch, b_ch, a_ch = overlay.split()
                    a_ch = a_ch.point(lambda v: int(v * alfa / 255))
                    overlay = Image.merge("RGBA", (r_ch, g_ch, b_ch, a_ch))
                img = Image.alpha_composite(img, overlay)
                frame = _p2f(img.convert("RGB"))
        return frame

    return fn


# ─────────────────────────────────────────────────────────────────────────────
# RASTREAMENTO OPENCV
# ─────────────────────────────────────────────────────────────────────────────

def rastrear_jogador(video_path: str, t_analise: float, t_fim_analise: float,
                     bbox_inicial: List[int]) -> Dict[int, Tuple[int, int]]:
    """
    Rastreia o jogador com CSRT entre t_analise e t_fim_analise.
    Rejeita saltos maiores que _MAX_DESL_FRAME pixels por frame.
    Retorna {frame_idx_relativo: (cx, cy)}.
    """
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_start = int(t_analise * fps)
    frame_end   = int(t_fim_analise * fps)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_start)
    ret, primeiro_frame = cap.read()
    if not ret:
        cap.release()
        return {}

    if hasattr(cv2, "TrackerCSRT_create"):
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = cv2.legacy.TrackerCSRT_create()

    x, y, bw, bh = [int(v) for v in bbox_inicial]
    tracker.init(primeiro_frame, (x, y, bw, bh))

    cx0, cy0 = x + bw // 2, y + bh // 2
    positions: Dict[int, Tuple[int, int]] = {0: (cx0, cy0)}
    ultima_pos = (cx0, cy0)

    total = frame_end - frame_start
    print(f"    [Tracking] Rastreando {total} frames ...")
    for k in range(1, total + 1):
        ret, frame_cv = cap.read()
        if not ret:
            break
        success, bbox = tracker.update(frame_cv)
        if success:
            cx = int(bbox[0] + bbox[2] / 2)
            cy = int(bbox[1] + bbox[3] / 2)
            desl = math.hypot(cx - ultima_pos[0], cy - ultima_pos[1])
            if desl < _MAX_DESL_FRAME:
                ultima_pos = (cx, cy)
            # salto acima do limite: mantém ultima_pos (rejeita o jump)
        positions[k] = ultima_pos

    cap.release()
    print(f"    [Tracking] {len(positions)} posições registradas.")
    return positions


# ─────────────────────────────────────────────────────────────────────────────
# PIPELINE POR CLIPE
# ─────────────────────────────────────────────────────────────────────────────

def processar_clipe(cfg: dict, source: VideoFileClip,
                    source_path: str) -> VideoFileClip:
    nome         = cfg["nome"]
    tipo         = cfg["tipo"]
    label        = cfg["label_abertura"]
    t0           = ts(cfg["inicio"])
    t1           = ts(cfg["fim"])
    t_analise    = ts(cfg["momento_analise"])
    tipo_analise = cfg.get("tipo_analise", "slow_motion")
    vel_slow     = float(cfg.get("velocidade_slow") or 0.5)
    dur_freeze   = float(cfg.get("duracao_freeze") or 2.5)
    janela       = float(cfg.get("janela_analise_segundos") or 2.0)
    grafismos    = cfg.get("grafismos", [])
    legenda      = cfg.get("legenda_analise", "")
    dur_label    = cfg.get("duracao_label", None)

    if tipo not in _CORES_TIPO:
        raise ValueError(f"'{nome}': tipo deve ser 'acerto' ou 'ajuste'")

    cor = _CORES_TIPO[tipo]["primaria"]
    raw = source.subclip(t0, t1)
    dur_clip = t1 - t0
    t_rel = t_analise - t0

    if not (0 < t_rel < dur_clip):
        raise ValueError(
            f"'{nome}': momento_analise deve estar entre inicio e fim"
        )

    if dur_label is None:
        dur_label = min(t_rel, 5.0)   # padrão: 5s (era 3s)

    # ── Etapa 1: Abertura ────────────────────────────────────────────────────
    step1 = raw.subclip(0, t_rel).fl(_fn_abertura(tipo, label, dur_label))

    # ── Detectar grafismos com tracking ──────────────────────────────────────
    tem_tracking = any("tracking" in g.get("tipo", "") for g in grafismos)

    # ── Etapa 2a: Análise ─────────────────────────────────────────────────────
    if tipo_analise == "freeze":
        step2a = raw.to_ImageClip(t=t_rel).set_duration(dur_freeze)
        if tem_tracking:
            g_track = next(g for g in grafismos if "tracking" in g["tipo"])
            bx, by, bw, bh = g_track["bbox_inicial"]
            pos_unica = (bx + bw // 2, by + bh // 2)
            # Converte tracking → estático para freeze frame
            grafismos_freeze = []
            for g in grafismos:
                if g["tipo"] == "circulo_tracking":
                    grafismos_freeze.append({
                        "tipo": "circulo",
                        "x": pos_unica[0], "y": pos_unica[1],
                        "raio": g["raio"],
                    })
                elif g["tipo"] == "seta_tracking":
                    grafismos_freeze.append({
                        "tipo": "seta",
                        "x1": pos_unica[0], "y1": pos_unica[1],
                        "x2": pos_unica[0] + int(g.get("dx", 0)),
                        "y2": pos_unica[1] + int(g.get("dy", 0)),
                    })
                elif g["tipo"] == "seta_alvo":
                    grafismos_freeze.append({
                        "tipo": "seta",
                        "x1": pos_unica[0], "y1": pos_unica[1],
                        "x2": int(g["alvo_x"]), "y2": int(g["alvo_y"]),
                    })
                else:
                    grafismos_freeze.append(g)
            fn_a = _fn_analise_estatico(grafismos_freeze, cor, legenda, tipo)
        else:
            fn_a = _fn_analise_estatico(grafismos, cor, legenda, tipo)
        step2a = step2a.fl_image(fn_a)
        t_apos_analise = t_rel

    else:
        t_end_slow = min(t_rel + janela, dur_clip)
        clip_slow_src = raw.subclip(t_rel, t_end_slow)

        if tem_tracking:
            g_track = next(g for g in grafismos if "tracking" in g["tipo"])
            bx, by, bw, bh = [int(v) for v in g_track["bbox_inicial"]]
            pos_inicial = (bx + bw // 2, by + bh // 2)
            tracked = rastrear_jogador(
                source_path, t_analise, t_analise + janela,
                g_track["bbox_inicial"],
            )
            fn_tracking = _fn_analise_com_tracking(
                grafismos, cor, legenda, tipo,
                tracked, source.fps, vel_slow, pos_inicial,
            )
            step2a = clip_slow_src.fx(vfx.speedx, vel_slow).fl(fn_tracking)
        else:
            fn_a = _fn_analise_estatico(grafismos, cor, legenda, tipo)
            step2a = clip_slow_src.fx(vfx.speedx, vel_slow).fl_image(fn_a)

        t_apos_analise = t_end_slow

    # ── Etapa 2b: Continuação normal até o fim do clipe ───────────────────────
    partes = [step1, step2a]
    if t_apos_analise < dur_clip:
        partes.append(raw.subclip(t_apos_analise, dur_clip))

    # ── Etapa 3: Replay completo ──────────────────────────────────────────────
    partes.append(raw.fl(_fn_replay()))

    return concatenate_videoclips(partes)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Gera pílulas de vídeo de análise esportiva.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("config", help="Arquivo JSON com a configuração dos clipes")
    parser.add_argument(
        "--saida", help="Diretório de saída (sobrescreve 'diretorio_saida' do JSON)"
    )
    parser.add_argument(
        "--clipe", help="Processar somente o clipe com este nome"
    )
    args = parser.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = json.load(f)

    video_origem = cfg["video_origem"]
    dir_saida    = Path(args.saida or cfg.get("diretorio_saida", "saida"))
    fps_saida    = int(cfg.get("fps_saida", 30))
    clipes       = cfg["clipes"]

    if args.clipe:
        clipes = [c for c in clipes if c["nome"] == args.clipe]
        if not clipes:
            sys.exit(f"[ERRO] Clipe '{args.clipe}' não encontrado no config.")

    dir_saida.mkdir(parents=True, exist_ok=True)

    print(f"\n>>> Carregando vídeo: {video_origem}")
    source = VideoFileClip(video_origem)
    print(
        f"    Duração: {source.duration:.1f}s | "
        f"FPS: {source.fps} | "
        f"Resolução: {source.size[0]}x{source.size[1]}"
    )

    total = len(clipes)
    erros = []

    for i, cfg_clipe in enumerate(clipes, 1):
        nome   = cfg_clipe["nome"]
        atleta = cfg_clipe.get("atleta", "")
        sufixo = f" ({atleta})" if atleta else ""
        print(f"\n[{i}/{total}] Processando: {nome}{sufixo} ...")

        try:
            clip_final = processar_clipe(cfg_clipe, source, video_origem)
            arquivo    = dir_saida / f"{nome}.mp4"
            clip_final.write_videofile(
                str(arquivo),
                fps=fps_saida,
                codec="libx264",
                audio_codec="aac",
            )
            print(f"    -> Salvo: {arquivo}  ({clip_final.duration:.1f}s)")
            clip_final.close()
        except Exception as e:
            msg = f"[ERRO] {nome}: {e}"
            print(f"    {msg}", file=sys.stderr)
            erros.append(msg)

    source.close()

    print(f"\n{'=' * 50}")
    print(f"Concluído: {total - len(erros)}/{total} clipes gerados.")
    print(f"Saída: {dir_saida}/")
    if erros:
        print(f"\nErros ({len(erros)}):")
        for e in erros:
            print(f"  {e}")
    print()


if __name__ == "__main__":
    main()
