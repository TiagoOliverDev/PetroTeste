from PIL import Image 


class Execute:

    def recort_pil():
        Image1 = Image.open('/home/tiagoetical/Área de Trabalho/Solpe/Petrobras/repos/primeiroTeste/Images/image1.jpg') 
        croppedIm = Image1.crop((130, 120, 200, 200)) 
        croppedIm.show()

    def recort_pil2():
        Image1 = Image.open('/home/tiagoetical/Área de Trabalho/Solpe/Petrobras/repos/primeiroTeste/Images/image1.jpg') 
        croppedIm = Image1.crop((130, 120, 200, 200)) 
        print('Teste 2')
        croppedIm.show()









if __name__ == "__main__": 
    cmd = Execute
    cmd.recort_pil()  
