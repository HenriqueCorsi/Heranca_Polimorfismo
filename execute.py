from construct import Catalogo
from construct import Filmes
from construct import Serie

# criando o objeto e os seus parametros
vingadores = Filmes('vingadores guerra infinita', 2020, 175)
godzilla = Filmes('Godzilla', 2014, 120)
walking_dead = Serie('The walking dead', 2013, 12)
mandalorian = Serie('Mandalorian', 2020, 2)

# Dando likes
vingadores.add_likes()
vingadores.add_likes()
walking_dead.add_likes()
walking_dead.add_likes()
godzilla.add_likes()
godzilla.add_likes()
godzilla.add_likes()
godzilla.add_likes()
mandalorian.add_likes()
mandalorian.add_likes()
mandalorian.add_likes()
mandalorian.add_likes()


# Polimorfismo
filmes_series = [vingadores, godzilla, walking_dead, mandalorian]

for loop in filmes_series:
    print(loop)

