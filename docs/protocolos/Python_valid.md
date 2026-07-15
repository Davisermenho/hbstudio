# PYTHON - PESQUISA TÉNCNICA

Para uma pesquisa científica e técnica séria sobre código Python, a IA não deve usar uma hierarquia única e cega. A fonte prioritária depende da afirmação investigada:

 semântica da linguagem, funcionamento de uma biblioteca, desempenho, segurança, arquitetura ou comportamento do projeto.

A hierarquia operacional mais segura é a seguinte.

## 1. Evidência executável do projeto analisado

Quando a pergunta é “o que este código realmente faz?”, a fonte mais forte é o próprio artefato em execução:

* código-fonte real;
* versão ou commit analisado;
* `pyproject.toml`, arquivos de configuração e lockfiles;
* testes automatizados;
* dados de entrada e saída;
* logs, traces e exceções;
* ambiente de execução;
* experimento reproduzível mínimo.

A documentação pode descrever a intenção, mas somente a execução controlada demonstra o comportamento observado naquele ambiente.

Essa evidência deve registrar, no mínimo:

```text
Python: 3.x.y
Implementação: CPython, PyPy etc.
Sistema operacional:
Arquitetura:
Commit:
Dependências e versões:
Comando executado:
Entrada:
Saída:
Resultado esperado:
Resultado observado:
```

## 2. Especificação oficial da linguagem Python

Para questões sobre sintaxe, escopo, objetos, expressões, exceções, importação, resolução de nomes e semântica, deve-se priorizar:

1. Python Language Reference;
2. gramática oficial;
3. modelo de dados;
4. documentação da versão exata do Python.

O Python Language Reference é o documento que descreve a sintaxe e a semântica central da linguagem; a documentação da biblioteca padrão trata dos módulos, funções e tipos distribuídos com Python. ([Python documentation][1])

Exemplo: para decidir como `__getattribute__`, `yield`, `async`, closures ou comparações funcionam, um tutorial ou resposta de fórum não deve prevalecer sobre a referência oficial.

## 3. PEPs aplicáveis, considerando seu status

Os Python Enhancement Proposals são documentos técnicos que descrevem recursos, processos, padrões e decisões do ecossistema Python. Um PEP deve conter uma especificação técnica e a justificativa da proposta. ([Python Enhancement Proposals (PEPs)][2])

A IA precisa verificar:

* número do PEP;
* tipo;
* status;
* versão do Python relacionada;
* se foi substituído por outro documento;
* se a especificação normativa foi transferida para outra fonte.

Ordem prática de confiança:

```text
Final / Active / Accepted
↓
Provisional
↓
Draft
↓
Deferred
↓
Superseded
↓
Rejected / Withdrawn
```

Um PEP rejeitado pode ser útil para compreender uma discussão histórica, mas não comprova que o comportamento proposto tenha sido adotado.

Também é necessário distinguir:

* PEP normativo;
* PEP informativo;
* PEP de processo;
* PEP de release;
* PEP histórico.

## 4. Documentação oficial da biblioteca padrão

Quando a investigação envolve `pathlib`, `asyncio`, `sqlite3`, `typing`, `subprocess`, `json`, `dataclasses` ou outro módulo padrão, deve-se consultar a documentação da versão efetivamente usada.

A documentação da biblioteca padrão descreve os módulos, componentes opcionais, funções, classes, exceções e contratos públicos distribuídos com Python. ([Python documentation][3])

A IA não deve consultar somente `/3/` ou a documentação “latest” sem confirmar a versão do projeto. Uma API pode:

* não existir em versões anteriores;
* ter parâmetros diferentes;
* ter mudado de comportamento;
* estar depreciada;
* ter sido removida.

## 5. Especificações oficiais do ecossistema Python

Para empacotamento, ambientes, builds, metadados, wheels, índices e instalação, a prioridade deve ser:

1. especificações ativas da Python Packaging Authority;
2. Python Packaging User Guide;
3. PEPs de packaging ainda normativos;
4. documentação oficial da ferramenta concreta.

A PyPA mantém especificações de interoperabilidade atualmente ativas e o Python Packaging User Guide reúne referências e orientações sobre distribuição e instalação de pacotes.

Isso é especialmente relevante para:

```text
pyproject.toml
build backends
wheel
sdist
pip
virtual environments
package metadata
dependency resolution
editable installs
package indexes
```

## 6. Código-fonte e testes da implementação de referência

Quando a documentação é ambígua ou insuficiente, deve-se inspecionar:

* código-fonte do CPython;
* testes oficiais;
* documentação interna;
* tag correspondente à versão;
* histórico do commit relevante.

O repositório `python/cpython` contém a implementação do interpretador, a biblioteca padrão, os testes e a documentação do projeto Python. ([GitHub][5])

Entretanto, há uma distinção crítica:

```text
Especificação da linguagem ≠ detalhe interno do CPython
```

Um comportamento observado no CPython pode ser detalhe de implementação e não uma garantia válida para PyPy, GraalPy ou outras implementações.

Portanto, a IA deve classificar a descoberta como:

* requisito da linguagem;
* contrato público da biblioteca;
* comportamento específico do CPython;
* detalhe interno sem garantia de estabilidade.

## 7. Documentação oficial da biblioteca ou framework analisado

Para pacotes de terceiros, a hierarquia interna deve ser:

1. documentação da versão exata;
2. referência oficial da API;
3. release notes e changelog;
4. guia de migração;
5. documentação de segurança;
6. código-fonte da tag instalada;
7. testes oficiais;
8. exemplos mantidos pelo projeto.

Por exemplo, para `pytest`, a documentação oficial deve prevalecer sobre tutoriais externos ao definir fixtures, descoberta de testes, configuração e comportamento da API. A documentação apresenta fixtures como contextos explícitos, modulares e reutilizáveis, e descreve o teste em etapas de preparação, ação, verificação e limpeza. ([Documentação do pytest][6])

A versão instalada deve ser confirmada por evidência como:

```bash
python -VV
python -m pip show nome-do-pacote
python -m pip freeze
```

ou pelo lockfile do projeto.

## 8. Código-fonte, testes, issues e pull requests do pacote

Quando existe divergência entre documentação e comportamento:

```text
tag instalada
→ código-fonte
→ testes oficiais
→ changelog
→ pull request que introduziu a mudança
→ issue relacionada
```

Issues e pull requests são fontes primárias importantes, mas não são automaticamente normativas. Uma issue pode conter:

* hipótese não confirmada;
* informação antiga;
* solução rejeitada;
* workaround temporário;
* comentário de usuário sem autoridade;
* comportamento ainda não lançado.

A IA deve verificar se o PR foi aprovado, incorporado e incluído na versão utilizada.

## 9. Normas e referências institucionais de segurança e qualidade

Para segurança, não basta usar documentação comum da biblioteca. Devem ser priorizados:

* advisories oficiais do projeto;
* bancos oficiais de vulnerabilidades;
* identificadores CVE e CWE;
* documentação do fornecedor;
* NIST;
* OWASP, quando aplicável;
* políticas de segurança do projeto;
* correções e versões afetadas.

O NIST Secure Software Development Framework define práticas de desenvolvimento seguro aplicáveis a diferentes tecnologias e linguagens, com foco nos resultados de segurança, e não em uma ferramenta específica. ([Publicações Técnicas NIST][7])

Ferramentas de análise estática são evidência auxiliar. O NIST caracteriza analisadores de código-fonte como ferramentas que examinam o código para detectar fraquezas que podem resultar em vulnerabilidades. ([NIST][8])

Um alerta de ferramenta não deve ser tratado como vulnerabilidade comprovada sem:

* confirmação no código;
* fluxo de dados alcançável;
* contexto de execução;
* versão afetada;
* demonstração ou teste controlado.

## 10. Literatura científica revisada por pares

A literatura científica é prioritária para questões como:

* eficácia de técnicas de teste;
* comparação entre ferramentas;
* qualidade de software;
* manutenibilidade;
* produtividade;
* detecção de defeitos;
* desempenho;
* segurança;
* engenharia de software baseada em evidências;
* efeitos de práticas arquiteturais.

A ordem científica recomendada é:

```text
Revisão sistemática ou meta-análise atualizada
↓
Estudo de replicação
↓
Experimento controlado
↓
Estudo empírico com múltiplos projetos
↓
Estudo de caso industrial
↓
Estudo observacional
↓
Artigo conceitual ou opinião técnica
```

A ACM SIGSOFT estabeleceu padrões empíricos para melhorar a avaliação metodológica de pesquisas em engenharia de software, incluindo estudos experimentais e benchmarking. ([ACM Digital Library][9])

Contudo, um artigo científico não substitui a documentação de uma API. Ele pode demonstrar que uma técnica tende a funcionar, mas não define a assinatura atual de uma função ou o comportamento normativo de uma versão específica.

## 11. Benchmarks independentes e reproduzíveis

Para afirmações de desempenho, como “biblioteca A é mais rápida que B”, a hierarquia deve priorizar:

1. benchmark reproduzido no ambiente relevante;
2. metodologia publicada;
3. código e dados disponíveis;
4. aquecimento e repetição controlados;
5. distribuição dos resultados;
6. análise de variância e incerteza;
7. comparação em múltiplas cargas;
8. estudos independentes.

Um benchmark sem controle de versão, hardware, sistema operacional, dados e metodologia não é evidência suficiente.

A IA deve rejeitar conclusões baseadas somente em:

```text
“rodei uma vez”
“pareceu mais rápido”
“este gráfico mostra”
“um blog afirmou”
```

## 12. Documentação técnica secundária de alta qualidade

Inclui:

* livros técnicos reconhecidos;
* artigos escritos por mantenedores;
* conferências técnicas;
* documentação de organizações especializadas;
* cursos produzidos por responsáveis pelo projeto.

Essas fontes são úteis para interpretação e aplicação, mas não devem prevalecer sobre:

* especificação;
* documentação oficial;
* versão real do código;
* teste reproduzível.

## 13. Fóruns e discussões comunitárias

Podem ser consultados:

* discuss.python.org;
* Stack Overflow;
* GitHub Discussions;
* listas de discussão;
* fóruns especializados.

Sua função é principalmente:

* localizar hipóteses;
* descobrir casos extremos;
* identificar referências primárias;
* encontrar exemplos;
* compreender problemas recorrentes.

A resposta encontrada deve ser validada contra documentação, código, versão e execução. Número de votos ou reputação do autor não transforma uma resposta em especificação.

## 14. Blogs, tutoriais, vídeos e conteúdo comercial

São fontes de orientação inicial, não de autoridade técnica.

Podem:

* simplificar excessivamente;
* omitir versões;
* usar APIs depreciadas;
* repetir erros;
* não apresentar testes;
* misturar opinião com contrato técnico;
* estar otimizados para engajamento ou venda.

Devem ser usados apenas quando apontam para fontes primárias ou quando sua afirmação pode ser reproduzida.

## 15. Conteúdo gerado por IA

Uma resposta de IA, inclusive minha resposta, não deve ser tratada como fonte científica ou técnica primária.

O conteúdo gerado deve funcionar como:

* síntese;
* mecanismo de busca orientado;
* explicação;
* geração de hipóteses;
* auxílio na criação de testes;
* organização de evidências.

A conclusão precisa ser vinculada às fontes reais e à evidência executável.

## Regra de prioridade por tipo de pergunta

| Pergunta investigada                              | Evidência prioritária                                        |
| ------------------------------------------------- | ------------------------------------------------------------ |
| “Esta sintaxe é válida?”                          | Language Reference e gramática da versão                     |
| “Qual é a semântica desta operação?”              | Language Reference, PEP aplicável e teste                    |
| “Como esta função da biblioteca padrão funciona?” | Documentação da versão, código e testes do CPython           |
| “Esta API do pacote existe?”                      | Documentação e código da versão instalada                    |
| “Este comportamento é um bug?”                    | Reprodução mínima, código, testes, changelog e issue oficial |
| “Esta técnica é melhor?”                          | Literatura empírica e experimentos contextualizados          |
| “Qual implementação é mais rápida?”               | Benchmark reproduzível no ambiente-alvo                      |
| “Este código é seguro?”                           | Modelo de ameaça, advisories, normas, análise e testes       |
| “Esta prática é recomendada?”                     | Especificações, guias oficiais e evidência científica        |
| “O projeto funciona corretamente?”                | Requisitos, testes, execução, logs e critérios de aceitação  |

## Hierarquia consolidada

```text
1. Artefato real e experimento reproduzível
2. Especificação oficial da linguagem
3. PEP vigente e aplicável
4. Documentação oficial da versão exata
5. Especificações oficiais do ecossistema
6. Código-fonte e testes da implementação
7. Documentação e código do pacote da versão instalada
8. Normas, advisories e bases institucionais de segurança
9. Revisões sistemáticas e literatura científica revisada por pares
10. Benchmarks independentes reproduzíveis
11. Documentação técnica secundária qualificada
12. Fóruns e discussões comunitárias
13. Blogs, tutoriais e vídeos
14. Conteúdo gerado por IA sem validação externa
```

## Critério final de pesquisa séria

A pesquisa somente deve ser considerada tecnicamente fundamentada quando cada conclusão relevante possuir:

```yaml
afirmacao: "O que está sendo afirmado"
tipo_de_afirmacao: "normativa | comportamental | empírica | segurança | desempenho"
python_version: "versão analisada"
implementation: "CPython | PyPy | outra"
dependency_versions: []
fonte_primaria: ""
fonte_secundaria: ""
evidencia_executavel: ""
metodo_de_validacao: ""
resultado: ""
limitacoes: []
conflitos_entre_fontes: []
nivel_de_confianca: "alto | moderado | baixo"
```

A regra central é:

> **Especificações definem contratos; código e testes demonstram implementações; experimentos demonstram comportamento; estudos científicos sustentam generalizações.**

Misturar essas quatro categorias sem distingui-las é uma das principais causas de pesquisas técnicas incorretas sobre Python.

Não é possível garantir esses resultados apenas com um prompt. A garantia deve ser construída no **pipeline de pesquisa**, por meio de fontes controladas, registros estruturados, validadores determinísticos, revisão independente e critérios explícitos de bloqueio.

A regra central é:

> **A IA pesquisa e sintetiza; o sistema registra, valida e bloqueia; o revisor humano aprova as conclusões críticas.**

O NIST recomenda que validade e confiabilidade de sistemas de IA sejam verificadas por testes e monitoramento contínuos, com documentação das limitações e das condições em que os resultados são generalizáveis. Portanto, confiar somente na “capacidade de raciocínio” do modelo não constitui controle suficiente. ([NIST AI Resource Center][1])

## 1. Separar afirmações científicas de afirmações técnicas

O sistema deve classificar cada afirmação antes de pesquisar.

| Tipo de afirmação | Exemplo                                        | Evidência prioritária                    |
| ----------------- | ---------------------------------------------- | ---------------------------------------- |
| Normativa         | “A sintaxe de Python funciona assim”           | Especificação oficial                    |
| Técnica           | “Esta função aceita este parâmetro”            | Documentação da versão exata             |
| Comportamental    | “Este código produz este resultado”            | Execução e teste reproduzível            |
| Empírica          | “Esta técnica reduz defeitos”                  | Estudos científicos                      |
| Comparativa       | “A biblioteca A é mais rápida”                 | Benchmark reproduzível                   |
| Consenso          | “A literatura considera esta prática superior” | Revisão sistemática, guideline ou padrão |
| Segurança         | “Esta construção é vulnerável”                 | Advisory, análise do código e reprodução |

No caso de Python, a referência oficial descreve a sintaxe e a semântica central da linguagem; a documentação da biblioteca padrão descreve módulos, funções e tipos; e os PEPs possuem tipos e estados que determinam se representam proposta, orientação ou decisão adotada. ([Python documentation][2])

Sem essa classificação, a IA pode usar um estudo científico para responder sobre uma API ou usar a documentação de uma API para justificar uma generalização científica.

---

# 2. Controle contra interpretação incorreta

Cada conclusão deve ser decomposta em uma ou mais afirmações atômicas.

Em vez de registrar:

> “A biblioteca é segura, rápida e recomendada.”

O sistema deve exigir:

```yaml
- claim_id: CLM-001
  afirmacao: "A biblioteca não executa shell por padrão."
  tipo: "seguranca"

- claim_id: CLM-002
  afirmacao: "A biblioteca foi mais rápida no benchmark X."
  tipo: "comparativa"

- claim_id: CLM-003
  afirmacao: "A documentação recomenda o uso da API Y."
  tipo: "normativa"
```

Para cada afirmação, devem existir:

* fonte específica;
* página, seção, linha, função ou commit;
* trecho ou dado que sustenta a conclusão;
* interpretação produzida pela IA;
* teste de compatibilidade entre fonte e afirmação;
* evidência contrária encontrada;
* limitações da interpretação.

O validador deve perguntar:

```text
A fonte afirma diretamente isso?
A afirmação é mais ampla do que a evidência?
A fonte fala de correlação ou causalidade?
A fonte fala de uma versão diferente?
A conclusão depende de uma condição omitida?
Existe evidência contrária?
```

Para código Python, a interpretação documental deve ser acompanhada, quando possível, por:

* exemplo mínimo reproduzível;
* entrada controlada;
* saída esperada;
* saída observada;
* versão do Python;
* versão das dependências;
* sistema operacional;
* implementação utilizada, como CPython ou PyPy.

A documentação oficial do Python reconhece que a descrição textual da linguagem pode deixar algumas ambiguidades; por isso, especificação, implementação e teste não devem ser confundidos. ([Python documentation][3])

### Regra de bloqueio

```text
FAIL — a evidência não implica diretamente a afirmação.
FAIL — a conclusão é mais abrangente que a fonte.
FAIL — faltam condições relevantes da afirmação.
FAIL — o comportamento não foi reproduzido quando era reproduzível.
```

---

# 3. Controle de atualização e validade das fontes

“Usar apenas fontes atualizadas” não deve significar “usar apenas fontes recentes”. Uma fonte antiga pode continuar sendo normativa ou cientificamente válida.

O requisito correto é:

> **Usar fontes atuais para o objeto e a versão analisados, verificando correções, substituições, retratações e obsolescência.**

Cada fonte deve registrar:

```yaml
publicada_em: "YYYY-MM-DD"
atualizada_em: "YYYY-MM-DD | desconhecido"
consultada_em: "YYYY-MM-DDTHH:MM:SSZ"
versao_documento: ""
versao_software: ""
commit_ou_tag: ""
status: "vigente | substituida | depreciada | corrigida | retraida"
substituida_por: ""
doi: ""
url_canonica: ""
```

Para literatura científica, o pipeline deve verificar:

* DOI;
* página oficial do editor;
* correções;
* erratas;
* expressões de preocupação;
* retratações;
* versão do artigo;
* estudos ou revisões posteriores.

Crossmark permite registrar atualizações, correções e retratações relacionadas a trabalhos científicos. A base Retraction Watch disponibilizada pela Crossref é atualizada em dias úteis, embora sua cobertura de correções e expressões de preocupação não seja tão completa quanto a de retratações. ([www.crossref.org][4])

Para Python, devem ser registrados:

* versão completa do interpretador;
* versão exata da biblioteca;
* versão da documentação;
* status do PEP;
* tag ou commit do código;
* changelog e guia de migração aplicáveis.

Um PEP pode estar como rascunho, provisório, aceito, ativo, final, rejeitado ou substituído. Além disso, a própria documentação do Python alerta que alguns PEPs deixam de ser atualizados depois que o recurso é implementado; nesse caso, a documentação vigente da versão deve prevalecer para o comportamento público atual. ([Python Enhancement Proposals (PEPs)][5])

### Regra de bloqueio

```text
FAIL — versão não identificada.
FAIL — fonte retraída.
FAIL — documentação de versão diferente usada sem justificativa.
FAIL — PEP rejeitado ou substituído tratado como norma vigente.
FAIL — correção ou errata encontrada, mas não considerada.
WARN — data de atualização desconhecida.
WARN — não foi possível verificar o estado pós-publicação.
```

---

# 4. Controle para não confundir estudo preliminar com consenso

Toda evidência científica deve receber uma classificação explícita:

```text
PROTOCOLO DE ESTUDO
↓
PREPRINT
↓
ESTUDO ÚNICO PUBLICADO
↓
ESTUDO REPLICADO
↓
CONJUNTO DE ESTUDOS INDEPENDENTES
↓
REVISÃO SISTEMÁTICA
↓
META-ANÁLISE
↓
GUIDELINE OU PADRÃO
↓
CONSENSO INSTITUCIONAL ATUALIZADO
```

Um preprint, protocolo ou estudo isolado nunca deve ser apresentado como consenso.

O termo **consenso** somente pode ser usado quando houver:

1. síntese atualizada da literatura;
2. estudos metodologicamente adequados;
3. resultados razoavelmente consistentes;
4. independência suficiente entre grupos de pesquisa;
5. avaliação de risco de viés;
6. ausência de contradição relevante não resolvida;
7. certeza da evidência classificada.

PRISMA melhora a transparência no relato de revisões sistemáticas, incluindo estratégia, seleção e exclusões, mas não garante sozinho que a revisão seja metodologicamente boa. O Cochrane Handbook trata de busca sistemática, seleção, risco de viés, síntese e interpretação. O GRADE classifica a certeza da evidência e considera fatores como risco de viés, inconsistência, evidência indireta, imprecisão e viés de publicação. ([PRISMA statement][6])

### Vocabulário obrigatório

| Situação              | Linguagem permitida                           |
| --------------------- | --------------------------------------------- |
| Preprint              | “resultado preliminar não revisado por pares” |
| Estudo único          | “um estudo encontrou”                         |
| Estudos divergentes   | “a evidência é conflitante”                   |
| Evidência limitada    | “há indícios, com baixa confiança”            |
| Evidência consistente | “múltiplos estudos convergem”                 |
| Síntese robusta       | “a revisão encontrou evidência de…”           |
| Guideline atual       | “a recomendação institucional vigente é…”     |

### Regra de bloqueio

```text
FAIL — preprint descrito como consenso.
FAIL — estudo único usado para generalização ampla.
FAIL — ausência de classificação do nível de evidência.
FAIL — conclusão de causalidade baseada apenas em associação.
```

---

# 5. Controle para priorizar fontes primárias

A fonte secundária deve servir principalmente para:

* descobrir terminologia;
* localizar estudos;
* compreender o debate;
* encontrar referências primárias;
* identificar possíveis conflitos.

Para afirmações técnicas diretas, a fonte principal deve ser:

* especificação oficial;
* documentação oficial;
* código-fonte;
* teste oficial;
* changelog;
* advisory oficial;
* commit ou pull request incorporado.

Para afirmações científicas empíricas, devem ser citados:

* artigo original;
* dados;
* protocolo;
* registro do estudo;
* materiais e código, quando disponíveis.

Porém, existe uma exceção importante:

> Para afirmar que existe consenso ou avaliar o conjunto da evidência, a revisão sistemática, meta-análise ou guideline é a fonte apropriada.

Nesse caso, a resposta deve citar:

1. a síntese de alto nível;
2. os estudos primários mais importantes;
3. eventuais estudos que contradizem a síntese.

Cochrane recomenda uma busca sistemática e abrangente, com critérios de elegibilidade, gerenciamento das referências, documentação da busca e justificativas para a seleção dos estudos. ([Cochrane][7])

### Regra de bloqueio

```text
FAIL — blog é a única fonte para uma afirmação normativa.
FAIL — tutorial é usado para definir comportamento de uma API.
FAIL — revisão narrativa é a única evidência de um efeito empírico.
FAIL — fonte secundária não conduz à fonte original.
EXCEÇÃO — sínteses são aceitas para afirmações sobre o conjunto da evidência.
```

# 6. Controle de conflitos de interesse e limitações metodológicas

A IA não consegue “sempre perceber” conflitos ocultos. Ela pode apenas verificar os conflitos declarados e procurar indicadores observáveis.

Por isso, o campo não deve ser binário:

```text
conflito = sim | não
```

Deve ser:

```yaml
financiamento:
  declarado: true
  financiadores: []
  papel_do_financiador: ""
  verificacao_externa: ""

conflitos_autores:
  declarados: []
  vinculos_institucionais: []
  patentes_ou_participacoes: []
  nao_declarados_suspeitos: []

limitacoes:
  desenho_do_estudo: []
  tamanho_da_amostra: ""
  representatividade: ""
  risco_de_vies: []
  dados_ausentes: ""
  preregistro: ""
  dados_disponiveis: false
  codigo_disponivel: false
  replicacao_independente: false

estado:
  conflito: "identificado | não identificado | não informado | indeterminado"
```

A ausência de declaração não significa ausência de conflito. O resultado deve ser registrado como **não informado** ou **indeterminado**.

O Cochrane Handbook distingue vieses decorrentes dos estudos e da própria síntese e observa que ações de pesquisadores e revisores podem ser influenciadas por conflitos de interesse. O RoB 2 utiliza domínios estruturados e perguntas de sinalização para avaliar diferentes fontes de viés. ([Cochrane][8])

## Regra de bloqueio

```text
FAIL — campo de financiamento ausente.
FAIL — conflito não informado tratado como inexistente.
FAIL — limitações metodológicas omitidas.
FAIL — estudo financiado pelo interessado apresentado sem registrar o papel do financiador.
WARN — dados, protocolo ou código indisponíveis.
WARN — ausência de replicação independente.
```

# 7. Controle para não misturar níveis de confiabilidade

A confiança deve ser atribuída a **cada afirmação**, não ao relatório inteiro.

Uma matriz adequada seria:

| Claim   | Evidência                  | Risco de viés | Consistência |    Confiança | Situação      |
| ------- | -------------------------- | ------------: | -----------: | -----------: | ------------- |
| CLM-001 | Especificação oficial      |         Baixo |         Alta |         Alta | Estabelecida  |
| CLM-002 | Um benchmark               |      Moderado | Desconhecida |        Baixa | Preliminar    |
| CLM-003 | Três estudos independentes |      Moderado |         Alta |     Moderada | Provável      |
| CLM-004 | Estudos divergentes        |          Alto |        Baixa |        Baixa | Conflitante   |
| CLM-005 | Nenhuma evidência direta   |             — |            — | Insuficiente | Não concluída |

O relatório deve separar:

* fatos normativos;
* comportamentos reproduzidos;
* evidência empírica consolidada;
* resultados preliminares;
* opiniões técnicas;
* inferências da IA;
* lacunas de evidência;
* resultados contraditórios.

Não se deve produzir uma “média narrativa” que esconda fontes conflitantes.

### Regra de bloqueio

```text
FAIL — afirmação sem nível de confiança.
FAIL — fontes de qualidade diferente combinadas sem separação.
FAIL — conflito entre fontes omitido.
FAIL — inferência da IA apresentada como conteúdo explícito da fonte.
FAIL — nível de confiança do parágrafo usado para claims diferentes.
```

---

# 8. Artefatos obrigatórios do pipeline

Uma implementação controlada deveria produzir pelo menos seis artefatos:

```text
pesquisa/
├── protocolo_pesquisa.yaml
├── registro_fontes.jsonl
├── matriz_claim_evidencia.json
├── avaliacao_metodologica.json
├── sintese.md
└── relatorio_validacao.json
```

## `protocolo_pesquisa.yaml`

Define:

* pergunta;
* escopo;
* fontes permitidas;
* hierarquia;
* critérios de inclusão e exclusão;
* data-limite;
* versões técnicas;
* critérios para consenso;
* regras de confiança.

## `registro_fontes.jsonl`

Registra uma linha por fonte:

* autoria;
* DOI ou URL canônica;
* versão;
* datas;
* tipo;
* condição pós-publicação;
* financiamento;
* conflitos;
* limitações;
* fonte primária ou secundária.

## `matriz_claim_evidencia.json`

Liga cada afirmação às evidências que efetivamente a sustentam.

## `avaliacao_metodologica.json`

Registra risco de viés, qualidade, aplicabilidade e independência.

## `sintese.md`

Apresenta conclusões separadas por nível de evidência.

## `relatorio_validacao.json`

Registra todos os critérios aprovados, reprovados e indeterminados.

---

# 9. Garantia operacional real

O processo deve ter quatro camadas independentes:

```text
IA pesquisadora
      ↓
IA ou processo revisor independente
      ↓
Validador determinístico de contratos e schemas
      ↓
Aprovação humana para conclusões críticas
```

O validador não avalia somente se um campo existe. Ele deve verificar relações semânticas mínimas:

```text
Se claim_type = "consenso"
então source_level não pode ser "preprint" ou "estudo_unico".

Se source_type = "documentacao_tecnica"
então software_version é obrigatório.

Se conflict_of_interest = "não informado"
então confidence não pode ser elevada sem justificativa.

Se source_status = "retraída"
então a fonte não pode sustentar uma conclusão positiva.

Se evidence_conflict = true
então a seção "fontes_divergentes" é obrigatória.

Se claim_type = "comportamental"
então evidência executável ou justificativa de impossibilidade é obrigatória.
```

## Conclusão

A garantia não está em fazer a IA “ser mais cuidadosa”. Ela está em impedir tecnicamente que uma resposta seja aceita quando:

* a afirmação não estiver ligada à evidência;
* a fonte não tiver versão ou estado verificado;
* evidência preliminar for apresentada como consenso;
* a fonte primária não tiver sido consultada;
* conflitos e limitações não tiverem sido registrados;
* evidências de confiabilidade diferente forem misturadas;
* divergências relevantes forem omitidas.

Mesmo com esses controles, a garantia será de **conformidade com o protocolo**, e não de verdade absoluta. A formulação correta é:

> **O sistema garante que nenhuma conclusão seja aceita sem rastreabilidade, avaliação metodológica, classificação da evidência, validação automática e tratamento explícito das incertezas.**

[1]: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/?utm_source=chatgpt.com "AI Risks and Trustworthiness - AIRC - NIST AI Resource Center"
[2]: https://docs.python.org/3/reference/index.html?utm_source=chatgpt.com "The Python Language Reference"
[3]: https://docs.python.org/3/reference/introduction.html?utm_source=chatgpt.com "1. Introduction — Python 3.14.6 documentation"
[4]: https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/?utm_source=chatgpt.com "Retraction Watch"
[5]: https://peps.python.org/?utm_source=chatgpt.com "PEP 0 – Index of Python Enhancement Proposals (PEPs ..."
[6]: https://www.prisma-statement.org/prisma-2020-statement?utm_source=chatgpt.com "PRISMA 2020 statement"
[7]: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04?utm_source=chatgpt.com "Chapter 4: Searching for and selecting studies"
[8]: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-07?utm_source=chatgpt.com "Chapter 7: Considering bias and conflicts of interest among ..."
[9]: https://docs.python.org/3/reference/index.html?utm_source=chatgpt.com "The Python Language Reference"
[10]: https://peps.python.org/?utm_source=chatgpt.com "PEP 0 – Index of Python Enhancement Proposals (PEPs ..."
[11]: https://docs.python.org/3/library/index.html?utm_source=chatgpt.com "The Python Standard Library"
[13]: https://packaging.python.org/?utm_source=chatgpt.com "Python Packaging User Guide"
[14]: https://github.com/python/cpython?utm_source=chatgpt.com "python/cpython: The Python programming language"
[15]: https://docs.pytest.org/?utm_source=chatgpt.com "pytest documentation"
[16]: https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf?utm_source=chatgpt.com "Secure Software Development Framework (SSDF) Version 1.1"
[17]: https://www.nist.gov/itl/csd/secure-systems-and-applications/source-code-security-analyzers?utm_source=chatgpt.com "Source Code Security Analyzers | NIST"
[18]: https://dl.acm.org/doi/10.1145/3437479.3437483?utm_source=chatgpt.com "ACM SIGSOFT Empirical Standards Released"