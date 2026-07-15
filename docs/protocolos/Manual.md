# Manual do script de edição de vídeos

## Finalidade

O script `editar_video.py` gera clipes de análise de desempenho esportivo a
partir de um vídeo. Cada clipe produzido contém três etapas:

1. abertura em velocidade normal, com uma identificação visual;
2. análise do momento-chave, em câmera lenta ou com quadro congelado;
3. repetição completa em velocidade normal.

As instruções deste manual usam o arquivo
[config_exemplo.json](config_exemplo.json) como referência.

## Pré-requisitos

Antes de executar o script, confirme que o ambiente possui:

- Python 3 com suporte à criação de ambientes virtuais;
- o vídeo indicado pelo campo `video_origem`;
- permissão para criar arquivos no diretório de saída;
- as dependências declaradas em
  [requirements.txt](requirements.txt).

Os exemplos abaixo usam o ambiente virtual `.venv` para isolar as dependências
do projeto.

## Início rápido

### 1. Instalar as dependências

Execute os comandos no diretório que contém o script:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

### 2. Preparar o arquivo de configuração

Crie uma cópia do [config_exemplo.json](config_exemplo.json), preserve a
extensão `.json` e ajuste seus campos. O arquivo precisa continuar sendo um
documento JSON válido.

### 3. Executar o script

```bash
.venv/bin/python editar_video.py config_exemplo.json
```

## Estrutura da configuração

O arquivo JSON possui campos globais e uma lista chamada `clipes`. Cada item de
`clipes` descreve um arquivo de vídeo que será gerado.

### Campos globais

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `video_origem` | Sim | Caminho do vídeo que será processado. |
| `diretorio_saida` | Não | Diretório de saída; padrão: `saida`. |
| `fps_saida` | Não | Quadros por segundo do vídeo final. O padrão é `30`. |
| `clipes` | Sim | Lista de objetos que descrevem os clipes. |

### Campos de cada clipe

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| `nome` | Sim | Nome do clipe e do arquivo `.mp4`. |
| `atleta` | Não | Nome do atleta, usado nas mensagens do terminal. |
| `tipo` | Sim | Classificação visual: `acerto` ou `ajuste`. |
| `label_abertura` | Sim | Texto exibido na abertura do clipe. |
| `inicio` | Sim | Início do trecho no vídeo original. |
| `fim` | Sim | Final do trecho no vídeo original. |
| `momento_analise` | Sim | Instante da análise, entre `inicio` e `fim`. |
| `tipo_analise` | Não | `slow_motion` ou `freeze`; padrão: `slow_motion`. |
| `velocidade_slow` | Não | Fator da câmera lenta. O padrão é `0.5`. |
| `janela_analise_segundos` | Não | Duração desacelerada; padrão: `2.0` s. |
| `duracao_freeze` | Não | Duração do quadro congelado. O padrão é `2.5`. |
| `grafismos` | Não | Lista de grafismos; padrão: `[]`. |
| `legenda_analise` | Não | Texto exibido durante a análise. |

Os campos de tempo aceitam uma marca no formato `HH:MM:SS.mmm` ou um número de
segundos. No arquivo de exemplo, todas as marcas usam o formato textual.

O fator de velocidade indica a proporção em relação à velocidade original:

| Valor | Efeito |
| --- | --- |
| `0.5` | Reproduz na metade da velocidade original. |
| `0.25` | Reproduz a um quarto da velocidade original. |

Use `null` nos parâmetros de análise que não se aplicam ao clipe. O script
substitui valores ausentes ou nulos pelos respectivos padrões quando necessário.

### Grafismos

As coordenadas são expressas em pixels do quadro do vídeo.

| Valor de `tipo` | Campos necessários | Resultado |
| --- | --- | --- |
| `circulo` | `x`, `y` e `raio` | Círculo com centro em `x` e `y`. |
| `seta` | `x1`, `y1`, `x2` e `y2` | Seta contínua. |
| `seta_tracejada` | `x1`, `y1`, `x2` e `y2` | Seta tracejada. |
| `zona` | `pontos` | Preenche o polígono definido pela lista de coordenadas. |

## Comandos de execução

Execute os comandos a partir do diretório que contém `editar_video.py`.

### Processar todos os clipes

```bash
.venv/bin/python editar_video.py config_exemplo.json
```

### Processar somente um clipe

O valor de `--clipe` deve corresponder ao campo `nome` de um item da lista
`clipes`.

```bash
.venv/bin/python editar_video.py config_exemplo.json --clipe infiltracao_silva
```

### Alterar o diretório de saída

O argumento `--saida` substitui o valor de `diretorio_saida` para a execução
atual.

```bash
.venv/bin/python editar_video.py config_exemplo.json --saida reuniao_07_14
```

## Validação da configuração

Antes de processar os vídeos, verifique a sintaxe do arquivo JSON:

```bash
.venv/bin/python -m json.tool config_exemplo.json > /dev/null
```

O comando termina sem mensagem quando o JSON é válido. Em ambientes que não
possuem `/dev/null`, execute-o sem o redirecionamento para exibir o JSON
formatado.

Essa validação verifica a sintaxe do JSON, mas não confirma a existência do
vídeo nem a validade de todos os campos exigidos pelo script.

## Resultado esperado

Para cada item processado de `clipes`, o script cria um arquivo com o padrão
`<diretorio_saida>/<nome>.mp4`. Na ausência de configuração específica, os
arquivos são gravados em `saida/` com `30` quadros por segundo.

Os vídeos usam os codecs H.264 para imagem e AAC para áudio. A compatibilidade
final com projetores ou aplicativos de mensagens depende do dispositivo usado
na reprodução.

Ao terminar, o terminal informa quantos clipes foram gerados e apresenta os
erros encontrados. Uma falha em um clipe é registrada sem impedir a tentativa
de processar os demais.
