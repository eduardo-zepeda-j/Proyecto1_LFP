from Token import Token
from Error import Error
import re
palabrasReservadas = ['TITULO','ANCHO','ALTO','FILAS','COLUMNAS','CELDAS','TRUE','FALSE','TRUE','FILTROS','MIRRORX','MIRRORY','DOUBLEMIRROR']
class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        
    def impTokens(self):
        cadena = ''
        for i in self.listaTokens:
           cadena+=i.impToken()
           cadena+='\n'
        archivo = open('tokens.txt','w')
        archivo.write(cadena)
        archivo.close()
        
    
    def impErrorers(self):
        print(self.listaErrores)
        return self.listaErrores()
        
    def analizar(self,codigo_fuente):
        self.listaTokens= []
        self.listaErrores = []
        
        linea = 1
        columna = 1
        buffer = ''
        centinela = '$'
        estado = 0
        
        codigo_fuente+=centinela
        
        i = 0
        
        while i<len(codigo_fuente):
            c = codigo_fuente[i]
            if c == '\n':
                linea+=1
                columna = 1
                if estado == 20 or estado == 19:
                    estado =0
            
            elif c == '@':
                columna+=1
                buffer+=c
            elif buffer == '@@@@':
                
                self.listaTokens.append(Token(buffer,'separador',linea,columna))
                buffer = ''
                estado = 0
            elif estado == 0:
                if re.search('[a-zA-Z]',c):
                    buffer+=c
                    columna+=1
                    estado = 1
            elif estado == 1:
                if re.search('[a-zA-Z0-9]',c):
                    buffer+=c
                    columna+=1
                    estado=1
                elif c == '=':
                    self.listaTokens.append(Token(buffer,'palabra_reservada',linea,columna-len(buffer)))
                    buffer=''
                    
                    self.listaTokens.append(Token(c,'igual',linea,columna))
                    columna+=1
                    
                    estado=2
            elif estado ==2:
                if re.search('[0-9]',c):
                    buffer+=c
                    columna+=1
                    estado=5
                
                elif re.search('[a-zA-Z]',c):
                    buffer+=c
                    columna+=1
                    estado=4
                
                elif re.search('"',c):
                    buffer+=c
                    
                    self.listaTokens.append(Token(buffer,'comillaA',linea,columna))
                    columna+=1
                    buffer=''
                    
                    estado = 3
                
                elif re.search('{',c):
                    buffer+=c
                    self.listaTokens.append(Token(buffer,'llaveA',linea,columna))
                    buffer=''
                    columna+=1
                    estado = 6
                
            elif estado ==5:
                if re.search('[0-9]',c):
                    buffer+=c
                    columna+=1
                    estado=5
                    
                elif c == ';':
                    self.listaTokens.append(Token(buffer,'entero',linea,columna-len(buffer)))
                    buffer = ''
                    
                    self.listaTokens.append(Token(c,'punto_coma',linea,columna))
                    columna+=1
                    estado = 0
            elif estado == 4:
                if re.search('[a-zA-Z]',c):
                    buffer+=c
                    columna+=1
                    estado = 4
                elif c == ';':
                    self.listaTokens.append(Token(buffer,'filtro',linea,columna-len(buffer)))
                    buffer = ''
                    
                    self.listaTokens.append(Token(c,'punto_coma',linea,columna))
                    columna+=1
                    estado = 8
                elif c == ',':
                    self.listaTokens.append(Token(buffer,'filtro',linea,columna-len(buffer)))
                    buffer = ''
                    
                    self.listaTokens.append(Token(c,'coma',linea,columna))
                    columna+=1
                    estado = 4
            
            elif estado == 8:
                if c == '$':
                    print('la cadena se ha aceptado')
            
            elif estado == 3:
                
                if re.search('[a-zA-Z0-9]',c):
                    buffer+=c 
                    columna+=1
                    estado = 7
            elif estado == 7:
                if re.search('[a-zA-Z0-9]',c):
                    buffer+=c
                    columna+=1
                    estado = 7
                elif c == '"':
                    self.listaTokens.append(Token(buffer,'cadena',linea,columna-len(buffer)))
                    buffer = ''
                    
                    self.listaTokens.append(Token(c,'comillaB',linea,columna))
                    columna+=1
                    estado = 20
            elif estado == 20:
                if c == ';':
                    self.listaTokens.append(Token(c,'punto_coma',linea,columna))
                    buffer = ''
                    columna+=1
                    estado = 0
            elif estado == 6:
                if c == '[':
                    buffer+=c
                    self.listaTokens.append(Token(buffer,'corcheteA',linea,columna))
                    buffer=''
                    columna+=1
                    estado = 9
            elif estado == 9:
                if re.search('[0-9]',c):
                    buffer+=c
                    columna+=1
                    estado =10
            elif estado ==10:
                if re.search('[0-9]',c):
                    buffer+=c
                    columna+=1
                    estado =10
                elif c ==',':
                    self.listaTokens.append(Token(buffer,'posicionX',linea,columna-len(buffer)))
                    buffer=''
                    
                    self.listaTokens.append(Token(c,'coma',linea,columna))
                    columna+=1
                    estado =11
            elif estado ==11:
                if re.search('[0-9]',c):
                    buffer+=c
                    columna+=1
                    estado =12
            elif estado ==12:
                if re.search('[0-9]',c):
                    buffer+=c
                    columna+=1
                    estado =12
                elif c ==',':
                    self.listaTokens.append(Token(buffer,'posicionY',linea,columna-len(buffer)))
                    buffer=''
                    
                    self.listaTokens.append(Token(c,'coma',linea,columna))
                    columna+=1
                    estado =13
                    
            
            elif estado ==13:
                if re.search('[a-zA-Z]',c):
                    buffer+=c
                    columna+=1
                    estado =14
                    
            elif estado ==14:
                if re.search('[a-zA-Z]',c):
                    buffer+=c
                    columna+=1
                    estado =14
                elif c ==',':
                    if buffer.upper() =='TRUE' or buffer.upper() == 'FALSE':
                        self.listaTokens.append(Token(buffer,'booleano',linea,columna-len(buffer)))
                        buffer=''
                        columna+=1
                        
                    else:
                        self.listaErrores.append(Token(buffer,'booleano',linea,columna-len(buffer)))
                        buffer = ''
                        
                    self.listaTokens.append(Token(c,'coma',linea,columna))
                    columna+=1
                    estado =15
            elif estado == 15:
                if c == '#':
                    buffer+=c
                    columna+=1
                    estado = 16
            elif estado==16:
                if re.search('[a-zA-Z0-9]',c):
                    buffer+=c
                    columna+=1
                    estado = 17
            
            elif estado==17:
                if re.search('[a-zA-Z0-9]',c):
                    buffer+=c
                    columna+=1
                    estado = 17
                
                elif c ==']':
                    self.listaTokens.append(Token(buffer,'color_hexadecimal',linea,columna-len(buffer)))
                    buffer=''
                    
                    self.listaTokens.append(Token(c,'corcheteB',linea,columna))
                    columna+=1
                    estado =18
            elif estado == 18:
                if c == ',':
                    self.listaTokens.append(Token(c,'coma',linea,columna))
                    buffer=''
                    columna+=1
                    estado = 6
                
                elif c == '}':
                    self.listaTokens.append(Token(c,'llaveB',linea,columna))
                    columna+=1
                    estado =1
            
            elif estado == 19:
                if c ==';':
                    self.listaTokens.append(Token(c,'punto_coma'))
                    columna+=1
                    estado =0
                
            
                
            
            i+=1
                    
                    
        