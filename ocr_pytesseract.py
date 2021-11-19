from PIL import Image
import pytesseract

im = Image.open("test2.jpeg")
result = pytesseract.image_to_string(im, lang='chi_sim+eng')
print(result)