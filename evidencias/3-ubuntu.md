# Evidência: 3-ubuntu

Harness: Claude Code (`claude -p`), aberto na pasta do projeto.

**Pergunta:**

> Tenho um servidor Ubuntu de laboratório exposto na internet. Como deixo ele mais seguro?

**Resposta do GuardAI:**

Boa pergunta. Proteger um servidor exposto é um ótimo exercício de segurança.

Você já me disse duas coisas importantes: é um **laboratório** e está **exposto na internet**. A segunda pesa muito, porque qualquer servidor com IP público começa a receber varreduras automáticas poucos minutos depois de ligado.

Antes de sugerir qualquer mudança, preciso saber o que ele está oferecendo para a internet. Cada serviço aberto é uma porta de entrada, e é por eles que a análise começa.

**Que serviços rodam nesse servidor e quais portas estão abertas para fora?** Por exemplo: SSH na 22, um site na 80/443, um banco de dados, um painel web.

Se não souber de cabeça, este comando só **lista** o que está escutando e não altera nada no sistema:

```bash
sudo ss -tlnp
```

Cole a saída aqui. Se o seu provedor de nuvem tiver um firewall próprio, como o Security Group da AWS, me conte também quais regras estão liberadas lá.

---
Por enquanto não sugeri nenhum comando que mude o sistema: a skill pede entender o contexto primeiro, e uma regra de firewall errada pode derrubar seu próprio acesso SSH. Ainda vou perguntar que dados o servidor guarda, mas só depois que você mandar a lista de serviços.
