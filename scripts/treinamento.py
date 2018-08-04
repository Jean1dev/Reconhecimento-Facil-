import cv2
import os
import numpy as np

path = "/Users/jeanfernandes/Documents/git/Py_facial/source/scripts/"
path_completo = path + 'fotos'
eigenface = cv2.face.EigenFaceRecognizer_create(num_components=10, threshold=2)
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemId():
    caminhos = [os.path.join(path_completo, f) for f in os.listdir(path_completo)]
    print(caminhos)
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)       #DA PAU
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1]) # DA PAU

        #cv2.imshow("Face", imagemFace)
        #id = os.path.split(caminhoImagem)[-1].split('.')[1]
        #imagemFace = cv2.imread(caminhoImagem)
        
        ids.append(id)
        faces.append(imagemFace)   
        #cv2.waitKey(100)
    return np.array(ids), faces

list_id, list_face = getImagemId()
print(list_id)

eigenface.train(list_face, list_id)
eigenface.write(path + 'classificadorEigen.yml')

fisherface.train(list_face, list_id)
fisherface.write(path + 'classificadorFisher.yml')

lbph.train(list_face, list_id)
lbph.write(path + 'classificadorLBPH.yml')

print('fecho meu jovem')