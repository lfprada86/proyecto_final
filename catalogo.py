import os

class Pelicula:

    def __init__(self,ruta_pelicula):
        self.peliculas=[]
        self.__ruta_privada=None # atributo privado (ruta del catalogo donde se va a guardar la pelicula)

class catalogo:


    def __init__(self, file_name):
        self.file_name = file_name
        self.ruta = "/Users/lfpradag/Desktop/final/final/"

    def existe_catalogo(self):
        self.file_name = input("Ingrese el nombre del catalogo (sin la extensión): ")
        
        ruta_completa = self.ruta + self.file_name + ".txt"
        print("Ruta completa del archivo:", ruta_completa)
        
        existe = os.path.isfile(ruta_completa)
        if existe == False:
            return False
        else:
            return True
        
    def agregar_catalogo(self):
        '''
        Función que crea un catalogo vacío para guardar una lista de peliculas.
        Parámetros:
        file_name: Es un catalogo.
        Devuelve:
        Un mensaje informando sobre si el catalogo se ha creado correctamente o no.
        '''

        if catalogo.existe_catalogo(self) == False:
            try:
                file_ruta = os.path.join(self.ruta, self.file_name + ".txt")
                print(file_ruta)
                with open(file_ruta, 'w') as archivo:
                    archivo.write("")
                    
                print(f"El archivo de texto '{self.file_name}.txt' se ha creado exitosamente y se encuentra en la ruta {self.ruta}")
            
            except Exception as e:
              print(f"Error creando el archivo: {e}")

            
        else:
            print("El nombre del catalogo ingresado ya existe")

    
    def agregar_pelicula (self):
        '''
        Función que crea y agrega peliculas al catálogo seleccionado. 
        Parámetros:
        peliculas: Es un diccionario que solicita al usuario completar su información.
        '''


        if catalogo.existe_catalogo(self) == True:
            try:
                file_ruta = os.path.join(self.ruta, self.file_name + ".txt")
                print(file_ruta)
                with open(file_ruta, 'a') as archivo:
                    peliculas={"Nombre pelicula: ": input("Ingrese el nombre de la película: "), "Año: ": input("Ingrese el año en el que se lanzo la película: "), "Director: ": input("Ingrese la inicial del nombre y el apellido del director de la película: ")}
                    archivo.write("- " + str(peliculas) + "\n")

            except Exception as e:
              print(f"Error creando el archivo: {e}")

            
        else:
            print("El nombre del catalogo ingresado No existe")
            
    def Listar_pelicula (self):
        '''
        Función que lista las peliculas de  un catalogo seleccionado.
        '''


        if catalogo.existe_catalogo(self) == True:
            try:
                file_ruta = os.path.join(self.ruta, self.file_name + ".txt")
                print(file_ruta)
                with open(file_ruta, 'r') as archivo:
                    contenido = archivo.read()
                    print(contenido)
                
            except Exception as e:
              print(f"Error creando el archivo: {e}")

            
        else:
            print("El nombre del catalogo ingresado No existe")

    def eliminar_catalogo(self):
        '''
        Función que elimina un catalogo de peliculas.
        Parámetros:
        file_name: Es un catalogo.
        Devuelve:
        Un mesaje informando sobre si el catalogo se ha eliminado correctamente o no.
        '''
        if catalogo.existe_catalogo(self) == True:
            answer = input('El catalogo ' + self.file_name + ' ya existe. ¿Desea eliminarlo (S/N)? ')
            if answer == 'N': 
                return print('El catalogo aun existe.\n')
            if answer == 'S':
                os.remove(os.path.join(self.ruta, self.file_name + ".txt"))
                return print('Se ha borrado el catálogo')
            
            
    def menu(self):
            '''
            Función que presenta un menú con las operaciones disponibles sobre un catálogo de películas 
            y devuelve la opción seleccionada por el usuario.
            Devuelve:
            La opción seleccionada por el usuario.
            '''
            print('Menú de catalogo de peliculas')
            print('============================')
            print('1 - Crear Catálogo')
            print('2 - Eliminar Catálogo')
            print('3 - Agregar películas')
            print('4 - Listar películas')
            print('0 - Terminar')
            option = input('Introduzca el número de la opción deseada: ')
            return option

    def menu_catalogo(self):
            '''
            Función que lanza la aplicación para el menu de catalogos y peliculas.
            '''
        
            while True:
                    option = self.menu()
                    if option == '1':
                        self.agregar_catalogo()
                    elif option == '2':
                        self.eliminar_catalogo()
                    elif option == '3':
                          self.agregar_pelicula()
                    elif option == '4':
                        self.Listar_pelicula()
                    elif option == '0':
                        break
                    else:
                        print('Opción no válida. Inténtelo de nuevo.')
    

