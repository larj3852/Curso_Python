"""
Colecciones

Python se envía con un módulo que contiene varios tipos de datos de contenedores llamados Colecciones. 
"""
#%%   defaultdict --> Crea diccionarios con valor por defecto 
""" defaultdict --> Crea diccionarios con valor por defecto  """
#   
from collections import defaultdict

d = defaultdict(float)  # tipo flotante por defecto
print(d['algo'])
print(d)                #defaultdict(float, {'algo': 0.0})

d = defaultdict(str)  # tipo cadena por defecto
print(d['algo'])
print(d)              # defaultdict(str, {'algo': ''})

#%%     OrderedDict --> Diccionarios ordendaso
""" OrderedDict --> Diccionarios ordendaso """
from collections import OrderedDict

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)            #   OrderedDict([('uno', 'one'), ('dos', 'two'), ('tres', 'three')])

#%%   Counter --> Cuenta el numero de elementos en la lista con mismo valor
"""Counter --> Cuenta el numero de elementos en la lista con mismo valor """
from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
Counter(l)                  # {'a': 3, 'b': 1, 'l': 1, 'p': 1, 'r': 1}
Counter("palabra")          #  {1: 4, 2: 3, 3: 2, 4: 1}

# Los mas repetidos
animales = "gato perro canario perro canario perro"
c = Counter(animales.split())
print(c.most_common(1))  # Primeros elemento más repetido
print(c.most_common(2))  # Primeros dos elementos más repetidos
print(c.most_common())   # Elementos ordenadores por repeticiones

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)

print(c.items())        # Registros del contador por clave-valor
print(c.keys())         # Registros del contador por clave
print(c.values())       # Registros del contador por valor

print(sum(c.values()))  # Suma total de elementos del contador

print(list(c))          # Conversión a lista
print(dict(c))          # Conversión a conjunto

#%% namedtuple  --> 
"""Utilizada para crear pequeñas estructuras inmutables parecida a una clase y sus objetos"""
from collections import namedtuple

Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Hector",apellido="Costa",edad=27)

print(p)

# Podemos acceder a los elementos como si fueran atributos de un objeto
print(p.nombre)
print(p.edad)

# O utilizando índices como con las tuplas clásicas
print(p[0])
print(p[-1])

#%% deque --> 
""" 
prove de una cola doble fin, lo que significa se puede agregar y eliminar elementos
de amobs lados de la cola. 
"""
from collections import deque
d = deque()

d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))       # Output: 3
print(d[0])         # Output: '1'
print(d[-1])        # Output: '3'

d = deque(range(5))
print(len(d))       # Output: 5

#You can pop values from both sides of the deque:
d.popleft()         # Output: 0
d.pop()             # Output: 4
print(d)            # Output: deque([1, 2, 3])

# We can also limit the amount of items a deque can hold. 
d = deque([0, 1, 2, 3, 5], maxlen=5)
print(d)            # Output: deque([0, 1, 2, 3, 5], maxlen=5)
d.extend([6])
print(d)            #Output: deque([1, 2, 3, 5, 6], maxlen=5)

#%% namedtuple -->
""" Converiter una tupla en contenedores convenientes para tareas simples
    Con nametuple's no se tiene que usar index para accesar a los miembors de la tupla
"""
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)
# Output: Animal(name='perry', age=31, type='cat')
print(perry.name)
# Output: 'perry'

#Conversion de namedtuple a diccionarios
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())      # Output: OrderedDict([('name', 'Perry'), ('age', 31), ...

#%% Enum
""" ENUM -->   Enums (enumerated type) are basically a way to organize various things.  """
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...

    # But we don't really care about age, so we can use an alias.
    kitten = 1
    puppy = 2

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

# And now, some tests.
    # >>> charlie.type == tom.type
    # True
    # >>> charlie.type
    # <Species.cat: 1>