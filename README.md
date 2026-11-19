# 🛡️ GuardAI: DIO Agent especialista em cibersegurança

> Desafio de Projeto do **Bootcamp Santander Cibersegurança** (DIO). Este repositório parte do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) e o especializa em **análise de vulnerabilidades**, só com arquivos Markdown. Nenhum modelo foi treinado.

## A especialização e por quê

O DIO Agent original é um mentor de estudos. O GuardAI acrescenta a ele o jeito de pensar de um profissional de AppSec. Antes de responder, ele entende o contexto (o que é o sistema, onde está exposto, que dados guarda). Depois aponta a falha com OWASP/CWE e MITRE ATT&CK, avalia o risco e orienta a correção, sem entregar o código pronto de primeira.

Um chat genérico costuma despejar uma lista de comandos de hardening na primeira resposta. Isso inclui regra de firewall e mudanças no SSH, que podem trancar a própria pessoa fora do servidor. O GuardAI pergunta antes de agir.

## Arquivos criados e alterados

| Arquivo | O que é |
|---------|---------|
| [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md) | **Novo.** O roteiro que o agente segue: contexto, falha, exploração, risco, correção, validação, com regras defensivas |
| [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md) | **Novo.** A skill explicada para pessoas |
| [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md) | **Novo.** Vulnerabilidade, ameaça e risco, a tríade CIA, a matriz de risco, OWASP/CWE/ATT&CK e boas práticas |
| [`agent/persona.md`](agent/persona.md) | **Alterado.** Seção "Modo GuardAI (segurança)" |
| [`AGENTS.md`](AGENTS.md) | **Alterado.** Linha da skill na tabela e o arquivo de conhecimento na base |
| [`lab/app.py`](lab/app.py) | **Novo.** Login de laboratório com SQL Injection proposital |
| [`lab/app_corrigido.py`](lab/app_corrigido.py) | **Novo.** O mesmo login com consulta parametrizada e um teste que prova o bloqueio |
| [`evidencias/`](evidencias/) | **Novo.** As respostas reais do agente nos testes abaixo |

## A melhoria escolhida: análise sempre no mesmo formato

Das ideias para evoluir, escolhi **fazer a análise sair sempre no mesmo formato**. Toda análise termina numa tabela de **impacto, probabilidade e severidade**, calculada pela matriz de risco do `security-basics.md`. Assim dá para comparar casos e decidir o que corrigir primeiro. Nos testes, o mesmo SQL Injection saiu como severidade **Média** no app só local, e o agente explicou que viraria **Crítica** se o app fosse para a internet.

## Como rodar

1. Instale um harness compatível com `AGENTS.md`. Usei o **Claude Code**; Hermes, OpenCode, Codex e Antigravity também servem (veja a tabela mais abaixo).
2. Clone e abra **na pasta do projeto**. Aberto em outra pasta, o agente não encontra os arquivos:
   ```bash
   git clone https://github.com/<seu-usuario>/guardai-dio-agent.git
   cd guardai-dio-agent
   claude            # ou: hermes, opencode, codex
   ```
3. Teste o laboratório:
   ```bash
   python3 lab/app.py            # a injeção ' OR '1'='1 entra sem senha
   python3 lab/app_corrigido.py  # ok: injeção bloqueada
   ```
4. Peça: *"Analise o lab/app.py como especialista em AppSec"*.

## Evidências

| Teste | O que o agente fez |
|-------|--------------------|
| [Análise do `app.py`](evidencias/1-analise-app.md) | Achou o SQL Injection na linha 11 (CWE-89, OWASP A03) e explicou o `' OR '1'='1`. Citou T1190 do MITRE ATT&CK, preencheu a tabela de risco e mostrou a consulta parametrizada. Ainda apontou a senha em texto puro como próximo passo, sem resolver por você |
| [Revarredura do `app_corrigido.py`](evidencias/2-revarredura.md) | Confirmou a mitigação, procurou outros pontos de concatenação e rebaixou a severidade. Listou o que resta (CWE-256, CWE-307) |
| [Servidor Ubuntu exposto](evidencias/3-ubuntu.md) | **Não sugeriu nenhum comando que altere o sistema.** Perguntou primeiro que serviços e portas estão abertos e só ofereceu um comando de leitura (`ss -tlnp`) |

Todos os testes usam só código e servidores de laboratório.

---

# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Encontra falhas de segurança, avalia o risco e orienta a correção | "Analisa a segurança do meu app.py?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           O que o agente sabe sobre a DIO
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
