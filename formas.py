import cv2
import math
from google.colab.patches import cv2_imshow

def encontrarCentro(approx):
  x,y,w,h = cv2.boundingRect(approx)
  return (x + w/2,y + h/2)


def esCuadrado(approx):
  x,y,w,h = cv2.boundingRect(approx)
  if (float(w)/h > 0.9 and float(w)/h < 1.1):
    return True
  else:
    return False

def decision(approx):
  x,y = encontrarCentro(approx)
  if (x < centroX):
    return "Izquierda"
  else:
    return "Derecha"

def direccionATomar(image):
  global centroX
  global centroY
  centroX = image.shape[1]/2
  centroY = image.shape[0]/2
  
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  canny = cv2.Canny(gray, 10, 150)
  canny = cv2.dilate(canny, None, iterations = 1)
  canny = cv2.erode(canny, None, iterations = 1)
  cnts,herarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  for c in cnts:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    if len(approx) == 3 and triangulo:
      return decision(approx)
    
    elif len(approx) == 4 and (rectangulo or cuadrado):
      if esCuadrado(approx) and cuadrado:
        return decision(approx)

      elif rectangulo:
        return decision(approx)

  print("No encontrado")

  cv2.destroyAllWindows()

triangulo = False
rectangulo = False
cuadrado = False
centroX = 0
centroY = 0

#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/CuadradoMedianoDerecha.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/CuadradoMedianoIzquierda.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/CuadradoPDerecha.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/CuadradoPIzquierda.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/CuaGDer.jpg")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/CuaGIzq.jpg")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/Original.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/U.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/TriMDe.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/TriMIz.png")
#image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/RecMIz.png")
image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/RecMDer.png")
direccionATomar(image)