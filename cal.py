import time

import math
print(""""
   _____      _            _           _                    __ _     _           
  / ____|    | |          | |         | |                  / _(_)   (_)          
 | |     __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _  | |_ _ ___ _  ___ __ _ 
 | |    / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` | |  _| / __| |/ __/ _` |
 | |___| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | | | | \__ \ | (_| (_| |
  \_____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_| |_| |_|___/_|\___\__,_|
                                                                       
""")
m=float(input("Ingrese la masa del cuerpo (Kilogramos) "))

f=float(input("Ingrese la fuerza aplicada al cuerpo (Newton)(Ingresar valor negativo (-) para mover el objeto en la direccion opuesta) "))
g=9.8
fx=f

pesoy=m*g
if input("¿El plano esta inclinado? (s/n) ").lower()=="s":
    +
    inc=int(input("¿Cuantos grados(°) esta inclinado el plano? "))
    while inc>90 or inc<0:
        print("No es posible, ingrese otro valor ")
        inc=int(input("¿Cuantos grados(°) esta inclinado el plano? "))
    fx=fx+m*g*math.sin(inc*math.pi/180)
    pesoy=m*g*math.cos(inc*math.pi/180)
if input("¿Hay friccion? (s/n) ").lower()=="s":
    material=input("¿Que materiales componen a los cuerpos?\na. Madera sobre madera\nb. Acero sobre hielo\nc. Teflón sobre teflón\nd. Caucho sobre cemento seco\ne. Vidrio sobre vidrio\nf. Esquí sobre nieve\ng. Madera sobre cuero\nh. Aluminio sobre acero\ni. Articulaciones humanas\nj. Personalizado\n")
    if material=="a":
        ue=0.5
        ud=0.3
    elif material=="b":
        ue=0.03
        ud=0.02
    elif material=="c":
        ue=0.04
        ud=0.04
    elif material=="d":
        ue=1
        ud=0.8
    elif material=="e":
        ue=0.9
        ud=0.4
    elif material=="f":
        ue=0.1
        ud=0.05
    elif material=="g":
        ue=0.5
        ud=0.4
    elif material=="h":
        ue=0.61
        ud=0.47
    elif material=="i":
        ue=0.02
        ud=0.003
    elif material=="j":
        ue=float(input("Coeficiente de friccion estatico: "))
        ud=float(input("Coeficiente de friccion dinamico: "))
    ffe=ue*pesoy
    ffd=ud*pesoy
    fuerzaNeta=fx-ffd
    if ffe>abs(fx):
        print("Fuerza Aplicada:",f,"Newton\nFuerza de Friccion Estatica:",ffe,"Newton\nEste objeto no se mueve porque la friccion entre los cuerpos es muy grande")
        exit()
    else:a=fuerzaNeta/m
else:
    a=fx/m
    if a==0:
        print("Este objeto no se mueve")
print("El objeto tiene una aceleracion de",a,"m/s^2 (Valor positivo: movimiento -> Valor negativo: <-)")