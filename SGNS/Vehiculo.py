import pyodbc


class Vehiculo:
    def __init__(self,marca: str, modelo: str,color: str, kilometraje:str , numeroSerie: str ,placa: str, idCliente: int ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = kilometraje
        self.numeroSerie = numeroSerie
        self.placa = placa
        self.idCliente = idCliente

    def registrarVehiculo(marca: str, modelo: str,color: str, kilometraje:str , numeroSerie: str ,placa: str, idCliente: int):
        from main import cursor, connection
        vehiculo = Vehiculo(marca,modelo,color, kilometraje,numeroSerie,placa,idCliente)
        
        #se agrega a la base de datos
        sqlQuery = "INSERT INTO Vehiculo (marca, modelo, color, kilometraje, numeroSerie, placa , idCliente) VALUES (?,?,?,?,?,?,?);"
        cursor.execute(sqlQuery, (str(vehiculo.marca), str(vehiculo.modelo) , str(vehiculo.color) , str(vehiculo.kilometraje) , str(vehiculo.numeroSerie), str(vehiculo.placa),  int(vehiculo.idCliente) ))
        connection.commit()


#Vehiculo.registrarVehiculo("volkswagen","bocho","gris","14265","1458712","wer14552",2)