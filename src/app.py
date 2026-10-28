
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def conectar_bd():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "app123"),
        database=os.getenv("DB_NAME", "holamundo")
    )

@app.route("/")
def inicio():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT 'MySQL conectado correctamente!'")
        resultado = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return f"""
        <h1>¡Hola Mundo!</h1>
        <p>Aplicación web funcionando con Docker.</p>
        <p>Base de datos: {resultado}</p>
        """
    except Exception as error:
        return f"Error conectando a MySQL: {error}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
