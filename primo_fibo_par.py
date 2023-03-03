
def primo(int):
    b=0
    for i in range(1,x+1):
        if x%i==0:
            b=b+1
    print("es primo") if b<=2 else print("no es primo")

def fibonacci(int):
    a=0
    b=1
    for i in range(x):
        c=a+b
        b=a
        a=c
        if b==x:
            break
        
    print("es fibonaci") if x==b else print("no es fibonacci")

def par(int):
    print("es par") if x%2==0 else print("es impar")

if __name__=="__main__":
    x=int(input("ingrese un número :\n"))
    primo(x)
    fibonacci(x)
    par(x)
