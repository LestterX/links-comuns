from flask import Flask, render_template, redirect, request, send_from_directory
import sqlite3 as sq
import os

def get_deb_connection():
    conn = sq.connect('static/db/database.db')
    conn.row_factory = sq.Row
    return conn
def adicionar_db(nome, link):
    conn = get_deb_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sites (nome, link) VALUES ('"+nome+"', '"+link+"')")
    conn.commit()
    conn.close
def remover_db(nome):    
    conn = get_deb_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sites WHERE nome='"+nome+"'")
    conn.commit()
    conn.close

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='static/db' #LOCAL DO BANCO DE DADOS DOS SITES

@app.route("/", methods = ['POST', 'GET'])
def inicio():
    title = "Gerenciador"
    conn = get_deb_connection()
    sites = conn.execute('SELECT * FROM sites ORDER BY nome ASC').fetchall()
    conn.close()
    return render_template("index-main.html", sites = sites, title = title)

@app.route("/login", methods=["POST", "GET"])
def login(user = None, senha = None):
    if request.method == "POST": 
        user = request.form["usuario"]  
        senha = request.form["senha"]
        if user.lower() == "administrador" and senha == "upjet1349":
            return redirect("/editar")
        else:
            return '<script>alert("Senha ou usuário incorretos");</script>'
    elif request.method == "GET":
        return redirect("/")
    else:
        return None
    
@app.route("/editar", methods=["POST", "GET"])
def editar():
    title = "Gerenciador"
    conn = get_deb_connection()
    sites = conn.execute('SELECT * FROM sites ORDER BY nome ASC').fetchall()
    conn.close()
    if request.method == "GET":
        return render_template("index.html", sites = sites, title = title)
    else:
        return None

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(app.root_path)
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    print(full_path)
    return send_from_directory(full_path, filename)

@app.route('/adicionar', methods=["POST"])
def adcionar(nome=None, link=None):
    if request.method == 'POST':
        nome = request.form['nome']
        link = request.form['link']
        adicionar_db(nome, link)
        return redirect('/editar')
    else:
        return redirect('/editar')

@app.route('/remover', methods=['POST'])
def remover(nome = None):
    if request.method == 'POST':
        nome = request.form['nome']
        remover_db(nome)
        return redirect('/editar')
    else:
        return redirect('/editar')

if __name__ == "__main__":
    # app.run(host='10.0.0.112', port='5000',debug=True)
    app.run(debug=True)