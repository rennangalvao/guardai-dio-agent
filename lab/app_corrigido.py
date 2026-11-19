"""Mesmo login do app.py, corrigido com consulta parametrizada."""
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE usuarios (login TEXT, senha TEXT)")
db.execute("INSERT INTO usuarios VALUES ('admin', 'segredo123')")


def login(usuario, senha):
    # o driver trata usuario e senha como dados, nunca como SQL
    sql = "SELECT * FROM usuarios WHERE login = ? AND senha = ?"
    return db.execute(sql, (usuario, senha)).fetchone() is not None


if __name__ == "__main__":
    assert login("admin", "segredo123")
    assert not login("admin", "x")
    assert not login("admin", "' OR '1'='1"), "injeção ainda funciona"
    print("ok: injeção bloqueada")
