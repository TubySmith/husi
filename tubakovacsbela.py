# First Project
 
# írjunk összeadó függvényt 
# legyen két paraméter
def osszead(x,y):
    return x + y


#készítsünk összeadó lambda függvényt
lambda_osszeado = lambda x,y: x + y

# print("Összead: ",osszead(1,2))
# print("LAMBDA: ",lambda_osszeado(1,2))

# készítsünk függvényt, mely igaz értéket ad párosra
is_pair = lambda x : x % 2 == 0

# írjunk függvényt mely karakteresen adja vissza, hogy
# páros/páratlan a szám, használja az előző függvényt
def paros_e(x):
    return "páros" if is_pair(x) else "páratlan"

# print('1', paros_e(1))
# print('2', paros_e(2))

# irjunk fabonacci sor függvényt
def fabonacci (n):
    '''fabonacci sor elemei
    '''
    return n if n<2 else fabonacci(n-2) + fabonacci(n-1)

for i in range(7):
    print(fabonacci(i),end=' ')
print()

def fabonacci_generator(n:int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fabonacci_start = fabonacci_generator(7)
for _ in range(7):
    print(next(fabonacci_start), end=' ')
print()

def fabonacci_list(n):
    fib_list = [0, 1]
    for _ in range(n-2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n] 

print(fabonacci_list(7))