import os  # Para acceder a variables de entorno
from flask import Flask, request, jsonify
from flask_cors import CORS  # Para permitir solicitudes desde diferentes orígenes

app = Flask(__name__)
CORS(app)  # Habilita CORS

# Almacenar el estado de las acciones
current_action = {"action": None}

@app.route('/data', methods=['GET', 'POST'])
def data():
    global current_action
    if request.method == 'POST':
        # Guardar la acción enviada por el administrador
        data = request.json
        current_action['action'] = data['value']
        return jsonify({"message": "Action received!"}), 201
    else:
        # Devolver la acción actual
        return jsonify(current_action)

if __name__ == '__main__':
    # Usa el puerto 51051 si no está configurada la variable de entorno PORT
    port = int(os.environ.get('PORT', 51051))
    app.run(host='0.0.0.0', port=port)
