import sys
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog
from PyQt5.QtGui import QPixmap
from ventana import Ventana
from app import *

archivo = ''
class VentanMain(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ventana()
        self.ui.setupUi(self)
        
        self.ui.btnCargar.clicked.connect(self.openFile)
        self.ui.btnAnalizar.clicked.connect(self.analizar)
        self.ui.btnReportes.clicked.connect(self.reportes)
        self.ui.btnOriginal.clicked.connect(self.original)
        self.ui.btnMirrorY.clicked.connect(self.mirrorY)
        self.ui.btnMirrorX.clicked.connect(self.mirrorX)                        
        self.ui.btnDblMirror.clicked.connect(self.doubleMirror)
        self.ui.btnCrear.clicked.connect(self.crearImagenes) 
        self.ui.btnSalir.clicked.connect(self.close)
        self.ui.comboBox.currentTextChanged.connect(self.prueba)
        
            
        self.show()
    
    def prueba(self,text):
        try:
            
            self.ui.visor.setStyleSheet(f"background-image:url(imagenes/{text}.png);border:2px solid black;background-attachment:scroll")
        except:
            print('salto')
    def original(self):
        crearHTML()
        
        
        self.ui.comboBox.clear()
        for i in listaTablas:
            self.ui.comboBox.addItem(i[0])
            
        self.ui.visor.setText('Todos los Filtros Creados')
        
    
    def mirrorX(self):
        crearHTMLmirrorX()
        self.ui.comboBox.clear()
        
        for i in listaTablas:
            self.ui.comboBox.addItem(i[0])
            
        self.ui.visor.setText('Mirror X Creado')
    
    def mirrorY(self):
        crearHTMLmirrorY()
        self.ui.comboBox.clear()
        
        for i in listaTablas:
            self.ui.comboBox.addItem(i[0])
            
        self.ui.visor.setText('Mirror Y Creado')
    
    def doubleMirror(self):
        crearHTMLdoublemirror()
        
        self.ui.comboBox.clear()
        for i in listaTablas:
            self.ui.comboBox.addItem(i[0])
         
        self.ui.visor.setText('Double Mirror Creado')
    def reportes(self):
        crearReporteTokens()
        crearReporteErrores
        self.ui.visor.setText('Reportes Creados')
        
        
    
    def crearImagenes(self):
        crearGraphviz()
        self.ui.visor.setText('Imagenes Creadas')
        
    def analizar(self):
        global archivo
        
        crearMatriz(archivo)
        global listaTablas
        
        self.ui.visor.setText('ARCHIVO ANALIZADO')
        
    def openFile(self):
        global archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename,_ = QFileDialog.getOpenFileName(self,'QFileDialog.getOpenFileName()',"","All Files(*);PXLA (*.pxla)",options=options)
        if filename:
            archivo = filename
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = VentanMain()
    dialogo.show()
    sys.exit(app.exec_())