from PIL import Image, ExifTags
import cv2
import numpy as np


def readimage(name):
    try:
        Image.open(name)
        return('')
        pass

    except:
        return('Failed to read image')

def infoPreview(name):

    try:

        image = Image.open(name)

        try:

            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            exif = dict(image._getexif().items())
            exif_info = str(exif[orientation])
            if exif_info == 3:
                img_obs = "image rotated 180"
            elif exif_info == 6:
                img_obs = "image rotated 270"
            elif exif_info == 8:
                img_obs = "image rotated 90"
            else:
                img_obs = ""


        except:
            exif_info = 0

        width, height = image.size

        if width < height :
            img_obs = "Vertical Image"

    except:
        exif_info = ""
        width = ""
        height = ""
        img_obs = "Corrupted image" 

    return([exif_info, width, height, img_obs])

def checkWhitePixels(img):

    try:

        image = cv2.imread(img)
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        left = image[0:h, 0:cX]
        right = image[0:h, cX:w]
        up = image[0:cY, 0:w]
        down = image[cY:h, 0:w]
        label = {"left": np.sum(left == 255), "right": np.sum(right == 255),
                 "up": np.sum(up == 255), "down": np.sum(down == 255)}

        fin_max = max(label, key=label.get)

    except:

        fin_max = ''

    return(fin_max)
