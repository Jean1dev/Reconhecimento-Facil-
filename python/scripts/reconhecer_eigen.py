import cv2

def getName(tnId):
    if tnId == 1:
        return 'jean' 
    elif tnId == 2:
        return 'desconhecido'

path = "/Users/jeanfernandes/Documents/git/Py_facial/source/scripts/"
file = "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(path + file)
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read(path + 'classificadorEigen.yml')

largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

while(True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectados = detector.detectMultiScale(imagemCinza,
                                                 scaleFactor = 1.5,
                                                 minSize = (30, 30))

    for(x, y, l, a) in facesDetectados:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        cv2.rectangle(imagem, (x, y), (x +l, y + a), (0, 0, 255), 2)
        id, confianca = reconhecedor.predict(imagemFace)
        cv2.putText(imagem, getName(id), (x, y + (a + 30)), font, 2, (0, 0, 255))                                        


    cv2.imshow('Face', imagem)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
