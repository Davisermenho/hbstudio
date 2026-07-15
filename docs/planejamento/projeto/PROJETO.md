# EDITOR DE VIDEO -

O projeto não deve ser tratado como a criação genérica de um “editor de vídeo”. O escopo correto é:

> **Sistema automatizado de geração de clipes de análise técnico-tática em vídeo, configurado por dados estruturados e executado por linha de comando.**

Os arquivos em contexto já definen um protótipo funcional: `editar_video.py` recebe um arquivo de configuração, gera clipes com abertura, análise em câmera lenta ou congelamento, grafismos, continuação e replay; utiliza `inspecionar_frame.py` para coordenadas e tracking; e exporta MP4 para `saida/`. Portanto, a atividade necessária é **transformar esse script existente em um projeto de software formal, reproduzível, testável e validável**, não começar novamente do zero.

## Fatos confirmados

O projeto possui atualmente as seguintes definições técnicas:

* script principal: `editar_video.py`;
* ferramenta auxiliar: `inspecionar_frame.py`;
* entrada orientada por `config.json`;
* execução geral ou de um clipe específico por CLI;
* tipos de análise `slow_motion` e `freeze`;
* tipos de clipe `acerto` e `ajuste`;
* grafismos fixos e com tracking;
* uso de `bbox_inicial` para rastreamento;
* saída MP4 em `saida/`;
* ambiente Python em `.venv`;
* plataforma WSL2/Linux;
* dependência crítica `opencv-contrib-python`, necessária para o tracker CSRT.

O estado operacional (`STA-CUR-001`) foi corrigido na Fase 0 e registra os 4 clipes gerados em 2026-07-14 a partir do `config_exemplo.json`, com status `gerado — aguardando validacao visual`. A inconsistência documental foi resolvida.

## Ações necessárias para criar formalmente o projeto

## 1. Definir o problema e o escopo

Antes do código, criar uma especificação curta e objetiva.

### Objetivo

Gerar automaticamente pílulas de análise técnico-tática a partir de vídeos de jogos, para:

* reuniões coletivas;
* correções individuais;
* apresentação de acertos;
* explicação visual de decisões táticas;
* compartilhamento controlado com atletas.

### Entradas

* arquivo de vídeo;
* timestamps do clipe;
* identificação pseudonimizada do atleta;
* tipo do clipe;
* tipo de análise;
* textos;
* grafismos;
* coordenadas;
* parâmetros de tracking;
* parâmetros de exportação.

### Saídas

* clipe MP4;
* log da execução;
* relatório de validação;
* metadados do arquivo gerado;
* registro de falhas, advertências e parâmetros usados.

### Fora do escopo inicial

O MVP não deve tentar ser:

* editor não linear completo;
* substituto do DaVinci Resolve, Premiere ou CapCut;
* sistema automático de decisão tática;
* reconhecimento facial;
* ferramenta de scout completa;
* aplicação web ou móvel;
* gerador automático de coordenadas sem validação humana.

Isso impede crescimento descontrolado do escopo.

## 2. Registrar os requisitos funcionais

Criar `docs/REQUISITOS.md` ou documento equivalente.

### Requisitos mínimos

O sistema deve:

1. receber um vídeo e uma configuração válida;
2. validar todos os parâmetros antes da renderização;
3. recortar o intervalo correto;
4. inserir abertura com label;
5. aplicar `slow_motion` ou `freeze`;
6. desenhar grafismos;
7. continuar o clipe após a análise;
8. gerar replay completo;
9. exportar MP4;
10. permitir processar todos os clipes ou apenas um;
11. não sobrescrever arquivos silenciosamente;
12. registrar sucesso ou erro de cada clipe;
13. produzir mensagens compreensíveis quando a configuração for inválida;
14. continuar processando outros clipes quando uma falha isolada permitir;
15. preservar o vídeo original.

## Requisitos não funcionais

* execução reproduzível;
* configuração versionada;
* validação automática;
* logs estruturados;
* tratamento seguro de paths;
* baixo acoplamento entre renderização, tracking e configuração;
* testes sem depender sempre de vídeos completos;
* compatibilidade documentada com WSL2/Linux;
* proteção dos dados e imagens de atletas menores de idade;
* saída visual verificável.

---

## 3. Definir critérios de aceitação

Cada requisito precisa de evidência observável.

Exemplos:

| Requisito             | Critério de aceitação                                         |
| --------------------- | ------------------------------------------------------------- |
| Carregar configuração | Arquivo válido é aceito; inválido retorna erro específico     |
| Recortar vídeo        | Início e fim permanecem dentro da tolerância definida         |
| Slow motion           | Janela correta é desacelerada sem quebrar áudio ou duração    |
| Freeze                | Frame correto permanece congelado pela duração configurada    |
| Tracking              | Grafismo acompanha o alvo ou declara perda de tracking        |
| Replay                | Replay aparece depois da sequência principal                  |
| Exportação            | MP4 abre no player e possui vídeo reproduzível                |
| Execução individual   | `--clipe nome` processa somente o clipe solicitado            |
| Falha isolada         | Um clipe inválido não corrompe os demais                      |
| Log                   | Toda execução registra parâmetros, resultado e arquivo gerado |

“Arquivo criado” não é aceitação suficiente. O vídeo precisa ser aberto e inspecionado.

---

## 4. Definir a arquitetura do projeto

O código não deve permanecer concentrado em um único `editar_video.py`.

Estrutura recomendada:

```text
editor-video/
├── pyproject.toml
├── uv.lock
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
├── src/
│   └── editor_video/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── models.py
│       ├── validation.py
│       ├── timeline.py
│       ├── renderer.py
│       ├── exporter.py
│       ├── tracking.py
│       ├── logging_config.py
│       ├── errors.py
│       └── graphics/
│           ├── circle.py
│           ├── arrow.py
│           ├── zone.py
│           ├── labels.py
│           └── tracking_graphics.py
├── scripts/
│   ├── editar_video.py
│   └── inspecionar_frame.py
├── schemas/
│   └── video_config.schema.json
├── configs/
│   ├── config.example.json
│   └── README.md
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contracts/
│   ├── fixtures/
│   └── golden/
├── samples/
│   └── README.md
├── docs/
│   ├── REQUISITOS.md
│   ├── ARQUITETURA.md
│   ├── CONFIGURACAO.md
│   ├── OPERACAO.md
│   ├── VALIDACAO_VISUAL.md
│   └── PRIVACIDADE.md
├── entrada/
├── saida/
├── temporarios/
└── logs/
```

### Responsabilidades

* `cli.py`: argumentos e comandos;
* `config.py`: carregamento da configuração;
* `models.py`: modelos de dados;
* `validation.py`: validação semântica;
* `timeline.py`: segmentos, análise, continuação e replay;
* `renderer.py`: composição visual;
* `tracking.py`: CSRT e estado do rastreamento;
* `exporter.py`: codecs, arquivos e metadados;
* `graphics/`: implementação isolada de cada grafismo;
* `errors.py`: exceções específicas;
* `logging_config.py`: logs estruturados.

---

## 5. Criar o contrato de configuração

O `config.json` deve deixar de ser apenas um exemplo informal e se tornar um contrato versionado.

### Artefatos necessários

* `schemas/video_config.schema.json`;
* `configs/config.example.json`;
* modelos Python equivalentes;
* validação semântica adicional;
* versão explícita do contrato.

Exemplo conceitual:

```json
{
  "schema_version": "1.0.0",
  "video": {
    "arquivo": "entrada/jogo.mp4"
  },
  "exportacao": {
    "diretorio": "saida",
    "resolucao": "source",
    "fps": "source"
  },
  "clipes": [
    {
      "id": "clip-001",
      "nome": "cobertura_defensiva",
      "atleta_id": "ATL-015",
      "inicio": "00:06:20.000",
      "fim": "00:06:32.000",
      "tipo": "ajuste",
      "tipo_analise": "freeze",
      "momento_analise": "00:06:26.000",
      "duracao_freeze": 2.5,
      "grafismos": []
    }
  ]
}
```

### Validações semânticas

O JSON Schema sozinho não resolve tudo. O código também deve verificar:

* início menor que fim;
* análise dentro do intervalo do clipe;
* `duracao_freeze` presente somente quando aplicável;
* `velocidade_slow` válida;
* coordenadas dentro das dimensões do vídeo;
* `bbox_inicial` não vazia;
* IDs de clipes únicos;
* nomes de saída seguros;
* paths restritos às pastas permitidas;
* grafismos compatíveis com o tipo de análise.

---

## 6. Definir a pipeline de processamento

A sequência deve ser documentada e implementada de forma determinística:

```text
CLI
  ↓
Carregar configuração
  ↓
Validar schema
  ↓
Validar regras semânticas
  ↓
Inspecionar metadados do vídeo
  ↓
Construir timeline do clipe
  ↓
Recortar trecho
  ↓
Aplicar label inicial
  ↓
Aplicar slow motion ou freeze
  ↓
Aplicar grafismos
  ↓
Continuar vídeo
  ↓
Gerar replay
  ↓
Compor áudio
  ↓
Exportar MP4
  ↓
Validar arquivo
  ↓
Registrar log e manifesto
```

Cada etapa deve receber dados e retornar resultados explícitos. Evitar funções que façam recorte, tracking, grafismo e exportação simultaneamente.

---

## 7. Formalizar o sistema de grafismos

Cada grafismo precisa de contrato próprio.

### Tipos já previstos

* `circulo`;
* `circulo_tracking`;
* `seta`;
* `seta_tracking`;
* `seta_alvo`;
* `seta_tracejada`;
* `zona`.

### Para cada tipo, definir

* parâmetros obrigatórios;
* parâmetros opcionais;
* sistema de coordenadas;
* comportamento durante resize;
* cor por tipo de clipe;
* espessura;
* opacidade;
* duração;
* animação de entrada e saída;
* tratamento de coordenada inválida;
* comportamento quando o tracking é perdido.

Não espalhar condições como `if tipo == "seta"` por todo o código. Cada grafismo deve implementar uma interface comum de renderização.

---

## 8. Estruturar o tracking

O tracking é uma parte de alto risco.

### Ações

1. encapsular o CSRT em módulo próprio;
2. validar a bounding box inicial;
3. registrar confiança ou falha por frame;
4. definir política para perda do alvo;
5. permitir fallback para posição fixa;
6. impedir que grafismos “saltem” para outro atleta;
7. testar mudança de iluminação, oclusão e câmera;
8. permitir correção manual de keyframes em versões futuras.

### Estados recomendados

* `TRACKING_OK`;
* `TRACKING_INSTAVEL`;
* `TRACKING_PERDIDO`;
* `BBOX_INVALIDA`;
* `FALLBACK_FIXO_APLICADO`.

O sistema não deve fingir que o tracking funcionou quando o alvo foi perdido.

---

## 9. Definir áudio e codecs

Decisões necessárias:

* manter áudio original ou remover;
* comportamento do áudio durante slow motion;
* silêncio durante freeze;
* normalização ou não;
* codec de vídeo;
* codec de áudio;
* pixel format;
* resolução;
* FPS;
* qualidade;
* compatibilidade com WhatsApp.

Recomendação inicial:

* vídeo H.264;
* áudio AAC;
* pixel format `yuv420p`;
* resolução preservada;
* FPS preservado;
* opção de saída otimizada para WhatsApp.

Esses valores devem ser configuráveis e registrados no log.

---

## 10. Implementar observabilidade

Cada execução deve gerar um registro estruturado.

Exemplo:

```json
{
  "run_id": "RUN-2026-07-15-001",
  "config_schema_version": "1.0.0",
  "video_entrada": "entrada/jogo.mp4",
  "video_sha256": "...",
  "iniciado_em": "...",
  "finalizado_em": "...",
  "clipes_solicitados": 3,
  "clipes_gerados": 2,
  "clipes_com_falha": 1,
  "resultados": [
    {
      "id": "clip-001",
      "status": "GERADO_AGUARDANDO_VALIDACAO_VISUAL",
      "arquivo": "saida/ATL-015_cobertura_defensiva.mp4"
    }
  ]
}
```

Estados recomendados:

* `CONFIGURADO`;
* `VALIDADO`;
* `EM_PROCESSAMENTO`;
* `GERADO_AGUARDANDO_VALIDACAO_VISUAL`;
* `APROVADO`;
* `REPROVADO`;
* `FALHA_DE_CONFIGURACAO`;
* `FALHA_DE_TRACKING`;
* `FALHA_DE_RENDERIZACAO`.

---

## 11. Criar a estratégia de testes

### Testes unitários

Validar isoladamente:

* parser de timestamps;
* validação de configuração;
* nomes de saída;
* cálculo de timeline;
* seleção de cores;
* escala de coordenadas;
* parâmetros de grafismos;
* tratamento de erros;
* geração de comandos de renderização.

### Testes de contrato

* configuração válida;
* campo obrigatório ausente;
* enum inválido;
* timestamp inválido;
* bbox inválida;
* ID duplicado;
* configuração de `freeze`;
* configuração de `slow_motion`.

### Testes de integração

* processar pequeno vídeo sintético;
* gerar clipe sem grafismo;
* gerar clipe com freeze;
* gerar slow motion;
* gerar replay;
* processar somente um clipe;
* processar múltiplos clipes;
* simular perda de tracking.

### Golden tests

Manter pequenos arquivos de referência e comparar:

* duração;
* resolução;
* FPS;
* número de frames;
* presença de trechos esperados;
* hashes de frames selecionados;
* imagens de referência de pontos críticos.

O hash do MP4 inteiro pode variar entre versões do encoder; a validação deve considerar metadados e frames de referência.

### Validação visual humana

Obrigatória para:

* posição dos grafismos;
* legibilidade das legendas;
* tracking do atleta correto;
* momento exato do freeze;
* significado tático;
* ritmo da apresentação;
* ausência de exposição inadequada.

---

## 12. Criar fixtures seguras

Os testes não devem depender sempre do vídeo integral de uma partida.

Criar:

* vídeo sintético curto;
* amostra pseudonimizada;
* imagem de quadra fictícia;
* objeto em movimento para tracking;
* configs válidas e inválidas;
* bbox conhecida;
* saída visual esperada.

Vídeos reais com atletas devem ficar fora do repositório público e ser protegidos por `.gitignore`.

---

## 13. Gerenciar dependências e reprodutibilidade

Ações necessárias:

1. definir versão mínima e máxima do Python;
2. declarar dependências em `pyproject.toml`;
3. manter arquivo de lock;
4. separar dependências de produção e desenvolvimento;
5. registrar versão do OpenCV;
6. verificar disponibilidade do backend de vídeo;
7. validar codec e executáveis externos;
8. criar comando único de instalação;
9. criar comando único de verificação do ambiente.

Exemplo de interface:

```bash
uv sync
uv run editor-video doctor
uv run editor-video validate configs/config.example.json
uv run editor-video render configs/config.example.json
```

O comando `doctor` deve verificar:

* Python;
* OpenCV contrib;
* FFmpeg ou backend equivalente;
* codecs;
* permissões;
* pastas;
* leitura do vídeo;
* escrita em `saida/`.

---

## 14. Criar qualidade automática

Pipeline mínimo:

```text
formatação
→ lint
→ análise de tipos
→ validação de schemas
→ testes unitários
→ testes de contrato
→ testes de integração
→ relatório
```

Ferramentas possíveis:

* Ruff;
* mypy ou Pyright;
* pytest;
* coverage;
* jsonschema;
* pre-commit;
* CI no GitHub Actions.

Critério de gate:

* lint sem erro;
* análise de tipos aprovada;
* schemas válidos;
* testes aprovados;
* cobertura mínima definida;
* nenhuma dependência crítica ausente;
* amostra renderizada com sucesso.

---

## 15. Documentar operação e recuperação de falhas

O `README.md` precisa conter:

* finalidade;
* limites;
* instalação;
* estrutura;
* preparação do vídeo;
* inspeção de frames;
* preenchimento da configuração;
* execução;
* validação;
* solução de erros;
* privacidade;
* exemplos.

Criar também um guia operacional:

```text
1. Copiar vídeo para entrada/
2. Inspecionar timestamps
3. Executar inspecionar_frame.py
4. Registrar bbox e coordenadas
5. Preencher config
6. Validar config
7. Gerar clipe de teste
8. Inspecionar visualmente
9. Corrigir parâmetros
10. Gerar lote final
11. Registrar aprovação
12. Compartilhar por canal autorizado
```

---

## 16. Definir segurança e privacidade

Como os vídeos podem conter atletas menores de idade, são necessárias ações específicas:

* pseudonimizar IDs em configurações e testes;
* não versionar vídeos reais;
* não registrar nomes completos em logs desnecessários;
* não enviar vídeos a serviços externos sem autorização;
* remover metadados sensíveis quando aplicável;
* controlar destino dos arquivos;
* definir política de retenção;
* impedir path traversal;
* restringir leitura e escrita às pastas do projeto;
* registrar quem aprovou o compartilhamento.

A ferramenta deve apoiar a comissão sem substituir a decisão técnica e sem tratar conteúdo gerado automaticamente como análise aprovada. Essa separação entre execução, verificação e aceitação é exigida pela política operacional do projeto.

## 17. Criar governança de versões

Artefatos necessários:

* `CHANGELOG.md`;
* versionamento semântico;
* registro das versões do schema;
* política de migração das configurações;
* depreciação controlada de campos;
* tags de release;
* manifesto de cada execução.

Exemplo:

* `0.1.0`: recorte, label e replay;
* `0.2.0`: freeze e slow motion;
* `0.3.0`: grafismos fixos;
* `0.4.0`: tracking;
* `0.5.0`: validação, logs e lotes;
* `1.0.0`: contrato estável e pipeline validado.

## Matriz de capacidade

| Ação                           | Classificação      | Responsável principal | Validação                 |
| ------------------------------ | ------------------ | --------------------- | ------------------------- |
| Especificar requisitos         | `ASSISTIDA`        | Davi + IA             | Revisão de escopo         |
| Criar arquitetura              | `AUTO/ASSISTIDA`   | IA                    | Revisão técnica           |
| Criar estrutura do repositório | `AUTO`             | IA/agente de código   | Inventário dos arquivos   |
| Gerar JSON Schema              | `AUTO`             | IA                    | Testes de contrato        |
| Implementar módulos            | `AUTO`             | Agente de código      | Testes e análise estática |
| Definir timestamps táticos     | `MANUAL`           | Davi                  | Conferência no vídeo      |
| Selecionar atleta e bbox       | `MANUAL/ASSISTIDA` | Davi + ferramenta     | Inspeção do frame         |
| Executar tracking              | `AUTO`             | Script                | Log por frame             |
| Validar interpretação tática   | `MANUAL`           | Daniela/Davi          | Aprovação técnica         |
| Validar resultado visual       | `ASSISTIDA`        | Davi + IA             | Inspeção do MP4           |
| Compartilhar com atletas       | `MANUAL`           | Comissão              | Canal autorizado          |
| Declarar projeto concluído     | `ASSISTIDA`        | Davi + IA             | Todos os gates aprovados  |

## Ordem recomendada de implementação

## Fase 0 — Saneamento

* reconciliar a inconsistência de `videos_disponiveis` no `STA-CUR-001`;
* inventariar o código existente;
* registrar dependências e versões;
* identificar amostra, configuração e saída esperada;
* preservar uma baseline reproduzível.

## Fase 1 — Contratos

* requisitos;
* arquitetura;
* JSON Schema;
* modelos de dados;
* CLI;
* critérios de aceitação.

## Fase 2 — Núcleo determinístico

* leitura de vídeo;
* recorte;
* timeline;
* label;
* freeze;
* slow motion;
* replay;
* exportação.

## Fase 3 — Grafismos fixos

* círculo;
* seta;
* seta tracejada;
* zona;
* textos e badges.

## Fase 4 — Tracking

* CSRT;
* círculo com tracking;
* setas relacionadas ao alvo;
* perda e recuperação do rastreamento.

## Fase 5 — Qualidade

* testes;
* lint;
* tipos;
* logs;
* validação de saída;
* fixtures;
* CI.

## Fase 6 — Homologação esportiva

* selecionar lances reais;
* gerar clipes;
* validar com Davi;
* submeter interpretação técnica à Daniela;
* corrigir ritmo, grafismos e textos;
* aprovar fluxo operacional.

## Fase 7 — Release

* documentação;
* versão;
* changelog;
* pacote;
* instruções de instalação;
* política de privacidade;
* exemplo funcional;
* release `1.0.0`.

## Critério para considerar o projeto concluído

O projeto somente estará concluído quando:

1. o ambiente puder ser recriado;
2. a configuração possuir contrato validado;
3. todos os tipos de análise funcionarem;
4. os grafismos previstos estiverem testados;
5. falhas de tracking forem detectadas;
6. os testes automatizados passarem;
7. um vídeo real for processado;
8. a saída for inspecionada visualmente;
9. a comissão validar a utilidade técnica;
10. a documentação permitir nova execução sem reconstruir o conhecimento;
11. a privacidade dos atletas estiver protegida;
12. execução, verificação e aceitação estiverem registradas separadamente.

**Fase 0 concluída em 2026-07-15.** `Better_IA.md` foi validado como parte obrigatória do fluxo. `ESPECIFICACAO.md` foi validado como especificação v1.0 com 17 seções completas. As 4 inconsistências do inventário foram corrigidas. Próximo passo: **Fase 1 — Contratos**.
