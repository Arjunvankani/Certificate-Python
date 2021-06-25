import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_csv(r'list.csv') 
name_list = data["name"].tolist() 
for i in name_list:
    im = Image.open('certificate.jpg')
    d = ImageDraw.Draw(im)
    location = (725, 760)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 120)
    d.text(location, i, fill = text_color, font = font)
    im.save("certificate_" + i + ".pdf")



