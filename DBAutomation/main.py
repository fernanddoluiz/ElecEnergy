# Script para conectar no Windows Server + SQL Server 2017

# Conector recomendado na documentação oficial.
import pyodbc


def conectar_mssql_docker(usuario, senha):
    con = pyodbc.connect(
        # Driver que será utilizado na conexão
        'DRIVER={ODBC Driver 17 for SQL Server};'
        # IP ou nome do servidor.
        'SERVER=192.168.100.178\SQLEXPRESS;'
        # Porta
        'PORT=1433;'
        # Banco que será utilizado.
        'DATABASE=PythonMSSQL;'
        # Nome de usuário.
        f'UID={usuario};'
        # Senha.
        f'PWD={senha}')

    # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
    cur = con.cursor()
    return cur


if __name__ == "__main__":
    usuario = str(input('Usuario: '))
    print(usuario)
    senha = str(input('Senha: '))
    print(senha)

    cursor = conectar_mssql_docker(usuario=usuario, senha=senha)
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()

    print(row[0])
