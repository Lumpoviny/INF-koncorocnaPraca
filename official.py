from cProfile import label
from tkinter import *
from time import *
master=Tk()
master.title("World of Tanks")

### ?VEĽKOSŤ CANVASU ###
width = 1000
height = 800
### ?POČIATOČNÁ POLOHA ###
x = 500
y = 750
### ?CANVAS ###
canvas=Canvas(master, width=width, height=height)
canvas.pack()
### ?OBJEKTY ###
### !TANK ###
lavyPas=canvas.create_rectangle(x-30, y-30, x-30+5, y+30, fill="#1b4332")
pravyPas=canvas.create_rectangle(x+30, y-30, x+30-5, y+30, fill="#1b4332")
korba=canvas.create_rectangle(x-25, y-25, x+25, y+25, fill="#40916c")
delo=canvas.create_rectangle(x-2.5, y-50, x+2.5, y, fill="#95d5b2")
poloha="up"
### !PREKÁŽKY ###
prekazkyFile = open("prekazky.txt", "r")
prekazky = prekazkyFile.read().split("\n")
prekazky = list(filter(None, prekazky))
def getCoordinates(lst):
  newLst = []
  for el in lst:
    sub = el.split(' ')
    sub = [float(x) for x in sub]
    newLst.append(sub)
  return(newLst)
prekazky=(getCoordinates(prekazky))

for i in prekazky:
  canvas.create_rectangle(i[0], i[1], i[2], i[3], outline="#1b4332", fill="#fafafa")
prekazkyFile.close()
# !CIEĽ
cielY=0
farba=1
for i in range(6):
  cielX=440
  for j in range(6):
    if farba % 2 == 1:
      farba+=1
      canvas.create_rectangle(cielX, cielY, cielX+20, cielY+20, fill="black")
      cielX+=20
    else:
      farba+=1
      canvas.create_rectangle(cielX, cielY, cielX+20, cielY+20, fill="white")
      cielX+=20
  cielY+=20
  farba+=1
# !blogáda cieľa
blockade=canvas.create_rectangle(320, 190, 440, 200, fill="black")
# !Otvorenie cieľa
opening=canvas.create_rectangle(685, 365, 715, 395, outline="red")
# !Zrýchlenie
speed=canvas.create_rectangle(625, 525, 655, 555, outline="red")

def rotateUp(event):
    global x, y, poloha
    canvas.coords(delo,x-2.5,y-50,x+2.5,y)
    canvas.coords(korba,x-25, y-25, x+25, y+25)
    canvas.coords(lavyPas,x-30, y-30, x-30+5, y+30)
    canvas.coords(pravyPas,x+30, y-30, x+30-5, y+30)
    poloha="up"

def rotateDown(event):
    global x, y, poloha
    canvas.coords(delo,x-2.5,y,x+2.5,y+50)
    canvas.coords(korba,x-25, y-25, x+25, y+25)
    canvas.coords(lavyPas,x-30, y-30, x-30+5, y+30)
    canvas.coords(pravyPas,x+30, y-30, x+30-5, y+30)
    poloha="down"

def rotateLeft(event):
    global x, y, poloha
    canvas.coords(delo,x-50,y-2.5,x,y+2.5)
    canvas.coords(korba,x-25, y-25, x+25, y+25)
    canvas.coords(lavyPas,x-30, y-30, x+30, y-30+5)
    canvas.coords(pravyPas,x-30, y+30, x+30, y+30-5)
    poloha="left"

def rotateRight(event):
    global x, y, poloha
    canvas.coords(delo,x,y-2.5,x+50,y+2.5)
    canvas.coords(korba,x-25, y-25, x+25, y+25)
    canvas.coords(lavyPas,x-30, y-30, x+30, y-30+5)
    canvas.coords(pravyPas,x-30, y+30, x+30, y+30-5)
    poloha="right"

def reset(event):
    global x, y, poloha
    canvas.coords(delo,x-2.5,y-50,x+2.5,y)
    canvas.coords(korba,x-25, y-25, x+25, y+25)
    canvas.coords(lavyPas,x-30, y-30, x-30+5, y+30)
    canvas.coords(pravyPas,x+30, y-30, x+30-5, y+30)
    poloha="up"
    y=750
    x=500
    canvas.update()
    master.after(1, pohyb)

def pohyb():
  global poloha, x, y
  v=5

  def checkObstacles(smer):
    global blockade
    obstacle=False
    ##!PREKAZKY##
    prekazkyFile = open("prekazky.txt", "r")
    prekazky = prekazkyFile.read().split("\n")
    prekazky = list(filter(None, prekazky))
    
    def getCoordinates(lst):
      newLst = []
      for el in lst:
        sub = el.split(' ')
        sub = [float(x) for x in sub]
        newLst.append(sub)
      return(newLst)

    prekazky=getCoordinates(prekazky)

    for prekazka in prekazky:
      if smer == "up":
        if prekazka[0]-30<=x<=30+prekazka[2] and prekazka[1]<=y-v-50<=prekazka[3]:
          obstacle=True
      elif smer == "down":
        if prekazka[0]-30<=x<=30+prekazka[2] and prekazka[1]<=y+v+50<=prekazka[3]:
          obstacle=True
      elif smer == "left":
        if prekazka[0]<=x-v-50<=prekazka[2] and prekazka[1]-30<=y<=30+prekazka[3]:
          obstacle=True
      elif smer == "right":
        if prekazka[0]<=x+v+50<=prekazka[2] and prekazka[1]-30<=y<=30+prekazka[3]:
          obstacle=True

    if smer == "up" and blockade:
        if 320-30<=x<=30+440 and 190<=y-v-50<=200:
          obstacle=True

    prekazkyFile.close()
    return obstacle

  while True:
    global blockade
    obstacle=checkObstacles(poloha)
    # if obstacle==True:
    #   prehraMaster = Tk()
    #   prehraMaster.title("Prehral si")
    #   plocha = Canvas(master, width="400", height="200")
    #   plocha.pack()
      
    #   prehraLabel=Label(prehraMaster,text="PREHRAL SI")
    #   prehraLabel.pack()
    #   break

    if poloha == "up":
      if 0+50 < y:
        if obstacle == False:
          canvas.move(lavyPas,0,-v)
          canvas.move(pravyPas,0,-v)
          canvas.move(korba,0,-v)
          canvas.move(delo,0,-v)
          y-=v
    elif poloha == "down":
      if y < height-50:
        if obstacle == False:
          canvas.move(lavyPas,0,+v)
          canvas.move(pravyPas,0,+v)
          canvas.move(korba,0,+v)
          canvas.move(delo,0,+v)
          y+=v
    elif poloha == "left":
      if 0+50 < x:
        if blockade and opening and 685-50<=x<=715+50 and 365<=y<=395:
          canvas.delete(blockade)
          canvas.delete(opening)
          blockade=0
        elif 625-50<=x<=655+50 and 525<=y<=555:
          v=10
          canvas.delete(speed)

        if obstacle == False:
          canvas.move(lavyPas,-v,0)
          canvas.move(pravyPas,-v,0)
          canvas.move(korba,-v,0)
          canvas.move(delo,-v,0)
          x-=v
    elif poloha == "right":
      if x < width-50:
        if 625-50<=x<=655+50 and 525<=y<=555:
          v=10
          canvas.delete(speed)

        if obstacle == False:
          canvas.move(lavyPas,+v,0)
          canvas.move(pravyPas,+v,0)
          canvas.move(korba,+v,0)
          canvas.move(delo,+v,0)
          x+=v

    if 440+50<=x<=560 and 0<=y<=120:
      break
    canvas.after(1)
    canvas.update()

canvas.bind_all('<Down>',rotateDown)
canvas.bind_all('<Right>',rotateRight)
canvas.bind_all('<Up>',rotateUp)
canvas.bind_all('<Left>',rotateLeft)
canvas.bind_all("<space>", reset)

master.after(1, pohyb)
mainloop()
