from colorImage import *
import cv2

if __name__ == '__main__':
    path = input("Ingrese la ruta de la imagen con la que desea trabajar: ")  #Se pide al usuario ingresar path de imagen a trabajar.
    
    #Llaman a las funciones respectivas para realizar los procesos indicados.
    ejercicio = colorImage(path)
    ejercicio.displayProperties()
    ejercicio.makeGray()
    ejercicio.colorizeRGB('red')     #Se asigna red para que la imagen obtenida sea rojiza. 
    ejercicio.makeHue()                                                      
