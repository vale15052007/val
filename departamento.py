class Departamento:

    def __init__(self, id_departamento:int, nombre:str, piso:int):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.piso = piso
 
    @property
    def id_departamento(self)-> int: 
        return self._id_departamento

    @id_departamento.setter
    def id_departamento(self,id_departamento:int)-> None:
        self._id_departamento = id_departamento

    @property
    def nombre(self)-> str:
        return self._nombre

    @nombre.setter
    def nombre(self,nombre:str)-> None:
        self._nombre = nombre

    @property
    def piso(self)->int:
        return self._piso

    @piso.setter
    def piso(self,piso:int)-> None:
        self._piso = piso

    def __str__(self)-> str:
        return f"Información del departamento:\nid_departamento: {self.id_departamento}\nNombre: {self.nombre}\npiso: {self.piso}"

    def __repr__(self)-> str:
        return f"Departamento(id_departamento='{self.id_departamento}', nombre='{self.nombre}', 'piso={self.piso}')"

    #https://github.com/larriag13/01-POOS-Python-n2p13c1.git