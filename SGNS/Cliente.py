import pyodbc


class Cliente:
    def __init__(self,nombreCliente: str, rfc: str,email: str, telefono:str , direccion: str ) -> None:
        self.nombreCliente = nombreCliente
        self.rfc = rfc
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def registrarCliente(nombreCliente: str, rfc: str,email: str, telefono:str , direccion: str ):
        from main import cursor, connection
        cliente = Cliente(nombreCliente, rfc, email, telefono, direccion)
        
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Cliente (nombreCliente, rfc, email, telefono, direccion) VALUES (?,?,?,?,?);"
        cursor.execute(sqlQuery, (str(cliente.nombreCliente), str(cliente.rfc) , str(cliente.email) , str(cliente.telefono) , str(cliente.direccion)))
        connection.commit()

#Cliente.registrarCliente("Felipe Rubio", "RUFI89", "FELIPE9201@GMAIL.COM", "6623251442", "GENERAL PIÑA 66")
