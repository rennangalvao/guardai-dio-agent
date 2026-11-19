# Evidência: 2-revarredura

Harness: Claude Code (`claude -p`), aberto na pasta do projeto.

**Pergunta:**

> Apliquei a correção em lab/app_corrigido.py. Faça uma nova varredura e confirme se o SQL Injection foi mitigado. É o mesmo app de laboratório, só local.

**Resposta do GuardAI:**

# Revarredura de `lab/app_corrigido.py`: o SQL Injection foi mitigado ✅

Rodei os dois arquivos lado a lado:

```
app.py           → injeção ' OR '1'='1: True    (entra sem senha)
app_corrigido.py → ok: injeção bloqueada         (os 3 asserts passaram)
```

## O que mudou e por que funciona

Em `lab/app_corrigido.py:11-12`, a consulta usa `?` como marcador e manda `usuario` e `senha` separados, como uma tupla. Antes, o texto digitado era colado dentro do SQL com f-string. Agora o banco recebe a estrutura da consulta e os valores por canais diferentes. Assim, um `' OR '1'='1` vira só uma senha esquisita que não bate com nenhuma linha.

Procurei outros pontos onde texto de fora vira SQL (f-string, `%`, `.format`, `+`). Só sobraram os `execute` das linhas 5 e 6, que criam a tabela com valores fixos e não recebem nada do usuário. Esses estão seguros.

## Risco depois da correção

| Critério | Avaliação | Por quê |
|----------|-----------|---------|
| Impacto | Baixo | Para o SQL Injection (CWE-89), o caminho para burlar o login ou ler a tabela foi fechado |
| Probabilidade | Baixa | A entrada não chega mais ao SQL como código, e o app roda só local |
| Severidade | Baixa | A falha original (Crítica) está mitigada |

## O que ainda resta (fora do SQL Injection)

Nada disso reabre a injeção. São os próximos degraus se você quiser levar o lab adiante:

1. **Senha em texto puro** (CWE-256): `'segredo123'` fica gravada do jeito que foi digitada. Se alguém copiar o banco, leva todas as senhas. O princípio da correção é guardar só um hash lento com salt (bcrypt, scrypt ou argon2) e comparar hashes no login.
2. **Sem limite de tentativas** (CWE-307): nada impede alguém de testar milhares de senhas seguidas. Num app só local isso pesa pouco, mas vira problema se ele for exposto na rede.

Bom trabalho: você trocou a montagem da string pela consulta parametrizada, que é a correção certa, e ainda deixou um teste que prova o bloqueio. 👏

Para continuar, vale procurar na DIO um Curso ou Desafio de Projeto de segurança em aplicações web. Na trilha de cibersegurança, armazenamento de senhas costuma ser o tema que vem logo depois de SQL Injection.

Pergunta para você: como você faria para o banco nunca guardar a senha original e o login continuar funcionando?
