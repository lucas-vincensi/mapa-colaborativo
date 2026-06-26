import os
import psycopg2
from dotenv import load_dotenv
import bcrypt
load_dotenv()


def get_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def listar_marcacoes(tipo):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               tipo,
               rua,
               descricao,
               latitude,
               longitude
        FROM marcacoes
        WHERE tipo = %s
        ORDER BY id
    """, (tipo,))

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    resultado = []

    for linha in dados:

        resultado.append({

            "id": linha[0],
            "tipo": linha[1],
            "rua": linha[2],
            "descricao": linha[3],
            "lat": linha[4],
            "lon": linha[5]

        })

    return resultado


def adicionar_marcacao(tipo, rua, descricao, lat, lon):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO marcacoes
        (tipo, rua, descricao, latitude, longitude)

        VALUES (%s,%s,%s,%s,%s)

    """, (tipo, rua, descricao, lat, lon))

    conn.commit()

    cursor.close()
    conn.close()

def remover_marcacao(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM marcacoes
        WHERE id = %s
    """, (id,))

    conn.commit()

    cursor.close()
    conn.close()


import bcrypt

def autenticar(usuario, senha):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT senha
        FROM usuarios
        WHERE usuario = %s
    """, (usuario,))

    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if not resultado:
        return False

    hash_salvo = resultado[0].encode()

    return bcrypt.checkpw(
        senha.encode(),
        hash_salvo
    )