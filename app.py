from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import request, redirect

app = Flask(__name__)
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["renacer_con_color"]


colecciones = [
    "participantes",
    "cursos",
    "obras",
    "materiales",
    "recursos"
]

for coleccion in colecciones:
    if coleccion not in db.list_collection_names():
        db.create_collection(coleccion)

if db.participantes.count_documents({}) == 0:
    db.participantes.insert_many([
        {
            "nombre": "Ana López",
            "edad": 16,
            "curso": "Pintura Acrílica"
        },
        {
            "nombre": "Carlos Martínez",
            "edad": 18,
            "curso": "Dibujo Artístico"
        },
        {
            "nombre": "María Hernández",
            "edad": 17,
            "curso": "Acuarela"
        },
        {
            "nombre": "Luis García",
            "edad": 19,
            "curso": "Pintura al Óleo"
        }
    ])

if db.materiales.count_documents({}) == 0:
    db.materiales.insert_many([
        {
            "nombre": "Pintura Acrílica",
            "cantidad": 25,
            "estado": "Disponible"
        },
        {
            "nombre": "Pinceles",
            "cantidad": 40,
            "estado": "Disponible"
        },
        {
            "nombre": "Lienzos",
            "cantidad": 15,
            "estado": "Disponible"
        },
        {
            "nombre": "Paletas de Mezcla",
            "cantidad": 12,
            "estado": "Disponible"
        },
        {
            "nombre": "Caballetes",
            "cantidad": 10,
            "estado": "En uso"
        }
    ])

# =====================================
# PÁGINA PRINCIPAL
# =====================================
@app.route('/')
def inicio():
    return render_template('index.html')

# =====================================
# LOGIN
# =====================================
@app.route('/login')
def login():
    return render_template('login.html')

# =====================================
# DASHBOARD
# =====================================
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# =====================================
# PARTICIPANTES
# =====================================
@app.route('/participantes')
def participantes():
    participantes = list(db.participantes.find())
    return render_template(
        'participantes.html',
        participantes=participantes
    )

# =====================================
# CURSOS
# =====================================
@app.route('/cursos')
def cursos():
    cursos = list(db.cursos.find())
    return render_template(
        'cursos.html',
        cursos=cursos
    )

# =====================================
# OBRAS
# =====================================
@app.route('/obras')
def obras():
    obras = list(db.obras.find())
    return render_template(
        'obras.html',
        obras=obras
    )

# =====================================
# MATERIALES
# =====================================
@app.route('/materiales')
def materiales():
    materiales = list(db.materiales.find())
    return render_template(
        'materiales.html',
        materiales=materiales
    )

# =====================================
# RECURSOS
# =====================================
@app.route('/recursos')
def recursos():
    recursos = list(db.recursos.find())
    return render_template(
        'recursos.html',
        recursos=recursos
    )
@app.route('/ejemplos_paisajes')
def ejemplos_paisajes():
    return render_template('ejemplos_paisajes.html')

# Galería de obras
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# Subir obra
@app.route('/subir_obra')
def subir_obra():
    return render_template('subir_obra.html')

@app.route('/login_admin')
def login_admin():
    return render_template('login_admin.html')

@app.route('/login_usuario')
def login_usuario():
    return render_template('login_usuario.html')

@app.route('/eliminar_participante/<id>')
def eliminar_participante(id):

    db.participantes.delete_one({
        "_id": ObjectId(id)
    })

    return redirect('/participantes')

@app.route('/editar_participante/<id>')
def editar_participante(id):

    participante = db.participantes.find_one({
        "_id": ObjectId(id)
    })

    return render_template(
        'editar_participante.html',
        participante=participante
    )
@app.route('/actualizar_participante/<id>', methods=['POST'])
def actualizar_participante(id):

    db.participantes.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "nombre": request.form['nombre'],
                "edad": request.form['edad'],
                "taller": request.form['taller']
            }
        }
    )

    return redirect('/participantes')

@app.route('/validar_admin', methods=['POST'])
def validar_admin():

    usuario = request.form['usuario']
    password = request.form['password']

    if usuario == "lucero" and password == "1234":
        return redirect('/dashboard')

    return """
    <h2>Usuario o contraseña incorrectos</h2>
    <a href="/login_admin">Volver</a>
    """
# =====================================
# EJECUTAR APP
# =====================================
if __name__ == '__main__':
    app.run(debug=True)

