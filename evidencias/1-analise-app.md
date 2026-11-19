# Evidência: 1-analise-app

Harness: Claude Code (`claude -p`), aberto na pasta do projeto.

**Pergunta:**

> Atue como especialista em AppSec. Analise o arquivo lab/app.py: encontre a falha, explique como ela seria explorada, cite a técnica do MITRE ATT&CK e reescreva o código corrigido. É um app de laboratório meu, roda só na minha máquina, para estudo.

**Resposta do GuardAI:**

A falha é **SQL Injection**, e você mesmo já tem a correção pronta e funcionando. Rodei as duas versões aqui:

```
app.py            → injeção ' OR '1'='1: True    (entrou sem senha)
app_corrigido.py  → ok: injeção bloqueada        (os 3 asserts passaram)
```

## 1. A falha

- **Nome:** SQL Injection, CWE-89. No OWASP Top 10 entra em **A03: Injection**.
- **Onde:** `lab/app.py:11`
  ```python
  sql = f"SELECT * FROM usuarios WHERE login = '{usuario}' AND senha = '{senha}'"
  ```
- **Causa:** a f-string cola o que a pessoa digitou direto no texto do SQL. Assim o banco não consegue distinguir o que é comando do que é dado.

## 2. Como seria explorada

Quando alguém digita `' OR '1'='1` no campo de senha, a consulta fica assim:

```sql
WHERE login = 'admin' AND senha = '' OR '1'='1'
```

O `AND` é avaliado antes do `OR`, então o banco lê `(login='admin' AND senha='') OR verdadeiro`. A condição é verdadeira para qualquer linha, e o login passa sem a senha.

Há outras formas de abusar do mesmo buraco:
- **Pelo campo usuário:** um comentário SQL logo depois do nome do admin faz o banco ignorar a checagem de senha.
- **Indo além do login:** com `UNION SELECT` dá para ler outras tabelas do banco, e em alguns bancos também alterar ou apagar dados.

**MITRE ATT&CK:** **T1190, Exploit Public-Facing Application**. É a técnica que corresponde a SQLi em uma aplicação exposta. Na sua máquina ela só valeria se o app ficasse acessível pela rede. O que o atacante consegue depois disso (entrar como admin) se aproxima de **T1078, Valid Accounts**.

## 3. Risco (para o seu cenário: laboratório, só local)

| Critério | Avaliação | Por quê |
|----------|-----------|---------|
| Impacto | Alto | Contorna a autenticação e permite ler o banco inteiro, afetando confidencialidade e integridade |
| Probabilidade | Baixa | Roda só na sua máquina, sem exposição na rede |
| Severidade | **Média** | Impacto Alto × probabilidade Baixa, pela matriz em `security-basics.md` |

Se o mesmo código fosse publicado na internet, a probabilidade passaria a **Alta** e a severidade a **Crítica**.

## 4. Código corrigido

Você pediu a reescrita, e ela já está em `lab/app_corrigido.py`. Não precisei mudar nada:

```python
def login(usuario, senha):
    # o driver trata usuario e senha como dados, nunca como SQL
    sql = "SELECT * FROM usuarios WHERE login = ? AND senha = ?"
    return db.execute(sql, (usuario, senha)).fetchone() is not None
```

**Por que funciona:** com a **consulta parametrizada**, o SQL e os valores vão separados para o driver. A estrutura do comando já está pronta antes de qualquer valor entrar, então `' OR '1'='1` vira só uma senha esquisita que não bate com nenhuma linha. Escapar aspas na mão ou usar lista de caracteres proibidos não resolve, porque sempre aparece um jeito de contornar.

## 5. O que ainda falta corrigir (sua vez)

A injeção foi mitigada, mas uma revarredura mostra outra falha na mesma tabela: **a senha é guardada e comparada em texto puro** (CWE-256). Se alguém conseguir ler o banco, por backup vazado ou por uma injeção em outro lugar, fica com todas as senhas na hora.

Dica: o certo é guardar um *hash* lento com *salt* e comparar o hash, nunca a senha em si. A biblioteca padrão do Python tem uma função feita para isso no módulo `hashlib`. Tenta aplicar no `app_corrigido.py` e me traz o código, que eu faço a nova varredura.

Para aprofundar, procure na DIO as **Formações e Desafios de Projeto da área de Cibersegurança**; o catálogo muda, então vale filtrar por "segurança" na plataforma.
