import requests
from lxml import etree
import json
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup

url = "http://164.100.128.47/case/guiCaseWise.php"
r = requests.session()
rurl = requests.get(url)
soup = BeautifulSoup(rurl.text, 'lxml')
captcha = "http://164.100.128.47/case/" + soup.find('img', {'id' : 'captchaimg'}).get('src')
rcaptcha = r.get(captcha)

f = open('yourcaptcha.png', 'wb')
f.write(rcaptcha.content)
f.close()

im = Image.open("yourcaptcha.png")
text = pytesseract.image_to_string(im, lang = 'eng')
print(text)

ctype = "W.P.(C)"
regno =	"123"
regyr =	"2017"
letters_code	= text.encode('UTF-8')
# Submit = "Submit"

data = [
      ('ctype', ctype),
      ('regno', regno),
      ('regyr', regyr),
      ('6_letters_code', letters_code),
      ('Submit', "Submit"),]

url = "http://164.100.128.47/case/s_adv.php"
r2 = r.post(url=url,  data=data)

soup = BeautifulSoup(r2.text, 'lxml')
print soup.prettify()
print text
