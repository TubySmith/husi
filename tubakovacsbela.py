# First Project
# HUSI 

 
# írjunk összeadó függvényt 
# legyen két paraméter
def osszead(x,y):
    return x + y

#készítsünk összeadó lambda függvényt
lambda_osszeado = lambda x,y: x + y

print("Összead: ",osszead(1,2))
print("lambda összeadó: ",lambda_osszeado(1,2))

# készítsünk függvényt, mely igaz értéket ad párosra
is_pair = lambda x : x % 2 == 0

# írjunk függvényt mely karakteresen adja vissza, hogy
# páros/páratlan a szám, használja az előző függvényt
def paros_e(x):
    return "páros" if is_pair(x) else "páratlan"

print('páros-e az 1? ', paros_e(1))
print('páros-e az 2? ', paros_e(2))


# irjunk fabonacci sor függvényt

# rekulzív megvalósítás
def fabonacci (n):
    return n if n<2 else fabonacci(n-2) + fabonacci(n-1)


# fabonacci generator
def fabonacci_generator(n:int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# fabonacci list
def fabonacci_list(n):
    fib_list = [0, 1]
    for _ in range(n-2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]    
 
# fabonacci darabszám megadása
FABONACCI_NUMBER = 10

# rekulzió kiírása
print('rekulzió kiírása')
for i in range(FABONACCI_NUMBER):
    print(fabonacci(i),end=' ')
print()

# generátor kiírása
print('generátor kiírása')
fabonacci_start = fabonacci_generator(FABONACCI_NUMBER)
for _ in range(FABONACCI_NUMBER):
    print(next(fabonacci_start), end=' ')
print()

print('lista kiírása')
print(fabonacci_list(FABONACCI_NUMBER))

# készítsünk változó paraméterű függvényt, 
# mely összegzi a paramétereket
def szumma(*args):
    sz = 0
    for i in args:
        if isinstance(i,(int,float)):
            sz += i
        if isinstance(i,(list,tuple)):
            sz += szumma(*i)
    return sz    

print('szummázó')
print('üres:',szumma())
print('1:',szumma(1))
print('1,2:',szumma(1,2))
print('1,2,3:',szumma(1,2,3))
print('(1,2),3:',szumma((1,2),3))
print('(1,2),(3):',szumma((1,2),(3)))
print('(1, [2, [3, 4], (5, 6)])',szumma(1, [2, [3, 4], (5, 6)]))
