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

def direccion(x):
    if (x < centroX):
      return "Izquierda"
    else:
      return "Derecha"

def areaCuadrilateros(approx):
  x,y,w,h = cv2.boundingRect(approx)
  return w*h

def areaTriangulo(approx):
  x,y,w,h = cv2.boundingRect(approx)
  return (w*h)/2

def direccionATomar(image):
  global centroX
  global centroY
  global areaMasGrande
  centroX = image.shape[1]/2
  centroY = image.shape[0]/2
  areaMasGrande = 0

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  canny = cv2.Canny(gray, 10, 150)
  canny = cv2.dilate(canny, None, iterations = 1)
  canny = cv2.erode(canny, None, iterations = 1)
  cnts,herarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  for c in cnts:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 3:
      areaAux = areaTriangulo(approx)
      if (areaAux > areaMasGrande):
        areaMasGrande = areaAux

    elif len(approx) == 4:
      areaAux = areaCuadrilateros(approx)
      if (areaAux > areaMasGrande):
        areaMasGrande = areaAux

  for c in cnts:
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    if len(approx) == 3:
      areaAux = areaTriangulo(approx)
      if (areaAux/areaMasGrande) > 0.6 and grande:
        x,y = encontrarCentro(approx)
        return direccion(x)

      elif (areaAux/areaMasGrande) <= 0.6 and (areaAux/areaMasGrande) > 0.4 and mediano:
        x,y = encontrarCentro(approx)
        return direccion(x)

      elif (areaAux/areaMasGrande) <= 0.4 and pequeno:
        x,y = encontrarCentro(approx)
        return direccion(x)

    elif len(approx) == 4:
      areaAux = areaCuadrilateros(approx)
      if (areaAux/areaMasGrande) > 0.6 and grande:
        x,y = encontrarCentro(approx)
        return direccion(x)

      elif (areaAux/areaMasGrande) <= 0.6 and (areaAux/areaMasGrande) > 0.4 and mediano:
        x,y = encontrarCentro(approx)
        return direccion(x)

      elif (areaAux/areaMasGrande) <= 0.4 and pequeno:
        x,y = encontrarCentro(approx)
        return direccion(x)

  cv2_imshow(image)
  print("No encontrado")

  cv2.destroyAllWindows()


pequeno = True
mediano = False
grande = False
centroX = 0
centroY = 0
areaMasGrande = 0

image = cv2.imread("/content/drive/MyDrive/DeteccionDeFormas/AhoraSi.png")
direccionATomar(image)  