import base64

def saveImage(imageData):
    imageData.replace("image/octet-stream", "image/png")
    if len(imageData) % 4:
        #not a multiple of 4, add padding:
        imageData += '=' * (4 - len(imageData) % 4) 
    print(imageData)
    with open("drawing.png", "wb") as file:
        file.write(base64.b64decode(imageData))
    
