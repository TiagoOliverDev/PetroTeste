import numpy as np
import cv2
from PIL import Image 
import numpy as gfg 
from matplotlib import pyplot as plt

class CropImageNumpy:
    
    def __init__(self):
        # self.y = y
        # self.x = x
        pass
        
    def using_np():
        # criar uma matriz para manipular a imagem, toda imagem é na verdade uma matriz
        # Imagem é uma matriz de diversos números de 0 a 255 em rgb. Não irei usar rgb, será mais simples.

        # matrix com array tendo N arrays dentro dele.
        # teremos que cropar
        matrix = np.array([ # Essa matrix é como se fosse uma imagem
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [10, 20, 30, 40, 50, 60, 70, 80, 90],
            [100, 200, 300, 400, 500, 600, 700, 800, 900],
            [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],
        ])

        # parâmetros: eixos y,x
        croped = matrix[0:2, 4:7]

        print(croped)


    def turn_image_into_matrix(self):
        # essa function será criada no intuito de retornar a matriz de uma determinada imagem
        pass
        # NÃO necessário se for usar o OpenCv


    def parameter_return_y():
        # pegar o retorno da matriz de imagem aqui
        # essa function será criada no intuito de retornar os valores dos eixos x e y para manipular na function using_cv() que será a do recorte..
        
        y = 100

        return y

    def parameter_return_x():
        # pegar o retorno da matriz de imagem aqui
        # essa function será criada no intuito de retornar os valores dos eixos x e y para manipular na function using_cv() que será a do recorte..
        
        x = 50

        return x


    def using_cv():     
        # Parâmetros: y = linha vertical, x = linha horizontal, h = altura, w = largura

        # eixoY = self.parameter_return_y()
        # eixoX = self.parameter_return_x()

        # print(eixoY, eixoX)
        img = cv2.imread('Images/image1.jpg')
        cv2.imshow('image', img)
        cv2.waitKey(0) # espera qualquer tecla
        # eixos inicias
        # y = eixoY
        # x = eixoX
        y = 300
        x = 500     
        h = 200  # height
        w = 500  # width

        croped = img[y:y+h, x:x+w] # Eixos y,x. Eixo y com recorte começando no pixel 100 até 200. Eixo x do pixel 50 até 300
        
        cv2.imshow('imageCv', croped)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()


    def dimensions(self):
        # Essa function deverar abrir a imagem e ter um seletor para o usuário selecionar os eixos onde deseja recortar
        # Após eixos selecionados deverá ter um button de aplicar e a function deve retornar os valores desses eixos
        # Após valores dos eixos retornados deverá ser utilizado na function de recorte
        pass


    def newCroped():
        #https://www.youtube.com/watch?v=HzgYJXoj92A
        img = cv2.imread('Images/image1.jpg')
        cv2.imshow('image', img) 
        cv2.waitKey(0) 

        # os pixels abaixo foram retirados do gimp 
        # 1161 e 1315 a 1507 e 1331 [largura = x]
        # 1161 e 1315 a 1161 e 2431 [altura = y]
        
        # y, x
        #croped = img[250:500, 150:300]
        croped = img[1315:2431, 1161:1507] # y, x
        cv2.imshow('imageCroped', croped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showImage(self, img):
        #https://www.youtube.com/watch?v=HzgYJXoj92A
        #https://www.youtube.com/watch?v=mW-PmvvzXP8
        
        img = cv2.imread('Images/image1.jpg', 0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(img) 
        plt.show()

    def cropedDinamic():
        obj_img = cv2.imread('Images/image1.jpg', 0)
        obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)

        #print("height, widht, qtd_canaisDeCor: ", obj_img.shape)

        height, widht, qtd_canaisDeCor = obj_img.shape
        print("Dimensões da imagem: " + str(widht) + "x" + str(height))
        print("Canais de cor: ", qtd_canaisDeCor)

        # for y in range(0, height):
        #     for x in range(0, widht):
        #         print("[" + str(x) + "," + str(y) + "] = " + str(obj_img[y][x]))
        #         # input()

        # petro = obj_img[]


        plt.imshow(obj_img) 
        plt.show()
        
        cv2.imwrite("Image croped.png", obj_img)


    # function criada para converter imagem em matrix    
    def convertToMatrice(image):
        img = Image.open(image) 
        imageToMatrice = gfg.asarray(img) 
        print(imageToMatrice.shape)

if __name__ == "__main__": 
    cmd = CropImageNumpy
    #cmd.using_np()  
    #cmd.using_cv()
    #cmd.newCroped()
    #cmd.convertToMatrice(image='Images/image1.jpg')
    cmd.cropedDinamic()