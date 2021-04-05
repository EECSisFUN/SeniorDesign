import base64

def saveImage(imageData):
    imageData.replace("image/octet-stream", "image/png")
    
    print(imageData)
    byteData = bytes(imageData, "utf-8")
    if len(byteData) % 4:
        #not a multiple of 4, add padding:
        byteData += b'=' * (4 - len(byteData) % 4) 
    file = open("drawing.png", "w")
    file.write(base64.decodestring(byteData))
    file.close()
    
