#examen
import numpy as nym
import time 

platinum=120000
gold=80000
silver=50000

contador_platinum=[0]
contador_gold=[0]
contador_silver=[0]

run=[]
nombre=[]

arrayx=[]
arrayY=[]
array=nym.empty((10,10),object)
array.fill("✅")
def mostrar_ubicaciones():
    Contador=1
    for x in range(10):
        print(Contador,end=" ")
        for y in range(10):
            print(array[x][y], end=" ")
        Contador+=1
        print(" ")
        print("  1  2  3  4  5  6  7  8  9  10")
    time.sleep(3)

def mostar_menu_de_navegacion():
    print('''
    \t Menú 
    1). Comprar entradas
    2). Mostrar ubicaciones disponibles
    3). Ver listado de asistentes
    4). Mostrar ganancias totales
    5). Salir

    
    ''')
    print("para nevegar en el menú seleccione el nro")
#-----------------------------------------------------------
def val_navegacion_menu():
    while True:
        try:
            menu=int(input("ingrese nro_"))
            if menu in(1,2,3,4,5):
                return menu
            else:
                print("ERROR de datos ")
        except:
            print("ERROR solo nro enteros")
#-----------------------------------------
def opc_1():
    rut=val_rut()
    name=val_nombre()
    mostrar_ubicaciones()
 
    while True:
        try:
            cant_entra=int(input("ingrese cantidad entradas"))
            if cant_entra >=0 and cant_entra <=3:
                break
            else:
                print("ERROR de datos")
        except:
            print("ingrese solo nro enteros")
    if cant_entra>=1:
        for x in range(cant_entra):
            print("selecione ubicacion")
            ubiX=posicionX()
            ubiY=posicionY()
            if "✅" in array[ubiX][ubiY]:
                if ubiX in(0,1):
                    print(f"precio de cada asiento es ${platinum}")

                    
                    contador_platinum[0]+=1
                elif ubiX in (2,3,4,5):
                    print(f"precio de cada asiento es ${gold}")
                    
                    contador_gold[0]+=1
                elif ubiX in (6,7,8,9):
                    print(f"precio de cada asiento es ${silver}")

                    contador_silver[0]+=1
                array[ubiX][ubiY]="❎"
            elif "❎" in array[ubiX][ubiY]:
                print("print no disponible")

    
    
    run.append(rut)
    nombre.append(name)
    
def opc2():#terminada
    print("cargando posiciones")
    mostrar_ubicaciones()
    while True:
        try:
            opcV=int(input("desea comprar entradas (si=1/no=2"))
            if opcV in (1,2):
                break
            else:
                print("ERROR de ingreso de datos solo 1 o 2")    
        except:
            print("ERROR solo nro enteros")
    if opcV == 1:
        opc_1()
    else:
        print("regresando al menú")

#---------------------------------------------------------------------------------
def posicionX():
    OPCX=int(input("selecione X (desde el 1 al 10)"))
    OPCX=OPCX-1
    return OPCX

def posicionY():
    OPCY=int(input("selecione Y (desde el 1 al 10)"))
    OPCY=OPCY-1
    return OPCY
    
#revisar bien       
#------------------------------------------------------------------------

    

def opc_3():
    print("cargando listado de asistentes")
    print(f"lista de usuarios {run}")
    time.sleep(4)

    

    
#----------------------------------------------------------------
def val_rut():
    rut=int(input("ingrese rut (sin puntos ni -) __:"))
    try:   
        if rut >=10000000 and rut <=999999999:
            return rut
        else:
            print("ERROR ingrese bien el rut")
    except:
        print("ERROR solo nro enteros")
def rut_into_run():
    rut=val_rut()
    if rut in run:
        print("Todo en orden")
        return rut
    else:
        print("Rut no encontrado")
def val_nombre():
    while True:
        name=input("ingrese nombre  ")
        if len(name.strip())>=3 and name.isalpha():
            return name
        else:
            print("ERROR de datos")

def ganancias_totales():
    completo_pre = contador_gold+contador_platinum+contador_silver
    total_full = silver*contador_silver[0] + gold*contador_gold[0] + platinum*contador_platinum[0]
    print(f'''
    /tipo entrada__________/Cantidad_________/Total__________________________
    --------------------------------------------------------------------
    platinum ${platinum}---{contador_platinum[0]}----${platinum*contador_platinum[0]}
    --------------------------------------------------------------------
    gold ${gold}------{contador_gold[0]}-----${gold*contador_gold[0]}
    --------------------------------------------------------------------
    silver ${silver}-----{contador_silver[0]}--${silver*contador_silver[0]}
    --------------------------------------------------------------------
    totales_______________{completo_pre}______${total_full}
    ''')
    time.sleep(3)


def cerrar_menu():
    while True:
        print("Desea cerrar? (si=1/no=2)")
        cerrar=int(input("ingrese opc deseada_"))
        try:
            if cerrar in (1,2):
                print("ok cerrando")
                print("by Dreyco Román date system 6/7/2023")
                return cerrar
            else:
                print("ERROR en el ingreso de datos")
        except:
            print("solo nro enteros")
    
    