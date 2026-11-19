# Fundamentos de segurança

Referência do GuardAI para analisar falhas. Use estes termos do mesmo jeito em todas as respostas.

## Vulnerabilidade, ameaça e risco

- **Vulnerabilidade:** uma fraqueza no sistema. Ex.: um login que junta o texto digitado na consulta SQL.
- **Ameaça:** quem ou o que pode explorar a fraqueza. Ex.: um atacante na internet.
- **Risco:** a chance de a ameaça explorar a vulnerabilidade, vezes o estrago que isso causa. Sem ameaça ou sem vulnerabilidade, não há risco.

## Tríade CIA

- **Confidencialidade:** só quem deve vê a informação. Vazamento de senhas quebra a confidencialidade.
- **Integridade:** a informação não é alterada sem autorização. Um `UPDATE` injetado quebra a integridade.
- **Disponibilidade:** o sistema funciona quando é preciso. Um `DROP TABLE` ou um ataque de negação de serviço quebra a disponibilidade.

## Matriz de risco

| Probabilidade \ Impacto | Baixo | Médio | Alto | Crítico |
|---|---|---|---|---|
| **Alta** | Média | Alta | Crítica | Crítica |
| **Média** | Baixa | Média | Alta | Crítica |
| **Baixa** | Baixa | Baixa | Média | Alta |

- **Impacto** cresce com o quanto da tríade CIA é afetado e com a sensibilidade dos dados.
- **Probabilidade** cresce com a exposição (internet > rede interna > local) e com a facilidade de explorar (sem login, ferramenta pública).

## Referências que o GuardAI cita

- **OWASP Top 10:** as dez categorias de falha mais comuns em aplicações web. Ex.: A03 Injection.
- **CWE:** catálogo de tipos de fraqueza. Ex.: CWE-89, SQL Injection.
- **MITRE ATT&CK:** catálogo de técnicas de ataque. Ex.: T1190, Exploit Public-Facing Application; T1110, Brute Force.

## Boas práticas

- **Validar a entrada** e usar consultas parametrizadas, nunca concatenar texto do usuário em SQL ou comandos.
- **Menor privilégio:** cada usuário e serviço só com o acesso de que precisa.
- **Defesa em profundidade:** várias camadas (firewall, autenticação, logs), porque uma sozinha falha.
- **Senhas com hash forte** (bcrypt, argon2), nunca em texto puro.
- **Atualizar** sistema e dependências, e expor só as portas necessárias.
- **Registrar e monitorar** acessos, para perceber o ataque cedo.
