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
        self.clean_one = QPushButton("Un champ")
        self.clean_all = QPushButton("Tous les champs")

        # Connect radio buttons to our functions
        self.clean_one.clicked.connect(self.nettoyer_un)
        self.clean_all.clicked.connect(self.nettoyer_tous)

        #Add the widgets to the layout:
        self.layout.addWidget(self.clean_one)
        self.layout.addWidget(self.clean_all)

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
        
    def nettoyer_un(self, on):
        print('un')
        self.iface = iface
        layer = iface.activeLayer()
        
        items = ([field.name() for field in layer.fields()])
        item, ok = QInputDialog.getItem(self, "Choisissez un champ", 
                 "Liste des champs", items, 0, False) # get field to delete with selector
        if ok and item:
            field_to_clean = item
            self.close()
            print(field_to_clean)
            cleaning_one(field_to_clean, layer)
            
    def nettoyer_tous(self, on):
        print('tous')
        self.iface = iface
        layer = iface.activeLayer()
        all_fields = layer.fields()
        fields_to_clean = [field.name() for field in all_fields]
        self.close()
        cleaning_all(fields_to_clean, layer)
        
clean = cleaner()
clean.show()


def cleaning_one(field_to_clean, layer):
    layer = iface.activeLayer()

    print('cleaning one field...')  
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
            value = value.replace('Â©', '©')
            #print(value)
            feature.setAttribute(feature.fieldNameIndex(field_to_clean), value)        
            layer.updateFeature(feature)
    print('cleaned!')
    
def cleaning_all(field_to_clean, layer):
    layer = iface.activeLayer()

    print('cleaning all fields...')  
    with edit (layer):
        prov = layer.dataProvider()
        for field_name in field_to_clean:
            print('cleaning ',field_name)
            for field in prov.fields():
                for feature in layer.getFeatures():
                    value = str(feature[field_name])
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
                    value = value.replace('Â©', '©')
                    #print(value)
                    feature.setAttribute(feature.fieldNameIndex(field_name), value)        
                    layer.updateFeature(feature)
            print('finished cleaning ', field_name)
    print('cleaned!')
