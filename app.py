from flask import Flask, render_template,request, redirect, url_for
import os 
import database as db

#accedemos a nustro repositorio con el siguiente codigo
templete_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#accedemos a las recuros que tiene nuestro proyecto 
templete_dir = os.path.join(templete_dir, 'src', 'templates')

#inicializamos Flask y le indicamos el donde estara nuestro index.html
app = Flask(__name__, template_folder=templete_dir)

#establecemos las rutas de la aplicacion 
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/categories')
def categories():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM categories")
    myresult = cursor.fetchall()
    #convertir  los datos a diccionario
    insertObject = []
    columnames =[column[0] for column in cursor.description]
    for record in myresult:
    #usamos la funcion append para ir metiendo los datos en formato diccionario
        insertObject.append(dict(zip(columnames, record)))
    cursor.close
    return render_template('categories.html', data= insertObject)

@app.route('/addcategories', methods=['POST'])
def addCategories():
     name = request.form['name']
     description = request.form['description']
     createdat = request.form['createdat']
     createdby = request.form['createdby']

     if name and description and createdat and  createdby :
        cursor = db.connection.cursor()
        sql = "INSERT INTO categories (name, description, created_at, created_by) VALUES (%s, %s, %s, %s)"
        data = (name,  description, createdat, createdby)
        cursor.execute(sql, data)
        db.connection.commit()
     return redirect(url_for('categories'))

@app.route('/deleteCategories/<string:id>')
def deleteCategories(id):
    cursor = db.connection.cursor()
    sql = "DELETE FROM categories WHERE idcategories=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('categories'))


@app.route('/editCategories/<string:id>', methods=['POST'])
def editCategories(id):
    name = request.form['name']
    description = request.form['description']
    createdat = request.form['createdat']
    createdby = request.form['createdby']

    
    if name and description and createdat and  createdby :
        cursor = db.connection.cursor()
        sql = "UPDATE  categories SET name = %s, description = %s, created_at = %s, created_by = %s WHERE idcategories = %s"
        data = (name,  description, createdat, createdby, id)
        cursor.execute(sql, data)
        db.connection.commit()
    return redirect(url_for('categories'))
