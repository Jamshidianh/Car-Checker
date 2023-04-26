# to open the site,  to get the screen shot, time for sleep,to crop the screenshot,to read whats on the image 
import webbrowser as web
import pyautogui
import time
from PIL import Image
import cv2
import pytesseract


# define the site url, carl model and distance, zipcode and set chrome path
siteUrl = "https://www.picknpull.com/check-inventory/vehicle-search?make=90&model=1244&distance=25&zip=94707&year="
chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# register and open site url via chrome
web.register("Chrome",None, web.BackgroundBrowser(chromePath))
web.get("Chrome").open_new_tab(siteUrl)


# wait a bit till site loads
time.sleep(6)


# save image here 
imgUrl = r"C:\PorgramTest\myImage.png"

myScreenshot = pyautogui.screenshot()
myScreenshot.save(imgUrl)


# open imagie
im = Image.open(imgUrl)
width, height = im.size
 

# Setting the points for cropped image
left = 460
top = (height / 2)+80
right = 1200
bottom = (3 * height / 3)-100
 

# Cropp image of above dimension Save image and replace old file
im1 = im.crop((left, top, right, bottom))
im1 = im1.save("C:\PorgramTest\myImage.png")


# find where the tesseract program is 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


#define the image it's looking for, read it and print 
img = cv2.imread("C:\PorgramTest\myImage.png")
text = pytesseract.image_to_string(img)

print(text)