import os
import inspect
from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]      

class cleaner(QWidget):
    def __init__(self, parent=None):
        self.iface = iface
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()

        # Add the radio buttons
        self.open_clean = QPushButton("Nettoyer")

        # Connect radio buttons to our functions
        self.open_clean.clicked.connect(self.nettoyer)

        #Add the widgets to the layout:
        self.layout.addWidget(self.open_clean)

        #Set the layout:
        self.setLayout(self.layout)  
        self.setWindowTitle("Nettoyer les caractères spéciaux")
        
            
    def initGui(self):
      icon = os.path.join(os.path.join(cmd_folder, 'logo.jpg'))
      self.action = QAction(QIcon(icon), 'Cleaner', self.iface.mainWindow())
      self.action.triggered.connect(self.run)
      self.iface.addPluginToMenu('&Cleaner', self.action)
      self.iface.addToolBarIcon(self.action)

    def unload(self):
      self.iface.removeToolBarIcon(self.action)
      self.iface.removePluginMenu('Cleaner', self.action)  
      del self.action
        
    def run(self):        
        clean.show()
        clean.activateWindow() ## met le widget au premier plan
        
    def nettoyer(self, on):
        self.iface = iface
        layer = iface.activeLayer()
        
        items = ([field.name() for field in layer.fields()])
        item, ok = QInputDialog.getItem(self, "Choisissez un champ", 
                 "Liste des champs", items, 0, False) # get field to delete with selector
        if ok and item:
            field_name=item
            self.close()
            cleaning(field_name, layer)
        
clean = cleaner()

def cleaning(field_to_clean, layer):
    layer = iface.activeLayer()

    print('cleaning...')  
    with edit (layer):
        for feature in layer.getFeatures():
            value = str(feature[field_to_clean])
            value = value.replace('Å“', 'œ')
            value = value.replace("Å’", 'Œ')
            value = value.replace('Ã€', 'À')
            value = value.replace('Ã', 'Ã')
            value = value.replace('Ã†', 'Æ')
            value = value.replace('Ã‡', 'Ç')
            value = value.replace('Ãˆ', 'È')
            value = value.replace('Ã‰', 'É')
            value = value.replace('ÃŠ', 'Ê')
            value = value.replace('Ã‹', 'Ë')
            value = value.replace('Ã¢', 'â')
            value = value.replace('Ã¡', 'Ã')
            value = value.replace('Ã¢', 'â')
            value = value.replace('Ã¤', 'ä')
            value = value.replace('Ã¦', 'æ')
            value = value.replace('Ã¨', 'è')
            value = value.replace('Ãª', 'ê')
            value = value.replace('Ã«', 'ë')
            value = value.replace('Ã¬', 'ì')
            value = value.replace('Ã®', 'î')
            value = value.replace('Ã¹', 'ù')
            value = value.replace('Ãº', 'ú')
            value = value.replace('Ã»', 'û')
            value = value.replace('Ã§', 'ç')
            value = value.replace('Ã±', 'ñ')
            value = value.replace('Ã´', 'ô')
            value = value.replace('Ã²', 'ò')
            value = value.replace('Ã³', 'ó')
            value = value.replace('Ã©', 'é')
            value = value.replace('Ã©', 'é')
            #print(value)
            feature.setAttribute(feature.fieldNameIndex(field_to_clean), value)        
            layer.updateFeature(feature)
    print('cleaned!')

