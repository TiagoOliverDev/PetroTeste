from PIL import Image 


class Execute:

    def recort_pil():
        # Import an image from directory:
        input_image = Image.open('Images/image1.jpg') 

        # Extracting pixel map:
        pixel_map = input_image.load()

        # Extracting the width and height 
        # of the image:
        width, height = input_image.size

        # taking half of the width:
        for i in range(width//2):
            for j in range(height):
                
                # getting the RGB pixel value.
                r, g, b = input_image.getpixel((i, j))
                
                # Apply formula of grayscale:
                grayscale = (0.299*r + 0.587*g + 0.114*b)
        
                # setting the pixel value.
                pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))

        # Saving the final output
        # as "grayscale.png":
        input_image.save("grayscale.png", format="png")
        
        # use input_image.show() to see the image on the
        # output screen.
        input_image.show()




    def recort_pil2():
        Image1 = Image.open('Images/image1.jpg') 
        croppedIm = Image1.crop((130, 120, 200, 200)) 
        print('Teste 2')
        croppedIm.show()




if __name__ == "__main__": 
    cmd = Execute
    cmd.recort_pil()  
