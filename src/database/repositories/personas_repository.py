from ..conexion_db import session
from ..models.personas_model import Personas

class PersonaRepository:
    def __init__(self):
        self.session = session

    def _consulta_base(self, consulta):
        return [
                {
                "id": persona.id_persona,
                "cedula": persona.cedula,
                "nombre": persona.nombre,
                "apellido": persona.apellido,
                "residencia": persona.residencia
                }
                for persona in consulta
                ]
        
    def obtener_todas_las_personas(self):
        try:
            consulta = self.session.query(Personas).all()
            return self._consulta_base(consulta)
        except:
            print("No se pudo realizar la consulta en obtener_todas_las_personas")

    def obtener_persona_por_id(self, arg_id_persona):
        try:
            consulta = self.session.query(Personas).filter_by(id_persona = arg_id_persona)
            return self._consulta_base(consulta)
        except:
            print("No se pudo realizar la consulta en obtener_todas_las_personas")

    




h = PersonaRepository()

print(h.obtener_persona_por_id(5))