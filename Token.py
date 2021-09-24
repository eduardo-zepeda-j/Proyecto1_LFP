class Token:
    def __init__(self,lexema, tipo,linea,columna):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.linea = linea
    
    
    def impToken(self):
        return self.lexema+'   '+self.tipo+'   '+str(self.linea)+'   '+str(self.columna)
        
    def getLexema(self,lexema):
        return lexema
        