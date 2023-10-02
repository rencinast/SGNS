import pyodbc

class Servicio:
    def __init__(self,nombreServicio: str, precio: float) -> None:
        self.nombreServicio = nombreServicio
        self.precio = precio
        

    def registrarServicio(nombreServicio: str, precio: float):
        from main import cursor, connection
        servicio = Servicio(nombreServicio,precio)
        
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Servicio (nombreServicio, precio) VALUES (?,?);"
        cursor.execute(sqlQuery, (str(servicio.nombreServicio), float(servicio.precio)))
        connection.commit()

#Servicio.registrarServicio("cambio de aceite", 200.30)
