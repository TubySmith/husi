# hi 
# oszeadofugveny
# legyen keto paramater
def oszead(x, y) :
    return x + y

print(oszead (1,2))

# keszitcsunk lambda fugvenyt
f = lambda x: x + 1
print(f(5))  # Kimenet: 6

# Egyszerű összeadás
osszead = lambda x, y: x + y
print(osszead(5, 3))  # Kimenet: 8

# Négyzetre emelés
negyzet = lambda x: x**2
print(negyzet(4))  # Kimenet: 16

# Páros szám ellenőrzése
paros = lambda x: x % 2 == 0
print(paros(4))  # Kimenet: True
print(paros(7))  # Kimenet: False