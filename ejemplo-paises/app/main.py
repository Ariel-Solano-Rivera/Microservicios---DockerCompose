from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psycopg2
import random

app = FastAPI()

DB_CONFIG = {
    "host": "db",              # nombre del servicio en docker-compose
    "database": "paisesdb",
    "user": "postgres",
    "password": "postgres",
}

# Lista base de países de donde elegimos aleatoriamente
PAISES_BASE = [
    {"pais": "Ecuador", "capital": "Quito", "habitantes": 17643060},
    {"pais": "Perú", "capital": "Lima", "habitantes": 33050325},
    {"pais": "Colombia", "capital": "Bogotá", "habitantes": 50882884},
    {"pais": "Chile", "capital": "Santiago", "habitantes": 19107216},
    {"pais": "Argentina", "capital": "Buenos Aires", "habitantes": 45195777},
    {"pais": "México", "capital": "Ciudad de México", "habitantes": 128932753},
    {"pais": "España", "capital": "Madrid", "habitantes": 47351567},
]

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

# ---------- 1) Endpoint JSON: ver todo lo de la BD ----------
@app.get("/datos")
def datos_json():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT pais, capital, habitantes FROM paises ORDER BY id;")
    filas = cur.fetchall()
    cur.close()
    conn.close()

    return {
        "paises": [
            {"pais": f[0], "capital": f[1], "habitantes": f[2]} for f in filas
        ]
    }

# ---------- 2) Endpoint HTML: agregar aleatorio y mostrar bonito ----------
@app.get("/", response_class=HTMLResponse)
def pagina_html():
    # Elegimos un país aleatorio y lo insertamos
    pais_random = random.choice(PAISES_BASE)

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO paises (pais, capital, habitantes) VALUES (%s, %s, %s)",
        (pais_random["pais"], pais_random["capital"], pais_random["habitantes"]),
    )
    conn.commit()

    # Recuperamos todos los registros para mostrarlos
    cur.execute("SELECT id, pais, capital, habitantes FROM paises ORDER BY id;")
    filas = cur.fetchall()
    cur.close()
    conn.close()

    # Construimos un HTML sencillo y bonito
    html = """
    <html>
      <head>
        <title>Países registrados</title>
        <meta charset="utf-8">
        <style>
          body { font-family: Arial, sans-serif; padding: 20px; }
          h1 { color: #2c3e50; }
          table { border-collapse: collapse; width: 100%; margin-top: 15px;}
          th, td { border: 1px solid #ccc; padding: 8px; text-align: left;}
          th { background-color: #f2f2f2; }
          tr:nth-child(even) { background-color: #fafafa; }
          .nota { margin-top: 10px; font-size: 0.9rem; color: #555; }
        </style>
      </head>
      <body>
        <h1>Lista de países</h1>
        <p class="nota">
          Cada vez que recargas esta página (<code>/</code>) se agrega un país aleatorio
          a la base de datos (puede repetirse).
        </p>
        <table>
          <tr>
            <th>#</th>
            <th>País</th>
            <th>Capital</th>
            <th>Habitantes</th>
          </tr>
    """

    for i, fila in enumerate(filas, start=1):
        id_, pais, capital, hab = fila
        html += f"""
          <tr>
            <td>{i}</td>
            <td>{pais}</td>
            <td>{capital}</td>
            <td>{hab:,}</td>
          </tr>
        """

    html += """
        </table>
      </body>
    </html>
    """

    return HTMLResponse(content=html)
