"""App de LABORATÓRIO com SQL Injection proposital. Não use em produção."""
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE usuarios (login TEXT, senha TEXT)")
db.execute("INSERT INTO usuarios VALUES ('admin', 'segredo123')")


def login(usuario, senha):
    # VULNERÁVEL: o texto digitado entra direto na consulta
    sql = f"SELECT * FROM usuarios WHERE login = '{usuario}' AND senha = '{senha}'"
    return db.execute(sql).fetchone() is not None


if __name__ == "__main__":
    print("senha certa:", login("admin", "segredo123"))
    print("senha errada:", login("admin", "x"))
    print("injeção ' OR '1'='1:", login("admin", "' OR '1'='1"))
