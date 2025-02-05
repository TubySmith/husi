# First Project
 
# írjunk összeadó függvényt 
# legyen két paraméter
def osszead(x,y):
    return x + y


#készítsünk összeadó lambda függvényt
lambda_osszeado = lambda x,y: x + y

print("Összead: ",osszead(1,2))
print("LAMBDA: ",lambda_osszeado(1,2))

# készítsünk függvényt, mely igaz értéket ad párosra
is_pair = lambda x : x % 2 == 0

# írjunk függvényt mely karakteresen adja vissza, hogy
# páros/páratlan a szám, használja az előző függvényt
def paros_e(x):
    return "páros" if is_pair(x) else "páratlan"

print('1', paros_e(1))
print('2', paros_e(2))
