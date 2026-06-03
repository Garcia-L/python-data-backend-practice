# Proyecto 1 — CLI App (nivel junior)
# Agregar tarea - Listar tareas - Eliminar tarea
import re

lista = []
patron = re.compile(r"^[a-zA-Z\s]+$")

while True:
    print("\n1.Agregar tarea")
    print("2.Ver tareas")
    print("3.Eliminar tarea")
    print("4.Salir")
    
    seleccion = input("Elige una opción: ")
    
    if seleccion == "1":
        tarea = (input("\nEscriba una nueva tarea: "))
        
        if patron.match(tarea):
            lista.append(tarea)
            print("\nTarea agregada")
        else:
            print("\nError, solo se permiten letras")
        
    elif seleccion == "2":
        if not lista:
            print("\nNo hay tareas")
        else:
            for index, item in enumerate(lista):
                print(f"\n {index}. {item}")
            
    elif seleccion == "3":
        if not lista:
            print("\nNo hay tareaas")
            continue
        
        try:
            indice = int(input("\nIngresa el indice que deseas eliminar: "))
            eliminado = lista.pop(indice)
            print(f"Tarea eliminada: {eliminado}")
        
        except (ValueError, IndexError):
            print("\nIndice invalido")
            
    elif seleccion == 4:
        print("\nSaliendo...")
        break
    
    else:
        print("\nOpción inválida")
            