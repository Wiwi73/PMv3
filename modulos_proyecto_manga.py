class Manga:
    def __init__(self,  tomos, capitulos, nombre,precio=None ):
        self.precio = precio
        self.tomos = tomos
        self.capitulos = capitulos
        self.nombre = nombre
       

    def nombre_manga(self):
        self.nombre = input("Como se llama el manga?")
    def cant_caps(self):
        self.capitulos=int(input("Cuantos capitulos tiene actualmente?"))
    def cant_tomos (self):
        self.tomos=int(input("Cuantos tomos tenes?"))
    def valor (self):
        self.precio=int(input("Cual es el valor del tomo?"))
    def to_list(self):
        # Método que convierte el objeto en una lista
        return [self.nombre, self.capitulos, self.tomos, self.__class__.__name__, self.precio]
    
    def __str__(self):
        precio_info = f" con un precio de {self.precio}" if self.precio is not None else ""
        return f"Manga {self.nombre} con {self.tomos} tomos, {self.capitulos} capítulos{precio_info}"
        
class Takeboun (Manga):
    def __init__(self, precio, tomos, capitulos, nombre,):
        super().__init__(tomos, capitulos, nombre,precio)
        
     # Sobrescribimos __str__ para agregar el precio
    def __str__(self):
        # Llamamos a __str__ de la superclase para reutilizar la representación
        return f"{super().__str__()}"
   
    
class Recopilatorio(Manga):
    def __init__(self, precio, tomos, capitulos, nombre):
        # Llamamos al constructor de la clase base `Manga`
        super().__init__(tomos, capitulos, nombre, precio)

    def __str__(self):
        # Reutilizamos la representación de la clase base y añadimos información adicional
        return f"{super().__str__()}, Caps. Recopilados: {self.capitulos}."


class Online(Manga):
    def __init__(self, web, tomos, capitulos, nombre):
        super().__init__( tomos, capitulos, nombre)
        self.web = web
    
    def sitio(self):
        self.web = input("¿En qué página lo leíste?")

    def __str__(self):
        return f"{super().__str__()}, Leído en: {self.web}."
        
    
        
    
 
   