import validaciones as vali




while True:
    vali.mostar_menu_de_navegacion()
    menu=vali.val_navegacion_menu()
    if menu==1:#comprar entradas
        vali.opc_1()
    elif menu==2:#mostrar ubicaciones✅
        vali.opc2()
    elif menu==3:#listado de asistentes
        vali.opc_3()
    elif menu==4:#mostrar ganancias totales✅
       vali.ganancias_totales()
    else:#Cierre✅
        cerrar=vali.cerrar_menu()
        if cerrar==1:
            break
        else:
            print("regresando")