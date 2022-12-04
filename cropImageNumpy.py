import numpy as np

class CropImageNumpy:

    def usingNp():
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


if __name__ == "__main__": 
    cmd = CropImageNumpy
    cmd.usingNp()  