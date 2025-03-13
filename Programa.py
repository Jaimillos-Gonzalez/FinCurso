#Práctica Fin de Curso: SISTEMA DE GESTIÓN DE BIBLIOTECA

#Variables globales 
biblioteca_libros = []

#Clase Libros
class Libro:
    
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def agregar(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
        else:
            print("Este libro ya está prestado")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print("Este libro ya estaba disponible")

    def mostrar(self):
        for libro in biblioteca_libros:
            print("{} ({}) - ISBN: {} - Disponible:  {}\n".format(libro.titulo, libro.autor, libro.isbn, libro.disponible))
    
    def buscar(self):
        pass

def get_libro_por_isbn(isbn):
    for libro in biblioteca_libros:
        if libro.isbn == isbn:
            return libro
    
    return None

def gestion_inventario():

    seguir = "SI"

    texto_menu = "Bienvenido al Sistema de Gestión de Biblioteca\n\n"
    linea_agregar = "1. Agregar libro\n"
    linea_prestar = "2. Prestar libro\n"
    linea_devolver = "3. Devolver libro\n"
    linea_mostrar = "4. Mostrar libros\n"
    linea_buscar = "5. Buscar\n"
    linea_salir = "6. Salir\n\n"
    linea_elegir_opcion = "Elige una opción:" 

    print (texto_menu + linea_agregar + linea_prestar + linea_devolver + linea_mostrar + linea_buscar + linea_salir)

    while seguir == "SI":
        entrada_usuario = input(linea_elegir_opcion)

        if entrada_usuario == "6":
            print("Salimos de la aplicación")
            seguir = "NO"
        # AGREGAR UN LIBRO
        elif entrada_usuario == "1":
            titulo = input("Título:")
            autor = input ("Autor:")
            isbn = input("ISBN:")

            #Comprobamos que no exista ya ese libro
            libro = get_libro_por_isbn(isbn)

            if not libro is None:
                print ("Ya existía el libro con ISDN:{} en el catálogo".format(libro.isdn))
            else:
            #Lo añadimos
                libro = Libro(titulo,autor,isbn,True)
                biblioteca_libros.append(libro)
                print("Libro agregado con éxito.")
        # PRESTAR UN LIBRO
        elif entrada_usuario == "2":
            pass
        # DEVOLVER UN LIBRO
        elif entrada_usuario == "3":
            pass
        # MOSTRAR TODOS LOS LIBROS
        elif entrada_usuario == "4":
            


        # BUSCAR UN LIBRO
        elif entrada_usuario == "5":
            pass
        # ENTRADAS NO VÁLIDAS
        else:
            print("Los valores válidos son de 1,2,3,4,5 y 6 para Salir")


gestion_inventario()
