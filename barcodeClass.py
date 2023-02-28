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
            # print("detected barcode:", obj)
            image = draw_barcode(obj, image)
            # print barcode type & data
            # recognizeType = obj.type
            recognizeData.append(obj.data)
            recognizeType.append(obj.type)

        return image
    else:
        print("nodata")
        recognizeType = ""
        recognizeData = ""


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    # uncomment above and comment below if you want to draw a polygon and not a rectangle
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
    print("lib")
    # from glob import glob
    # barcodes = glob("*.jpg")
    # for barcode_file in barcodes:
        # load the image to opencv
        # barcode_file = "E:/Python code/PyBarcode/bar.png"
        # init(barcode_file)
        # img = cv2.imread(barcode_file)
        # # decode detected barcodes & get the image
        # # that is drawn
        # img = decode(img)
        # # show the image
        # cv2.imshow("img", img)
        # cv2.imwrite("barcode_detected.png", img)
        # cv2.waitKey(0)
