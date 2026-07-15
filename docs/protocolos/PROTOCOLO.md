# PROTOCOLO DE IMPLEMENTAÇÃO

> Use o seguinte prompt antes de solicitar qualquer implementação:

```md
Antes de escrever código, pseudocódigo, arquitetura, patch ou proposta de solução, execute exclusivamente o protocolo de confirmação de entendimento abaixo.

OBJETIVO
Confirmar que você compreendeu integralmente a especificação, sem omitir requisitos, inventar comportamentos ou transformar suposições em decisões.

REGRAS OBRIGATÓRIAS

1. Não escreva código, pseudocódigo ou solução nesta etapa.
2. Não acrescente requisitos que não estejam na especificação.
3. Não resolva ambiguidades silenciosamente.
4. Diferencie claramente:
informação confirmada pela especificação;
inferência;
suposição;
informação ausente ou ambígua.
1. Use os identificadores originais dos requisitos.
2. Não altere os critérios de aceite.
3. Quando houver conflito, não escolha uma regra sem aprovação.
4. Termine aguardando aprovação explícita.

FORMATO OBRIGATÓRIO DA RESPOSTA

1. Objetivo compreendido
Explique, em suas palavras

- qual problema deverá ser resolvido;
- por que a solução é necessária;
- qual resultado observável é esperado;
- como será possível verificar que o objetivo foi alcançado.

2. Contexto e usuários
Identifique:

- quem ou o que utilizará o sistema;
- como ele será acionado;
- em qual contexto será executado;
- quais permissões e conhecimentos serão necessários.

3. Escopo incluído
Liste somente os comportamentos que fazem parte da tarefa.

4. Escopo excluído
Liste:
- funcionalidades que não fazem parte da tarefa;
- arquivos, dados ou sistemas que não podem ser alterados;
- melhorias que dependem de autorização.

5. Requisitos interpretados
Para cada requisito, preencha:


| ID | Entendimento | Condição | Entrada | Comportamento | Saída | Critério de aceite |

>Não agrupe requisitos diferentes em uma única linha. 
>Não crie identificadores inexistentes.

6. Ambiente técnico
Confirme:

- linguagem e versão;
- sistema operacional;
- framework;
- dependências e versões;
- forma de execução;
- limitações do ambiente;
- tecnologias permitidas e proibidas.

7. Entradas
Para cada entrada, informe:

- identificador;
- origem;
- tipo;
- formato;
- obrigatoriedade;
- valores permitidos;
- limites;
- validações.

8. Saídas
Para cada saída, informe:

- conteúdo;
- tipo e formato;
- destino;
- momento em que será produzida;
- exemplo esperado, quando disponível.

9. Regras, restrições e proibições
Separe:

- regras obrigatórias;
- exceções;
- restrições técnicas;
- comportamentos proibidos.

10. Situações de erro
Para cada erro previsto, informe:

- causa;
- condição de ocorrência;
- resposta esperada;
- mensagem ou código;
- possibilidade de recuperação;
- decisão de continuar, repetir ou encerrar;
- estado esperado dos dados após o erro.

11. Ambiguidades
Para cada ambiguidade, preencha:

| Requisito ou trecho | Interpretações possíveis | Impacto | Classificação | Pergunta necessária |

Use uma das classificações:
- bloqueadora;
- relevante;
- menor;
- resolvida pela especificação.

> Uma ambiguidade é bloqueadora quando diferentes interpretações podem produzir comportamentos incompatíveis ou causar perda, corrupção ou alteração indevida de dados.

12. Conflitos e inconsistências
> Identifique contradições entre:

- requisitos;
- regras;
- exemplos;
- restrições;

> Não considere nenhuma suposição automaticamente aprovada.

14. Riscos
>Identifique riscos relacionados a:

- interpretação;
- compatibilidade;
- segurança;
- perda ou corrupção de dados;
- regressão;
- dependências;
- critérios não verificáveis.

15. Decomposição da tarefa
>Divida o trabalho em unidades pequenas e ordenadas.

Para cada unidade, informe:
- objetivo;
- requisitos atendidos;
- entrada necessária;
- resultado esperado;
- dependências.

>Não proponha arquitetura, pseudocódigo ou implementação ainda.

16. Matriz de cobertura
Preencha:

| Elemento obrigatório | Encontrado? | Completo? | Observação |

Avalie, no mínimo:
- objetivo;
- problema;
- contexto;
- usuários;
- escopo incluído;
- escopo excluído;
- ambiente técnico;
- entradas;
- saídas;
- requisitos funcionais;
- requisitos não funcionais;
- regras de negócio;
- restrições;
- situações de erro;
- dependências;
- premissas;
- critérios de aceite;
- exemplos;
- casos-limite;
- glossário, quando necessário.

17. Estado do protocolo

> Classifique a especificação como:

**APROVÁVEL**

> Use quando:
- todos os requisitos estiverem cobertos;
- entradas, saídas e restrições estiverem claras;
- os critérios de aceite forem verificáveis;
- não existirem ambiguidades ou conflitos bloqueadores;
- não houver suposições críticas sem aprovação.

**BLOQUEADO**

> Use quando:
- faltar informação necessária;
- existir conflito não resolvido;
- uma ambiguidade puder alterar o comportamento;
- algum requisito não possuir critério verificável;
- uma suposição crítica depender de decisão humana.

Apresente:
- estado;
- justificativa;
- itens que precisam ser corrigidos;
- perguntas que precisam ser respondidas;
- condições necessárias para tornar o protocolo aprovável.

> Não prossiga para proposta de solução, pseudocódigo ou implementação até receber aprovação explícita do usuário.
