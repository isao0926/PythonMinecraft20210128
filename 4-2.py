from mcpi.minecraft import Minecraft
ll=Minecraft.create()
import random
x,y,z=ll.player.getTilePos()
for i in range(20):
    r=random.randrange(1,7)
    if  r==1:
        ll.setBlocks(x,y,z,x,y,z+4,57)
        z=z+4
    if  r==2:
        ll.setBlocks(x,y,z,x,y,z-4,57)
        z=z-4
    if  r==3:
        ll.setBlocks(x,y,z,x+4,y,z,57)
        x=x+4
    if  r==4:
        ll.setBlocks(x,y,z,x-4,y,z,57)
        x=x-4
    if  r==5:
        ll.setBlocks(x,y,z,x,y+4,z,57)
        y=y+4
    if  r==6:
        ll.setBlocks(x,y,z,x,y-4,z,57)
        y=y-4