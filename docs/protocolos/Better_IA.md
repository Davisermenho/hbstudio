# MELHORAR O DESENVOLVIMENTO COM IA

A inteligência artificial frequentemente falha em captar a intenção humana, o que resulta em erros na geração de código. Superar esse desafio exige uma abordagem multidisciplinar, deixando esse assunto na interseção de várias áreas dos domínios de conhecimento.

1. **Engenharia de Software** – Trata da análise, projeto, implementação e manutenção de sistemas. Se você está desenvolvendo um script, este é o domínio principal.  
2. **Engenharia de Prompt (Prompt Engineering)** – É a área que estuda como formular instruções para que modelos de IA entendam corretamente sua intenção. Muitas vezes o problema não é a IA "não saber programar", mas a comunicação entre você e ela.  
3. **Especificação de Requisitos (Requirements Engineering)** – Ensina como transformar uma ideia em requisitos claros e não ambíguos. Quanto mais precisa for a especificação, maior a chance da IA gerar o código esperado.  
4. **Arquitetura de Software** – Quando o script cresce, definir a estrutura antes de escrever o código evita que a IA se perca ou gere soluções inconsistentes.  
5. **Design de Software e Padrões de Projeto** – Ajudam a organizar o código de forma que a IA consiga manter consistência ao longo do desenvolvimento.  
6. **Interação Humano*Computador (Human*Computer Interaction * HCI)** – Estuda como humanos se comunicam com sistemas computacionais, incluindo modelos de IA.

## RESOLVENDO OS PROBLEMAS

Na prática, o que você está enfrentando é um problema de "comunicação de requisitos"

Por exemplo, em vez de dizer:
"Crie um sistema para gerenciar usuários."

Você pode especificar:

* Objetivo do sistema.  
* Linguagem (Python, JavaScript, etc.).  
* Framework.  
* Estrutura dos arquivos.  
* Entradas.  
* Saídas.  
* Restrições.  
* Critérios de aceitação.  
* O que **não** deve ser feito.

Quanto mais detalhada for a especificação, menor a chance da IA "inventar" uma solução diferente da que você imaginou.

### **Existe até um nome para essa habilidade**

Hoje muitos desenvolvedores chamam isso de **AI*Assisted Software Development** (Desenvolvimento de Software Assistido por IA). Esse campo reúne práticas como:

* Escrever bons prompts.  
* Dividir o projeto em pequenas tarefas.  
* Validar continuamente o código gerado.  
* Fornecer contexto suficiente para a IA.  
* Revisar e testar cada etapa antes de seguir.

Esse conjunto de práticas está se tornando uma competência própria para quem desenvolve software com auxílio de modelos de IA.

Se o seu objetivo é trabalhar de forma muito eficiente com IA na programação, vale estudar principalmente:

* Engenharia de Software.  
* Engenharia de Requisitos.  
* Engenharia de Prompt.  
* Design e Arquitetura de Software.  
* Desenvolvimento de Software Assistido por IA (AI*Assisted Software Development).

Essas áreas, combinadas, explicam exatamente os problemas que você descreveu e oferecem métodos para reduzi*los significativamente.

## 1. AI Assisted Software Development

Para reduzir significativamente os erros da IA durante a criação do seu script, você precisa tratar a IA menos como “alguém que adivinha sua ideia” e mais como um desenvolvedor que depende de especificações, exemplos, testes e revisão.

## 1.1 Escreva uma especificação  

Antes de solicitar a implementação, escreva uma especificação estruturada, verificável e suficientemente precisa para que outra pessoa — ou uma IA — consiga compreender o comportamento esperado sem depender de explicações verbais adicionais.

A especificação não deve apenas descrever uma ideia. Ela deve transformar a ideia em requisitos pequenos, objetivos, rastreáveis e verificáveis por inspeção ou teste.

>A ESPECIFICAÇÃO foi escrita em `ESPECIFICAÇÃO.md`

< ! - LEIA O CONTEÚDO DO ARQUIVO `ESPECIFICAÇÃO.md` VERIFICANDO CADA SESSÃO DO CONTEUDO, E EM SEGUIDA VALIDE CONTRA AS INFORMAÇÕES ABAIXO.>

### 1.1.1 Estrutura mínima obrigatória

A especificação deve conter:

1. objetivo e problema;  
2. contexto de uso;  
3. usuários, sistemas ou processos envolvidos;  
4. escopo incluído;  
5. escopo excluído;  
6. ambiente técnico;  
7. entradas;  
8. saídas;  
9. requisitos funcionais;  
10. requisitos não funcionais;  
11. regras de negócio;  
12. restrições;  
13. situações de erro;  
14. dependências e premissas;  
15. critérios de aceite;  
16. exemplos válidos, inválidos e casos*limite;  
17. glossário, quando houver termos que possam causar ambiguidade.

### 1.1.2 Objetivo e problema

A especificação deve declarar:

* qual problema precisa ser resolvido;  
* por que o script é necessário;  
* qual resultado observável é esperado;  
* como será possível saber que o problema foi resolvido.

Critérios de aceite:

* o problema está descrito de forma explícita;  
* o resultado esperado está relacionado diretamente ao problema;  
* termos vagos, como “melhorar” ou “organizar”, foram acompanhados de uma explicação mensurável;  
* outra pessoa consegue explicar a finalidade do script após ler somente essa parte.

### 1.1.3 Contexto e usuários

Deve ser identificado:

* quem ou o que utilizará o script;  
* se a execução será manual, automática ou acionada por outro sistema;  
* em qual situação o script será executado;  
* quais permissões serão necessárias;  
* qual conhecimento técnico é esperado do usuário.

Critérios de aceite:

* o executor está identificado;  
* a forma de acionamento está definida;  
* o contexto de uso está descrito;  
* as permissões relevantes estão documentadas.

### 1.1.4 Escopo

O escopo deve ser separado em:

Incluído:  

* comportamentos que o script deverá implementar.

Excluído:  

* funcionalidades que não fazem parte da tarefa;  
* arquivos, dados ou sistemas que não podem ser alterados;  
* melhorias adicionais que dependem de autorização.

Critérios de aceite:

* os limites da implementação estão explícitos;  
* é possível distinguir uma funcionalidade obrigatória de uma funcionalidade futura;  
* o que não deve ser feito está declarado de maneira testável.

### 1.1.5 Ambiente técnico

Deve informar, quando aplicável:

* linguagem e versão;  
* sistema operacional;  
* framework;  
* bibliotecas e respectivas versões;  
* banco de dados;  
* estrutura de arquivos;  
* forma de instalação e execução;  
* acesso ou ausência de acesso à internet;  
* limites de memória, processamento ou armazenamento;  
* tecnologias proibidas.

Critérios de aceite:

* não é necessário presumir versões ou dependências;  
* as bibliotecas permitidas e proibidas estão identificadas;  
* o comando ou procedimento de execução está documentado;  
* o ambiente pode ser reproduzido.

### 1.1.6 Entradas

Para cada entrada, informar:

* identificador;  
* nome;  
* origem;  
* tipo;  
* formato;  
* obrigatoriedade;  
* valores permitidos;  
* limites;  
* valor padrão, quando houver;  
* validações;  
* exemplo válido;  
* exemplo inválido.

Critérios de aceite:

* todas as entradas estão enumeradas;  
* entradas obrigatórias e opcionais estão diferenciadas;  
* tipo, formato e origem estão definidos;  
* valores inválidos possuem comportamento esperado;  
* os exemplos são consistentes com as regras.

### 1.1.7 Saídas

Para cada saída, informar:

* identificador;  
* conteúdo;  
* tipo e formato;  
* destino;  
* momento em que será produzida;  
* codificação, quando aplicável;  
* exemplo esperado.

Critérios de aceite:

* todas as saídas observáveis estão documentadas;  
* formato e destino estão definidos;  
* mensagens ao usuário estão diferenciadas de arquivos, logs ou valores retornados;  
* existe pelo menos um exemplo de saída completa.

### 1.1.8 Escrita dos requisitos

Cada requisito deve:

* possuir um identificador único;  
* representar somente um comportamento principal;  
* declarar a condição em que se aplica;  
* declarar o comportamento esperado;  
* apresentar um resultado observável;  
* possuir ao menos um critério de aceite;  
* informar prioridade e origem quando necessário;  
* registrar suposições explicitamente.

Formato recomendado:

ID: RF*001  
Tipo: requisito funcional  
Prioridade: obrigatória  
Descrição: [comportamento esperado]  
Condição: [quando o requisito se aplica]  
Entrada: [dados envolvidos]  
Saída: [resultado observável]  
Exceções: [situações especiais]  
Restrições: [limites da implementação]  
Critérios de aceite: [verificações objetivas]  
Exemplos: [caso normal, inválido e limite]

### 1.1.9 Requisitos de qualidade

Cada requisito deve ser:

* necessário: representa uma necessidade real;  
* correto: corresponde ao comportamento desejado;  
* completo: contém condição, comportamento e resultado;  
* atômico: descreve um comportamento principal;  
* claro: utiliza linguagem direta;  
* não ambíguo: permite apenas uma interpretação operacional;  
* consistente: não contradiz outros requisitos;  
* factível: pode ser implementado no ambiente definido;  
* verificável: pode ser comprovado por teste ou inspeção;  
* rastreável: possui identificador e origem;  
* independente da solução, quando a tecnologia ainda não estiver decidida.

### 1.1.10 Linguagem recomendada

Preferir frases com:

* sujeito identificado;  
* verbo obrigatório;  
* objeto definido;  
* condição;  
* resultado mensurável.

Estrutura:

“Quando [condição], o sistema deve [comportamento], produzindo [resultado observável].”

Evitar palavras vagas:

* rápido;  
* adequado;  
* simples;  
* eficiente;  
* intuitivo;  
* normalmente;  
* entre outros;  
* quando possível.

Substituir por limites observáveis:

* “em até dois segundos”;  
* “arquivo de no máximo 10 MB”;  
* “codificação UTF*8”;  
* “sem modificar o arquivo original”;  
* “retornar código HTTP 200”.

### 1.1.11 Regras de negócio

Cada regra deve possuir:

* condição;  
* ação;  
* resultado;  
* exceção, quando existir;  
* prioridade em relação a regras conflitantes.

Formato recomendado:

Dado que [estado inicial],  
quando [evento ou ação],  
então [resultado esperado].

### 1.1.12 Situações de erro

Para cada erro previsível, definir:

* causa;  
* condição de ocorrência;  
* comportamento esperado;  
* mensagem ou código retornado;  
* registro em log, quando necessário;  
* possibilidade de recuperação;  
* decisão de continuar, repetir ou encerrar;  
* garantia de que não haverá perda ou corrupção de dados.

Critérios de aceite:

* os principais erros previsíveis estão enumerados;  
* cada erro possui uma resposta definida;  
* mensagens são específicas e acionáveis;  
* o estado dos dados após o erro está documentado.

### 1.1.13 Critérios de aceite

Cada requisito deve possuir critérios de aceite:

* objetivos;  
* observáveis;  
* mensuráveis;  
* reproduzíveis;  
* relacionados diretamente ao requisito;  
* independentes de julgamento subjetivo;  
* acompanhados de resultado esperado.

Um critério de aceite deve permitir uma resposta binária: aprovado ou reprovado.

Formato recomendado:

Dado [estado inicial],  
quando [ação],  
então [resultado esperado].

### 1.1.14 Exemplos e casos de teste

Incluir, sempre que aplicável:

* caso normal;  
* entrada vazia;  
* entrada inválida;  
* valor mínimo;  
* valor máximo;  
* duplicidade;  
* ausência de arquivo;  
* falha de permissão;  
* dado inesperado;  
* conflito entre regras;  
* interrupção da operação.

Os exemplos não substituem os requisitos. Eles demonstram como os requisitos devem ser interpretados.

### 1.1.15 Critério geral de conclusão

A especificação será considerada pronta quando:

* todos os campos obrigatórios estiverem preenchidos;  
* cada requisito possuir identificador;  
* cada requisito tratar um comportamento principal;  
* todas as entradas e saídas estiverem definidas;  
* restrições e proibições estiverem explícitas;  
* ambiguidades conhecidas estiverem resolvidas ou registradas;  
* cada requisito possuir pelo menos um critério de aceite;  
* casos normais, inválidos e limites estiverem representados;  
* não existirem contradições conhecidas;  
* outra pessoa puder compreender e testar o comportamento esperado sem precisar perguntar ao autor o que ele quis dizer.

Exemplo ruim:

Crie um script para organizar arquivos.

Exemplo melhorado:

Objetivo:  
Organizar automaticamente os arquivos existentes em uma pasta, reduzindo a separação manual por tipo.

Ambiente:  
Python 3.12, Windows 11 e somente biblioteca padrão.

Escopo incluído:  
Processar os arquivos presentes diretamente na pasta informada.

Escopo excluído:  
Não percorrer subpastas e não modificar o conteúdo dos arquivos.

RF*001 — Seleção da pasta  
O script deve receber do usuário o caminho absoluto de uma pasta existente.

Critério de aceite:  
Dado um caminho válido, quando o script for iniciado, então ele deverá começar a leitura da pasta informada.

RF*002 — Classificação  
O script deve mover cada arquivo para uma subpasta correspondente à sua extensão.

Critério de aceite:  
Dado o arquivo “relatorio.pdf”, quando o processamento terminar, então o arquivo deverá estar na subpasta “PDF”.

RF*003 — Nomes duplicados  
Quando já existir um arquivo com o mesmo nome no destino, o script deve preservar ambos, acrescentando um número sequencial ao novo nome.

Critério de aceite:  
Dado que “foto.jpg” já existe no destino, quando outro arquivo com esse nome for processado, então ele deverá ser salvo como “foto_1.jpg”, sem sobrescrever o arquivo anterior.

Restrição:  
O script não deve excluir, sobrescrever ou modificar o conteúdo de arquivos.

Saída:  
Ao final, exibir as quantidades de arquivos movidos, ignorados e não processados.

Erro:  
Se a pasta não existir, o script deverá encerrar sem criar diretórios e apresentar a mensagem “A pasta informada não foi encontrada”.

Essa estrutura reduz ambiguidades porque separa objetivo, escopo, requisitos, restrições, erros e critérios verificáveis. Ela também permite que a implementação produzida pela IA seja comparada diretamente com resultados esperados.

### 1.1.16 Template reutilizável

```txt
Nome da especificação:  
Objetivo:  
Problema:  
Contexto:  
Usuários ou sistemas envolvidos:  
Escopo incluído:  
Escopo excluído:  
Ambiente técnico:  
Dependências:  
Premissas:  
Entradas:  
Saídas:  
Requisitos funcionais:  
Requisitos não funcionais:  
Regras de negócio:  
Restrições:  
Situações de erro:  
Critérios de aceite:  
Exemplos:  
Casos*limite:  
Questões em aberto:  
Glossário:
```

### 1.1.17 Checklist antes de enviar à IA

* O problema e o objetivo estão claros?  
* O escopo incluído e excluído está definido?  
* Cada requisito possui somente um comportamento principal?  
* Os requisitos utilizam termos mensuráveis?  
* Entradas, saídas e erros estão definidos?  
* As proibições estão explícitas?  
* Cada requisito possui critério de aceite?  
* Existem exemplos válidos, inválidos e casos*limite?  
* As suposições estão declaradas?  
* A IA poderá verificar objetivamente se concluiu a tarefa?

## **2. Peça para a IA repetir o entendimento antes de programar**

Não solicite código, pseudocódigo, arquitetura ou proposta de solução imediatamente. Primeiro, execute um protocolo formal de confirmação do entendimento.

O objetivo dessa etapa é verificar se a IA compreendeu integralmente a especificação produzida na seção 1.1, sem omitir requisitos, inventar comportamentos ou transformar suposições em decisões.

### 2.1 Finalidade do protocolo

O protocolo deve confirmar:

* qual problema será resolvido;  
* qual resultado observável é esperado;  
* quais comportamentos estão incluídos no escopo;  
* quais comportamentos estão excluídos;  
* quais requisitos precisam ser atendidos;  
* quais entradas e saídas estão envolvidas;  
* quais regras, restrições e erros foram definidos;  
* quais critérios de aceite serão usados;  
* quais informações estão ausentes, conflitantes ou ambíguas.

A resposta desta etapa não é uma solução. É uma verificação estruturada da compreensão da especificação.

### 2.2 Regras de bloqueio

Durante o protocolo, a IA deve obedecer às seguintes regras:

1. Não escrever código, pseudocódigo, arquitetura, patch ou solução.  
2. Não acrescentar requisitos que não estejam na especificação.  
3. Não alterar os critérios de aceite fornecidos.  
4. Não resolver ambiguidades silenciosamente.  
5. Não escolher entre requisitos conflitantes sem autorização.  
6. Não apresentar inferências como informações confirmadas.  
7. Usar os identificadores originais dos requisitos.  
8. Registrar explicitamente qualquer suposição.  
9. Informar quando uma informação necessária estiver ausente.  
10. Aguardar aprovação explícita antes de avançar.

### 2.3 Prompt do protocolo de confirmação

Use o seguinte prompt antes de solicitar qualquer implementação:

Antes de escrever código, pseudocódigo, arquitetura, patch ou proposta de solução, execute exclusivamente o protocolo de confirmação de entendimento abaixo.

**OBJETIVO**  
Confirmar que você compreendeu integralmente a especificação, sem omitir requisitos, inventar comportamentos ou transformar suposições em decisões.

**REGRAS OBRIGATÓRIAS**
Seguir as seguintes regras:

1. Não escreva código, pseudocódigo ou solução nesta etapa.  
2. Não acrescente requisitos que não estejam na especificação.  
3. Não resolva ambiguidades silenciosamente.  
4. Diferencie claramente:
   * informação confirmada pela especificação;  
   * inferência;  
   * suposição;  
   * informação ausente ou ambígua.
5. Use os identificadores originais dos requisitos.  
6. Não altere os critérios de aceite.  
7. Quando houver conflito, não escolha uma regra sem aprovação.  
8. Termine aguardando aprovação explícita.

**FORMATO OBRIGATÓRIO DA RESPOSTA**  
**1. Objetivo compreendido**  
Explique, em suas palavras:  

* qual problema deverá ser resolvido;  
* por que a solução é necessária;  
* qual resultado observável é esperado;  
* como será possível verificar que o objetivo foi alcançado.

**2. Contexto e usuários**  
Identifique:  

* quem ou o que utilizará o sistema;  
* como ele será acionado;  
* em qual contexto será executado;  
* quais permissões e conhecimentos serão necessários.

**3. Escopo incluído**  
Liste somente os comportamentos que fazem parte da tarefa.

**4. Escopo excluído**
Liste:  

* funcionalidades que não fazem parte da tarefa;  
* arquivos, dados ou sistemas que não podem ser alterados;  
* melhorias que dependem de autorização.

**5. Requisitos interpretados**
Para cada requisito, preencha:  

| ID | Entendimento | Condição | Entrada | Comportamento | Saída | Critério de aceite |  
Não agrupe requisitos diferentes em uma única linha. Não crie identificadores inexistentes.

**6. Ambiente técnico**
Confirme:  

* linguagem e versão;  
* sistema operacional;  
* framework;  
* dependências e versões;  
* forma de execução;  
* limitações do ambiente;  
* tecnologias permitidas e proibidas.

**7. Entradas**
Para cada entrada, informe:  

* identificador;  
* origem;  
* tipo;  
* formato;  
* obrigatoriedade;  
* valores permitidos;  
* limites;  
* validações.

**8. Saídas**  
Para cada saída, informe:  

* conteúdo;  
* tipo e formato;  
* destino;  
* momento em que será produzida;  
* exemplo esperado, quando disponível.

**9. Regras, restrições e proibições**  
Separe:  

* regras obrigatórias;  
* exceções;  
* restrições técnicas;  
* comportamentos proibidos.

**10. Situações de erro**  
Para cada erro previsto, informe:

* causa;  
* condição de ocorrência;  
* resposta esperada;  
* mensagem ou código;  
* possibilidade de recuperação;  
* decisão de continuar, repetir ou encerrar;  
* estado esperado dos dados após o erro.

**11. Ambiguidades**  
Para cada ambiguidade, preencha:

| Requisito ou trecho | Interpretações possíveis | Impacto | Classificação | Pergunta necessária |

Use uma das classificações:  

* bloqueadora;  
* relevante;  
* menor;  
* resolvida pela especificação.

Uma ambiguidade é bloqueadora quando diferentes interpretações podem produzir comportamentos incompatíveis ou causar perda, corrupção ou alteração indevida de dados.

**12. Conflitos e inconsistências**
Identifique contradições entre:  

* requisitos;  
* regras;  
* exemplos;  
* restrições;  
* critérios de aceite;  
* escopo incluído e excluído.

Quando não houver conflito aparente, declare explicitamente: “A verificação de consistência foi realizada e não foram encontradas contradições aparentes.”

**13. Suposições**  
Preencha:

| Suposição proposta | Motivo | Impacto | Requer aprovação? |

Não considere nenhuma suposição automaticamente aprovada.

**14. Riscos**  
Identifique riscos relacionados a:  

* interpretação;  
* compatibilidade;  
* segurança;  
* perda ou corrupção de dados;  
* regressão;  
* dependências;  
* critérios não verificáveis.

**15. Decomposição da tarefa**
Divida o trabalho em unidades pequenas e ordenadas.  
Para cada unidade, informe:  

* objetivo;  
* requisitos atendidos;  
* entrada necessária;  
* resultado esperado;  
* dependências.

Não proponha arquitetura, pseudocódigo ou implementação ainda.

**16. Matriz de cobertura**
Preencha:

| Elemento obrigatório | Encontrado? | Completo? | Observação |

Avalie, no mínimo:  

* objetivo;
* problema;  
* contexto;  
* usuários;  
* escopo incluído;  
* escopo excluído;  
* ambiente técnico;  
* entradas;  
* saídas;  
* requisitos funcionais;  
* requisitos não funcionais;  
* regras de negócio;  
* restrições;  
* situações de erro;  
* dependências;  
* premissas;  
* critérios de aceite;  
* exemplos;  
* casos*limite;  
* glossário, quando necessário.

**17. Estado do protocolo**  
Classifique a especificação como:

APROVÁVEL

Use quando:  

* todos os requisitos estiverem cobertos;  
* entradas, saídas e restrições estiverem claras;  
* os critérios de aceite forem verificáveis;  
* não existirem ambiguidades ou conflitos bloqueadores;  
* não houver suposições críticas sem aprovação.

BLOQUEADO

Use quando:  

* faltar informação necessária;  
* existir conflito não resolvido;  
* uma ambiguidade puder alterar o comportamento;  
* algum requisito não possuir critério verificável;  
* uma suposição crítica depender de decisão humana.

Apresente:

* estado;
* justificativa;  
* itens que precisam ser corrigidos;  
* perguntas que precisam ser respondidas;  
* condições necessárias para tornar o protocolo aprovável.

>Não prossiga para proposta de solução, pseudocódigo ou implementação até receber aprovação explícita do usuário.

### 2.4 Critérios de aceite do protocolo

O protocolo será considerado corretamente executado quando:

* nenhum código ou pseudocódigo tiver sido produzido;  
* todos os requisitos estiverem associados aos seus identificadores;  
* nenhum requisito inexistente tiver sido criado;  
* fatos, inferências e suposições estiverem separados;  
* entradas, saídas, regras, restrições e erros estiverem cobertos;  
* ambiguidades estiverem localizadas e classificadas;  
* conflitos tiverem sido verificados explicitamente;  
* suposições estiverem registradas e não aprovadas automaticamente;  
* a tarefa tiver sido decomposta sem antecipar a solução;  
* a matriz de cobertura avaliar todos os elementos da seção 1.1;  
* o resultado terminar em APROVÁVEL ou BLOQUEADO;  
* a IA aguardar uma autorização explícita para continuar.

### 2.5 Fluxo após a confirmação

Se o estado for BLOQUEADO:

* responda às perguntas;  
* corrija ou complete a especificação;  
* execute novamente o protocolo.

Se o estado for APROVÁVEL:

* revise a interpretação;  
* aprove ou corrija o entendimento;  
* somente depois solicite a proposta de solução e o pseudocódigo.

O fluxo recomendado passa a ser:

especificar → confirmar entendimento → resolver ambiguidades → aprovar o entendimento → propor a solução → escrever o pseudocódigo → implementar → testar → revisar.

## **3. Divida o script em partes pequenas**

Quanto maior a tarefa enviada de uma só vez, maior a probabilidade de a IA:

* esquecer alguma regra;  
* misturar responsabilidades;  
* criar funções incompatíveis;  
* alterar partes que já estavam funcionando;  
* produzir código difícil de testar.

Divida o projeto em módulos, por exemplo:

* leitura das configurações;  
* validação das entradas;  
* processamento principal;  
* gravação dos resultados;  
* tratamento de erros;  
* geração de relatório;  
* testes.

Solicite e valide uma parte de cada vez.

## Conceito central

**Dividir o script em partes pequenas** significa transformar uma tarefa ampla em unidades independentes, compreensíveis, implementáveis e verificáveis.

A finalidade não é apenas criar vários arquivos ou funções. A decomposição deve reduzir a quantidade de decisões que a IA precisa tomar simultaneamente.

## 1. Separar responsabilidades

Cada parte deve possuir **uma responsabilidade principal**.

Exemplo:

* leitura: obtém os dados;
* validação: verifica se os dados são aceitáveis;
* processamento: aplica as regras;
* persistência: grava os resultados;
* apresentação: informa o resultado ao usuário.

Uma parte não deve, ao mesmo tempo:

* ler arquivos;
* validar conteúdo;
* aplicar regras;
* salvar resultados;
* exibir mensagens.

Quanto mais responsabilidades misturadas, maior a dificuldade para testar, corrigir e substituir a parte.

## 2. Definir contratos entre as partes

A decomposição só funciona quando cada unidade possui um contrato claro.

Para cada parte, definir:

```text
Nome:
Responsabilidade:
Entradas:
Saídas:
Regras:
Erros:
Efeitos colaterais:
Dependências:
Critérios de aceite:
```

Exemplo:

```text
Nome:
validar_caminho

Responsabilidade:
Verificar se o caminho informado pode ser processado.

Entrada:
Uma string contendo o caminho.

Saída:
Um objeto Path validado.

Erros:
ValueError se o valor estiver vazio.
FileNotFoundError se o caminho não existir.
NotADirectoryError se o caminho não for uma pasta.

Efeitos colaterais:
Nenhum.

Critério de aceite:
A função não cria, remove, move ou modifica arquivos.
```

## 3. Separar lógica de negócio de infraestrutura

A lógica de negócio representa **o que o sistema deve fazer**.

A infraestrutura representa **como o sistema interage com o ambiente**.

Exemplo:

### Infraestrutura

* ler arquivos;
* acessar banco de dados;
* chamar APIs;
* escrever logs;
* salvar relatórios.

### Lógica de negócio

* classificar um arquivo pela extensão;
* determinar o nome de destino;
* decidir se um registro é válido;
* calcular um valor;
* resolver uma duplicidade.

Essa separação permite testar as regras sem depender do sistema de arquivos, da rede ou do banco de dados.

## 4. Organizar por fluxo de dados

Uma forma eficiente de decompor é acompanhar o caminho percorrido pelos dados:

```text
entrada
→ leitura
→ conversão
→ validação
→ processamento
→ geração do resultado
→ gravação
→ relatório
```

Cada etapa deve receber uma saída válida da etapa anterior.

Exemplo:

```text
caminho informado
→ caminho validado
→ lista de arquivos
→ arquivos classificados
→ plano de movimentação
→ arquivos movimentados
→ relatório final
```

## 5. Diferenciar planejamento de execução

Antes de alterar dados, é recomendável criar um plano.

Em vez de:

```text
ler arquivo → mover imediatamente
```

Preferir:

```text
ler arquivos
→ analisar
→ criar plano de alterações
→ validar o plano
→ executar o plano
→ conferir o resultado
```

Isso reduz o risco de:

* alterações parciais;
* perda de dados;
* sobrescrita;
* decisões inconsistentes;
* dificuldade de desfazer operações.

## 6. Definir a granularidade adequada

Uma parte não deve ser grande demais nem pequena demais.

### Grande demais

```text
processar_tudo()
```

Essa função pode esconder leitura, validação, transformação, gravação e tratamento de erros.

### Pequena demais

```text
obter_primeiro_caractere()
adicionar_um()
converter_para_string()
```

Partes excessivamente pequenas aumentam a quantidade de conexões e tornam o fluxo difícil de acompanhar.

### Granularidade adequada

Uma unidade deve representar uma ação relevante do domínio:

```text
validar_configuracao()
listar_arquivos()
classificar_arquivo()
resolver_nome_duplicado()
criar_plano_de_movimentacao()
executar_movimentacoes()
gerar_relatorio()
```

## 7. Identificar dependências

Cada unidade deve informar do que depende.

Exemplo:

```text
listar_arquivos
depende de:
- caminho validado

criar_plano_de_movimentacao
depende de:
- lista de arquivos
- regras de classificação
- política de duplicidade

executar_movimentacoes
depende de:
- plano validado
```

Isso permite estabelecer a ordem correta de implementação.

## 8. Implementar na ordem de menor risco

Uma sequência segura é:

1. definir modelos e contratos;
2. implementar funções puras;
3. validar entradas;
4. criar o planejamento das operações;
5. implementar leitura;
6. implementar escrita ou alteração de dados;
7. adicionar tratamento de erros;
8. gerar relatórios;
9. integrar as partes;
10. executar testes completos.

As operações destrutivas ou com efeitos colaterais devem ficar para depois que as regras estiverem testadas.

## 9. Testar cada parte isoladamente

Cada unidade deve possuir testes próprios.

Exemplo:

### `classificar_arquivo`

* arquivo `.pdf` retorna `PDF`;
* arquivo `.CSV` retorna `CSV`;
* arquivo sem extensão retorna a categoria definida;
* arquivo oculto segue a regra especificada.

### `resolver_nome_duplicado`

* nome livre permanece inalterado;
* primeiro duplicado recebe `_1`;
* segundo duplicado recebe `_2`;
* extensão é preservada;
* arquivo existente não é sobrescrito.

Depois dos testes unitários, devem ser feitos testes de integração entre as partes.

## 10. Definir critérios de conclusão por unidade

Cada parte precisa ter uma condição objetiva de aceite.

Exemplo:

```text
Unidade:
criar_plano_de_movimentacao

Será aprovada quando:

- todos os arquivos elegíveis estiverem presentes no plano;
- nenhum arquivo excluído estiver presente;
- nenhum destino duplicado permanecer sem resolução;
- nenhuma alteração tiver sido executada;
- cada operação possuir origem, destino e justificativa;
- os testes normais, inválidos e de limite forem aprovados.
```

## 11. Entregar uma parte por interação

Ao trabalhar com IA, cada solicitação deve possuir uma unidade principal.

Em vez de:

```text
Crie todo o programa para organizar arquivos.
```

Use uma sequência:

```text
Etapa 1:
Defina os modelos de entrada, saída e relatório.
Não implemente operações de arquivo.
```

```text
Etapa 2:
Implemente somente a validação do caminho.
Inclua testes.
Não liste nem mova arquivos.
```

```text
Etapa 3:
Implemente somente a listagem dos arquivos da pasta raiz.
Não percorra subpastas.
```

```text
Etapa 4:
Implemente a classificação por extensão como função pura.
```

```text
Etapa 5:
Implemente a criação do plano de movimentação.
Não mova arquivos ainda.
```

```text
Etapa 6:
Implemente a execução do plano aprovado.
```

Cada etapa deve ser validada antes da próxima.

## Decomposição completa do exemplo

```text
Sistema de organização de arquivos
│
├── 1. Configuração
│   ├── receber caminho
│   ├── validar caminho
│   └── carregar regras
│
├── 2. Descoberta
│   ├── listar arquivos
│   ├── ignorar subpastas
│   └── identificar arquivos não processáveis
│
├── 3. Classificação
│   ├── extrair extensão
│   ├── normalizar extensão
│   └── determinar pasta de destino
│
├── 4. Planejamento
│   ├── construir destino
│   ├── detectar duplicidade
│   ├── gerar nome alternativo
│   └── criar plano de movimentação
│
├── 5. Execução
│   ├── criar diretórios necessários
│   ├── mover arquivos
│   ├── preservar arquivos existentes
│   └── registrar falhas
│
├── 6. Resultado
│   ├── contar arquivos movidos
│   ├── contar arquivos ignorados
│   ├── contar erros
│   └── gerar relatório
│
└── 7. Testes
    ├── testes unitários
    ├── testes de integração
    ├── casos inválidos
    ├── casos-limite
    └── testes de não sobrescrita
```

## Critério geral de boa decomposição

A decomposição está adequada quando cada parte:

* possui uma responsabilidade principal;
* tem entradas e saídas explícitas;
* pode ser implementada separadamente;
* pode ser testada isoladamente;
* possui dependências conhecidas;
* não exige compreender todo o sistema para ser modificada;
* não altera partes não relacionadas;
* possui critério objetivo de aceite;
* pode falhar sem deixar o sistema em estado inconsistente.

## **4. Defina critérios de aceitação**

Critérios de aceitação descrevem como saber se o código está correto.

Exemplo:  
O código será considerado correto quando:

1. rejeitar arquivos com extensão diferente de CSV;  
2. mostrar uma mensagem clara quando o arquivo estiver vazio;  
3. ignorar linhas duplicadas;  
4. salvar o resultado em UTF*8;  
5. não modificar o arquivo original;  
6. passar nos casos de teste apresentados.

Sem critérios de aceitação, a IA pode produzir algo tecnicamente válido, mas diferente do que você esperava.

## **5. Forneça exemplos de entrada e saída**

Exemplos ajudam muito mais do que descrições genéricas.

Use este formato:

Entrada:

nomes = ["Ana", "Carlos", "ana", "", "Bruno"]

Saída esperada:

["Ana", "Bruno", "Carlos"]

Regras:

* ignorar valores vazios;
* remover duplicados sem diferenciar maiúsculas de minúsculas;
* ordenar alfabeticamente;
* preservar a capitalização da primeira ocorrência.

Inclua também exemplos de erros:

Entrada inválida:

nomes = null

Comportamento esperado:

Lançar ValueError com a mensagem "A lista de nomes é obrigatória".

## **6. Informe o ambiente técnico completo**

Muitos erros de código acontecem porque a IA presume versões, bibliotecas ou sistemas diferentes.

Informe:

* linguagem e versão;  
* sistema operacional;  
* framework;  
* bibliotecas permitidas;  
* versões das dependências;  
* banco de dados;  
* forma de execução;  
* estrutura de pastas;  
* limitações do ambiente.

Exemplo:
Ambiente:

* Python 3.12
* Windows 11
* pandas 2.3
* execução pelo terminal
* sem acesso à internet
* não usar bibliotecas além da biblioteca padrão e pandas

## **7. Defina contratos para funções e módulos**

> Determine claramente o que cada função recebe e retorna.

Exemplo:

```python
def carregar_clientes(caminho: str) *> list[dict]:
    """
    Recebe o caminho de um arquivo JSON.
    Retorna:
        Lista de clientes válidos.
    Erros:
        FileNotFoundError se o arquivo não existir.
        ValueError se o JSON estiver inválido.
    """
```

Peça à IA para não alterar esses contratos sem autorização. Isso reduz incompatibilidades entre partes do script.

## **8. Solicite pseudocódigo antes do código real**

O pseudocódigo permite identificar falhas de lógica sem se distrair com sintaxe.

Exemplo de solicitação:

Antes de programar, escreva o algoritmo em pseudocódigo. Mostre as decisões, validações, repetições e tratamentos de erro. Não escreva código Python ainda.

Depois de aprovar a lógica, peça a conversão para a linguagem desejada.

## **9. Exija testes automatizados junto com o código**

Não aceite apenas a implementação. Solicite também testes.

Peça testes para:

* caso normal;  
* entrada vazia;  
* entrada inválida;  
* valor mínimo;  
* valor máximo;  
* duplicidades;  
* falhas de arquivo;  
* falhas de rede;  
* dados inesperados;  
* exceções.

Exemplo:

Implemente a função e crie testes com pytest. Inclua casos normais, extremos e inválidos. Não considere a tarefa concluída enquanto os testes não cobrirem todos os critérios de aceitação.

Os testes transformam expectativas subjetivas em verificações objetivas.

## **10. Peça uma revisão separada da implementação**

Depois que a IA gerar o código, não pergunte apenas “está correto?”. Peça uma análise orientada.

Use algo como:

Revise este código como um revisor técnico. Não o reescreva ainda. Identifique:

* erros de lógica;  
* variáveis incorretas;  
* casos não tratados;  
* problemas de segurança;  
* incompatibilidades de versão;  
* funções que não atendem aos requisitos;  
* possíveis efeitos colaterais;  
* testes ausentes.

Depois, solicite as correções.

## **11. Faça alterações por diferença, não por reescrita completa**

Quando uma parte já está funcionando, evite pedir:

Reescreva o código com esta nova função.

Prefira:

Altere somente a função processar_arquivo. Não modifique as demais funções, nomes, assinaturas, imports ou comportamento existente. Mostre exatamente quais linhas foram alteradas.

Reescritas completas frequentemente eliminam comportamentos corretos ou introduzem novos erros.

## **12. Mantenha uma fonte única de verdade**

Crie um documento curto contendo:

* objetivo;  
* requisitos;  
* regras;  
* estrutura;  
* contratos;  
* decisões tomadas;  
* itens concluídos;  
* itens pendentes.

Atualize esse documento durante o desenvolvimento e forneça*o novamente quando a conversa ficar longa.

Isso evita que a IA trabalhe com instruções antigas ou contraditórias.

## **13. Controle o contexto da conversa**

Conversas longas podem causar perda de detalhes importantes. Periodicamente, peça:

Resuma o estado atual do projeto, incluindo requisitos aprovados, arquivos existentes, decisões técnicas, erros conhecidos e próxima tarefa. Não inclua ideias descartadas.

Use esse resumo como contexto para a próxima etapa.

Quando possível, envie apenas:

* o arquivo relevante;  
* o erro relevante;  
* os requisitos relacionados;  
* a alteração solicitada.

Contexto demais também pode confundir.

## **14. Não envie apenas a mensagem de erro**

Ao depurar, forneça:

* código completo da função relacionada;  
* mensagem de erro completa;  
* rastreamento da pilha;  
* entrada utilizada;  
* resultado esperado;  
* resultado obtido;  
* ambiente;  
* última alteração realizada.

Exemplo:

Erro:

TypeError: unsupported operand type(s) for +: 'int' and 'str'

Entrada usada:

{"quantidade": "10", "preco": 5.5}

Resultado esperado:

55.0

Resultado obtido:

Exceção

Não altere o formato da entrada. Corrija a validação e explique a causa.

## **15. Peça diagnóstico antes da correção**

Quando o código falhar, use duas etapas:

Primeiro, identifique a causa raiz do erro. Não altere o código.

Depois:

Agora proponha a menor correção possível e explique quais comportamentos podem ser afetados.

Isso impede que a IA aplique mudanças aleatórias sem entender o problema.

## **16. Limite explicitamente o que a IA pode fazer**

Inclua restrições como:

* não adicionar dependências;  
* não alterar nomes de funções;  
* não modificar a interface;  
* não remover validações;  
* não ocultar exceções;  
* não usar dados fictícios;  
* não substituir código funcional;  
* não alterar arquivos não relacionados;  
* não criar funcionalidades não solicitadas.

A IA frequentemente tenta “melhorar” coisas que você não pediu. Essas limitações diminuem esse comportamento.

## **17. Use uma lista de decisões técnicas**

Registre escolhas como:

Decisões fixas:

* usar SQLite;
* datas no formato ISO 8601;
* valores monetários com Decimal;
* nomes de funções em português;
* logs usando o módulo logging;
* não usar variáveis globais;
* erros devem gerar exceções específicas;
* funções devem ter type hints.

Peça para a IA verificar essa lista antes de cada implementação.

## **18. Trabalhe com uma tarefa por solicitação**

Evite pedidos que misturam muitos objetivos:

Corrija os erros, melhore o desempenho, organize o código, crie interface, adicione banco de dados e escreva testes.

Prefira solicitações isoladas:

1. corrigir o erro;  
2. adicionar testes;  
3. refatorar sem alterar comportamento;  
4. melhorar desempenho;  
5. adicionar nova funcionalidade.

Isso facilita descobrir qual alteração introduziu um problema.

## **19. Use controle de versão**

Utilize Git, mesmo em projetos pequenos.

Antes de aceitar uma alteração:

* salve uma versão funcional;  
* crie um commit;  
* aplique a mudança;  
* execute os testes;  
* compare as diferenças;  
* reverta se necessário.

Sugestão de commits:

feat: adiciona validação de entrada

fix: corrige conversão de valores monetários

test: adiciona casos de arquivo vazio

refactor: separa leitura e processamento

A IA pode errar; o controle de versão permite desfazer o erro com segurança.

## **20. Execute ferramentas automáticas de validação**

Dependendo da linguagem, utilize:

* formatadores;  
* linters;  
* verificadores de tipos;  
* testes automatizados;  
* analisadores de segurança;  
* medidores de cobertura.

Para Python, por exemplo:

ruff check .

mypy .

pytest

pytest **cov

A IA pode produzir código com aparência correta, mas essas ferramentas encontram problemas objetivos.

## **21. Use um prompt*base para todas as etapas**

Você pode reutilizar esta estrutura:

Contexto:

[Explique o projeto e o problema.]

Objetivo desta tarefa:

[Uma única tarefa específica.]

Ambiente:

[Linguagem, versão, bibliotecas e sistema.]

Código atual:

[Inclua apenas o código relevante.]

Requisitos obrigatórios:

1. [...]

2. [...]

3. [...]

Restrições:

1. Não alterar [...]

2. Não adicionar [...]

3. Manter compatibilidade com [...]

Entrada de exemplo:

[...]

Saída esperada:

[...]

Casos de erro:

[...]

Critérios de aceitação:

1. [...]

2. [...]

3. [...]

Antes de implementar:

1. Resuma o entendimento.

2. Aponte ambiguidades.

3. Explique a estratégia.

4. Escreva o pseudocódigo.

Na implementação:

1. Faça a menor alteração possível.

2. Use tratamento de erros.

3. Inclua testes.

4. Não invente requisitos.

5. Informe qualquer suposição.

## **Processo recomendado**

O fluxo mais seguro para desenvolver com IA é:

**Especificar → confirmar entendimento → criar pseudocódigo → implementar uma parte → testar → revisar → integrar → registrar decisões.**

Os métodos com maior impacto são: requisitos claros, tarefas pequenas, exemplos de entrada e saída, testes automatizados, contratos de funções, diagnóstico antes da correção, alterações mínimas e controle de versão. Juntos, eles reduzem tanto os erros de entendimento quanto os erros de implementação.  