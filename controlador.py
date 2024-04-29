from db import get_db


def get_pacientes():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, tipoId,numid, nombre, telefono FROM pacientes"
    cursor.execute(query)
    return cursor.fetchall()

def get_paciente_by_id(Id):
    db = get_db()
    cursor = db.cursor()
    stament = "SELECT id, tipoId,nombre, telefono FROM pacientes where id= ?"
    cursor.execute(stament, [Id])
    return cursor.fetchall()

def insert_paciente(tipoId, numid,  nombre, telefono):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO pacientes(tipoId,numid, nombre, telefono) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [tipoId,numid, nombre, telefono])
    db.commit()
    return True

def update_paciente(tipoid, numid, nombre, telefono, id):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE pacientes set tipoid=?, numid=?, nombre=?, telefono= ? WHERE id = ? "
    cursor.execute(statement, [tipoid, numid, nombre, telefono, id])
    db.commit()
    return True

def get_doctores():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, nombre, especialidad FROM doctores"
    cursor.execute(query)
    return cursor.fetchall()

def get_citas_doctores():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT d.nombredoctor as Doctor, d.especialidad, p.nombre, c.fecha \
            FROM doctores d \
            inner join citas c on c.doctor_id= d.id \
            inner join pacientes p ON p.id = c.paciente_id\
            "
    cursor.execute(query)
    return cursor.fetchall()

def insert_doctor(nombre, especialidad):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO doctores(nombreDoctor, especialidad) VALUES (?, ?)"
    cursor.execute(statement, [nombre, especialidad])
    db.commit()
    return True

def update_doctor(id, nombre, especialidad):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE doctores set nombre = ?, especialidad = ? WHERE id = ? "
    cursor.execute(statement, [id, nombre, especialidad])
    db.commit()
    return True

def insert_cita(paciente_id, doctor_id, fecha):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO citas(paciente_id, doctor_id, fecha) VALUES (?, ?, ?)"
    cursor.execute(statement, [paciente_id, doctor_id, fecha])
    db.commit()
    return True

def delete_cita(paciente_id, doctor_id,fecha):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE citas WHERE paciente_id = ?, doctor_id = ?, fecha = ? "
    cursor.execute(statement, [paciente_id, doctor_id,fecha])
    db.commit()
    return True