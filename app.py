from AnalizadorLexico import AnalizadorLexico
from GeneradorMatriz import Matriz,pixel
import os
from os import system
objetosMatriz = []
titulo = ''
ancho = ''
alto = ''
filas = ''
columnas = ''
pixeles = []
scanner = AnalizadorLexico()

def leerArchivo(ruta):
    archivo = open(ruta,'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def crearReporteTokens():
    global scanner
    
    html='''   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border=1>
    <tr><td>LEXEMA</td><td>TIPO</td><td>FILA</td><td>COLUMNA</td></tr>
    '''
    for i in scanner.listaTokens:
        html+=f'<tr><td>{i.lexema}</td><td>{i.tipo}</td><td>{i.linea}</td><td>{i.columna}</td></tr>'
    html+='</table></body>\n</html>'
    
    file = open('Tokens.html','w')
    file.write(html)
    file.close()
def crearReporteErrores():
    global scanner
    
    html='''   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border=1>
    <tr><td>DESCRIPCION</td><td>TIPO</td><td>FILA</td><td>COLUMNA</td></tr>
    '''
    for i in scanner.listaErrores:
        html+=f'<tr><td>{i.descripcion}</td><td>{i.tipo}</td><td>{i.linea}</td><td>{i.columna}</td></tr>'
    html+='</table></body>\n</html>'
    
    file = open('Errores.html','w')
    file.write(html)
    file.close()
    
    
def crearMatriz(ruta):
    global scanner
    codigo_fuente = leerArchivo(ruta)
    
    
    scanner.analizar(codigo_fuente)
    listaMatrices = []
    separadores = []
    
    global objetosMatriz
    try:
        for i in scanner.listaTokens:
            if i.lexema == '@@@@':
                separadores.append(scanner.listaTokens.index(i))

        
        listaMatrices.append(scanner.listaTokens[0:separadores[0]])
    except:
        listaMatrices.append(scanner.listaTokens[0:])
    for i in separadores:
        if separadores.index(i)==len(separadores)-1:
            listaMatrices.append(scanner.listaTokens[i:])    
        else:
            listaMatrices.append(scanner.listaTokens[i:separadores[separadores.index(i)+1]])

    for matriz in listaMatrices:
        
        global titulo,ancho,alto,pixeles,filas,columnas
        inFiltroA = ''
        inFiltroB = ''
        for lexema in matriz:
            global titulo,ancho,alto,pixeles,filas,columnas,filtros
            
            
            if lexema.lexema == 'TITULO':
                index = matriz.index(lexema)
                titulo = matriz[index+3].lexema
            elif lexema.lexema == 'ANCHO':
                index = matriz.index(lexema)
                ancho = matriz[index+2].lexema
                
            elif lexema.lexema == 'ALTO':
                index = matriz.index(lexema)
                alto = matriz[index+2].lexema
            elif lexema.lexema == 'FILAS':
                index = matriz.index(lexema)
                filas= matriz[index+2].lexema
            elif lexema.lexema == 'COLUMNAS':
                index = matriz.index(lexema)
                columnas= matriz[index+2].lexema
            
            elif lexema.lexema == 'FILTROS':
                index = matriz.index(lexema)
                filtros=[ matriz[index+2].lexema.upper(),matriz[index+4].lexema.upper(),matriz[index+6].lexema.upper()]


            
            elif lexema.lexema == 'CELDAS':
                indexA = ''
                
                
                for i in matriz:
                   
                    if i.lexema == '[':
                        indexA = matriz.index(i)
                        posX = matriz[indexA+1].lexema
                        posY = matriz[indexA+3].lexema
                        bool = matriz[indexA+5].lexema
                        color = matriz[indexA+7].lexema
                        anc = int(ancho)/int(columnas)
                        alt = int(alto)/int(columnas)
                        p = pixel(int(posX),int(posY),bool,color,anc,alt)
                        
                        
                        pixeles.append(p)
                    
                        
                    
        newMatriz = Matriz(titulo,ancho,alto,filas,columnas,filtros)
        newMatriz.listaPixeles = sorted(pixeles,key=lambda pix:pix.posicionY)
        pixeles = []
        
        objetosMatriz.append(newMatriz)
listaTablas = []   

   
def crearHTML():
    global listaTablas
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    '''
    
    for i in objetosMatriz:
        x = 0
        y = 0
        ancho = int(i.ancho)
        alto = int(i.alto)
        filas = int(i.filas)
        columnas = int(i.columnas)
        if 'MIRRORX' in i.filtros:
            crearHTMLmirrorX()
        if 'MIRRORY' in i.filtros:
            crearHTMLmirrorY()
        if 'DOUBLEMIRROR' in i.filtros:
            crearHTMLdoublemirror()
        
        
        table = f'''<table border = "1" width = "{ancho}px" height = "{alto}px" cellspacing="0">
        '''
        
        pixeles = i.listaPixeles
        
        pixelAncho = ancho/columnas
        pixelAlto = alto/filas
        
        for a in range(columnas):
            table+='''<tr>\n'''
            for b in range(filas):
                fila = b
                columna =a
                color = 'white'
                for p in pixeles:
                    if p.posicionX ==columna and p.posicionY==fila:
                        if p.bool =='TRUE':
                            color = p.color
                table+=f'''<td id="{columna,fila}" width = "{pixelAlto}px" height="{pixelAncho}px" bgcolor = "{color}"></td>\n'''                         
            table+='</tr>\n'
                
            
        table+="</table>\n"
        html +=table
        listaTablas.append([i.titulo,table])
      
    html +='''</body>
    </html>'''
    
    archivo = open('tablas.html','w')
    archivo.write(html)
    archivo.close()
    
def crearHTMLmirrorX():
    global listaTablas
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    '''
    
    for i in objetosMatriz:
        x = 0
        y = 0
        ancho = int(i.ancho)
        alto = int(i.alto)
        filas = int(i.filas)
        columnas = int(i.columnas)
        
        
        table = f'''<table border = "1" width = "{ancho}px" height = "{alto}px" cellspacing="0">
        '''
        
        pixeles = i.listaPixeles
        
        pixelAncho = ancho/columnas
        pixelAlto = alto/filas
        
        for a in (range(columnas)):
            table+='''<tr>\n'''
            for b in reversed(range(filas)):
                fila = b
                columna =a
                color = 'white'
                for p in pixeles:
                    if p.posicionY ==fila and p.posicionX==columna:
                        if p.bool =='TRUE':
                            color = p.color
                table+=f'''<td id="{columna,fila}" width = "{pixelAlto}px" height="{pixelAncho}px" bgcolor = "{color}"></td>\n'''                         
            table+='</tr>\n'
                
            
        table+="</table>\n"
        html +=table
        listaTablas.append([i.titulo+'mirrorX',table])
      
    html +='''</body>
    </html>'''
    
    archivo = open('tablasMirrorX.html','w')
    archivo.write(html)
    archivo.close()
    
def crearHTMLmirrorY():
    global listaTablas
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    '''
    
    for i in objetosMatriz:
        x = 0
        y = 0
        ancho = int(i.ancho)
        alto = int(i.alto)
        filas = int(i.filas)
        columnas = int(i.columnas)
        
        
        table = f'''<table border = "1" width = "{ancho}px" height = "{alto}px" cellspacing="0">
        '''
        
        pixeles = i.listaPixeles
        
        pixelAncho = ancho/columnas
        pixelAlto = alto/filas
        
        for a in reversed(range(columnas)):
            table+='''<tr>\n'''
            for b in (range(filas)):
                fila = b
                columna =a
                color = 'white'
                for p in pixeles:
                    if p.posicionY ==fila and p.posicionX==columna:
                        if p.bool =='TRUE':
                            color = p.color
                table+=f'''<td id="{columna,fila}" width = "{pixelAlto}px" height="{pixelAncho}px" bgcolor = "{color}"></td>\n'''                         
            table+='</tr>\n'
                
            
        table+="</table>\n"
        html +=table
        listaTablas.append([i.titulo+'mirrorY',table])
      
    html +='''</body>
    </html>'''
    
    archivo = open('tablasMirrorY.html','w')
    archivo.write(html)
    archivo.close()
def limpiarTablas():
    global listaTablas
    listaTablas = []
def crearHTMLdoublemirror():
    global listaTablas
    
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    '''
    
    for i in objetosMatriz:
        x = 0
        y = 0
        ancho = int(i.ancho)
        alto = int(i.alto)
        filas = int(i.filas)
        columnas = int(i.columnas)
        
        
        table = f'''<table border = "1" width = "{ancho}px" height = "{alto}px" cellspacing="0">
        '''
        
        pixeles = i.listaPixeles
        
        pixelAncho = ancho/columnas
        pixelAlto = alto/filas
        
        for a in reversed(range(columnas)):
            table+='''<tr>\n'''
            for b in reversed(range(filas)):
                fila = b
                columna =a
                color = 'white'
                for p in pixeles:
                    if p.posicionY ==fila and p.posicionX==columna:
                        if p.bool =='TRUE':
                            color = p.color
                table+=f'''<td id="{columna,fila}" width = "{pixelAlto}px" height="{pixelAncho}px" bgcolor = "{color}"></td>\n'''                         
            table+='</tr>\n'
                
            
        table+="</table>\n"
        html +=table
        listaTablas.append([i.titulo+'Doublemirror',table])
      
    html +='''</body>
    </html>'''
    
    archivo = open('tablasDoublemirror.html','w')
    archivo.write(html)
    archivo.close()
    
def crearGraphviz():
    global listaTablas
    os.makedirs('imagenes',exist_ok=True)
    for i in listaTablas:
        graphviz = '''
        digraph G {bgcolor=none;
    node[ style = "filled" shape=plaintext margin =0 width=0 height=0] a[ label=<
        
        '''
        graphviz+=i[1]
        graphviz+='>];}'
        name = f'./imagenes/{i[0]}.'
        myFile = open(name+'dot','w')
        myFile.write(graphviz)
        myFile.close()
        system(f'dot -Tpng {name}dot -o {name}png')
        


if __name__ == '__main__':
    crearMatriz('proyecto1.pxla')
    crearHTML()
    crearGraphviz()
    
    
    