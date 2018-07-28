import cv2
 
path = "/Users/jeanfernandes/Documents/git/Py_facial/source/scripts/"
file = "haarcascade_frontalface_default.xml"

classificador = cv2.CascadeClassifier(path + file)
camera = cv2.VideoCapture(0)
amostra = 1
numAmostras = 25
id = input('digite seu idenficador: ')
largura, altura = 220, 220
print("batendo as fotos..........")

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor = 1.5,
                                                     minSize = (200, 150))
 
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'): # sempre que aperta `q` cai aki
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x +1], (largura, altura))
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