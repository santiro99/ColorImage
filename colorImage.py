import cv2
import numpy as np

class colorImage:
    def __init__(self, path):                         #Consctructor de la clase, con parámetro de entrada: path de la imagen.
        self.path = path                              #Guarda el path en self.
        self.image = cv2.imread(self.path)            #Lee la imagen ubicada en el path y la almacena en una variable en self.
        self.imageColorize = cv2.imread(self.path)    #Lee la imagen ubicada en el path y la almacena en una variable en self, específicamente para colorizeRGB

    def displayProperties(self):
        self.propiedades = self.image.shape                                #Extrae el alto, ancho y canales de la imagen. Almacena datos en la variable propiedades.
        height = self.propiedades[0]                                       #Guarda en la variable height el alto de la imagen.
        width = self.propiedades[1]                                        #Guarda en la variable width el ancho de la imagen.
        print("El alto de la foto es", height,", y el ancho es", width)    #Muestra el alto y el ancho de la imagen.

    def makeGray(self):
        grises = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)    #Cambia la imagen original a escala de grises y la guarda en una variable.
        cv2.imshow("Grises", grises)                             #Muestra la imagen en escala de grises.
        cv2.waitKey(0)

    def colorizeRGB(self, color):
        canales_zeros = np.zeros(self.propiedades)                                                 #Crea matriz de ceros del mismo tamaño y dimensiones de la imagen que se trabaja
        if color == 'red':                                                                         #En caso de que la entrada al método sea red, realiza el proceso de imagen rojiza.
            canal_rojo = self.image[:, :, 2]                                                       #Se extrae el canal rojo de la imagen original
            canales_zeros[:, :, 2] = canal_rojo                                                    #En el canal rojo de la matriz de ceros, se asigna el canal rojo de la imagen original
            cv2.imwrite("/Users/santiagorojasjaramillo/Downloads/Red_image.png", canales_zeros)    #Guarda la imagen roja en el path indicado
            rojiza = cv2.imread('/Users/santiagorojasjaramillo/Downloads/Red_image.png')           #Lee la imagen guardada y la almacena en la variable rojiza.
            cv2.imshow('Imagen_Rojiza', rojiza)                                                    #Muestra la imagen rojiza.
            cv2.waitKey(0)

        if color == 'green':                                                                       #Realiza el mismo proceso del color rojo pero con verde.
            canal_verde = self.image[:, :, 1]
            canales_zeros[:, :, 1] = canal_verde
            cv2.imwrite("/Users/santiagorojasjaramillo/Downloads/Green_image.png", canales_zeros)
            verdoza = cv2.imread('/Users/santiagorojasjaramillo/Downloads/Green_image.png')
            cv2.imshow('Imagen_Verdoza', verdoza)
            cv2.waitKey(0)

        if color == 'blue':                                                                        ##Realiza el mismo proceso del color rojo pero con azul.
            canal_azul = self.image[:, :, 0]
            canales_zeros[:, :, 0] = canal_azul
            cv2.imwrite("/Users/santiagorojasjaramillo/Downloads/Blue_image.png", canales_zeros)
            azuloza = cv2.imread('/Users/santiagorojasjaramillo/Downloads/Blue_image.png')
            cv2.imshow('Imagen_Azuloza', azuloza)
            cv2.waitKey(0)

    def makeHue(self):
        HSV = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)         #Cambia espacio de color de la imagen, pasa de RGB a HSV.
        HSV[1] = 255                                              #Componente S es fijada en 255 constante.
        HSV[2] = 255                                              #Componente V es fijada en 255 constante
        BGR_again = cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)   #Devuelve la imagen a espacio de color RGB y la guarda en variable.
        cv2.imshow('Hue', BGR_again)                              #Muestra imagen modificada en espacio RGB.                     
        cv2.waitKey(0)
