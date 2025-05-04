from flask import Blueprint, jsonify, render_template_string
import random
from .data import pokeneas
from .utils import get_container_id

main = Blueprint('main', __name__)

@main.route('/pokenea/json')
def pokenea_json():
    p = random.choice(pokeneas)
    return jsonify({
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "contenedor": get_container_id()
    })

@main.route('/pokenea/vista')
def pokenea_view():
    p = random.choice(pokeneas)
    html = f"""
    <h1>{p['nombre']}</h1>
    <img src="{p['imagen']}" alt="Imagen de {p['nombre']}" width="300"><br>
    <p><em>{p['frase']}</em></p>
    <p>ID del contenedor: <strong>{get_container_id()}</strong></p>
    """
    return render_template_string(html)
