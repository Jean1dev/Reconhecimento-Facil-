import cv2
import numpy as np

path = "/Users/jeanfernandes/Documents/git/Py_facial/source/scripts/"
file = "haarcascade_frontalface_default.xml"
file_eye = "haarcascade-eye.xml"

classificador = cv2.CascadeClassifier(path + file)
classificadorOlhos = cv2.CascadeClassifier(path + file_eye)

camera = cv2.VideoCapture(0)
amostra = 1
numAmostras = 25
id = input("digite seu idenficador: ")
largura, altura = 220, 220
print("batendo as fotos..........")

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    print(np.average(imagemCinza))
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor = 1.5,
                                                     minSize = (250, 250))
 
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiaoCinza = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinza)

        for(ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            if 0xFF: #cv2.waitKey(1) & 0xFF == ord('q'): # sempre que aperta `q` cai aki
                if np.average(imagemCinza) > 90:
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite(path + "fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
                    print("foto tirado" + str(amostra))
                    amostra += 1

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
    if(amostra >= numAmostras + 1):
        break
 
print("Finalizado") 
camera.release()
cv2.destroyAllWindows()

def prees_any_key(lkey):
    if(lkey == False):
        return (0xFF)
