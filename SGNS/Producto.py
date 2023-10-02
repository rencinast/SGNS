import pyodbc

class Producto:
    def __init__(self,nombreProducto: str, precio: float) -> None:
        self.nombreProducto = nombreProducto
        self.precio = precio
        

    def registrarProducto(nombreProduto: str, precio: float):
        from main import cursor, connection
        producto = Producto(nombreProduto,precio)
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Producto (nombreProducto, precio) VALUES (?,?);"
        cursor.execute(sqlQuery, (str(producto.nombreProducto), float(producto.precio)))
        connection.commit()
    
#Producto.registrarProducto("Aceite alkalino", 455.67)