# Changelog

Este arquivo registra a evolução auditável do sistema. O registro estruturado e
canônico de cada mudança fica em `changes/CHG-AAAA-NNN.json`. Uma versão só pode
ser publicada após passar pelo modo `--release` do validador.

## [0.4.0] — 2026-07-15

**Change ID:** `CHG-2026-001`  
**Estado:** baseline aprovada — publicação pendente  
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
de qualquer alteração posterior.
