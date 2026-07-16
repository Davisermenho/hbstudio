# Proposta de criação do `ENGINEERING_CONTEXT.md`

## Resumo executivo

* Documento: proposta de consolidação técnica.
* `CONTEXT.md`: identidade, autoridade e rotas documentais.
* `FERRAMENTAS_TECNICAS`: página existente e especializada em vídeo.
* `AGENT_POLICY.md`: políticas, capacidade operacional e validação.
* Lacuna: inventário técnico geral, factual e verificável.
* Decisão pendente: aprovar nome, escopo e criação da nova página.

Antes de criar um novo documento, há uma correção importante: já existe no `Notion` a página `FERRAMENTAS_TECNICAS`, vinculada ao `CONTEXT.md`. Ela registra o ambiente `WSL2/Linux`, o `.venv`, dependências `Python` e ferramentas de edição de vídeo. Porém, seu escopo é restrito à edição de vídeo e não cobre de forma suficiente computador, agentes, `VS Code`, repositórios, infraestrutura e fluxos de desenvolvimento.

A solução recomendada é criar um documento canônico mais amplo, mantendo `FERRAMENTAS_TECNICAS` como documento especializado.

## Documento proposto

`ENGINEERING_CONTEXT.md`

**Função:**

> Ponto de entrada canônico para ambiente computacional,agentes de IA, ferramentas, repositórios, convenções,capacidades e restrições de desenvolvimento.

**Ele não deve substituir:**

* `CONTEXT.md`, responsável por identidade, autoridade, contexto esportivo e
  rotas documentais;
* `AGENT_POLICY.md`, responsável por políticas, capacidade operacional,
  execução, verificação, aceitação e conclusão;
* `ENGINEERING_CONTEXT.md`, proposto para inventário factual, rotas técnicas,
  versões, caminhos, repositórios e evidências do ambiente, sem duplicar
  políticas;
* `FERRAMENTAS_TECNICAS`, especializada em scripts e ferramentas de vídeo;
* documentação interna de cada repositório, responsável pelos detalhes de
  implementação do respectivo projeto.

## Ações necessárias

### 1. Definir formalmente o escopo

Registrar o que pertence ao documento:

características do computador;
Windows e WSL;
ambiente de desenvolvimento;
VS Code;
agentes utilizados;
ferramentas instaladas;
repositórios;
diretórios;
restrições;
regras de uso dos agentes;
procedimentos de verificação do ambiente.

Registrar também o que não pertence:

resultados esportivos;
logística da competição;
saúde ou dados pessoais de atletas;
implementação detalhada de um único projeto;
senhas, tokens ou credenciais;
conteúdo completo de arquivos de configuração;
estado dinâmico de uma competição.

### 2. Decidir a relação com FERRAMENTAS_TECNICAS

A recomendação é:

ENGINEERING_CONTEXT.md
└── contexto técnico geral e rotas

FERRAMENTAS_TECNICAS
└── scripts e ferramentas específicas de vídeo

O novo documento deve apontar para FERRAMENTAS_TECNICAS, sem duplicar integralmente seu conteúdo.

Também convém renomear a página atual para:

FERRAMENTAS_TECNICAS.md

Isso mantém consistência com os demais documentos canônicos, mas a renomeação deve ser uma decisão separada e explícita.

### 3. Criar um inventário factual do computador

Os dados não devem ser preenchidos por memória. Devem ser coletados por comandos verificáveis.

Informações mínimas:

fabricante e modelo;
processador;
arquitetura;
quantidade de RAM;
GPU;
discos e espaço disponível;
versão do Windows;
versão do WSL;
distribuição Linux;
kernel;
nome do usuário de desenvolvimento;
diretórios principais;
suporte gráfico do WSL;
disponibilidade de virtualização.

Comandos sugeridos no Windows:

Get-ComputerInfo
systeminfo
Get-CimInstance Win32_Processor
Get-CimInstance Win32_PhysicalMemory
Get-CimInstance Win32_VideoController
Get-PhysicalDisk
wsl --version
wsl --status
wsl --list --verbose

No WSL:

uname -a
cat /etc/os-release
lscpu
free -h
lsblk
df -h
nvidia-smi

Cada informação deve registrar:

valor
fonte/comando
data da coleta
status de verificação

### 4. Inventariar o ambiente de desenvolvimento

Devem ser identificadas versões e disponibilidade de:

Git
Python
uv
pip
Node.js
npm
SQLite
FFmpeg
ffprobe
mpv
Docker
PyInstaller
Java
GitHub CLI

Comandos:

git --version
python3 --version
uv --version
pip --version
node --version
npm --version
sqlite3 --version
ffmpeg -version
ffprobe -version
mpv --version
docker --version
pyinstaller --version
gh --version

A ausência também deve ser registrada, por exemplo:

mpv:
  status: ausente
  verificado_por: "command -v mpv"
  impacto: "bloqueia integração real do player"

### 5. Inventariar o VS Code

Registrar:

versão do VS Code;
uso pelo Windows ou WSL;
extensões instaladas;
extensões obrigatórias;
extensões opcionais;
extensões obsoletas ou conflitantes;
configuração de terminal;
interpretador Python;
integração Git;
integração com agentes.

Comandos:

code --version
code --list-extensions --show-versions

A lista deve distinguir:

instalada
obrigatória
recomendada
não validada

### 6. Inventariar os agentes utilizados

Para cada agente, registrar:

Campo
Conteúdo
Nome
ChatGPT Web, Codex, Claude Code, Gemini
Interface
navegador, VS Code, terminal
Função principal
análise, edição, código, pesquisa
Acesso a arquivos
sim, não ou condicionado
Acesso ao terminal
sim ou não
Capacidade de escrita
escopo real
Capacidade de validação
o que consegue reler
Limitações
permissões, contexto, conectores
Uso autorizado
tarefas permitidas
Evidência exigida
testes, diff, relatório
Dados proibidos
segredos e dados sensíveis


Também deve ser definida a precedência operacional. Exemplo:

Davi autoriza
→ agente executa no escopo
→ ferramenta produz evidência
→ outro agente ou Davi valida
→ somente então a ação é aceita

### 7. Inventariar repositórios e projetos

O documento não deve conter todo o código. Deve registrar rotas.

Campos mínimos:

nome do projeto
repositório
diretório local
branch principal
linguagem
ambiente
arquivo de entrada
documentação canônica
comando de instalação
comando de testes
estado

Projetos inicialmente relevantes:

IDEC Scout Maker;
HbTrack;
CEPRAEA;
repositório KB;
scripts de edição de vídeo.

Exemplo:

projeto:
  nome: "IDEC Scout Maker"
  diretorio_local: "/home/davis/IDEC_Scout_Markerv.0.1"
  repositorio_remoto: pendente
  ambiente: "WSL2"
  gerenciador: "uv"
  status: "v0.1.1 parcial"

### 8. Definir os diretórios canônicos

Devem ser documentados, após verificação:

diretório dos repositórios
diretório de vídeos
diretório de scouts
diretório de clipes
diretório de backups
diretório de credenciais
diretório de exportações

Não devem ser armazenados:

tokens;
senhas;
chaves privadas;
conteúdos de credenciais;
dados médicos;
documentos dos atletas.

Para credenciais, registrar apenas a política:

local protegido
fora do repositório
fora do Notion
fora dos logs

### 9. Criar uma taxonomia de status

Cada ferramenta deve usar estados controlados:

CONFIRMADO
INSTALADO — NÃO VALIDADO
AUSENTE
PENDENTE DE VERIFICAÇÃO
BLOQUEADO
DEPRECADO
NÃO APLICÁVEL

Isso impede que uma ferramenta apenas mencionada seja tratada como instalada ou funcional.

### 10. Definir fonte e autoridade de cada informação

Sugestão de hierarquia técnica:

* saída atual de comando;
* arquivo de configuração do repositório;
* lockfile;
* documentação oficial da ferramenta;
* configuração do VS Code;
* documentação interna atualizada;
* relato de Davi;
* inferência da IA.

Exemplo:

```md
python:
  versao: "3.x"
  fonte: "python3 --version"
  verificado_em: "AAAA-MM-DD"
```

### 11. Definir a estrutura do documento

Estrutura recomendada:

```md
# ENGINEERING_CONTEXT.md

## ENG-ID-001 — Identidade do ambiente
## ENG-HW-001 — Hardware
## ENG-OS-001 — Sistemas operacionais
## ENG-WSL-001 — WSL
## ENG-DEV-001 — Ferramentas de desenvolvimento
## ENG-VSC-001 — VS Code e extensões
## ENG-AGT-001 — Agentes de IA
## ENG-REP-001 — Repositórios e projetos
## ENG-PTH-001 — Diretórios canônicos
## ENG-SEC-001 — Credenciais e segurança
## ENG-CAP-001 — Matriz de capacidades
## ENG-VAL-001 — Verificação do ambiente
## ENG-ROU-001 — Rotas documentais
## ENG-CHG-001 — Histórico de alterações
```

### 12. Criar um bloco YAML canônico

Assim como o estado operacional, o ambiente técnico pode ter uma representação estruturada.

Exemplo:

```yaml
engineering_context:
  schema_version: "1.0.0"
  atualizado_em: "AAAA-MM-DDTHH:MM:SS-03:00"

  computador:
    modelo: pendente
    arquitetura: pendente
    ram_gb: pendente
    gpu: pendente

  sistemas:
    windows:
      versao: pendente
    wsl:
      versao: pendente
      distribuicao: pendente

  desenvolvimento:
    vscode:
      versao: pendente
    python:
      versao: pendente
    uv:
      versao: pendente
    git:
      versao: pendente
    ffmpeg:
      status: pendente
    mpv:
      status: ausente

  agentes:
    chatgpt_web:
      status: confirmado
    codex:
      status: pendente_de_verificacao
    claude_code:
      status: pendente_de_verificacao
    gemini_web:
      status: confirmado
```

Esse bloco não deve ser chamado STA-CUR-001, pois esse identificador pertence ao estado esportivo.

### 13. Criar um schema de validação

Para evitar campos livres e inconsistências, convém criar:

schemas/engineering-context.schema.json

O schema deve validar:

versão;
timestamp;
status permitidos;
ferramentas;
agentes;
caminhos;
fontes de evidência;
ausência de segredos;
obrigatoriedade de data de verificação.

### 14. Validar dados sensíveis

Antes de publicar no Notion, deve haver uma revisão específica para impedir:

endereços pessoais desnecessários;
número de série do computador;
IP público;
tokens;
chaves SSH;
credenciais OAuth;
conteúdo de .env;
documentos ou contatos de atletas;
senhas de Wi-Fi.

O documento deve conter contexto operacional suficiente, não um inventário de segurança explorável.

### 15. Integrar o documento ao CONTEXT.md

Após a criação, o CONTEXT.md precisa receber uma rota explícita:

DOC-ENG-001 — ENGINEERING_CONTEXT.md

Finalidade:

Ambiente computacional, agentes, ferramentas,
repositórios e capacidades técnicas.

O CONTEXT.md já contém uma referência à página FERRAMENTAS_TECNICAS, mas ela não está registrada na tabela de documentos especializados. Essa inconsistência deve ser corrigida durante a integração.

### 16. Atualizar `AGENT_POLICY.md`

Deve ser adicionada uma regra semelhante a:

Antes de responder sobre desenvolvimento, software, agentes,
VS Code, repositórios, terminal ou infraestrutura,
consultar ENGINEERING_CONTEXT.md.

Também deve determinar:

não presumir ferramenta instalada;
não presumir acesso ao terminal;
não inventar caminhos;
verificar versões antes de recomendar comandos sensíveis;
distinguir Windows, PowerShell, WSL e Linux;
registrar bloqueios de permissão.

### 17. Definir manutenção

Responsável recomendado:

Davi aprova alterações factuais.
A IA pode preparar e validar atualizações.

Eventos que exigem atualização:

troca de computador;
atualização de Windows ou WSL;
instalação ou remoção de ferramenta;
mudança de versão relevante;
novo agente;
novo repositório;
alteração de diretório;
mudança no fluxo de trabalho;
alteração de permissões.

Periodicidade mínima:

revisão após mudança técnica relevante
ou auditoria mensal quando houver desenvolvimento ativo

### 18. Executar validação final

Critérios de aceitação:

[ ] Página criada com Page ID único
[ ] Rota inserida no CONTEXT.md
[ ] Regra de consulta inserida no AGENT_POLICY.md
[ ] FERRAMENTAS_TECNICAS vinculada sem duplicação
[ ] Hardware coletado por comando
[ ] Sistemas coletados por comando
[ ] Ferramentas verificadas por comando
[ ] Extensões do VS Code inventariadas
[ ] Agentes classificados por capacidade
[ ] Repositórios e diretórios confirmados
[ ] Nenhuma credencial ou dado sensível exposto
[ ] YAML válido
[ ] Schema aprovado
[ ] Evidências e datas registradas
[ ] Davi aprovou o conteúdo

## Ordem recomendada de execução

1. Auditar FERRAMENTAS_TECNICAS existente
2. Aprovar nome e escopo do novo documento
3. Coletar hardware e sistemas
4. Coletar ferramentas e versões
5. Inventariar VS Code e extensões
6. Inventariar agentes e capacidades
7. Inventariar repositórios e diretórios
8. Redigir ENGINEERING_CONTEXT.md
9. Criar YAML e JSON Schema
10. Revisar segurança e privacidade
11. Criar a página no Notion
12. Atualizar CONTEXT.md
13. Atualizar AGENT_POLICY.md
14. Validar os links e Page IDs
15. Aprovação final de Davi

## Estado atual

documento_proposto: "ENGINEERING_CONTEXT.md"
pagina_existente_relacionada: "FERRAMENTAS_TECNICAS"
criacao_autorizada: false
arquivos_alterados: false
proxima_acao: "coletar e validar o inventário técnico antes da criação"
