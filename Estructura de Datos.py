s = {12, 23.4, 'alpaca'}
s = set([213, 234, 65])
print(type(s))
s.add(40)
s.add(30)
s.update([80, 90, 70])
s.remove(70)
s.discard(70)
elemento_aleatorio = s.pop()
s2 = s.copy()
s.clear()
print(s)
print(elemento_aleatorio)
# print(s[1]) incorrecto

# metodos de sets
fs = frozenset ([30, 40, 5, 6])
print(fs)
# fs.add(7) incorrecto
print(fs.union(s))
print(s.intersection(fs))
print(fs.difference(s))

squares = {x**2 for x in range (10)}
print(squares)

even_numbers = {x for x in squares if x % 2 == 0}
print(even_numbers)

# borrado de duplicados
lista = [1,1,1,1,2,5,6,7,8,9,4,3,2]
lista = list(set(lista))
print(lista)

# Comprobacion de miembros mas rapido que en las listas
n = {1,2,3,4,5,6}
print(3 in n)

# Busqueda de elementos unicos
l2 = [1,2,3,4,5]
l3 = [2,3,4]
print(set(l2)-set(l3))
print(set(l2) set(l3)) # diferencia ambos, no simbolo

# equivalencia: ==
# no equivalencia !=
# subconjunto: s1 <= s2
# union: s1 & s2
# diferencia primero: s1 - s2
# diferencia ambos: s1  s2