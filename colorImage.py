import cv2

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
        imagenColorize = self.imageColorize
        if color == 'red':                                      # En caso de que la entrada al método sea red, realiza el proceso de imagen rojiza.
            imagenColorize[:, :, 1] = 0                         #Canal 1 (verde) es fijada en 0.
            imagenColorize[:, :, 0] = 0                         #Canal 0 (azul) es fijada en 0.
            cv2.imshow('Imagen_Rojiza', imagenColorize)         #Muestra la imagen rojiza.
            cv2.waitKey(0)

        if color == 'green':                                    #Realiza el mismo proceso del color rojo pero con verde.
            imagenColorize[:, :, 2] = 0
            imagenColorize[:, :, 0] = 0
            cv2.imshow('Imagen_Verdoza', imagenColorize)
            cv2.waitKey(0)

        if color == 'blue':                                     #Realiza el mismo proceso del color rojo pero con azul.
            imagenColorize[:, :, 2] = 0
            imagenColorize[:, :, 1] = 0
            cv2.imshow('Imagen_Azuloza', imagenColorize)
            cv2.waitKey(0)

    def makeHue(self):
        HSV = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)         #Cambia espacio de color de la imagen, pasa de RGB a HSV.
        HSV[1] = 255                                              #Componente S es fijada en 255 constante.
        HSV[2] = 255                                              #Componente V es fijada en 255 constante
        BGR_again = cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)   #Devuelve la imagen a espacio de color RGB y la guarda en variable.
        cv2.imshow('Hue', BGR_again)                              #Muestra imagen modificada en espacio RGB.
        cv2.waitKey(0)
