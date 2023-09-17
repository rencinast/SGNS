from flask import Flask,flash, render_template,request,redirect,session
import pyodbc
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
        cursor.execute("SELECT correo FROM Clientes where correo = '"+ correo +"' AND contraseña = '"+contraseña+"'")
        resultado = cursor.fetchall()
        filas = len(resultado)

        #el query dio un resultado, el usario existe
        if filas == 1:
            session['logged'] = True
            cursor.execute("SELECT idCliente FROM Clientes where correo = '"+ correo +"'")
            resultado = cursor.fetchall()
            session['idCliente'] = resultado[0][0]
            print("sesion iniciada correctamente")
            return redirect("/HomeCliente")
        #el query no dio match, el usuario no existe
        else:
            print("no se encontro el usuario")
            session['logged'] = False
            return redirect("/Error")

#HomeCliente 
@app.route("/HomeCliente", methods= ["GET","POST"])
def HomeCliente():
    metodo = request.method
    if metodo == 'GET':
            if session['logged'] == True:
                return render_template('HomeCliente.html')
                
            else:
                return redirect("/Error")
            

if __name__ == "__main__":
    app.run(debug=True)