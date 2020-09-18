from math import *
from kandinsky import *
from random import *

#remplis la grille au hasard
def ra(t):
  ta=t
  x=0
  for i in range(1,320/t):
    y=0
    if x<320-t:
      for j in range(1,220/t):
        if y<220-t:
          r=randint(0,3)
          if r==1:
            fill_rect(x,y,t,t,color(0,0,0))
        y+=t
    x+=t

#renvoie la touche appuyée
def inpu(valable):
  a=int(input())
  if type(valable[a-1])==int:
    return a
  else:
    return inpu(valable)

#lance la simulation en permettant de choir ses cases de depart dans la grille
def jdlv(t):
  a=3
  set_pixel(1,1,color(248,252,248))
  x=t
  y=t
  val=[0,1,2,3,4,5,6,7,8,9]
  while a!=0:
    a=inpu(val)
    if a==4:
      x-=t
    if a==6:
      x+=t
    if a==8:
      y-=t
    if a==2:
      y+=t
    if a==5:
      fill_rect(x,y,t,t,color(0,0,0))
    if a==0:
      jeudelavie(t,0)

#lance la simulation en remplissant la grille aléatoirement
def jdlvra(t):
  jeudelavie(t,1)

#simulation du jeu de la vie après remplissage de la grille
def jeudelavie(t,ran):
  if ran==1:
    ra(t)
  x=t
  y=t
  end=0
  while end==0:
    cost=""
    x=t
    y=t
    #clalcul le nombre de cases noir autour
    for i in range(1,320/t):
      y=t
      if x<320-t:
        for j in range(1,220/t):
          if y<220-t:
            nb=0
            coor=get_pixel(x,y),get_pixel(x,y-t),get_pixel(x-t,y-t),get_pixel(x+t,y-t),get_pixel(x,y+t),get_pixel(x-t,y+t),get_pixel(x+t,y+t),get_pixel(x-t,y),get_pixel(x+t,y)
            for k in range(1,9):
              if coor[k]==color(0,0,0):
                nb+=1
            cost+=str(nb)
          y+=t
      x+=t
    compt=0
    x=t
    y=t
    r1=()
    #change la couleur de la case en fonction du nombre de cases noirs autour d'elle
    for i in range(1,320/t):
      if x<320-t:
        y=t
        for j in range(1,220/t):
          if y<220-t:
            if get_pixel(x,y)==color(0,0,0):
              if int(cost[compt])!=2 and int(cost[compt])!=3:
                fill_rect(x,y,t,t,color(248,252,248))
            else:
              if int(cost[compt])==3:
                fill_rect(x,y,t,t,color(0,0,0))
            compt+=1
          y+=t
      x+=t
