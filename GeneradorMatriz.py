class Matriz:

    def __init__(self,titulo,ancho,alto,filas,columnas,filtros):
        self.listaPixeles = []
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.titulo = titulo
        self.filtros = filtros
     
    
    
    
class pixel:
    def __init__(self,posicionX,posicionY,bool,color,ancho,alto):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.bool = bool
        