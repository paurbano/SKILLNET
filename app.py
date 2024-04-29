from flask import Flask, jsonify, request
import controlador
from db import create_tables

app = Flask(__name__)


@app.route('/pacientes', methods=["GET"])
def get_pacientes():
    pacientes = controlador.get_pacientes()
    return jsonify(pacientes)

@app.route('/paciente/<id>', methods=["GET"])
def get_paciente_id(id):
    paciente = controlador.get_paciente_by_id(id)
    return jsonify(paciente)

@app.route("/paciente", methods=["POST"])
def insert_paciente():
    datos_paciente = request.get_json()
    tipoId = datos_paciente["tipoId"]
    numid = datos_paciente["numid"]
    nombre = datos_paciente["nombre"]
    telefono = datos_paciente["telefono"]
    result = controlador.insert_paciente(tipoId, numid, nombre, telefono)
    return jsonify(result)

@app.route("/paciente/<id>", methods=["PUT"])
def update_paciente(id):
    datos_paciente = request.get_json()
    tipoId = datos_paciente["tipoId"]
    numid = datos_paciente["numid"]
    nombre = datos_paciente["nombre"]
    telefono = datos_paciente["telefono"]
    result = controlador.update_paciente(tipoId, numid, nombre, telefono, id)
    return jsonify(result)

@app.route('/doctores', methods=["GET"])
def get_doctores():
    doctores = controlador.get_doctores()
    return jsonify(doctores)


@app.route("/doctor", methods=["POST"])
def insert_doctor():
    doctor = request.get_json()
    nombre = doctor["nombre"]
    especialidad = doctor["especialidad"]
    result = controlador.insert_doctor(nombre, especialidad)
    return jsonify(result)

@app.route('/doctores/citas', methods=["GET"])
def get_citas_doctores():
    pacientes = controlador.get_citas_doctores()
    return jsonify(pacientes)

@app.route("/cita", methods=["POST"])
def insert_cita():
    cita = request.get_json()
    paciente_id = cita["paciente_id"]
    doctor_id = cita["doctor_id"]
    fecha = cita["fecha"]
    result = controlador.insert_cita(paciente_id, doctor_id, fecha)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    
    app.run(host='0.0.0.0', port=8000, debug=False)