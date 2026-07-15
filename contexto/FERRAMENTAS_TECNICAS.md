# Ferramentas técnicas — Edição de vídeo

## Registro

| Identificador | Conteúdo |
| --- | --- |
| `TEC-VID-001` | Script de edição de vídeo (editar_video.py) |
| `TEC-INS-001` | Ferramenta de inspeção de frame (inspecionar_frame.py) |
| `TEC-ENV-001` | Ambiente de execução |

## TEC-VID-001 — editar_video.py

**Propósito:** Gera pílulas de análise em vídeo para reuniões de equipe e envio
individual para atletas via WhatsApp.

**Estrutura de cada clipe:**

1. Abertura em velocidade normal com label animado (tipo e descrição da ação)
2. Momento de análise em câmera lenta ou freeze, com grafismos sobrepostos e
   legenda explicativa
3. Continuação do vídeo após a análise, em velocidade normal, até o fim do clipe
4. Replay completo do clipe com badge "REPLAY"

**Invocação:**

    .venv/bin/python editar_video.py config.json
    .venv/bin/python editar_video.py config.json --clipe nome_do_clipe

**Tipos de clipe (campo `tipo`):**

- `acerto` — destaca comportamento correto (cor verde)
- `ajuste` — indica comportamento a corrigir (cor amarela/laranja)

**Tipo de análise (campo `tipo_analise`):**

- `slow_motion` — câmera lenta; requer `velocidade_slow` e `janela_analise_segundos`
- `freeze` — frame congelado; requer `duracao_freeze`

**Grafismos disponíveis (campo `grafismos`):**

| Tipo | Quando usar | Parâmetros principais |
| --- | --- | --- |
| `circulo` | Destacar posição fixa na quadra | `x`, `y`, `raio` |
| `circulo_tracking` | Destacar jogador em movimento — rastreia automaticamente | `raio`, `bbox_inicial` |
| `seta` | Indicar direção ou alvo entre dois pontos fixos | `x1`, `y1`, `x2`, `y2` |
| `seta_tracking` | Seta com cauda no jogador rastreado e ponta em offset fixo | `dx`, `dy` |
| `seta_alvo` | Seta com cauda no jogador rastreado e ponta em coordenada fixa da quadra | `alvo_x`, `alvo_y` |
| `seta_tracejada` | Movimento sugerido ou correção | `x1`, `y1`, `x2`, `y2` |
| `zona` | Destacar região da quadra (polígono semitransparente) | `pontos` (lista de [x,y]) |

O campo `bbox_inicial` para `circulo_tracking` é obtido com `inspecionar_frame.py`.
O campo `alvo_x`, `alvo_y` para `seta_alvo` também é obtido com a mesma ferramenta,
clicando no destino tático no frame.

**Saída:** arquivos MP4 no diretório `saida/`, nomeados por atleta e nome do clipe.

## TEC-INS-001 — inspecionar_frame.py

**Propósito:** Extrai um frame do vídeo como PNG e exibe interface para identificar
coordenadas e definir bounding box para tracking.

**Invocação:**

    .venv/bin/python inspecionar_frame.py <video.mp4> <timestamp>

Exemplo:

    .venv/bin/python inspecionar_frame.py videos/jogo.mp4 00:06:26.000

**Saída:** PNG salvo na pasta atual (sempre) + janela interativa (quando disponível).

**Em WSL2:** a janela do matplotlib não abre. Abrir o PNG salvo no Windows
(Paint ou visualizador de imagens) para identificar as coordenadas visualmente.

## TEC-ENV-001 — Ambiente de execução

- Ambiente virtual Python localizado em `.venv/` na raiz do repositório
- Sempre usar `.venv/bin/python` e `.venv/bin/pip` — nunca o Python do sistema
- Dependência crítica: `opencv-contrib-python` (não `opencv-python`) — necessário
  para o tracker CSRT usado pelo `circulo_tracking`
- Plataforma: WSL2 / Linux
- Em caso de dúvida sobre dependências, consultar `requirements.txt` na raiz
