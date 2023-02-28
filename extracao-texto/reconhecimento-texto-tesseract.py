import pytesseract
import cv2

import sys

sys.path.append('H:/Users/basto/AppData/Local/Programs/Tesseract-OCR')
pytesseract.pytesseract.tesseract_cmd = 'H:/Users/basto/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

imagem = cv2.imread('H:/Users/basto/Documents/visao-computacional/Images/teste01.jpg')

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

texto = pytesseract.image_to_string(imagem)

print(texto)
janela = 'imagem'
cv2.imshow(janela, imagem)
cv2.waitKey(0)