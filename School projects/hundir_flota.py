import os

os.system("cls")

tablero=[]
for fila in range(5):
    tablero.append([])
    for cols in range(5):
        tablero[fila].append(int(input()))
print(tablero)

encontrado=False
barco3=0
time = 3
while time > 0:
    time = time-1
    coorX=int(input("dime la cordenada x: "))
    coorY=int(input("dime la cordenada y: "))
    if tablero[coorX-1][coorY-1]==0:
        print("agua")
    elif tablero[coorX-1][coorY-1]==1:
        print("tocado")
        tablero[coorX-1][coorY-1]=0
        barco3=barco3+1
        time=time+2
        
    if barco3==3:
        encontrado=True
        break

if encontrado==False:
    print("has perdido la parida")
else:
    print("Has ganado la partida")
