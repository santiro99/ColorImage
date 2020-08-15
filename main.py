from colorImage import *
import cv2

def print_hi(name):
    print(f'Hi, {name}') 

if __name__ == '__main__':
    path = input("Ingrese la ruta de la imagen con la que desea trabajar: ")  #/Users/santiagorojasjaramillo/Downloads/lena.png
    ejercicio = colorImage(path)
    ejercicio.displayProperties()
    ejercicio.makeGray()
    ejercicio.colorizeRGB('red')
    ejercicio.makeHue()                                                       #Llama a las funciones respectivas para realizar 
