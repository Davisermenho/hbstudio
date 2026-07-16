# Plano patch/diff para `ENGENHARIA.md`

## 1. Controle do plano

```yaml
plano_id: PATCH-ENG-001
tipo: implementacao_documental
alvo_primario: ENGENHARIA.md
fontes_canonicas:
  - notion:CONTEXT.md
  - notion:AGENT_POLICY.md
  - notion:FERRAMENTAS_TECNICAS
estado_inicial:
  linhas: 521
  palavras: 1506
  sha256: 961cc09075522af02672e65a55a8a39063b29a5b1cd4a9e3f5d7f7d7c6974226
  markdownlint_erros: 11
estado_do_plano: pronto_para_implementacao
aprovacao_de_conteudo_final: pendente
```

Este plano transforma a revisão corrigida em ações verificáveis. Ele não autoriza
automaticamente a criação ou a alteração de páginas no Notion. Alterações
persistentes no Notion dependem de autorização explícita e devem ser validadas por
releitura da página modificada.

## 2. Resultado esperado

Ao concluir todas as ações, `ENGENHARIA.md` deve:

- identificar-se inequivocamente como proposta de consolidação técnica;
- usar as páginas do Notion como fontes documentais canônicas;
- distinguir inventário factual de política operacional;
- não duplicar as regras já existentes em `AGENT_POLICY.md`;
- apresentar hierarquia, listas, tabelas, links e blocos de código válidos;
- separar estados de inventário dos estados de execução;
- registrar decisões, pendências, evidências e critérios de conclusão;
- passar pelas verificações sintáticas, semânticas e factuais deste plano.

## 3. Fontes canônicas e precedência

<!-- markdownlint-disable MD013 -->

| Prioridade | Fonte | Uso durante a implementação |
| --- | --- | --- |
| 1 | [`CONTEXT.md`](https://app.notion.com/p/39cf2ae06fc88051bb8fee62048b5551) | Identidade, autoridade, escopo e rotas documentais |
| 2 | [`AGENT_POLICY.md`](https://app.notion.com/p/39cf2ae06fc880a39fc1cb1e32dfb08e) | Políticas, capacidade, execução, verificação e aceitação |
| 3 | [`FERRAMENTAS_TECNICAS`](https://app.notion.com/p/39df2ae06fc88090b281e57896fbe8a2) | Scripts e ambiente especializado de edição de vídeo |
| 4 | Evidência atual do ambiente | Versões, caminhos, ferramentas e capacidades observadas |
| 5 | `ENGENHARIA.md` | Proposta e consolidação; nunca substitui evidência mais atual |

<!-- markdownlint-enable MD013 -->

Se uma afirmação de `ENGENHARIA.md` divergir das fontes 1–3, a implementação deve
corrigir a afirmação ou marcá-la como pendente. A ausência de resultado em uma busca
no Notion não deve ser apresentada como prova absoluta de inexistência.

## 4. Convenção de cada ação

Cada ação possui:

- **Patch:** mudança a aplicar;
- **Critérios de aceitação:** condições individualmente observáveis;
- **Verificação:** procedimento que produz evidência;
- **Validação:** decisão sobre a suficiência da evidência;
- **Bloqueio:** condição que impede marcar a ação como concluída.

Estados permitidos para as ações deste plano:

- `NÃO INICIADA`;
- `EM EXECUÇÃO`;
- `EXECUTADA — AGUARDANDO VALIDAÇÃO`;
- `VALIDADA`;
- `BLOQUEADA`;
- `NÃO APLICÁVEL`.

## 5. Ações de implementação

### PATCH-ENG-001 — Preservar a linha de base

**Patch:** antes de editar, registrar hash, contagem de linhas, estado do Git e
resultado inicial do `markdownlint`. Não modificar arquivos não relacionados.

```diff
 sem alteração em ENGENHARIA.md nesta ação
+ evidência: hash, contagem, git status e relatório inicial do markdownlint
```

**Critérios de aceitação:**

- [ ] O SHA-256 anterior à edição está registrado.
- [ ] O estado inicial do `markdownlint` está preservado.
- [ ] Mudanças preexistentes do usuário estão identificadas e não foram removidas.

**Verificação:** executar `sha256sum ENGENHARIA.md`, `wc -l -w -c
ENGENHARIA.md` e `git status --short`.

**Validação:** comparar os resultados com o bloco `estado_inicial` deste plano.

**Bloqueio:** hash divergente sem explicação ou sobreposição não controlada com
alteração concorrente do usuário.

### PATCH-ENG-002 — Corrigir a identidade do documento

**Patch:** substituir o título que apresenta a proposta como documento canônico.

```diff
-# ENGINEERING_CONTEXT.md
+# Proposta de criação do `ENGINEERING_CONTEXT.md`
```

**Critérios de aceitação:**

- [ ] Existe exatamente um cabeçalho de nível 1.
- [ ] O título contém a palavra “Proposta”.
- [ ] O texto não afirma que `ENGINEERING_CONTEXT.md` já existe.
- [ ] A condição de documento proposto aparece antes do plano de ações.

**Verificação:** pesquisar cabeçalhos de nível 1 e ocorrências de
`ENGINEERING_CONTEXT.md`.

**Validação:** um revisor deve conseguir distinguir proposta, documento futuro e
páginas existentes sem consultar o final do arquivo.

**Bloqueio:** qualquer trecho continuar tratando a página proposta como criada ou
aprovada sem evidência.

### PATCH-ENG-003 — Adicionar resumo executivo e estado documental

**Patch:** inserir, imediatamente após o título, resumo, fontes consultadas,
conclusão, decisões pendentes e estado atual.

```diff
+## Resumo executivo
+
+- Documento: proposta de consolidação técnica.
+- Página relacionada existente: `FERRAMENTAS_TECNICAS`.
+- Lacuna confirmada: inventário técnico geral e verificável.
+- Sobreposição existente: políticas de capacidade e validação em
+  `AGENT_POLICY.md`.
+- Decisão pendente: aprovar nome, escopo e criação da nova página.
```

**Critérios de aceitação:**

- [ ] O resumo aparece antes de detalhes de implementação.
- [ ] As três páginas canônicas do Notion são identificadas.
- [ ] A sobreposição com `AGENT_POLICY.md` está declarada.
- [ ] Decisões pendentes não são apresentadas como decisões aprovadas.
- [ ] O resumo pode ser compreendido isoladamente.

**Verificação:** inspecionar as primeiras 40 linhas e conferir todos os itens.

**Validação:** comparar o resumo com o conteúdo relido das três páginas do Notion.

**Bloqueio:** fonte inacessível ou afirmação factual sem página ou evidência atual.

### PATCH-ENG-004 — Corrigir a divisão de responsabilidades

**Patch:** declarar explicitamente a responsabilidade de cada documento e remover
a ideia de que `AGENT_POLICY.md` não possui engenharia de execução.

```diff
-`AGENT_POLICY.md`, que continua responsável pelas políticas;
+`AGENT_POLICY.md`, responsável por políticas, capacidade operacional,
+execução, verificação, aceitação e conclusão;
+`ENGINEERING_CONTEXT.md`, proposto para inventário factual, rotas técnicas,
+versões, caminhos, repositórios e evidências do ambiente;
```

**Critérios de aceitação:**

- [ ] `CONTEXT.md` permanece responsável por identidade, autoridade e rotas.
- [ ] `AGENT_POLICY.md` permanece responsável por políticas operacionais.
- [ ] `FERRAMENTAS_TECNICAS` permanece especializado em vídeo.
- [ ] O documento proposto não duplica matrizes e regras normativas completas.
- [ ] Documentação interna de repositórios continua fora do escopo canônico geral.

**Verificação:** construir uma matriz documento × responsabilidade a partir do texto
final e procurar responsabilidades duplicadas.

**Validação:** confrontar a matriz com as páginas canônicas do Notion.

**Bloqueio:** duas fontes serem declaradas simultaneamente canônicas para a mesma
regra sem precedência explícita.

### PATCH-ENG-005 — Corrigir a hierarquia dos cabeçalhos

**Patch:** transformar falsos títulos em cabeçalhos e usar um único nível para as
18 ações.

```diff
-#### 8. Definir os diretórios canônicos
+### 8. Definir os diretórios canônicos

-13. Criar um schema de validação
+### 13. Criar um schema de validação

-16. Atualizar AGENT_POLICY.md
+### 16. Atualizar `AGENT_POLICY.md`

-17. Definir manutenção
+### 17. Definir manutenção

-18. Executar validação final
+### 18. Executar validação final
```

Também transformar “Documento proposto”, “Ordem recomendada de execução” e
“Estado atual” em seções coerentes.

**Critérios de aceitação:**

- [ ] Não há salto injustificado de nível de cabeçalho.
- [ ] As ações 1–18 usam o mesmo nível.
- [ ] Não existem títulos numerados como parágrafos comuns.
- [ ] Não existe espaço duplicado no título da ação 11.
- [ ] O sumário gerado a partir dos cabeçalhos representa a estrutura real.

**Verificação:** executar um analisador de Markdown e listar todas as linhas que
começam com `#`.

**Validação:** comparar a sequência obtida com as 18 ações esperadas.

**Bloqueio:** ação ausente, duplicada ou subordinada à ação errada.

### PATCH-ENG-006 — Converter enumerações em listas Markdown

**Patch:** adicionar o marcador `-` aos conjuntos de itens e padronizar a
pontuação.

```diff
-fabricante e modelo;
-processador;
-arquitetura;
+- fabricante e modelo;
+- processador;
+- arquitetura;
```

Aplicar ao escopo, exclusões, hardware, ferramentas, VS Code, repositórios,
diretórios, segurança, schema, manutenção e demais enumerações equivalentes.

**Critérios de aceitação:**

- [ ] Todo conjunto de três ou mais itens possui marcadores ou tabela.
- [ ] Itens da mesma lista usam estrutura gramatical paralela.
- [ ] A pontuação é uniforme dentro de cada lista.
- [ ] Listas possuem linhas em branco antes e depois, quando exigido.
- [ ] Não há parágrafos de uma ou duas palavras simulando listas.

**Verificação:** revisar os intervalos originalmente localizados nas linhas 26–46,
72–85, 120–133, 229–239, 263–285, 403–411, 417–425 e 464–472.

**Validação:** renderizar o Markdown e confirmar a separação visual e semântica
dos itens.

**Bloqueio:** perda de item ou alteração do significado durante a conversão.

### PATCH-ENG-007 — Delimitar comandos por ambiente

**Patch:** colocar comandos Windows em `powershell` e comandos WSL/Linux em
`bash`. Manter comandos curtos em código embutido somente quando fizerem parte de
uma frase.

````diff
-Get-ComputerInfo
-wsl --version
+```powershell
+Get-ComputerInfo
+wsl --version
+```

-uname -a
-cat /etc/os-release
+```bash
+uname -a
+cat /etc/os-release
+```
````

**Critérios de aceitação:**

- [ ] Todos os comandos executáveis estão em bloco ou código embutido.
- [ ] PowerShell e Bash não aparecem no mesmo bloco.
- [ ] Cada bloco possui linguagem explícita.
- [ ] Argumentos e caracteres especiais foram preservados.
- [ ] O documento não afirma que a execução dos comandos já ocorreu.

**Verificação:** pesquisar linhas iniciadas por nomes de comandos conhecidos e
confirmar que estão dentro de cercas.

**Validação:** revisar manualmente o ambiente indicado para cada comando; quando
autorizado, testar somente comandos não destrutivos em ambiente compatível.

**Bloqueio:** comando destrutivo, dependente de privilégio ou incompatível com o
ambiente sem aviso explícito.

### PATCH-ENG-008 — Corrigir blocos estruturados e linguagens

**Patch:** usar `yaml` para dados YAML, `md` para exemplos Markdown e `text` para
árvores ou fluxos sem linguagem executável.

````diff
-```md
+```yaml
 python:
   versao: "3.x"
   fonte: "python3 --version"
 verificado_em: "AAAA-MM-DD"
 ```
````

Colocar em cercas o YAML que atualmente aparece como texto e delimitar a árvore
de documentos e o fluxo de aprovação com `text`.

**Critérios de aceitação:**

- [ ] Todas as cercas estão balanceadas.
- [ ] Todo YAML possui identificador `yaml`.
- [ ] O exemplo de estrutura Markdown permanece identificado como `md`.
- [ ] Árvores e diagramas textuais usam `text` ou Mermaid válido.
- [ ] Os blocos YAML são aceitos por um parser.

**Verificação:** extrair cada bloco por linguagem e executar parser YAML nos blocos
correspondentes.

**Validação:** conferir que o valor parseado preserva todos os campos e tipos
pretendidos.

**Bloqueio:** YAML inválido, cerca não fechada ou conteúdo classificado com linguagem
incorreta.

### PATCH-ENG-009 — Converter o inventário de agentes em tabela

**Patch:** substituir a pseudotabela por uma tabela com associações explícitas entre
campo e conteúdo esperado.

```diff
-Campo
-Conteúdo
-Nome
-ChatGPT Web, Codex, Claude Code, Gemini
+| Campo | Conteúdo esperado |
+| --- | --- |
+| Nome | ChatGPT Web, Codex, Claude Code ou Gemini |
+| Interface | Navegador, VS Code ou terminal |
+| Acesso a arquivos | `sim`, `não` ou `condicionado` |
```

**Critérios de aceitação:**

- [ ] A tabela possui cabeçalho e separador válidos.
- [ ] Cada campo original aparece uma única vez.
- [ ] Campo e descrição permanecem associados na mesma linha.
- [ ] Capacidades são descritas como observadas, condicionadas ou pendentes.
- [ ] Nenhum agente recebe acesso ou permissão presumida.

**Verificação:** renderizar a tabela e comparar seus campos com a lista original.

**Validação:** verificar cada capacidade contra evidência atual antes de preencher
valores factuais.

**Bloqueio:** capacidade preenchida apenas por memória ou inferência.

### PATCH-ENG-010 — Converter referências do Notion em links

**Patch:** substituir menções soltas às páginas canônicas por links diretos e manter
nomes de documentos futuros identificados como propostos.

```diff
-`CONTEXT.md`
+[`CONTEXT.md`](https://app.notion.com/p/39cf2ae06fc88051bb8fee62048b5551)
```

**Critérios de aceitação:**

- [ ] `CONTEXT.md`, `AGENT_POLICY.md` e `FERRAMENTAS_TECNICAS` possuem links válidos.
- [ ] Nenhum link aponta para a pasta local `contexto/` como substituta do Notion.
- [ ] `ENGINEERING_CONTEXT.md` está marcado como proposto enquanto não existir.
- [ ] `schemas/engineering-context.schema.json` está marcado como futuro enquanto
  não existir.
- [ ] Não há Page IDs inventados.

**Verificação:** extrair todos os links, confirmar o formato e reler as três páginas
existentes por seus IDs.

**Validação:** cada link deve abrir a entidade cujo título corresponde ao texto
do link.

**Bloqueio:** falta de acesso, entidade divergente ou página futura tratada como
existente.

### PATCH-ENG-011 — Padronizar código embutido

**Patch:** aplicar crases a arquivos, caminhos, comandos, campos,
identificadores e valores controlados; retirar crases de marcas e conceitos em
prosa.

**Critérios de aceitação:**

- [ ] Arquivos como `CONTEXT.md` e `requirements.txt` usam código embutido quando
  não são links.
- [ ] Caminhos como `.venv/` e `saida/` usam código embutido.
- [ ] Identificadores como `DOC-ENG-001` e `STA-CUR-001` usam código embutido.
- [ ] Campos YAML e estados controlados usam código embutido em prosa.
- [ ] Notion, Python, Windows, Linux, VS Code e PowerShell não usam crases apenas
  por serem nomes de produtos ou tecnologias.
- [ ] Não existem crases desbalanceadas.

**Verificação:** pesquisar termos conhecidos e executar análise sintática de
Markdown.

**Validação:** revisão amostral de todas as categorias, não apenas de ocorrências
isoladas.

**Bloqueio:** código embutido alterar a função de um link ou englobar pontuação
indevida.

### PATCH-ENG-012 — Separar estados de inventário e execução

**Patch:** substituir a taxonomia única por dois campos independentes.

```yaml
inventory_status:
  - confirmado
  - instalado_nao_validado
  - ausente
  - pendente_de_verificacao
  - deprecado
  - nao_aplicavel

execution_status:
  fonte: AGENT_POLICY.md
  valores:
    - nao_iniciada
    - em_execucao
    - executada_aguardando_validacao
    - validada
    - bloqueada
    - nao_aplicavel
```

**Critérios de aceitação:**

- [ ] Instalação de ferramenta não é tratada como validação de ação.
- [ ] Cada estado possui definição e campo de aplicação.
- [ ] Estados de execução correspondem semanticamente a `AGENT_POLICY.md`.
- [ ] Exemplos usam valores controlados consistentes.
- [ ] A serialização YAML usa valores normalizados sem acentos nem travessões.

**Verificação:** procurar todos os estados no documento e classificá-los como
inventário ou execução.

**Validação:** confrontar os estados de execução com a página atual de
`AGENT_POLICY.md`.

**Bloqueio:** estado ambíguo ou usado em categoria diferente da sua definição.

### PATCH-ENG-013 — Reduzir a atualização de `AGENT_POLICY.md` ao necessário

**Patch:** substituir a duplicação de políticas por uma proposta de roteamento e
precedência.

```diff
-não presumir ferramenta instalada;
-não presumir acesso ao terminal;
-registrar bloqueios de permissão.
+Adicionar uma rota para o inventário técnico e determinar que evidência atual do
+ambiente prevalece sobre valores históricos do inventário.
```

**Critérios de aceitação:**

- [ ] O plano reconhece as políticas de capacidade já existentes.
- [ ] A alteração proposta limita-se a rota, gatilho de consulta e precedência.
- [ ] Não há cópia integral da matriz de capacidade.
- [ ] A edição do Notion permanece condicionada a autorização explícita.
- [ ] Caso autorizada, a atualização é relida e comparada ao patch aprovado.

**Verificação:** comparar a seção final com `AGENT_POLICY.md` e calcular as regras
duplicadas restantes.

**Validação:** confirmar que nenhuma política preexistente foi enfraquecida ou
contradita.

**Bloqueio:** ausência de autorização para escrita no Notion ou conflito normativo.

### PATCH-ENG-014 — Formalizar a integração com `CONTEXT.md`

**Patch:** manter `DOC-ENG-001` como identificador proposto e registrar a
inconsistência atual de `FERRAMENTAS_TECNICAS` sem inventar seu identificador.

**Critérios de aceitação:**

- [ ] `DOC-ENG-001` está marcado como proposta até aprovação.
- [ ] A referência existente a `FERRAMENTAS_TECNICAS` é reconhecida.
- [ ] A ausência dela na tabela de documentos especializados é registrada.
- [ ] O plano não cria identificador para `FERRAMENTAS_TECNICAS` sem decisão.
- [ ] Qualquer futura atualização de `CONTEXT.md` depende de autorização e releitura.

**Verificação:** reler a tabela de documentos especializados e os blocos de páginas
filhas em `CONTEXT.md`.

**Validação:** conferir que a rota proposta possui identificador, documento e
finalidade não ambíguos.

**Bloqueio:** conflito de identificador ou ausência de autorização para alteração.

### PATCH-ENG-015 — Refinar segurança e coleta factual

**Patch:** organizar a coleta como inventário mínimo, com fonte, data, status e
política explícita de minimização de dados.

**Critérios de aceitação:**

- [ ] Todo valor factual exige `fonte`, `coletado_em` e `inventory_status`.
- [ ] Valores não coletados permanecem `pendente_de_verificacao`.
- [ ] Tokens, senhas, chaves, conteúdo de `.env` e dados de atletas são proibidos.
- [ ] Número de série, IP público e endereços pessoais não são coletados sem
  necessidade aprovada.
- [ ] O plano não contém credenciais reais.

**Verificação:** executar busca por padrões de segredo e revisar todos os campos
de hardware, software, caminhos e agentes.

**Validação:** revisão humana de privacidade antes de qualquer publicação no Notion.

**Bloqueio:** segredo detectado, dado pessoal desnecessário ou ausência de fonte.

### PATCH-ENG-016 — Corrigir checklist e ordem de execução

**Patch:** converter caixas soltas em lista de tarefas, adicionar identificadores
de ação e ordenar dependências.

```diff
-[ ] Página criada com Page ID único
+- [ ] `ACC-ENG-001`: página criada com identificador único, quando autorizada.
```

**Critérios de aceitação:**

- [ ] Todas as caixas usam `- [ ]` ou `- [x]`.
- [ ] Nenhuma caixa está marcada sem evidência observada.
- [ ] Cada caixa referencia uma ação ou critério deste plano.
- [ ] A ordem respeita fonte → edição → verificação → validação → aprovação.
- [ ] Etapas condicionais de Notion estão claramente identificadas.

**Verificação:** contar caixas, identificadores e referências órfãs.

**Validação:** confirmar que cada ação possui ao menos um critério correspondente
no checklist final.

**Bloqueio:** caixa marcada apenas porque o arquivo foi salvo ou a ferramenta
retornou sucesso.

### PATCH-ENG-017 — Atualizar o estado final sem alegações não verificadas

**Patch:** substituir o YAML final por estado coerente com a execução realmente
observada.

```yaml
estado_documental:
  documento_proposto: ENGINEERING_CONTEXT.md
  pagina_existente_relacionada: FERRAMENTAS_TECNICAS
  criacao_autorizada: false
  pagina_criada: false
  fontes_notion_validadas: true
  inventario_tecnico_validado: false
  proxima_decisao: aprovar_nome_escopo_e_criacao
```

Os valores acima são modelo inicial e devem ser atualizados somente com evidência
observada no momento da implementação.

**Critérios de aceitação:**

- [ ] O estado diferencia autorização, execução, verificação e aceitação.
- [ ] Nenhum campo declara página criada sem Page ID relido.
- [ ] Nenhum campo declara inventário validado sem evidências de coleta.
- [ ] A próxima ação corresponde às pendências restantes.
- [ ] O YAML final é sintaticamente válido.

**Verificação:** analisar o YAML e comparar cada valor com evidência registrada.

**Validação:** obter aprovação humana para fatos que não podem ser confirmados por
ferramenta.

**Bloqueio:** divergência entre o estado declarado e as evidências.

### PATCH-ENG-018 — Executar verificação e validação final

**Patch:** não há alteração editorial nesta ação; ela produz o relatório final de
qualidade e decide se o documento pode ser aceito.

**Critérios de aceitação:**

- [ ] `markdownlint` retorna zero erro para `ENGENHARIA.md` com a configuração
  aprovada do projeto.
- [ ] Todos os blocos YAML são aceitos por parser.
- [ ] Todas as cercas de código estão balanceadas.
- [ ] Existe exatamente um H1 e uma sequência completa de 18 ações.
- [ ] Links das três páginas canônicas resolvem para os títulos esperados.
- [ ] Não há referência à pasta local `contexto/` como fonte substituta do Notion.
- [ ] Não há segredo ou dado sensível detectado.
- [ ] O diff contém apenas mudanças autorizadas.
- [ ] Todas as alegações factuais possuem fonte ou estado pendente.
- [ ] Um revisor humano aprovou o conteúdo final ou registrou pendências.

**Verificação mínima:**

```bash
git diff -- ENGENHARIA.md
npx --yes markdownlint-cli2 ENGENHARIA.md
sha256sum ENGENHARIA.md
```

Complementar com parser YAML, verificador de links, busca de segredos e releitura
das páginas do Notion.

**Validação:** produzir uma matriz final com as colunas `critério`, `evidência`,
`resultado`, `responsável` e `data`. Somente marcar o documento como `VALIDADA`
quando todos os critérios obrigatórios estiverem aprovados.

**Bloqueio:** qualquer erro de lint, YAML inválido, link canônico incorreto, alegação
factual sem fonte, dado sensível ou aprovação pendente.

## 6. Ordem obrigatória de execução

1. `PATCH-ENG-001` — preservar linha de base;
2. `PATCH-ENG-002` a `PATCH-ENG-004` — corrigir identidade e fatos;
3. `PATCH-ENG-005` a `PATCH-ENG-011` — corrigir estrutura Markdown;
4. `PATCH-ENG-012` a `PATCH-ENG-014` — reconciliar políticas e rotas;
5. `PATCH-ENG-015` — revisar segurança;
6. `PATCH-ENG-016` e `PATCH-ENG-017` — consolidar checklist e estado;
7. `PATCH-ENG-018` — verificar e validar o resultado final.

Uma ação pode começar somente quando as dependências anteriores necessárias estão
`VALIDADAS` ou formalmente classificadas como `NÃO APLICÁVEL`.

## 7. Matriz de evidências da implementação

<!-- markdownlint-disable MD013 -->

| Evidência | Conteúdo mínimo | Produzida por | Validação |
| --- | --- | --- | --- |
| `EVD-BASELINE` | Hash, contagens, lint e estado do Git anteriores | Agente executor | Comparação com este plano |
| `EVD-DIFF` | Diff integral de `ENGENHARIA.md` | Git | Revisão de escopo |
| `EVD-LINT` | Saída completa do `markdownlint` | Ferramenta | Zero erro |
| `EVD-YAML` | Lista de blocos e resultado do parser | Ferramenta | Todos válidos |
| `EVD-NOTION` | IDs, títulos e trechos relidos | Conector Notion | Correspondência factual |
| `EVD-LINKS` | URL, destino e resultado | Ferramenta | Todos resolvidos |
| `EVD-SECURITY` | Busca por padrões sensíveis | Ferramenta e revisor | Nenhum achado crítico |
| `EVD-REVIEW` | Matriz de critérios e decisão final | Revisor | Aprovação ou pendências |

<!-- markdownlint-enable MD013 -->

## 8. Gate final

```yaml
gate: GATE-ENG-FINAL
aprovado_quando:
  - todas_as_acoes_obrigatorias_validadas
  - markdownlint_zero_erros
  - yaml_valido
  - links_notion_validados
  - fatos_coerentes_com_fontes
  - ausencia_de_segredos
  - diff_restrito_ao_escopo
  - aprovacao_humana_registrada
resultado_inicial: pendente
```

Se qualquer condição falhar, o resultado deve ser `BLOQUEADA`, acompanhado da
ação afetada, evidência observada, correção necessária e responsável pela nova
validação. A simples alteração do arquivo não constitui aceitação do conteúdo.
