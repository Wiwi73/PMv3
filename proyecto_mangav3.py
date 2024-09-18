from modulos.modulos_proyecto_manga import *
from tabulate import tabulate 

def mostrar_menu_principal():
    print(""" Menú Principal:
    1 – Registrar manga          
    2 – Mostrar registro         
    3 – Salir     
        >>>""")
    

# Función que muestra el submenú específico de "Tipo de manga"
# Opción para seleccionar el tipo "Takeboun" 1
 # Opción para seleccionar el tipo "Recopilatorio"2
  # Opción para seleccionar el tipo "Online"3
def mostrar_submenu_manga():
    print("""Tipo de Manga:
    1 – Takeboun      
    2 – Recopilatorio
    3 – Online       
    >>>""")


# Función que procesa la opción de "Tipo de manga" seleccionada por el usuario
def procesar_tipo_manga():
    mostrar_submenu_manga()  # Se muestra el submenú de tipos de manga
    tipo_manga = int(input("Elija un tipo de manga: "))  # El usuario elige un tipo de manga
   

    # Dependiendo de la opción seleccionada, se crea una instancia de la clase correspondiente
    if tipo_manga == 1:
        manga = Takeboun(precio=0, tomos=0, capitulos=0, nombre= None)  # Crear un objeto "Takeboun"
        manga.nombre_manga() #Llama al metodo para introducir el nombre de la obra
        manga.valor()  # Llamar al método para introducir el precio
        manga.cant_caps()
        manga.cant_tomos()
        print(f"Manga Takeboun registrado: {manga}")  # Mostrar el objeto registrado
        return manga #Retornar objeto
       
    elif tipo_manga == 2:
        manga = Recopilatorio(precio=0, tomos=0, capitulos=0, nombre= None)  # Crear un objeto "Recopilatorio"
        manga.nombre_manga()
        manga.valor()  # Llamar al método para introducir el precio
        manga.cant_caps()
        manga.cant_tomos()
        print(f"Manga Recopilatorio registrado: {manga}")  # Mostrar el objeto registrado
        return manga #Retornar objeto
        
    elif tipo_manga == 3:
        manga = Online(web="", tomos=0, capitulos=0,nombre=None)  # Crear un objeto "Online"
        manga.sitio()  # Llamar al método para introducir la web donde se leyó
        manga.nombre_manga()
        manga.cant_caps()
        manga.cant_tomos()
        print(f"Manga Online registrado: {manga}")  # Mostrar el objeto registrado
        return manga #Retornar objeto
    else:
        print("Opción no válida. Volviendo al menú principal...\n")  # Manejar opciones no válidas
        return None, None
     

  
# Función principal que controla el flujo del programa
def main():
    registros_mangas = []  # Lista para almacenar los mangas registrados
    while True:  # Bucle infinito para que el menú se repita hasta que el usuario decida salir
        mostrar_menu_principal()  # Mostrar el menú principal
        try:
            opcion = int(input("Elija una de las opciones: "))  # El usuario elige una opción del menú

            if opcion == 1:
                manga = procesar_tipo_manga()  # Si elige 1, se procesa el tipo de manga (se muestra el submenú)
                if manga:
                    registros_mangas.append(manga.to_list()) # Convertir el objeto manga en una lista antes de agregarlo
                    print("Manga registrado correctamente.\n")
                    print(f"Lista de mangas hasta ahora: {registros_mangas}")  # Depuración

                        
            elif opcion == 2:
                if registros_mangas:
                    print("Mostrando los mangas registrados:\n")
                    encabezados = ["Nombre", "Capítulos", "Tomos", "Tipo", "Precio (Pesos Arg)"] # Encabezados de la tabla que se mostrarán como nombres de las columnas
                    print(tabulate(registros_mangas, headers=encabezados, tablefmt="fancy_grid")) # `tabulate` toma los datos (registros_mangas) y los encabezados, y los muestra como una tabla con el formato "fancy_grid"
                    #for i, manga in enumerate(registros_mangas, start=1):
                       # print(f"{i}. {manga}\n")  # Imprimir cada manga registrado
                else:
                    print("No hay mangas registrados.\n")
            elif opcion == 3:   
                print("Gracias por todo")  # Si elige 5, se termina el programa
                break  # Salir del bucle, terminando el programa
            else:
                print("Opción no válida. Por favor, intente de nuevo.\n")  # Manejar opciones no válidas
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.\n")  # Manejar entradas no numéricas

# Punto de entrada del programa
if __name__ == '__main__':
    main()  # Llamar a la función principal para iniciar el programa