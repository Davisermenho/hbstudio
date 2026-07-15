# Procedimento de rollback

## Preparação

Antes da publicação, confirme que a tag alvo existe, que os arquivos de entrada
permanecem preservados e que configurações incompatíveis possuem plano de migração
reversa. Nunca use o diretório `saida/` como única evidência ou backup.

## Execução controlada

1. Interromper novas renderizações da versão afetada.
2. Preservar execution logs, configuração usada, artefatos e mensagem de erro.
3. Registrar a decisão no changelog sem alterar a entrada histórica original.
4. Criar uma branch a partir da tag estável anterior.
5. Restaurar ou migrar a configuração conforme o registro da mudança.
6. Executar validação de ambiente, testes e uma renderização sintética.
7. Inspecionar a saída e obter a aprovação aplicável.
8. Publicar uma nova versão de correção; não mover nem reutilizar tags existentes.
9. Marcar a versão defeituosa como `rolled_back` e registrar a nova evidência.

## Aceitação

O rollback é aceito somente quando a versão ativa é identificável, os testes
passam, a saída relevante foi verificada e os execution logs confirmam a versão
restaurada. A simples troca de arquivos não caracteriza rollback concluído.

