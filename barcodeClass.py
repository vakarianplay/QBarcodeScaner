from pyzbar import pyzbar
import cv2
import os

def decode(image):
    global recognizeType
    global recognizeData
    recognizeData = []
    recognizeType = []
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    if len(decoded_objects) > 0:
        for obj in decoded_objects:
            # draw the barcode
            image = draw_barcode(obj, image)
            # print barcode type & data
            # recognizeType = obj.type
            recognizeData.append(obj.data)
            recognizeType.append(obj.type)
        return image
    else:
	#no data block
        recognizeType = ""
        recognizeData = ""


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    dir = os.path.abspath(os.curdir)
    cv2.imwrite(dir + "/barcode_detected.png", image)
    return image

def getData():
    return recognizeData

def getType():
    return recognizeType

def init(pathToFile):
    print ("barcode class")
    print(pathToFile)
    img = cv2.imread(pathToFile)
    img = decode(img)
    #dir = os.path.abspath(os.curdir)
    #cv2.imwrite(dir + "/barcode_detected.png", img)
    # cv2.waitKey(0)

if __name__ == "__main__":
    print("This is lib")
    
