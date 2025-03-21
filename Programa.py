#Práctica Fin de Curso: SISTEMA DE GESTIÓN DE BIBLIOTECA

#Variables globales. ESTO ES ERRONEO; debería estar dentro de la clase Biblioteca pero la tengo que poner global para que se pueda acceder desde
#la clase libro para poder omplementar los métodos mostrar y buscar
biblioteca_libros = []

#Clase Libros ------------------------------------------------
# ------------------------------------------------------------

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
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def mostrar(self):
        for libro in biblioteca_libros:
            print("{} ({}) - ISBN: {} - Disponible:  {}\n".format(libro.titulo, libro.autor, libro.isbn, libro.disponible))
    
    def buscar(self, isbn: str):
        for libro in biblioteca_libros:
            if libro.isbn == isbn:
                return str(libro)

    def __str__(self):
        return "Título: {}; Autor: {}; isbn:{}; Disponible:{}".format(self.titulo, self.autor, self.isbn, "Sí" if self.disponible else "No") 
    
#Clase Libros ------------------------------------------------
# ------------------------------------------------------------

#Clase biblioteca --------------------------------------------
# ------------------------------------------------------------
class Biblioteca:

    def __init__(self):
        pass

    def getLibro(self, isbn: str):
        for libro in biblioteca_libros:
            if libro.isbn == isbn:
                return libro
        return None
    
    def existsLibro(self, isbn: str):
        for libro in biblioteca_libros:
            if libro.isbn == isbn:
                return True
        return False
    
    def addLibro(self, titulo: str, autor: str, isbn:str):
        #Comprobamos que no exista
        if self.existsLibro(isbn):
            return "Ya existía el libro con ISDN:{} en el catálogo".format(isbn)
        else:
            biblioteca_libros.append(Libro(titulo,autor,isbn,True))
            return "Libro agregado con éxito."
        
    def prestarLibro(self, isbn: str):
        libro = self.getLibro(isbn)

        if libro is not None:
            if libro.disponible:
                libro.prestar()
                return "Libro prestado con éxito"
            else:
                return "Este libro se encuentra actualmente prestado"
        else:
            return "El libro de ISBN:{} no esiste".format(isbn)
        
    def devolverLibro(self, isbn: str):
        libro = self.getLibro(isbn)

        if libro is not None:
            if not libro.disponible:
                libro.devolver()
                return "Libro devuelto con éxito"
            else:
                return "Este libro no estaba prestado anteriormente"
        else:
            return "El libro de ISBN:{} no esiste".format(isbn)
        
    def mostrarLibros(self):
        lista_libros = ""
        for libro in biblioteca_libros:
                lista_libros = str(libro) + "\n"
        
        return lista_libros

#Clase biblioteca --------------------------------------------
# ------------------------------------------------------------

def gestion_inventario():

    biblioteca = Biblioteca()

    seguir = "SI"

    texto_menu = "Bienvenido al Sistema de Gestión de Biblioteca\n\n"
    linea_agregar = "1. Agregar libro\n"
    linea_prestar = "2. Prestar libro\n"
    linea_devolver = "3. Devolver libro\n"
    linea_mostrar = "4. Mostrar libros\n"
    linea_buscar = "5. Buscar\n"
    linea_salir = "6. Salir\n\n"
    linea_elegir_opcion = "Elige una opción: " 

    print (texto_menu + linea_agregar + linea_prestar + linea_devolver + linea_mostrar + linea_buscar + linea_salir)

    while seguir == "SI":
        entrada_usuario = input(linea_elegir_opcion)

        if entrada_usuario == "6":
            print(f"Salimos de la aplicación")
            seguir = "NO"
        # AGREGAR UN LIBRO
        elif entrada_usuario == "1":
            titulo = input("Título: ")
            autor = input ("Autor: ")
            isbn = input("ISBN: ")

            print(biblioteca.addLibro(titulo,autor,isbn))
        # PRESTAR UN LIBRO
        elif entrada_usuario == "2":
            isbn = input("Introduce el ISBN del libro: ")

            print(biblioteca.prestarLibro(isbn))
        # DEVOLVER UN LIBRO
        elif entrada_usuario == "3":
            isbn = input("Introduce el ISBN del libro: ")

            print(biblioteca.prestarLibro(isbn))
        # MOSTRAR TODOS LOS LIBROS
        elif entrada_usuario == "4":
            print(biblioteca.mostrarLibros())
        # BUSCAR UN LIBRO
        elif entrada_usuario == "5":
            isbn = input("Introduce el ISBN del libro: ")
            libro_encontrado = biblioteca.getLibro(isbn)

            if libro_encontrado is not None:
                print(str(libro_encontrado))
            else:
                print ("Libro no encontrado en la biblioteca")
        # ENTRADAS NO VÁLIDAS
        else:
            print("Los valores válidos son de 1,2,3,4,5 y 6 para Salir")


gestion_inventario()
