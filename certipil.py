from PIL import Image, ImageFont, ImageDraw



name="Kousik Rajesh"
city="Greater Noida"
i=3#index corresponding to certificate
rank="123"
squad="Junior"


names=["participation,jpg","gold.jpg","silver.jpg","citytopper.jpg"]
values=[[123,889,832,175,470,1045],[120,888,738,216,477,830,186,468,1148,613,852,1084],[120,888,730,216,477,822,228,508,1138,655,897,1075],[120,888,832,492,744,920,123,324,982]]


certi=Image.open(names[i])

nameblankStartX=values[i][0]
nameblankEndX=values[i][1]
nameblankY=values[i][2]

cityblankStartX=values[i][3]
cityblankEndX=values[i][4]
cityblankY=values[i][5]

if i==0:
    pass
elif i==3:
    squadStartX=values[i][6]
    squadEndX=values[i][7]
    squadY=values[i][8]

else:
    squadStartX=values[i][6]
    squadEndX=values[i][7]
    squadY=values[i][8]
    rankStartX=values[i][9]
    rankEndX=values[i][10]
    rankY=values[i][11]

    
nameFontSize=50#default size for small names
cityFontSize=35
rankFontSize=35
squadFontSize=35
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

if(i!=0):
    while True:
    
        font = ImageFont.truetype("Montserrat-Regular.ttf", squadFontSize) 
        
        if(font.getsize(squad)[0]>(squadEndX-squadStartX)):
            squadFontsize-=1
        else:
            break
    squadSize=font.getsize(squad)
    draw.text(((squadStartX+squadEndX)/2-squadSize[0]/2, squadY-squadSize[1]), squad, font=font,fill=(0,0,0))
        
if(i!=0 and i!=3):
    while True:
    
        font = ImageFont.truetype("Montserrat-Regular.ttf", rankFontSize) 
        
        if(font.getsize(rank)[0]>(rankEndX-rankStartX)):
            rankFontsize-=1
        else:
            break
    rankSize=font.getsize(rank)
    draw.text(((rankStartX+rankEndX)/2-rankSize[0]/2, rankY-rankSize[1]), rank, font=font,fill=(0,0,0))
    
certi.show()
certi.save("certinamed.jpg")
