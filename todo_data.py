# Lista de imports modulos y variables
import xml.etree.ElementTree as ET
from defusedxml.ElementTree import parse
from pathlib import Path
from constantes import DATA_FILENAME


"""
Notes:
    Using xml.etree.ElementTree to parse untrusted XML data is known to be
    vulnerable to XML attacks. Replace xml.etree.ElementTree with the
    equivalent defusedxml package, or make sure defusedxml.defuse_stdlib()
    is called.
"""


class todo_data:

    def __init__(self):
        todo_file = Path(DATA_FILENAME)
        if not todo_file.is_file():
            print("Creando el archivo principal... ")
            self.create_demo_file()

        self.read_xml_file()

    def read_xml_file(self):
        """ Leemos el archivo con el modulo ElementTree """
        self.data = parse(DATA_FILENAME)

    def save_demo_xml_file(self, data):
        """
        Guardar una estructura en un archivo
        Abrimos el archivo en binario porque es como funciona el modulo
        """
        mydata = ET.tostring(data)
        myfile = open(DATA_FILENAME, "wb")
        myfile.write(mydata)

    def save_xml_file(self):
        """ Guardar una estructura en un archivo """
        root = self.data.getroot()
        mydata = ET.tostring(root)
        myfile = open(DATA_FILENAME, "wb")
        myfile.write(mydata)

    def print_data(self):
        """ Mostramos la informacion de una forma clara """
        root = self.data.getroot()

        # Mostrar atributos del objeto
        # for elem in root:
        #     print(elem.attrib)

        # Mostramos todos los items
        for x, elem in enumerate(root):
            if elem.attrib['done'] == 'False':
                print(str(x + 1) + '. [ ] ' + elem.text)
            else:
                print(str(x + 1) + '. [x] ' + elem.text)

    def create_demo_file(self):
        # Crear la estructura
        data = ET.Element('data')

        # Crear los elementos
        item1 = ET.SubElement(data, 'item')
        item2 = ET.SubElement(data, 'item')

        # Agregar atributos a los elementos
        item1.set('done', 'False')
        item2.set('done', 'False')

        # Agregar texto a los elementos
        item1.text = 'Una tarea'
        item2.text = 'Otra tarea'

        self.save_demo_xml_file(data)

    def agregar_tarea(self, texto_tarea):
        root = self.data.getroot()
        item1 = ET.SubElement(root, 'item')
        item1.set('done', 'False')
        item1.text = texto_tarea

    def completar_tarea(self, indice_tarea):
        """
        Accede al objeto root y modifica el atributo
        done de un elemento, poniendolo en True
        """
        root = self.data.getroot()
        for index, elem in enumerate(root.iter('item')):
            if index == indice_tarea:
                elem.set('done', 'True')
