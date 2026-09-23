# Importa o SQLite
import sqlite3


# Nome do arquivo do banco de dados
DATABASE = "database.db"


# Abre o arquivo SQL com os comandos para criar o banco
with open("database.sql", "r", encoding="utf-8") as arquivo:
    script_sql = arquivo.read()


# Cria a conexão com o banco de dados
with sqlite3.connect(DATABASE) as conn:

    # Executa todos os comandos existentes em database.sql
    conn.executescript(script_sql)

    # Confirma as alterações
    conn.commit()


print("Banco de dados criado com sucesso!")