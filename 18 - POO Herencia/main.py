
import clases 

persona = clases.Persona()
persona.setNombre("Jesus")
persona.setApellidos("Lara")
persona.setEdad(24)
persona.setAltura(1.75)
print(persona.getAltura(),persona.getApellidos(),persona.getEdad(),persona.getNombre())


informatico = clases.Informatico()

informatico.setNombre("Roberto")
informatico.setAltura(2.00)
informatico.setEdad(33)
informatico.setApellidos("Robles")

print(informatico.getNombre(),informatico.getAltura(),informatico.getEdad(),informatico.getApellidos())

print("---------------------")
tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")

print(tecnico.lenguajes)
print(tecnico.AuditarRedes)