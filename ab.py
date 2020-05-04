import pytesseract
from PIL import Image
import numpy as np
import os
import cv2



pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img_name = cv2.imread('SirRafi_1.jpg')
filePath = r'C:\Users\Muhammad\PycharmProjects\abc\myImages'

#thresholding image
_, threshold = cv2.threshold(img_name, 155, 255, cv2.THRESH_BINARY)
img_gray = cv2.cvtColor(img_name, cv2.COLOR_BGR2GRAY)
mean_c = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)

cv2.imwrite(os.path.join(filePath , "thresholdImg.png"), gaus)
print("Threshold image...Done")

#
img_name = cv2.imread(r'C:\Users\Muhammad\PycharmProjects\abc\myImages\thresholdImg.png')

### load input image and convert it to grayscale
gray = cv2.cvtColor(img_name, cv2.COLOR_BGR2GRAY)

#### extract all contours
contours, _  = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# debug: draw all contours
cv2.drawContours(img_name, contours, -1, (0, 0, 0), 1)
cv2.imwrite(os.path.join(filePath , "all_contours.png"), img_name)
img_name = cv2.imread('all_contours.png')


img_name = cv2.imread(r'C:\Users\Muhammad\PycharmProjects\abc\myImages\all_contours.png')

#image bluring
mdBlur = cv2.bilateralFilter(img_name,9,75,75)


cv2.imwrite(os.path.join(filePath , "blurImg.png"), mdBlur)
#
img_name = cv2.imread(r'C:\Users\Muhammad\PycharmProjects\abc\myImages\blurImg.png')
blurImg = cv2.blur(img_name,(5, 5))
cv2.imwrite(os.path.join(filePath , "blurImg.png"), blurImg)

print("Bluring image...Done")

# img_name = "blurImg.png"

#Image Binarization
# col = Image.open(img_name)
col = Image.open(r"C:\Users\Muhammad\PycharmProjects\abc\myImages\blurImg.png")
gray = col.convert('L')

bw = np.asarray(gray).copy()

# Pixel range is 0...255, 256/2 = 128
bw[bw < 128] = 0    # Black
bw[bw >= 128] = 255 # White

# Now we put it back in Pillow/PIL land
imfile = Image.fromarray(bw)
imfile.save("result_bw.png")
print("Image binarization...Done")

#Remove Backgroud
img_name = Image.open('result_bw.png')#image path and name

img_name = img_name.convert("RGBA")
datas = img_name.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img_name.putdata(newData)
img_name.save("TransparentImage.png", "PNG")#converted Image name
print("Removing image background...Done")

img_name = "TransparentImage.png";
#resizing
basewidth = 700
img = Image.open(img_name)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save("resizedImage.png")
print("Image resizing...Done")

img_name = "resizedImage.png";

#Image to Text
text_img = Image.open(img_name)
text = pytesseract.image_to_string(text_img)
print('\n----Result After Binarization And Resize Image:----\n', text)


