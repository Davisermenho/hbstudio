# Política de versionamento e changelog

## Objetivo

Toda mudança relevante deve ser rastreável desde o problema observado até sua
avaliação, aprovação, publicação e eventual reversão. O histórico Git, sozinho,
não substitui o changelog; o changelog, sozinho, não substitui o histórico Git.

## Identificadores e versões

- Cada mudança recebe um identificador imutável `CHG-AAAA-NNN`.
- A numeração é sequencial dentro do ano e nunca deve ser reutilizada.
- O software usa versionamento semântico `MAJOR.MINOR.PATCH`.
- `MAJOR` indica incompatibilidade do contrato ou migração obrigatória.
- `MINOR` indica funcionalidade compatível adicionada.
- `PATCH` indica correção compatível, documentação operacional ou segurança sem
  alteração incompatível do contrato.
- A versão do contrato JSON é independente da versão do aplicativo e deve ser
  registrada em toda mudança que afete configurações.

## Componentes controlados

O campo `components` deve identificar todos os itens afetados: código, CLI,
renderização, tracking, configuração/schema, ferramentas, dependências,
infraestrutura, documentação, políticas, fixtures e datasets de avaliação.
Campos relacionados a modelos de IA, provedores, prompts ou parâmetros devem ser
usados somente quando esses componentes participarem da execução do produto.

## Fluxo obrigatório

1. Registrar problema, evidência e hipótese no arquivo da mudança.
2. Definir a versão candidata e os componentes afetados.
3. Implementar a alteração em branch própria.
4. Executar as mesmas avaliações sobre baseline e candidata.
5. Registrar qualidade, segurança, latência, custo e regressões.
6. Registrar incompatibilidades e procedimento de rollback.
7. Obter aprovação técnica e, quando aplicável, validação visual/tática.
8. Executar `python3 scripts/validate_changelog.py --release`.
9. Criar commit e tag imutável somente após todos os gates.
10. No evento de tag, validar a tag contra `VERSION` e `GITHUB_SHA` contra o
    commit verificado pelo Git.
11. Registrar a publicação ocorrida em `changes/publications/PUB-AAAA-NNN.json`.
12. Monitorar execuções posteriores e registrar regressões descobertas.

## Estados

- `pending`: informação ou decisão ainda não confirmada.
- `approved`: mudança aceita pelo responsável identificado.
- `rejected`: mudança recusada; não pode ser publicada.
- `not_released`: estado obrigatório do registro `CHG`, criado antes da publicação.
- `released`: publicação posterior associada a commit e tag em um registro `PUB`.
- `rolled_back`: publicação retirada por reversão controlada, registrada em `PUB`.

Execução, verificação, aceitação e conclusão são estados diferentes. A criação do
arquivo ou o sucesso de uma ferramenta não constituem aprovação.

## Aprovação

A aprovação precisa identificar pessoa, data/hora e evidência. Mudanças visuais ou
táticas exigem validação de Davi e, quando envolver interpretação técnica, de
Daniela. Nenhum agente pode preencher aprovação humana por inferência.

## Reversão

Cada mudança posterior à baseline deve apontar uma tag existente, listar comandos
ou etapas de restauração, informar migração de configuração e registrar o teste do
rollback. Reverter código não autoriza apagar registros ou substituir vídeos de
origem.

## Validação

Validação cotidiana do contrato:

```bash
python3 scripts/validate_changelog.py
python3 -m unittest discover -s tests -v
```

Gate de publicação:

```bash
python3 scripts/validate_changelog.py --release
```

Gate executado pelo evento de tag:

```bash
python3 scripts/validate_changelog.py --release --tag-context
```

O primeiro comando pode terminar com avisos. O gate de publicação transforma
aprovações, avaliações, evidências e rollback pendentes em erros bloqueadores. O
contexto da tag é obtido de `GITHUB_REF_NAME`, `GITHUB_SHA` e do `HEAD`; ele não é
antecipado no registro da mudança.
