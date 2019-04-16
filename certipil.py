from PIL import Image, ImageFont, ImageDraw
name="Kousik Rajesh"
city="Greater Noida"

names=["participation,jpg","gold.jpg","silver.jpg","citytopper.jpg"]
values=[[123,889,832,175,470,1045],[120,888,738,216,477,830],[120,888,730,216,477,822],[120,888,832,492,744,920]]

i=1#index corresponding to certificate
certi=Image.open(names[i])

nameblankStartX=values[i][0]
nameblankEndX=values[i][1]
nameblankY=values[i][2]

cityblankStartX=values[i][3]
cityblankEndX=values[i][4]
cityblankY=values[i][5]


nameFontSize=50#default size for small names
cityFontSize=35
draw = ImageDraw.Draw(certi)
while True:
    
    font = ImageFont.truetype("Montserrat-Regular.ttf", nameFontSize) 
    
    if(font.getsize(name)[0]>(nameblankEndX-nameblankStartX)):
        nameFontsize-=1
    else:
        break
nameSize=font.getsize(name)
draw.text(((nameblankStartX+nameblankEndX)/2-nameSize[0]/2, nameblankY-nameSize[1]), name, font=font,fill=(0,0,0))
while True:
    
    font = ImageFont.truetype("Montserrat-Regular.ttf", cityFontSize) 
    
    if(font.getsize(city)[0]>(cityblankEndX-cityblankStartX)):
        cityFontSize-=1
    else:
        break
citySize=font.getsize(city)






draw.text(((cityblankStartX+cityblankEndX)/2-citySize[0]/2, cityblankY-citySize[1]), city, font=font,fill=(0,0,0))
certi.show()
certi.save("certinamed.jpg")
