from PIL import Image, ImageFont, ImageDraw
name="abcdefghijklmnopqrstuvwxyz"

certi=Image.open("certi.jpg")

#123,834
#889,834

#change the blank starting and ending coordinates here(origin at top left corner)
blankStartX=123
blankEndX=889
blankY=832


fontsize=50#default size for small names
while True:
    
    font = ImageFont.truetype("Montserrat-Regular.ttf", fontsize) 
    
    if(font.getsize(name)[0]>(blankEndX-blankStartX)):
        fontsize-=1
    else:
        break

size=font.getsize(name)
draw = ImageDraw.Draw(certi)


draw.text(((blankStartX+blankEndX)/2-size[0]/2, blankY-size[1]), name, font=font,fill=(0,0,0))

certi.show()
certi.save("certinamed.jpg")
