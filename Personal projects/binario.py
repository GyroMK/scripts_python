import os
os.system("cls")

binario=[]
binTO=[]
Octal=[]
Hex=[]
def bin():
    decimal = int(input("escribe un numero decimal: "))
    if decimal < 0:
        print("el numero no puede ser negativo")
    while decimal/2 > 0:
        binario.insert(0,decimal%2)
        binTO.append(decimal%2)
        decimal = int(decimal/2)
        print(decimal)
    os.system("cls")
    print("El binario es:",binario)
def dec(binario):
    decimal=0
    for i in range(len(binario)):
        num = binTO[i]
        if num == 1:
            decimal += 2**i
    print("Decimal es:",decimal)

def octal():
    cont=0
    for i in range(len(binario)):
        num = binTO[i]
        while cont <=3:
            octal = 0
            if num == 1 and cont <=3:
                octal += 2**cont
                Octal.insert(0,octal)
            if cont==3:
                cont=0
            cont = cont+1
            break
    print("El octal es:",Octal)

def hex():
    cont=0
    for i in range(len(binario)):
        num = binTO[i]
        while cont <=4:
            hex = 0
            if num == 1 and cont <=4:
                hex += 2**cont
                Hex.insert(0,hex)
            if cont==4:
                cont=0
            cont = cont+1
            break
    print("El hexadecimal es:",Hex)
        

myBin=[]
bin()
dec()
octal()
hex()