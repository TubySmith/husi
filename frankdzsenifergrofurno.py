# First Project

# Irjunk osszeadofuggvenyt
# legyen ket parameter
def osszead(x,y,z):
    return x + y + z 
print(osszead(1,5,2))
#keszitsunk egy lambda fuggvenyt
lambda_osszeado = lambda x,y:  x + y
print("LAMBDA:", lambda_osszeado(1,249))
#negyzetreemeles
numbers = {1, 2, 3, 4}
squared = list(map(lambda x: x**2, numbers))
print(squared)
#paros vagy paratlan
is_pair = lambda x : x % 2 == 0
print(is_pair(1))
print(is_pair(2))
#irjunk fabonacci fuggvenyt
def fabonacci (n):
    '''fabonacci sor elemei
    '''
    return n if n<2 else fabonacci(n-2) + fabonacci(n-1)
for i in range(7):
    print(fabonacci(i), sep=' ',end=' ')
    def fabonacci_generator(n:int):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a+ b
    for i in range(9):
        print(fabonacci_generator(i), end=' ')
        #valtozo parameteru 
# függvény
def valami():
    pass
