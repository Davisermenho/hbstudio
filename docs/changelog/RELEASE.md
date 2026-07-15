# Processo de release

Uma versão somente pode ser publicada quando todos os itens abaixo estiverem
atendidos e evidenciados no respectivo `changes/CHG-AAAA-NNN.json`.

## Checklist

- [ ] ID único e data confirmados.
- [ ] `VERSION`, registro estruturado e `CHANGELOG.md` usam a mesma versão.
- [ ] Motivo, evidência, mudanças e comportamento esperado estão completos.
- [ ] Componentes afetados e incompatibilidades estão declarados.
- [ ] Baseline e candidata foram avaliadas com os mesmos casos.
- [ ] Qualidade, segurança, latência e custo foram medidos ou justificados como
      não aplicáveis.
- [ ] Não existem regressões críticas abertas.
- [ ] Validação visual foi registrada quando a mudança afeta o vídeo.
- [ ] Aprovação identifica responsável, data/hora e evidência.
- [ ] Rollback foi testado ou formalmente classificado como não aplicável.
- [ ] A tag planejada em `version_control.tag`, quando informada, corresponde a
      `v{VERSION}`; `version_control.commit` permanece nulo no pré-release.
- [ ] `python3 scripts/validate_changelog.py --release` termina com código zero.

## Publicação

1. Executar testes e avaliações.
2. Atualizar o registro da mudança e o resumo humano no `CHANGELOG.md`.
3. Executar o gate de release.
4. Revisar o diff completo, inclusive políticas, dependências e configurações.
5. Criar o commit aprovado.
6. Criar a tag anotada `vX.Y.Z` sem alterar novamente o commit aprovado.
7. No evento de tag, validar `v$(cat VERSION) = GITHUB_REF_NAME`, o `HEAD` contra
   `GITHUB_SHA`, os gates da mudança e os manifestos de baseline.
8. Publicar a tag e a release sem usar `--force` e sem mover tags existentes.
9. Criar posteriormente um registro `changes/publications/PUB-AAAA-NNN.json`
   com commit, tag, URL e resultado do CI.

O registro `CHG` representa o estado conhecido antes da publicação. Por isso,
`version_control.commit` deve ser nulo e `publication.status` deve permanecer
`not_released`. Exigir o hash do próprio commit ou marcar uma publicação ainda
não ocorrida cria uma dependência circular. A confirmação posterior pertence ao
registro `PUB` validado por `changes/publication.schema.json`.

Branches protegidas, revisão obrigatória e proteção de tags devem ser configuradas
no provedor Git quando o repositório remoto for criado.
