# Especificação — editar_video.py

Versão: 1.0
Data: 2026-07-14
Repositório: /home/davis/atletas-videos

## 1. Objetivo e problema

**Problema:**
A comissão técnica do IDEC produz análises táticas de jogadas individuais para
reuniões de equipe e para envio individual a atletas via WhatsApp. Sem automação,
o processo de cortar o vídeo, aplicar câmera lenta, adicionar grafismos e exportar
é realizado manualmente para cada jogada, o que é lento e inconsistente.

**Objetivo:**
O script automatiza a geração de "pílulas de análise": clipes curtos e padronizados,
cada um focado em uma jogada específica de um atleta, com abertura identificada,
análise em câmera lenta ou frame congelado com sobreposição de grafismos e replay.

**Resultado observável esperado:**
Dado um arquivo de configuração JSON válido com N clipes, o script produz N arquivos
MP4 na pasta de saída, prontos para uso em reunião ou envio por WhatsApp, sem
intervenção manual adicional.

**Critério de conclusão do problema:**
O problema é considerado resolvido quando o script produz arquivos MP4 visualmente
corretos para todos os clipes configurados em uma execução sem erros.

---

## 2. Contexto de uso

O script é executado manualmente por Davi Sermenho, auxiliar técnico, antes ou
durante reuniões de análise ou de preparação de jogo.

A execução ocorre via linha de comando no ambiente WSL2 (Windows Subsystem for Linux 2),
usando o ambiente virtual Python do repositório. O usuário possui conhecimento
técnico de Python e linha de comando.

O script não requer conexão com a internet. Nenhum dado é enviado para serviços externos.

---

## 3. Usuários, sistemas e processos envolvidos

| Papel | Descrição |
| --- | --- |
| Executor | Davi Sermenho, via linha de comando |
| Ferramenta auxiliar | `inspecionar_frame.py` (extrai coordenadas de bbox e alvos táticos) |
| Entrada | Arquivo de vídeo MP4 da partida e arquivo JSON de configuração |
| Saída | Arquivos MP4 por atleta/jogada, prontos para exibição ou envio |

---

## 4. Escopo incluído

- Extração de segmentos temporais de um vídeo-fonte MP4
- Aplicação de câmera lenta (fator de velocidade configurável)
- Congelamento de frame por duração configurável
- Sobreposição de grafismos: círculo, seta, seta tracejada e zona
- Rastreamento automático de posição de jogador (algoritmo CSRT, OpenCV)
- Grafismos ancorados na posição rastreada do jogador
- Animação de entrada e saída de legenda de abertura (slide + fade)
- Legenda de análise fixa no topo durante a análise
- Badge "REPLAY" animado durante o replay
- Exportação de cada clipe como arquivo MP4 independente
- Processamento de múltiplos clipes a partir de um único arquivo de configuração
- Processamento isolado de um único clipe identificado por nome

---

## 5. Escopo excluído

- Upload automático para WhatsApp, e-mail ou qualquer plataforma externa
- Edição de trilha sonora ou remoção de áudio
- Detecção automática de jogadores sem bounding box inicial fornecida manualmente
- Interface gráfica de configuração ou seleção de clipes
- Suporte a múltiplos vídeos-fonte em um único arquivo de configuração
- Processamento de vídeos em formatos diferentes de MP4
- Geração de thumbnails, GIFs ou formatos alternativos
- Publicação ou compartilhamento de saídas
- Modificação do arquivo de vídeo-fonte original

---

## 6. Ambiente técnico

| Campo | Valor |
| --- | --- |
| Linguagem | Python 3.x (testado em ambiente WSL2) |
| Sistema operacional | Linux (WSL2) |
| Ambiente virtual | `.venv/` na raiz do repositório |
| Execução | `.venv/bin/python editar_video.py` |
| Acesso à internet | Não requerido |

**Bibliotecas requeridas** (ver `requirements.txt`):

| Biblioteca | Versão | Uso |
| --- | --- | --- |
| moviepy | ==1.0.3 | Edição de vídeo (corte, concatenação, câmera lenta) |
| Pillow | >=10.0.0 | Renderização de grafismos e legendas sobre frames |
| numpy | >=1.24.0 | Conversão entre frames moviepy e PIL |
| opencv-contrib-python | >=4.8.0 | Rastreamento CSRT de jogadores |
| matplotlib | >=3.7.0 | Usado apenas em `inspecionar_frame.py` |

**Restrição crítica de dependência:**
O pacote deve ser `opencv-contrib-python`, não `opencv-python`. O algoritmo CSRT
requer os módulos `contrib` do OpenCV. A instalação do pacote errado produz o erro
`AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'`.

---

## 7. Entradas

### ENT-001 — Arquivo de configuração JSON

| Campo | Valor |
| --- | --- |
| Identificador | ENT-001 |
| Nome | Arquivo de configuração |
| Origem | Usuário (passado como argumento posicional) |
| Tipo | Arquivo texto |
| Formato | JSON, codificação UTF-8 |
| Obrigatoriedade | Obrigatório |

**Estrutura raiz do JSON:**

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `video_origem` | string | sim | Caminho para o arquivo MP4 da partida |
| `diretorio_saida` | string | sim | Pasta onde os MP4 gerados serão salvos |
| `fps_saida` | inteiro | sim | Taxa de quadros dos arquivos de saída |
| `clipes` | array | sim | Lista de clipes a gerar |

**Estrutura de cada clipe em `clipes`:**

| Campo | Tipo | Obrigatório | Valores permitidos | Descrição |
| --- | --- | --- | --- | --- |
| `nome` | string | sim | Qualquer string sem espaços | Identificador do clipe; define o nome do arquivo de saída |
| `atleta` | string | sim | Qualquer string | Nome do atleta |
| `tipo` | string | sim | `"acerto"` ou `"ajuste"` | Categoria visual do clipe |
| `label_abertura` | string | sim | Qualquer string | Texto exibido no label de abertura |
| `inicio` | string ou número | sim | `"HH:MM:SS.mmm"` ou segundos | Início do clipe no vídeo-fonte |
| `fim` | string ou número | sim | `"HH:MM:SS.mmm"` ou segundos | Fim do clipe no vídeo-fonte |
| `momento_analise` | string ou número | sim | `"HH:MM:SS.mmm"` ou segundos | Instante da ação tática; deve ser estritamente entre `inicio` e `fim` |
| `tipo_analise` | string | sim | `"slow_motion"` ou `"freeze"` | Tipo de análise |
| `velocidade_slow` | número (0,1) | condicional | Entre 0 (excl.) e 1 (excl.) | Fator de velocidade; obrigatório se `tipo_analise = slow_motion` |
| `janela_analise_segundos` | número positivo | condicional | > 0 | Duração da janela de análise em segundos do vídeo-fonte; obrigatório se `tipo_analise = slow_motion` |
| `duracao_freeze` | número positivo | condicional | > 0 | Duração do frame congelado em segundos; obrigatório se `tipo_analise = freeze` |
| `grafismos` | array | não | Ver tabela de grafismos | Lista de grafismos a sobrepor durante a análise |
| `legenda_analise` | string | não | Qualquer string | Texto exibido no bloco de legenda durante a análise |
| `duracao_label` | número positivo | não | > 0 | Duração do label de abertura em segundos; padrão: `min(t_rel, 5.0)` |

**Formato de timestamp:**
A função `ts()` aceita strings no formato `"HH:MM:SS.mmm"`, `"MM:SS.mmm"`, `"SS.mmm"`
ou valores numéricos (int/float) representando segundos. O componente mais à direita
pode conter casas decimais.

**Estrutura de cada grafismo em `grafismos`:**

| Tipo | Campos obrigatórios | Descrição |
| --- | --- | --- |
| `circulo` | `x`, `y`, `raio` | Círculo estático na posição (x, y) |
| `circulo_tracking` | `raio`, `bbox_inicial` | Círculo que segue o jogador rastreado |
| `seta` | `x1`, `y1`, `x2`, `y2` | Seta de (x1,y1) para (x2,y2) |
| `seta_tracking` | `dx`, `dy` | Seta do centro rastreado até (cx+dx, cy+dy) |
| `seta_alvo` | `alvo_x`, `alvo_y` | Seta do centro rastreado até coordenada fixa |
| `seta_tracejada` | `x1`, `y1`, `x2`, `y2` | Seta tracejada de (x1,y1) para (x2,y2) |
| `zona` | `pontos` | Polígono semitransparente definido por lista de [x,y] |

`bbox_inicial`: array `[x, y, largura, altura]` em pixels, obtido com `inspecionar_frame.py`.

### ENT-002 — Argumento `--saida`

| Campo | Valor |
| --- | --- |
| Identificador | ENT-002 |
| Nome | Diretório de saída alternativo |
| Origem | Linha de comando |
| Tipo | String (caminho de diretório) |
| Obrigatoriedade | Opcional |
| Comportamento | Sobrescreve o campo `diretorio_saida` do JSON quando fornecido |

### ENT-003 — Argumento `--clipe`

| Campo | Valor |
| --- | --- |
| Identificador | ENT-003 |
| Nome | Filtro de clipe único |
| Origem | Linha de comando |
| Tipo | String |
| Obrigatoriedade | Opcional |
| Valores permitidos | Deve corresponder ao campo `nome` de algum clipe do config |
| Comportamento | Quando fornecido, somente o clipe com o nome correspondente é processado |

---

## 8. Saídas

### SAI-001 — Arquivos MP4 gerados

| Campo | Valor |
| --- | --- |
| Identificador | SAI-001 |
| Conteúdo | Clipe editado com abertura, análise e replay |
| Tipo | Vídeo MP4, codec H.264 |
| Destino | `{diretorio_saida}/{nome}.mp4` |
| Momento | Ao final do processamento de cada clipe |

Estrutura temporal do vídeo gerado:

1. **Etapa 1 — Abertura:** trecho do início do clipe até `momento_analise`, velocidade normal, com label animado no topo
2. **Etapa 2a — Análise:** câmera lenta (`slow_motion`) ou frame congelado (`freeze`), com grafismos sobrepostos e legenda de análise no topo
3. **Etapa 2b — Continuação:** trecho de `momento_analise + janela` até o fim do clipe, velocidade normal (omitida se não houver trecho restante)
4. **Etapa 3 — Replay:** o clipe completo (do início ao fim) em velocidade normal, com badge "REPLAY" animado

### SAI-002 — Mensagens de progresso (stdout)

Ao processar cada clipe:

```
[1/3] infiltracao_bebe (Bebê — acerto)
    -> Salvo: saida/infiltracao_bebe.mp4  (38.3s)
```

### SAI-003 — Mensagens de erro (stderr)

Quando um clipe falha:

```
    [ERRO] gol_assistencia_santos: 'gol_assistencia_santos': momento_analise deve estar entre inicio e fim
```

### SAI-004 — Sumário final (stdout)

Ao final do processamento de todos os clipes:

```
Concluído: 2 gerados, 1 com erro.
```

ou

```
Concluído: 3 gerados.
```

---

## 9. Requisitos funcionais

---

**ID:** RF-001
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Parsing do arquivo de configuração JSON
**Condição:** Sempre que o script for executado
**Entrada:** Caminho do arquivo JSON (argumento posicional)
**Saída:** Estrutura de dados em memória com configuração dos clipes
**Exceções:** Arquivo inexistente ou JSON malformado

**Critérios de aceite:**

- Dado um JSON válido, quando o script iniciar, então os campos `video_origem`, `diretorio_saida`, `fps_saida` e `clipes` estão disponíveis em memória
- Dado um arquivo JSON inexistente, quando o script iniciar, então ele encerra imediatamente com `[ERRO] Arquivo de configuração não encontrado: {caminho}` no stderr, sem traceback e sem processar nenhum clipe
- Dado um JSON com erro de sintaxe, quando o script iniciar, então ele encerra imediatamente com `[ERRO] JSON inválido em {caminho}: {descrição com linha e coluna}` no stderr, sem traceback e sem processar nenhum clipe

---

**ID:** RF-002
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Criação automática do diretório de saída
**Condição:** Sempre que o script for executado
**Entrada:** Valor de `diretorio_saida` (ou `--saida`)
**Saída:** Diretório criado no sistema de arquivos se não existir

**Critérios de aceite:**

- Dado que `diretorio_saida` não existe, quando o script iniciar, então o diretório é criado antes do primeiro arquivo de saída ser gravado
- Dado que o diretório já existe, quando o script iniciar, então nenhum erro é gerado

---

**ID:** RF-003
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Filtro de clipe único via `--clipe`
**Condição:** Quando o argumento `--clipe` for fornecido
**Entrada:** Nome do clipe (string)
**Saída:** Somente o clipe nomeado é processado
**Exceções:** Nome não encontrado no config

**Critérios de aceite:**

- Dado `--clipe infiltracao_bebe`, quando executado, então somente o clipe com `"nome": "infiltracao_bebe"` é processado
- Dado `--clipe inexistente`, quando executado, então o script encerra imediatamente com a mensagem `[ERRO] Clipe 'inexistente' não encontrado no config.` e código de saída não-zero

---

**ID:** RF-004
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Validação de `tipo`
**Condição:** Ao iniciar o processamento de cada clipe
**Entrada:** Campo `tipo` do clipe
**Saída:** Erro se o valor não for `"acerto"` ou `"ajuste"`

**Critérios de aceite:**

- Dado `"tipo": "acerto"`, então o clipe é processado com cores verdes
- Dado `"tipo": "ajuste"`, então o clipe é processado com cores amarelas/laranjas
- Dado qualquer outro valor, então o clipe falha com `ValueError` e o erro é registrado; os clipes seguintes continuam sendo processados

---

**ID:** RF-005
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Validação de `momento_analise`
**Condição:** Ao iniciar o processamento de cada clipe
**Entrada:** Campos `inicio`, `fim`, `momento_analise`
**Saída:** Erro se `momento_analise` não estiver estritamente entre `inicio` e `fim`

**Critérios de aceite:**

- Dado `momento_analise = inicio`, então o clipe falha com erro descritivo
- Dado `momento_analise = fim`, então o clipe falha com erro descritivo
- Dado `momento_analise` entre `inicio` e `fim` (exclusivo), então o processamento prossegue

---

**ID:** RF-006
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Etapa 1 — Abertura com label animado
**Condição:** Para todo clipe processado
**Entrada:** Trecho do vídeo-fonte de `inicio` até `momento_analise`
**Saída:** Segmento de vídeo em velocidade normal com label no topo

**Critérios de aceite:**

- O segmento tem duração exatamente igual ao intervalo `[inicio, momento_analise]`
- O label de abertura aparece com animação de entrada (slide de cima + fade) e saída (slide para cima + fade)
- A duração visível do label é `duracao_label` se configurado, ou `min(t_rel, 5.0)` segundos
- O label exibe o texto de `label_abertura`
- O label é centralizado horizontalmente no topo da imagem, com cantos arredondados
- A cor do accent lateral do label corresponde ao `tipo` do clipe (verde para "acerto", laranja para "ajuste")

---

**ID:** RF-007
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Etapa 2a — Análise em câmera lenta
**Condição:** Quando `tipo_analise = "slow_motion"`
**Entrada:** `velocidade_slow`, `janela_analise_segundos`, `grafismos`, `legenda_analise`
**Saída:** Segmento de vídeo em câmera lenta com grafismos e legenda

**Critérios de aceite:**

- A duração real do segmento é `janela_analise_segundos / velocidade_slow` segundos
- O segmento representa `janela_analise_segundos` segundos do vídeo-fonte a partir de `momento_analise`, reproduzidos na velocidade `velocidade_slow`
- Os grafismos são sobrepostos quadro a quadro
- A legenda de análise aparece no topo durante todo o segmento

---

**ID:** RF-008
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Etapa 2a — Análise com frame congelado
**Condição:** Quando `tipo_analise = "freeze"`
**Entrada:** `duracao_freeze`, `grafismos`, `legenda_analise`
**Saída:** Frame único congelado por `duracao_freeze` segundos com grafismos e legenda

**Critérios de aceite:**

- O frame exibido corresponde ao instante `momento_analise` do vídeo-fonte
- A duração do segmento é exatamente `duracao_freeze` segundos
- Os grafismos são estáticos (grafismos de tracking são convertidos para posição única no frame congelado)
- A legenda de análise aparece no topo durante todo o segmento

---

**ID:** RF-009
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Etapa 2b — Continuação após análise
**Condição:** Para todo clipe em que `t_apos_analise < dur_clip`
**Entrada:** Trecho do vídeo-fonte de `t_apos_analise` até o fim do clipe
**Saída:** Segmento de vídeo em velocidade normal, sem grafismos
**Exceções:** Quando `t_apos_analise >= dur_clip`, a etapa é omitida

**Critérios de aceite:**

- Dado `momento_analise = 00:06:26`, `janela_analise_segundos = 3`, `fim = 00:06:35`, então a etapa 2b contém os últimos 6 segundos do clipe
- Dado `momento_analise = 00:06:26`, `janela_analise_segundos = 9`, `fim = 00:06:35`, então a etapa 2b é omitida sem erro

---

**ID:** RF-010
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Etapa 3 — Replay com badge
**Condição:** Para todo clipe processado
**Entrada:** Clipe completo do vídeo-fonte de `inicio` até `fim`
**Saída:** Clipe em velocidade normal com badge "REPLAY" animado no canto superior direito

**Critérios de aceite:**

- A duração do segmento é igual à duração total do clipe (`fim - inicio`)
- O badge "REPLAY" aparece com animação de slide e fica visível por 2,5 segundos
- O badge está posicionado no canto superior direito

---

**ID:** RF-011
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `circulo` — círculo estático
**Condição:** Quando o grafismo tem `"tipo": "circulo"`
**Entrada:** `x`, `y`, `raio`
**Saída:** Círculo colorido centrado em (x, y) com raio dado

**Critérios de aceite:**

- O círculo aparece na posição especificada em todos os frames da etapa de análise
- A cor do círculo corresponde à cor primária do `tipo` do clipe

---

**ID:** RF-012
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `circulo_tracking` — círculo com rastreamento
**Condição:** Quando o grafismo tem `"tipo": "circulo_tracking"`
**Entrada:** `raio`, `bbox_inicial` (`[x, y, w, h]` em pixels)
**Saída:** Círculo colorido centrado na posição rastreada do jogador em cada frame

**Critérios de aceite:**

- O círculo segue o jogador quadro a quadro durante câmera lenta
- Em freeze, o círculo aparece na posição do jogador no frame congelado
- Quando o tracker detecta um salto > 50 pixels entre frames, a posição anterior é mantida

---

**ID:** RF-013
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `seta` — seta estática
**Condição:** Quando o grafismo tem `"tipo": "seta"`
**Entrada:** `x1`, `y1`, `x2`, `y2`
**Saída:** Seta de (x1,y1) até (x2,y2)

**Critérios de aceite:**

- A seta aparece com cabeça direcional em (x2, y2)
- A cor corresponde à cor primária do `tipo` do clipe

---

**ID:** RF-014
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `seta_tracking` — seta com cauda no jogador rastreado
**Condição:** Quando o grafismo tem `"tipo": "seta_tracking"`
**Entrada:** `dx`, `dy` (offset em pixels)
**Saída:** Seta de (cx, cy) até (cx+dx, cy+dy), onde (cx,cy) é a posição rastreada do jogador

**Critérios de aceite:**

- A cauda da seta se move junto com o jogador
- O offset (dx, dy) é constante em todos os frames

---

**ID:** RF-015
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `seta_alvo` — seta com ponta em coordenada fixa da quadra
**Condição:** Quando o grafismo tem `"tipo": "seta_alvo"`
**Entrada:** `alvo_x`, `alvo_y` (coordenadas fixas do destino tático)
**Saída:** Seta de (cx, cy) até (alvo_x, alvo_y), onde (cx,cy) é a posição rastreada do jogador

**Critérios de aceite:**

- A cauda da seta se move junto com o jogador
- A ponta permanece fixa em (alvo_x, alvo_y) em todos os frames
- Em freeze, a seta usa a posição do jogador no frame congelado como origem

---

**ID:** RF-016
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `seta_tracejada` — seta tracejada estática
**Condição:** Quando o grafismo tem `"tipo": "seta_tracejada"`
**Entrada:** `x1`, `y1`, `x2`, `y2`
**Saída:** Seta com linha tracejada de (x1,y1) até (x2,y2)

**Critérios de aceite:**

- A linha é tracejada (segmentos alternados)
- A cor corresponde à cor primária do `tipo` do clipe

---

**ID:** RF-017
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Grafismo `zona` — polígono semitransparente
**Condição:** Quando o grafismo tem `"tipo": "zona"`
**Entrada:** `pontos` (lista de pares [x, y])
**Saída:** Polígono preenchido com transparência na região especificada

**Critérios de aceite:**

- A região definida pelos pontos aparece destacada
- O vídeo subjacente permanece visível através da transparência

---

**ID:** RF-018
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Rastreamento de jogador com limite de deslocamento
**Condição:** Quando há grafismos de tracking e `tipo_analise = slow_motion`
**Entrada:** `bbox_inicial`, frames do vídeo-fonte
**Saída:** Dicionário de posições `{frame_relativo: (cx, cy)}`
**Exceções:** Saltos > 50 pixels entre frames consecutivos são descartados

**Critérios de aceite:**

- Quando o tracker retorna uma posição com deslocamento <= 50px em relação à posição anterior, a nova posição é aceita
- Quando o deslocamento > 50px, a posição anterior é mantida sem encerrar o rastreamento
- O rastreamento ocorre sobre os frames originais do vídeo-fonte, não sobre os frames em câmera lenta

---

**ID:** RF-019
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Isolamento de erros por clipe
**Condição:** Quando ocorre uma exceção durante o processamento de um clipe
**Entrada:** Exceção capturada
**Saída:** Mensagem de erro no stderr; processamento dos clipes restantes continua

**Critérios de aceite:**

- Dado que o clipe 1 falha, quando o script processa os clipes 1, 2 e 3, então os clipes 2 e 3 são processados normalmente
- A mensagem de erro inclui o nome do clipe e a descrição do erro
- O sumário final informa quantos clipes foram gerados com sucesso e quantos falharam

---

**ID:** RF-020
**Tipo:** Requisito funcional
**Prioridade:** Obrigatória
**Descrição:** Exportação MP4
**Condição:** Ao final do processamento de cada clipe
**Entrada:** Clipe concatenado (etapas 1 + 2a + 2b + 3)
**Saída:** Arquivo `{diretorio_saida}/{nome}.mp4`

**Critérios de aceite:**

- O arquivo de saída é um MP4 válido reproduzível por players padrão
- A taxa de quadros do arquivo de saída é igual ao valor de `fps_saida`
- O nome do arquivo é exatamente `{nome}.mp4`, onde `nome` é o valor do campo `nome` do clipe

---

## 10. Requisitos não funcionais

---

**ID:** RNF-001
**Tipo:** Requisito não funcional
**Descrição:** O script não deve modificar nem sobrescrever o arquivo de vídeo-fonte

**Critério de aceite:** Dado qualquer execução bem-sucedida ou com erro, o arquivo de vídeo-fonte tem o mesmo tamanho e conteúdo após a execução.

---

**ID:** RNF-002
**Tipo:** Requisito não funcional
**Descrição:** Um clipe com erro não deve corromper ou apagar arquivos de saída já gerados

**Critério de aceite:** Dado que o clipe 2 falha após o clipe 1 ter sido exportado com sucesso, o arquivo do clipe 1 permanece intacto.

---

**ID:** RNF-003
**Tipo:** Requisito não funcional
**Descrição:** Mensagens de erro devem identificar o clipe e a causa

**Critério de aceite:** A mensagem de erro contém o nome do clipe e uma descrição acionável do problema (não apenas "Exception").

---

**ID:** RNF-004
**Tipo:** Requisito não funcional
**Descrição:** Execução reproduzível — dado o mesmo arquivo de vídeo-fonte e o mesmo arquivo de configuração, o script deve produzir arquivos MP4 com a mesma estrutura temporal, grafismos e metadados em qualquer execução subsequente no mesmo ambiente

**Critério de aceite:** Dado o mesmo config e vídeo-fonte, quando o script for executado duas vezes, então os arquivos de saída têm a mesma duração, FPS e estrutura de etapas.

---

**ID:** RNF-005
**Tipo:** Requisito não funcional
**Descrição:** Saída estruturada — o script deve usar stdout exclusivamente para progresso e sumário (SAI-002 e SAI-004) e stderr exclusivamente para erros (SAI-003); nenhuma mensagem de depuração interna deve aparecer na saída padrão durante execução normal

**Critério de aceite:** Dado uma execução sem erros, quando o stdout for capturado, então ele contém apenas as linhas de progresso por clipe e o sumário final; o stderr fica vazio.

---

**ID:** RNF-006
**Tipo:** Requisito não funcional
**Descrição:** Compatibilidade WSL2 — o script deve funcionar corretamente no ambiente WSL2 com Python no `.venv` local; caminhos devem ser tratados como paths Linux mesmo quando o vídeo-fonte estiver em um path montado do Windows

**Critério de aceite:** Dado um caminho de vídeo-fonte sob `/mnt/c/` ou `/mnt/d/`, quando o script for executado, então o vídeo é lido e os arquivos de saída são gerados sem erro de path.

---

**ID:** RNF-007
**Tipo:** Requisito não funcional
**Descrição:** Privacidade dos atletas — o campo `atleta` não deve aparecer em nomes de arquivos de saída, logs ou mensagens de progresso; somente o campo `nome` do clipe é usado para nomear o arquivo de saída

**Critério de aceite:** Dado um clipe com `"atleta": "João Silva"` e `"nome": "infiltracao_001"`, quando o script for executado, então o arquivo gerado é `infiltracao_001.mp4` e nenhuma mensagem de stdout ou stderr contém o valor do campo `atleta`.

---

## 11. Regras de negócio

**RN-001:**
Dado que `momento_analise <= inicio` ou `momento_analise >= fim`,
quando o script iniciar o processamento do clipe,
então o clipe falha com erro descritivo e os clipes restantes continuam.

**RN-002:**
Dado que `t_apos_analise >= dur_clip`
(onde `t_apos_analise = t_rel + janela_analise_segundos` para slow_motion, ou `t_rel` para freeze),
quando o script montar as etapas do clipe,
então a etapa 2b é omitida sem erro.

**RN-003:**
Dado que `duracao_label` não está configurado no JSON,
quando o script calcular a duração do label de abertura,
então `dur_label = min(t_rel, 5.0)`, onde `t_rel = momento_analise - inicio` em segundos.

**RN-004:**
Dado que o tracker CSRT retorna uma nova posição com deslocamento > 50 pixels em relação ao frame anterior,
quando o script registrar posições de rastreamento,
então a posição do frame anterior é mantida para esse frame (o salto é descartado silenciosamente).

**RN-005:**
Dado um grafismo de tipo `circulo_tracking`, `seta_tracking` ou `seta_alvo` em um clipe com `tipo_analise = freeze`,
quando o script converter grafismos para o frame congelado,
então o grafismo é convertido para sua versão estática usando a posição do jogador no instante do freeze.

**RN-006:**
Dado que `tipo = "acerto"`,
quando grafismos e legendas forem renderizados,
então a cor primária é RGB (0, 210, 0) e a secundária é RGB (30, 100, 255).

**RN-007:**
Dado que `tipo = "ajuste"`,
quando grafismos e legendas forem renderizados,
então a cor primária é RGB (255, 190, 0) e a secundária é RGB (255, 130, 0).

---

## 12. Restrições

- O vídeo-fonte deve existir no caminho informado antes da execução
- O arquivo de configuração deve ser JSON válido em UTF-8
- A biblioteca `opencv-contrib-python` deve estar instalada (não `opencv-python`)
- O Python do sistema não deve ser usado — usar exclusivamente `.venv/bin/python`
- O campo `nome` de cada clipe deve ser único dentro do arquivo de configuração (nomes duplicados resultam em sobrescrita do arquivo de saída)

---

## 13. Situações de erro

| Código | Causa | Comportamento | Mensagem |
| --- | --- | --- | --- |
| ERR-001 | Arquivo JSON inexistente | Encerramento imediato com mensagem formatada; sem traceback | `[ERRO] Arquivo de configuração não encontrado: {caminho}` |
| ERR-002 | JSON malformado | Encerramento imediato com mensagem formatada; sem traceback | `[ERRO] JSON inválido em {caminho}: {descrição do erro com linha e coluna}` |
| ERR-003 | `--clipe` não encontrado | Encerramento imediato com mensagem formatada | `[ERRO] Clipe '{nome}' não encontrado no config.` |
| ERR-004 | `tipo` inválido | Clipe falha; próximo clipe continua | `[ERRO] {nome}: tipo deve ser 'acerto' ou 'ajuste'` |
| ERR-005 | `momento_analise` fora do intervalo | Clipe falha; próximo clipe continua | `[ERRO] {nome}: momento_analise deve estar entre inicio e fim` |
| ERR-006 | Vídeo-fonte inexistente | Encerramento imediato com mensagem formatada; sem traceback | `[ERRO] Vídeo-fonte não encontrado: {caminho}` |
| ERR-007 | `tipo_analise` inválido | Clipe falha; próximo clipe continua | `[ERRO] {nome}: tipo_analise deve ser 'slow_motion' ou 'freeze'` |
| ERR-008 | Qualquer outra exceção por clipe | Clipe falha; próximo clipe continua | `[ERRO] {nome}: {mensagem original da exceção}` |

Para ERR-001, ERR-002, ERR-003 e ERR-006, o script encerra antes de processar qualquer clipe; nenhum arquivo de saída é criado ou alterado.

Para ERR-004 a ERR-008, o estado dos dados permanece intacto: o arquivo de saída do clipe com erro não é criado, e os arquivos de clipes anteriores não são afetados.

---

## 14. Dependências e premissas

**Dependências:**

- `editar_video.py` requer `moviepy 1.0.3`, `Pillow >=10`, `numpy >=1.24`, `opencv-contrib-python >=4.8`
- As dependências são instaladas via `.venv/bin/pip install -r requirements.txt`
- `inspecionar_frame.py` é uma ferramenta auxiliar independente, não um módulo importado por `editar_video.py`

**Premissas:**

- O vídeo-fonte está em formato MP4 compatível com moviepy
- As coordenadas de `bbox_inicial`, `alvo_x`, `alvo_y` e demais campos geométricos foram obtidas com `inspecionar_frame.py` e correspondem à resolução real do vídeo-fonte
- O usuário tem permissão de escrita no diretório de saída (ou em seu diretório pai, para criação automática)

---

## 15. Critérios de aceite globais

- Dado um config válido com 3 clipes sem tracking, quando executado, então 3 arquivos MP4 são gerados na pasta de saída
- Dado um config com 1 clipe com `circulo_tracking`, quando executado, então o círculo segue o jogador nos frames de câmera lenta
- Dado `--clipe nome_valido`, quando executado, então apenas 1 arquivo MP4 é gerado
- Dado `--clipe nome_invalido`, quando executado, então nenhum arquivo é gerado e a mensagem de erro é exibida
- Dado um config com 3 clipes onde o segundo tem `tipo = "invalido"`, quando executado, então os clipes 1 e 3 são gerados e o erro do clipe 2 é reportado no stderr
- Dado um config onde o `diretorio_saida` não existe, quando executado, então o diretório é criado e os arquivos são gerados nele

---

## 16. Exemplos e casos-limite

### Exemplo válido — câmera lenta com tracking

```json
{
  "nome": "infiltracao_bebe",
  "atleta": "Bebê",
  "tipo": "acerto",
  "label_abertura": "ACERTO: Boa leitura e infiltração",
  "inicio": "00:06:15.000",
  "fim": "00:06:35.000",
  "momento_analise": "00:06:26.000",
  "tipo_analise": "slow_motion",
  "velocidade_slow": 0.5,
  "janela_analise_segundos": 3.0,
  "grafismos": [
    { "tipo": "circulo_tracking", "raio": 70, "bbox_inicial": [1008, 690, 108, 174] },
    { "tipo": "seta_alvo", "alvo_x": 1650, "alvo_y": 400 }
  ],
  "legenda_analise": "Aproveitar a defesa desorganizada"
}
```

Resultado esperado:

- Etapa 1: 11s (de 00:06:15 a 00:06:26), label visível por 5s
- Etapa 2a: 6s (3s de janela / 0,5 de velocidade)
- Etapa 2b: 6s (de 00:06:29 a 00:06:35)
- Etapa 3: 20s (duração total do clipe)
- Total: ~43s

### Exemplo válido — freeze sem tracking

```json
{
  "nome": "cobertura_defensiva_alves",
  "atleta": "Pedro Alves",
  "tipo": "ajuste",
  "label_abertura": "AJUSTE: Cobertura da linha defensiva",
  "inicio": "00:02:10.000",
  "fim": "00:02:25.000",
  "momento_analise": "00:02:16.000",
  "tipo_analise": "freeze",
  "duracao_freeze": 2.5,
  "grafismos": [
    { "tipo": "seta_tracejada", "x1": 500, "y1": 400, "x2": 280, "y2": 270 },
    { "tipo": "zona", "pontos": [[200,240],[380,240],[380,410],[200,410]] }
  ],
  "legenda_analise": "Fechar o corredor central"
}
```

### Caso-limite — janela de análise ultrapassa o fim do clipe

```json
{
  "inicio": "00:02:10.000",
  "fim": "00:02:25.000",
  "momento_analise": "00:02:23.000",
  "tipo_analise": "slow_motion",
  "velocidade_slow": 0.5,
  "janela_analise_segundos": 5.0
}
```

`t_rel = 13s`, `t_apos_analise = 13 + 5 = 18s > dur_clip = 15s` → etapa 2b omitida, sem erro.

### Caso inválido — `momento_analise` igual a `fim`

```json
{
  "inicio": "00:02:10.000",
  "fim": "00:02:25.000",
  "momento_analise": "00:02:25.000"
}
```

Resultado: `ValueError: momento_analise deve estar entre inicio e fim`. Clipe ignorado; próximo continua.

### Caso inválido — `tipo` incorreto

```json
{ "tipo": "erro_ortografico" }
```

Resultado: `ValueError: tipo deve ser 'acerto' ou 'ajuste'`. Clipe ignorado.

---

## 17. Glossário

| Termo | Definição |
| --- | --- |
| Pílula de análise | Clipe de vídeo curto, padronizado, focado em uma jogada tática individual |
| Grafismo | Elemento gráfico (círculo, seta, zona) sobreposto ao vídeo para destacar a ação |
| Tracking | Rastreamento automático da posição de um jogador quadro a quadro |
| CSRT | Channel and Spatial Reliability Tracking — algoritmo de rastreamento do OpenCV usado pelo script |
| bbox / bounding box | Retângulo delimitador `[x, y, largura, altura]` em pixels que define a posição inicial do jogador para o tracker |
| t_rel | Duração em segundos do trecho de abertura (`momento_analise - inicio`) |
| t_apos_analise | Instante, em segundos relativos ao início do clipe, após o qual começa a etapa 2b |
| dur_clip | Duração total do clipe (`fim - inicio`) em segundos |
| Etapa 1 | Segmento de abertura do clipe, de `inicio` até `momento_analise`, com label animado |
| Etapa 2a | Segmento de análise: câmera lenta ou freeze, com grafismos e legenda |
| Etapa 2b | Segmento de continuação após a análise, sem grafismos, em velocidade normal |
| Etapa 3 | Replay completo do clipe com badge "REPLAY" |
| Acento lateral | Faixa colorida no lado esquerdo do bloco de legenda, na cor primária do tipo do clipe |
| seta_alvo | Seta cujo ponto de origem acompanha o jogador rastreado e cuja ponta aponta para uma coordenada fixa da quadra |
