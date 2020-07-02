import os
import inspect
from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
    print('cleaning...')
    for feature in layer.getFeatures():
        value = str(feature[field_to_clean]).replace('á', 'a')
        value = str(feature[field_to_clean]).replace('Á', 'A')
        value = str(feature[field_to_clean]).replace('â', 'a')
        value = str(feature[field_to_clean]).replace('Â', 'A')
        value = str(feature[field_to_clean]).replace('à', 'a')
        value = str(feature[field_to_clean]).replace('À', 'A')
        value = str(feature[field_to_clean]).replace('å', 'a')
        value = str(feature[field_to_clean]).replace('Å', 'A')
        value = str(feature[field_to_clean]).replace('ã', 'a')
        value = str(feature[field_to_clean]).replace('Ã', 'A')
        value = str(feature[field_to_clean]).replace('ä', 'a')
        value = str(feature[field_to_clean]).replace('Ä', 'A')
        value = str(feature[field_to_clean]).replace('æ', 'ae')
        value = str(feature[field_to_clean]).replace('Æ', 'AE')
        value = str(feature[field_to_clean]).replace('ç', 'c')
        value = str(feature[field_to_clean]).replace('Ç', 'C')
        value = str(feature[field_to_clean]).replace('é', 'e')
        value = str(feature[field_to_clean]).replace('É', 'E')
        value = str(feature[field_to_clean]).replace('ê', 'e')
        value = str(feature[field_to_clean]).replace('Ê', 'E')
        value = str(feature[field_to_clean]).replace('è', 'e')
        value = str(feature[field_to_clean]).replace('È', 'E')
        value = str(feature[field_to_clean]).replace('ë', 'e')
        value = str(feature[field_to_clean]).replace('Ë', 'E')
        value = str(feature[field_to_clean]).replace('í', 'i')
        value = str(feature[field_to_clean]).replace('Í', 'I')
        value = str(feature[field_to_clean]).replace('î', 'i')
        value = str(feature[field_to_clean]).replace('Î', 'I')
        value = str(feature[field_to_clean]).replace('ì', 'i')
        value = str(feature[field_to_clean]).replace('Ì', 'I')
        value = str(feature[field_to_clean]).replace('ï', 'i')
        value = str(feature[field_to_clean]).replace('Ï', 'I')
        value = str(feature[field_to_clean]).replace('ñ', 'n')
        value = str(feature[field_to_clean]).replace('Ñ', 'N')
        value = str(feature[field_to_clean]).replace('ó', 'o')
        value = str(feature[field_to_clean]).replace('Ó', 'O')
        value = str(feature[field_to_clean]).replace('ô', 'o')
        value = str(feature[field_to_clean]).replace('Ô', 'O')
        value = str(feature[field_to_clean]).replace('ò', 'o')
        value = str(feature[field_to_clean]).replace('Ò', 'O')
        value = str(feature[field_to_clean]).replace('ø', 'o')
        value = str(feature[field_to_clean]).replace('Ø', 'O')
        value = str(feature[field_to_clean]).replace('õ', 'o')
        value = str(feature[field_to_clean]).replace('Õ', 'O')
        value = str(feature[field_to_clean]).replace('ö', 'o')
        value = str(feature[field_to_clean]).replace('Ö', 'O')
        value = str(feature[field_to_clean]).replace('œ', 'oe')
        value = str(feature[field_to_clean]).replace('Œ', 'OE')
        value = str(feature[field_to_clean]).replace('š', 's')
        value = str(feature[field_to_clean]).replace('Š', 'S')
        value = str(feature[field_to_clean]).replace('ß', 'ss')
        value = str(feature[field_to_clean]).replace('ð', 'o')
        value = str(feature[field_to_clean]).replace('ú', 'u')
        value = str(feature[field_to_clean]).replace('Ú', 'U')
        value = str(feature[field_to_clean]).replace('û', 'u')
        value = str(feature[field_to_clean]).replace('Û', 'U')
        value = str(feature[field_to_clean]).replace('ù', 'u')
        value = str(feature[field_to_clean]).replace('Ù', 'U')
        value = str(feature[field_to_clean]).replace('ü', 'u')
        value = str(feature[field_to_clean]).replace('Ü', 'U')
        value = str(feature[field_to_clean]).replace('ý', 'y')
        value = str(feature[field_to_clean]).replace('Ý', 'Y')
        value = str(feature[field_to_clean]).replace('ÿ', 'y')
        value = str(feature[field_to_clean]).replace('Ÿ', 'Y')
        with edit(layer):
            feature.setAttribute(feature.fieldNameIndex(field_to_clean), value)
            layer.updateFeature(feature)
    print('cleaned!')
