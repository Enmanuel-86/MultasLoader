from ..conexion_db import session
from ..models.vehiculos_model import Vehiculos

class VehiculoRepository:
    def __init__(self):
        self.session = session

    def _consulta_base(self, consulta):
        return [
                {
                "id_vehiculo": vehiculo.id_vehiculo,
                "id_tipo": vehiculo.id_tipo,
                "id_modelo": vehiculo.id_modelo,
                "id_marca": vehiculo.id_marca,
                "placa": vehiculo.placa,
                "color": vehiculo.color
                }
                for vehiculo in consulta
                ]
    

    def obtener_todos_los_vehiculo(self):
        try:
            consulta = self.session.query(Vehiculos).all()
            return self._consulta_base(consulta)
        except ValueError as e:
            print("Error en la funcion de obtener_todos_los_vehiculos")
            print(e)
        


h = VehiculoRepository()

print(h.obtener_todos_los_vehiculo())