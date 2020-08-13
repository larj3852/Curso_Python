class Persona:
    """
    Nombre
    Apellidos
    Altura
    Edad
    """
    def getNombre(self):
        return self.Nombre
    def getApellidos(self):
        return self.Apellidos
    def getAltura(self):
        return self.Altura 
    def getEdad(self):
        return self.Edad 
    def setNombre(self,nombre):
        self.Nombre = nombre
    def setApellidos(self,apellidos):
        self.Apellidos = apellidos
    def setEdad(self,edad):
        self.Edad = edad
    def setAltura(self,altura):
        self.Altura = altura

    def hablar(self):
        return "Estoy Hablando"
    def caminar(self):
        return "Estoy Caminando"
    def dormir (self):
        return "Estoy Durmiendo"

#HERENCIA
class Informatico(Persona):
    """
    Lenguajes
    Experiencia
    """
    def __init__(self):
        self.lenguajes= "HTML, CSSS, JavaScript, PHP"
    
    def getLenguajes(self):
        return self.lenguajes
    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    def programar(self):
        return "Estoy Programando"
    def repararPC(self):
        return "Estoy Reparando PC"

# HERENCIA DE LA HERENCIA

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.AuditarRedes = "Experto"
        self.ExperienciaRedes = 15
    
    def auditoria(self):
        return "Estoy auditando una red"
