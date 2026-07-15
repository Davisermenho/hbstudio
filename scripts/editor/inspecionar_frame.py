#!/usr/bin/env python3
"""
inspecionar_frame.py — Extrai e exibe um frame para descobrir coordenadas.

Uso:
    python inspecionar_frame.py <video> <timestamp>

Exemplos:
    python inspecionar_frame.py jogo.mp4 00:06:26.000
    python inspecionar_frame.py jogo.mp4 386.5

Controles na janela:
    - Mova o mouse: mostra coordenadas no título
    - Clique e arraste: define um retângulo (bbox_inicial para tracking)
    - Pressione S: salva o frame como PNG na pasta atual
    - Feche a janela para sair
"""

import sys
from pathlib import Path

from moviepy.editor import VideoFileClip
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import RectangleSelector
import numpy as np


def ts(valor: str) -> float:
    """Converte 'HH:MM:SS.mmm' ou número para segundos float."""
    try:
        return float(valor)
    except ValueError:
        partes = valor.strip().split(":")
        s = 0.0
        for p in partes:
            s = s * 60 + float(p)
        return s


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    video_path = sys.argv[1]
    timestamp  = ts(sys.argv[2])

    print(f"Carregando frame em {sys.argv[2]} de {video_path} ...")
    clip = VideoFileClip(video_path)

    if timestamp < 0 or timestamp > clip.duration:
        sys.exit(
            f"[ERRO] Timestamp {timestamp:.2f}s fora do intervalo "
            f"[0, {clip.duration:.2f}s]"
        )

    frame = clip.get_frame(timestamp)
    clip.close()

    h, w = frame.shape[:2]
    print(f"Resolução do frame: {w}x{h}")

    # ── Salvar PNG de referência ──────────────────────────────────────────────
    ts_str = sys.argv[2].replace(":", "-").replace(".", "-")
    png_path = Path(f"frame_{ts_str}.png")

    from PIL import Image
    img_pil = Image.fromarray(frame.astype("uint8"), "RGB")
    img_pil.save(png_path)
    print(f"Frame salvo como: {png_path}")

    # ── Interface matplotlib ──────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(min(w / 80, 20), min(h / 80, 14)))
    ax.imshow(frame)
    ax.set_title(f"Mova o mouse | Arraste para definir bbox | S = salvar PNG")
    ax.axis("off")

    bbox_resultado = {}

    def on_mouse_move(event):
        if event.inaxes == ax and event.xdata and event.ydata:
            ax.set_title(
                f"x={int(event.xdata)}, y={int(event.ydata)}  |  "
                f"Arraste para definir bbox  |  S = salvar"
            )
            fig.canvas.draw_idle()

    def on_select(eclick, erelease):
        x1, y1 = int(eclick.xdata), int(eclick.ydata)
        x2, y2 = int(erelease.xdata), int(erelease.ydata)
        bx = min(x1, x2)
        by = min(y1, y2)
        bw = abs(x2 - x1)
        bh = abs(y2 - y1)
        cx = bx + bw // 2
        cy = by + bh // 2
        bbox_resultado["bbox"] = [bx, by, bw, bh]
        print(f"\n{'─' * 50}")
        print(f"  Centro clicado:   x={cx}, y={cy}")
        print(f"  bbox_inicial:     [{bx}, {by}, {bw}, {bh}]")
        print(f"  Copie no config:")
        print(f'    {{ "tipo": "circulo_tracking", "raio": 50, "bbox_inicial": [{bx}, {by}, {bw}, {bh}] }}')
        print(f"{'─' * 50}\n")

    def on_key(event):
        if event.key and event.key.lower() == "s":
            img_pil.save(png_path)
            print(f"Frame salvo: {png_path}")

    selector = RectangleSelector(
        ax, on_select,
        useblit=True,
        button=[1],
        minspanx=5, minspany=5,
        spancoords="pixels",
        interactive=True,
        props=dict(facecolor="yellow", edgecolor="red", alpha=0.3, fill=True),
    )

    fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)
    fig.canvas.mpl_connect("key_press_event", on_key)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
