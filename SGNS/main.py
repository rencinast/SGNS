from flask import Flask,flash, render_template,request,redirect,session
import pyodbc
from Cliente import Cliente
from Vehiculo import Vehiculo
from Servicio import Servicio
from Producto import Producto
#Inicio conexion a base de datos 
try:
    #aqui, cambien aurora por el nombre de su server, database por el nombre de la base de datos, UID Y PWD son el usuario y contraseña para conectarse con credenciales de sql server
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AURORA;DATABASE=ProyectoTaller;UID=Felipe;PWD=contra')
    print("conexion exitosa")
    cursor = connection.cursor()

except Exception as ex:
    print (ex)
#Fin conexion a base de datos 


#app de flask
app = Flask(__name__)
app.secret_key = "asdfvfñfes7u2nairfn"


#Inicio
@app.route("/", methods=['GET','POST'])
def index():
        return redirect("/Login")


#Login 
@app.route("/Login", methods= ["GET","POST"])
def Login():
    if request.method == 'GET':
        return render_template('Login.html')
    
    elif request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña'] 
        #verifica que el usuario existe y la contraseña es correcta
        cursor.execute("SELECT correo FROM Admin where correo = '"+ correo +"' AND contraseña = '"+contraseña+"'")
        resultado = cursor.fetchall()
        filas = len(resultado)

        #el query dio un resultado, el usario existe
        if filas == 1:
            session['logged'] = True
            cursor.execute("SELECT idAdmin FROM Admin where correo = '"+ correo +"'")
            resultado = cursor.fetchall()
            session['idAdmin'] = resultado[0][0]
            print("sesion iniciada correctamente")
            return redirect("/Home")
        #el query no dio match, el usuario no existe
        else:
            print("no se encontro el usuario")
            session['logged'] = False
            return redirect("/Error")

#Pagina Principal 
@app.route("/Home", methods= ["GET","POST"])
def HomeCliente():
    metodo = request.method
    if metodo == 'GET':
            if session['logged'] == True:
                return render_template('Home.html')
                
            else:
                return redirect("/Error")
            
#RegistrarCliente 
@app.route("/RegistrarCliente", methods= ["GET","POST"])
def RegistrarCliente():
        if request.method == 'GET':
             return render_template('RegistrarCliente.html')
    
        elif request.method == 'POST':
            Cliente.registrarCliente(request.form['nombreCliente'], request.form['rfc'], request.form['email'], request.form['telefono'],request.form['direccion'])
            


#ConsultarCliente 
@app.route("/ConsultarCliente", methods= ["GET","POST"])
def ConsultarCliente():
        if session['logged'] == True:
            return render_template('ConsultarCliente.html')
        else:
             return render_template('Error.html')

#RegistrarVehiculo
@app.route("/RegistrarVehiculo", methods= ["GET","POST"])
def RegistrarVehiculo():
        if request.method == 'GET':
            return render_template('RegistrarVehiculo.html')
        
        elif request.method == 'POST':
            Vehiculo.registrarVehiculo(request.form['marca'], request.form['modelo'], request.form['color'], request.form['kilometraje'], request.form['numeroSerie'], request.form['placa'], request.form['idCliente'])

#ConsultarVehiculo 
@app.route("/ConsultarVehiculo", methods= ["GET","POST"])
def ConsultarVehiculo():
        if session['logged'] == True:
            return render_template('ConsultarVehiculo.html')
        else:
             return render_template('Error.html')

#RegistrarServicio
@app.route("/RegistrarServicio", methods= ["GET","POST"])
def RegistrarServicio():
         if request.method == 'GET':
             return render_template('RegistrarServicio.html')
         
         elif request.method == 'POST':
              Servicio.registrarServicio(request.form['nombreServicio'], request.form['precio'])
          

#ConsultarServicio 
@app.route("/ConsultarServicio", methods= ["GET","POST"])
def ConsultarServicio():
        if session['logged'] == True:
            return render_template('ConsultarServicio.html')
        else:
             return render_template('Error.html')

#RegistrarProducto
@app.route("/RegistrarProducto", methods= ["GET","POST"])
def RegistrarProducto():
         if request.method == 'GET':
             return render_template('RegistrarProducto.html')
         
         elif request.method == 'POST':
              Producto.registrarProducto(request.form['nombreProducto'], request.form['precio'])
    
        
#ConsultarProducto
@app.route("/ConsultarProducto", methods= ["GET","POST"])
def ConsultarProducto():
        if session['logged'] == True:
            return render_template('ConsultarProducto.html')
        else:
             return render_template('Error.html')

#RegistrarNota
@app.route("/RegistrarNota", methods= ["GET","POST"])
def RegistrarNota():
        if session['logged'] == True:
            return render_template('RegistrarNota.html')
        else:
             return render_template('Error.html')
        
#ConsultarNota
@app.route("/ConsultarNota", methods= ["GET","POST"])
def ConsultarNota():
        if session['logged'] == True:
            return render_template('ConsultarNota.html')
        else:
             return render_template('Error.html')

if __name__ == "__main__":
    app.run(debug=True)