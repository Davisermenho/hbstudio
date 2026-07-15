# Inventário da baseline 0.4.0

Data: 2026-07-15
Versão registrada: `VERSION` → `0.4.0`
Git: repositório inicializado, sem commits

---

## 1. Estrutura de arquivos

### Scripts Python

| Arquivo | Linhas | Função |
| --- | --- | --- |
| `scripts/editor/editar_video.py` | 691 | Script principal — CLI, pipeline, grafismos, tracking, exportação |
| `scripts/editor/inspecionar_frame.py` | 130 | Ferramenta auxiliar — extrai frame e captura bbox via matplotlib |
| `scripts/validate_changelog.py` | — | Validador de entradas do CHANGELOG |
| `tests/test_validate_changelog.py` | — | Testes do validador de changelog |

### Configuração e dependências

| Arquivo | Conteúdo |
| --- | --- |
| `config_exemplo.json` | 4 clipes: `lance_01_transicao_bebe`, `lance_02_leitura_goleiro`, `lance_03_1x1_continuidade`, `lance_05_transicao_iago` — todos `slow_motion`, sem grafismos, sem tracking |
| `requirements.txt` | moviepy==1.0.3, Pillow>=10, numpy>=1.24, opencv-contrib-python>=4.8, matplotlib>=3.7 |
| `.gitignore` | Exclui `.venv/`, `videos/`, `saida/`, `entrada/`, `*.mp4`, `frame_*.png`, `logs/*.jsonl` |

### Versão e changelog

| Arquivo | Conteúdo |
| --- | --- |
| `VERSION` | `0.4.0` |
| `CHANGELOG.md` | Uma entrada: `[0.4.0] — 2026-07-15`, baseline importada, aguardando aprovação |
| `changes/CHG-2026-001.json` | Registro estruturado da baseline |
| `changes/baselines/0.4.0.sha256` | Hash de referência da baseline |

### Documentação

| Arquivo | Conteúdo |
| --- | --- |
| `docs/planejamento/projeto/PROJETO.md` | Escopo, arquitetura, fases e critérios de conclusão do projeto |
| `docs/planejamento/projeto/ESPECIFICACAO.md` | Especificação v1.0 com 20 RFs, 7 RNFs, 7 RNs, 8 erros, 17 seções |
| `docs/planejamento/projeto/logs.md` | — |
| `docs/planejamento/design/DESIGN SYSTEM.md` | — |
| `docs/planejamento/design/interface.md` | — |
| `docs/protocolos/Better_IA.md` | Metodologia de colaboração com IA |
| `docs/protocolos/Manual.md` | — |
| `docs/protocolos/PROTOCOLO.md` | — |
| `docs/protocolos/Python_valid.md` | — |
| `docs/protocolos/RECORTES.md` | — |
| `docs/changelog/RELEASE.md` | Processo de release |
| `docs/changelog/ROLLBACK.md` | Processo de rollback |
| `docs/changelog/VERSIONAMENTO.md` | Política de versionamento |
| `contexto/ESTADO_OPERACIONAL.md` | Estado diário, pendências e próximo jogo |
| `contexto/AGENT_POLICY.md` | Políticas para agentes de IA |
| `contexto/CONTEXT.md` | Contexto geral do projeto |
| `contexto/FERRAMENTAS_TECNICAS.md` | Ferramentas técnicas disponíveis |
| `contexto/PROGRAMACAO_COMPETICAO.md` | Programação da competição |

### CI

| Arquivo | Conteúdo |
| --- | --- |
| `.github/workflows/changelog.yml` | Validação automática do changelog no CI |

---

## 2. Ambiente instalado

| Componente | Versão instalada | Versão em requirements.txt |
| --- | --- | --- |
| Python | 3.12.3 | não fixado |
| moviepy | 1.0.3 | ==1.0.3 ✅ |
| Pillow | 12.3.0 | >=10.0.0 ✅ |
| numpy | 2.5.1 | >=1.24.0 ✅ |
| opencv-contrib-python | 5.0.0 | >=4.8.0 ✅ |
| matplotlib | 3.11.0 | >=3.7.0 ✅ |

**TrackerCSRT disponível:** sim — via `cv2.legacy.TrackerCSRT_create`. O OpenCV 5.x moveu os trackers legados para o submódulo `cv2.legacy`; o código em `rastrear_jogador` lida com isso corretamente pelo fallback `hasattr`.

---

## 3. Vídeos e saídas

### Vídeo-fonte

| Arquivo | Tamanho | Data |
| --- | --- | --- |
| `videos/ACISEG_35x24_IDEC_2026-07-13/ACISEG_35x24_IDEC_2026-07-13.mp4` | 679 MB | 2026-07-14 |

### Arquivos MP4 gerados em `saida/`

| Arquivo | Tamanho | Data | Origem |
| --- | --- | --- | --- |
| `infiltracao_bebe.mp4` | 31 MB | 2026-07-14 | Config anterior — não rastreável pela documentação atual |
| `lance_01_transicao_bebe.mp4` | 31 MB | 2026-07-14 | `config_exemplo.json` ✅ |
| `lance_02_leitura_goleiro.mp4` | 23 MB | 2026-07-14 | `config_exemplo.json` ✅ |
| `lance_03_1x1_continuidade.mp4` | 19 MB | 2026-07-14 | `config_exemplo.json` ✅ |
| `lance_05_transicao_iago.mp4` | 20 MB | 2026-07-14 | `config_exemplo.json` ✅ |

**Observação:** `infiltracao_bebe.mp4` foi gerado por uma config anterior sem registro. Não deve ser usado como referência de saída da baseline 0.4.0.

---

## 4. Conformidade do código com a especificação

### Requisitos funcionais

| ID | Descrição | Status |
| --- | --- | --- |
| RF-001 | Parsing do JSON | ✅ implementado — ❌ sem mensagem formatada para arquivo inexistente ou malformado (traceback Python nativo — diverge de ERR-001 e ERR-002) |
| RF-002 | Criar diretório de saída | ✅ — `mkdir(parents=True, exist_ok=True)` |
| RF-003 | Filtro `--clipe` | ✅ — `sys.exit` com mensagem formatada |
| RF-004 | Validação de `tipo` | ✅ — `ValueError` com mensagem descritiva |
| RF-005 | Validação de `momento_analise` | ✅ implementado |
| RF-006 | Etapa 1 — abertura com label animado | ✅ — slide + fade + badge + cor por tipo |
| RF-007 | Etapa 2a — slow motion | ✅ — `vfx.speedx` |
| RF-008 | Etapa 2a — freeze | ✅ — `to_ImageClip` |
| RF-009 | Etapa 2b — continuação | ✅ — omitida sem erro quando não há trecho restante |
| RF-010 | Etapa 3 — replay com badge | ✅ implementado |
| RF-011 | Grafismo `circulo` | ✅ implementado |
| RF-012 | Grafismo `circulo_tracking` | ✅ implementado |
| RF-013 | Grafismo `seta` | ✅ implementado |
| RF-014 | Grafismo `seta_tracking` | ✅ implementado |
| RF-015 | Grafismo `seta_alvo` | ✅ implementado |
| RF-016 | Grafismo `seta_tracejada` | ✅ implementado |
| RF-017 | Grafismo `zona` | ✅ implementado |
| RF-018 | Rastreamento CSRT com limite de deslocamento | ✅ — rejeita saltos > 50 px |
| RF-019 | Isolamento de erros por clipe | ✅ — `try/except` por clipe, sumário final |
| RF-020 | Exportação MP4 | ✅ — codec `libx264`, áudio `aac` |

### Requisitos não funcionais

| ID | Descrição | Status |
| --- | --- | --- |
| RNF-001 | Não modificar vídeo-fonte | ✅ — o script nunca escreve no vídeo-fonte |
| RNF-002 | Erro em clipe não apaga saídas anteriores | ✅ — arquivos escritos individualmente |
| RNF-003 | Mensagens de erro identificam o clipe e a causa | ✅ — `[ERRO] {nome}: {mensagem}` |
| RNF-004 | Execução reproduzível | ✅ — sem estado externo ou aleatório |
| RNF-005 | Stdout para progresso, stderr para erros | ✅ stdout/stderr separados — ⚠️ linha de progresso inclui nome do atleta (ver INC-002) |
| RNF-006 | Compatibilidade WSL2 | ✅ — usa `pathlib.Path`, sem dependência de paths Windows |
| RNF-007 | Nome do atleta não aparece em nomes de arquivo | ✅ nome do arquivo é `{nome}.mp4` — ❌ nome do atleta aparece na linha de progresso (ver INC-002) |

---

## 5. Inconsistências identificadas

### INC-001 — Divergência entre `ESTADO_OPERACIONAL.md` e `config_exemplo.json`

`STA-CUR-001` em `contexto/ESTADO_OPERACIONAL.md` lista três clipes como "configurados":

- `infiltracao_bebe`
- `cobertura_defensiva_alves`
- `gol_assistencia_santos`

O `config_exemplo.json` contém quatro clipes diferentes:

- `lance_01_transicao_bebe`
- `lance_02_leitura_goleiro`
- `lance_03_1x1_continuidade`
- `lance_05_transicao_iago`

`infiltracao_bebe.mp4` existe em `saida/` mas não tem config rastreável. `cobertura_defensiva_alves` e `gol_assistencia_santos` não têm arquivo de saída nem config.

**Ação necessária:** atualizar `ESTADO_OPERACIONAL.md` para refletir o estado real — os 4 lances do `config_exemplo.json` e as 4 saídas geradas em 2026-07-14.

### INC-002 — Nome do atleta no progresso vs RNF-007

A linha de progresso atual em `scripts/editor/editar_video.py` (linha 660):

```text
[1/4] Processando: lance_01_transicao_bebe (Bebê) ...
```

SAI-002 na especificação também exibe o nome do atleta entre parênteses. RNF-007 diz que o campo `atleta` não deve aparecer em mensagens de progresso.

**Decisão necessária:** suprimir o nome do atleta na linha de progresso (alinhar com RNF-007), ou relaxar RNF-007 para permitir pseudônimos visíveis no terminal local — ambiente de uso privado e sem log persistente.

### INC-003 — Tratamento de ERR-001, ERR-002 e ERR-006

`scripts/editor/editar_video.py` usa `open(args.config)` e `json.load(f)` diretamente sem `try/except` — gera traceback Python nativo para arquivo inexistente ou JSON malformado. O vídeo-fonte é aberto via `VideoFileClip(video_origem)` sem catch — gera erro do moviepy.

**Ação necessária:** envolver as três operações em blocos `try/except` com as mensagens formatadas definidas em ERR-001, ERR-002 e ERR-006 da especificação.

---

## 6. O que foi resolvido nesta revisão

| Item | Status |
| --- | --- |
| Arquivo residual `/=4.8.0` | ✅ removido |
| Reorganização da estrutura de `docs/` | ✅ concluída |
| Scripts movidos para `scripts/editor/` | ✅ concluído |
| INC-004 do inventário anterior | ✅ encerrado |
| INC-001 — `ESTADO_OPERACIONAL.md` desatualizado | ✅ corrigido — `videos_disponiveis` atualizado para os 4 lances reais |
| INC-002 — Nome do atleta no progresso (stdout) | ✅ resolvido — suprimido; linha de progresso exibe somente `{nome}` |
| INC-003 — ERR-001, ERR-002 e ERR-006 sem mensagem formatada | ✅ resolvido — `try/except` adicionado para `FileNotFoundError` e `JSONDecodeError` |

---

## 7. O que não existe ainda

Estrutura prevista em `docs/planejamento/projeto/PROJETO.md` ainda ausente:

- `src/editor_video/` — módulos separados (cli, config, models, validation, timeline, renderer, exporter, tracking, graphics/)
- `schemas/video_config.schema.json`
- `configs/config.example.json`
- `tests/unit/`, `tests/integration/`, `tests/contracts/`, `tests/golden/`
- `samples/`
- `docs/planejamento/projeto/REQUISITOS.md`
- `docs/planejamento/projeto/ARQUITETURA.md`
- `docs/planejamento/projeto/CONFIGURACAO.md`
- `docs/planejamento/projeto/OPERACAO.md`
- `docs/planejamento/projeto/VALIDACAO_VISUAL.md`
- `docs/planejamento/projeto/PRIVACIDADE.md`
- `entrada/`, `temporarios/`, `logs/`
- `pyproject.toml`

---

## 8. Baseline verificável

O protótipo é funcional para o conjunto de clipes testado (4 clipes `slow_motion` sem grafismos, sem tracking). As funcionalidades de grafismos fixos e tracking existem no código mas não foram exercidas pelo `config_exemplo.json` atual.

Para considerar a baseline 0.4.0 formalmente aprovada, faltam:

1. Corrigir INC-001 — atualizar `ESTADO_OPERACIONAL.md`
2. Decidir INC-002 — nome do atleta no progresso
3. Implementar INC-003 — mensagens formatadas para ERR-001, ERR-002 e ERR-006
4. Registrar validação visual dos 4 clipes gerados por Davi ou Daniela
