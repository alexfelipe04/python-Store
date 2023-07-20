from flask import Flask, render_template,request, redirect, url_for
import os 

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
