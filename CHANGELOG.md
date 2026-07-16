# Changelog

Este arquivo registra a evolução auditável do sistema. O registro estruturado e
canônico de cada mudança fica em `changes/CHG-AAAA-NNN.json`. Uma versão só pode
ser publicada após passar pelo modo `--release` do validador.

## [0.4.6] — 2026-07-15

**Change ID:** `CHG-2026-007`  
**Estado:** `PATCH-ENG-005` aplicado e validado  
**Versão anterior:** `0.4.5`

### Motivo

Corrigir exclusivamente a hierarquia de cabeçalhos de `ENGENHARIA.md`, tornando
as dezoito ações estruturalmente detectáveis e navegáveis.

### Alterações

- conversão de falsos títulos em cabeçalhos;
- uniformização das ações 1 a 18 como H3;
- promoção das seções externas às ações para H2;
- correção do espaço duplicado no título da ação 11;
- inserção do espaçamento exigido ao redor dos novos cabeçalhos.

### Estado

A hierarquia foi corrigida. Os erros de comprimento de linha e linhas em branco
fora do escopo continuam pendentes para ações posteriores.

## [0.4.5] — 2026-07-15

**Change ID:** `CHG-2026-006`  
**Estado:** `PATCH-ENG-004` aplicado e validado  
**Versão anterior:** `0.4.4`

### Motivo

Eliminar ambiguidades e sobreposições na divisão de responsabilidades entre o
contexto, as políticas, o inventário técnico proposto e documentos especializados.

### Alterações

- explicitação das responsabilidades de `CONTEXT.md` e `AGENT_POLICY.md`;
- definição do escopo proposto de `ENGINEERING_CONTEXT.md`;
- preservação de `FERRAMENTAS_TECNICAS` como documento especializado em vídeo;
- preservação da documentação interna como autoridade dos detalhes de projetos.

### Estado

A divisão de responsabilidades foi corrigida. Os demais problemas estruturais e
erros de lint continuam pendentes para ações posteriores.

## [0.4.4] — 2026-07-15

**Change ID:** `CHG-2026-005`  
**Estado:** `PATCH-ENG-003` aplicado e validado  
**Versão anterior:** `0.4.3`

### Motivo

Apresentar no início de `ENGENHARIA.md` um resumo autossuficiente, sustentado pelas
três páginas canônicas do Notion.

### Alterações

- inserção do resumo executivo após o título;
- identificação das responsabilidades das três fontes canônicas;
- declaração da lacuna técnica e da decisão ainda pendente;
- releitura das fontes sem alteração das páginas do Notion.

### Estado

O resumo foi adicionado. Os demais problemas estruturais e erros de lint continuam
pendentes para ações posteriores.

## [0.4.3] — 2026-07-15

**Change ID:** `CHG-2026-004`  
**Estado:** `PATCH-ENG-002` aplicado e validado  
**Versão anterior:** `0.4.2`

### Motivo

Identificar `ENGENHARIA.md` inequivocamente como proposta de criação do contexto
de engenharia, sem executar as demais ações do plano.

### Alteração

- substituição isolada do título de `ENGENHARIA.md`;
- preservação do conteúdo restante e das mudanças preexistentes;
- registro do impacto sintático e semântico observado.

### Estado

O título foi corrigido. Os demais problemas estruturais e erros de lint continuam
pendentes para ações posteriores.

## [0.4.2] — 2026-07-15

**Change ID:** `CHG-2026-003`  
**Estado:** plano documental criado e validado; implementação pendente  
**Versão anterior:** `0.4.1`

### Motivo

Transformar a revisão corrigida de `ENGENHARIA.md` em um plano patch/diff
completo, rastreável e validável, usando o Notion como fonte canônica.

### Alterações

- criação de `patch-diff.md` com 18 ações de implementação;
- critérios de aceitação, verificação, validação e bloqueio por ação;
- matriz de evidências e gate de validação final;
- separação entre políticas existentes e inventário técnico proposto.

### Estado

O plano foi criado e validado estruturalmente. A implementação em
`ENGENHARIA.md`, a alteração de páginas do Notion e a aprovação do conteúdo final
continuam pendentes.

## [0.4.1] — 2026-07-15

**Change ID:** `CHG-2026-002`  
**Estado:** correção de governança aprovada para publicação  
**Versão anterior:** `0.4.0`

### Motivo

Corrigir o gate que exigia que o commit de release contivesse o próprio hash e
uma confirmação de publicação que somente poderia existir depois desse commit.

### Alterações

- separação entre registros pré-release `CHG` e registros posteriores `PUB`;
- registro de `PUB-2026-001` para a publicação imutável da `v0.4.0`;
- validação da tag do evento contra `VERSION`;
- validação de `GITHUB_SHA` contra o commit verificado pelo Git;
- validação dos manifestos de baseline no gate de release;
- testes para aprovação, métricas, tag, SHA e publicação posterior.

### Compatibilidade e risco conhecido

Não há alteração no editor de vídeo nem na baseline publicada. A execução do
workflow da tag `v0.4.0` continuará vermelha por pertencer ao commit imutável;
a correção será comprovada por uma versão posterior.

## [0.4.0] — 2026-07-15

**Change ID:** `CHG-2026-001`  
**Estado:** baseline aprovada e publicada  
**Versão anterior:** estado não versionado

### Motivo

Preservar o protótipo funcional existente como primeira referência rastreável,
antes da modularização e da implantação dos gates completos de qualidade.

### Componentes registrados

- código de renderização e CLI;
- ferramenta de inspeção de frames;
- configuração de exemplo;
- dependências Python e infraestrutura local;
- especificação, documentação e políticas operacionais.

### Comportamento observado

O protótipo recebe uma configuração JSON, processa todos os clipes ou um clipe
selecionado e exporta MP4 com abertura, análise, continuação e replay. A baseline
restaurada foi executada em um teste funcional de fumaça reproduzível, com
integridade da fonte e da saída verificadas.

### Avaliação e regressões

- qualidade: 1/1 caso funcional aprovado técnica e audiovisualmente;
- segurança de dependências: nenhuma vulnerabilidade conhecida encontrada pelo `pip-audit 2.10.1`;
- latência: 35,92 s observados; p50 e p95 não disponíveis;
- custo: CPU, memória e armazenamento medidos; hardware e energia não calculados;
- regressões: não determináveis sem uma versão anterior comparável;
- limitações: cobertura funcional restrita a um teste de fumaça.

### Aprovação e reversão

A publicação foi aprovada por Davi Sermenho em 2026-07-15T16:12:00-03:00. A
origem era um diretório sem controle de versão, portanto não existe tag anterior
para reversão. O registro estruturado documenta a preservação necessária antes
de qualquer alteração posterior. A publicação está registrada separadamente em
`changes/publications/PUB-2026-001.json`; a falha do workflow da tag foi
classificada como defeito de governança e não invalida a integridade funcional
da baseline.
