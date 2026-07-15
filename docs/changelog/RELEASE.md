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
- [ ] Commit e tag estão registrados.
- [ ] `python3 scripts/validate_changelog.py --release` termina com código zero.

## Publicação

1. Executar testes e avaliações.
2. Atualizar o registro da mudança e o resumo humano no `CHANGELOG.md`.
3. Executar o gate de release.
4. Revisar o diff completo, inclusive políticas, dependências e configurações.
5. Criar o commit aprovado.
6. Preencher o hash do commit no registro, validar novamente e criar a tag `vX.Y.Z`.
7. Alterar `publication.status` para `released` e registrar `published_at`.
8. Confirmar em uma nova execução que a versão publicada aparece no manifesto.

Branches protegidas, revisão obrigatória e proteção de tags devem ser configuradas
no provedor Git quando o repositório remoto for criado.

