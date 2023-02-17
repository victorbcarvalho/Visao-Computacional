import cv2 # OpenCV

def imshow(window_name, imagem):
    cv2.imshow(window_name, imagem)
    cv2.waitKey(0)

window_name = 'image'

imagem = cv2.imread('../Images/people1.jpg')
# diminuindo o tamanho da imagem
imagem = cv2.resize(imagem, (800,600))
# Convertendo para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Detecção de faces
detector_faces = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml') # O openCV já disponibiliza um modelo treinado
deteccoes = detector_faces.detectMultiScale(imagem_cinza, scaleFactor=1.09) # cada linha indica uma face identificada
for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 5)
imshow(window_name, imagem)