"""Insert varying length text into a blank in an image by changing font size"""


from PIL import Image, ImageFont, ImageDraw



name=""
city=""
i = 0 #index corresponding to certificate
rank=""
squad=""
names=["participationnew.jpg","goldnew.jpg","silvernew.jpg","citytoppernew.jpg"]#file names of images

#values=[[123,889,832,175,470,1045],[120,888,738,216,477,830,186,468,1146,613,852,1082],[120,888,728,216,477,822,228,508,1136,655,897,1073],[120,888,831,492,744,919,123,324,982]]


values=[[140, 1015, 950, 199, 536, 1193], [137, 1014, 842, 246, 544, 947, 212, 534, 1308, 700, 973, 1235], [137, 1014, 831, 246, 544, 938, 260, 580, 1297, 748, 1024, 1225], [137, 1014, 949, 561, 849, 1049, 140, 370, 1121]]

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
