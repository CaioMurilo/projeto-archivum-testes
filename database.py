import sqlite3

DB_NAME = 'archivum.db'

def get_db_connection():
    # Cria a conexão com o banco de dados em arquivo
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row # Retorna os dados como dicionário
    return conn

def init_db():
    # Cria a tabela caso ela não exista
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT, 
            autor TEXT
        )
    ''')
    conn.commit()
    conn.close()