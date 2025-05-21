from flask import Flask, jsonify
import json

app = Flask(__name__)

# Cargar productos desde el archivo JSON
with open("productos.json", encoding="utf-8") as f:
    productos = json.load(f)

# Ruta raíz (opcional)
@app.route("/")
def home():
    return "<h1>FERREMAS API</h1><p>Consulta /api/productos</p>"

# Ruta de la API
@app.route("/api/productos", methods=["GET"])
def get_productos():
    return jsonify(productos)

if __name__ == "__main__":
    app.run(debug=True)
