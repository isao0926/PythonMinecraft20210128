from mcpi.minecraft import  Minecraft
ll=Minecraft.create()
from random import randrange

for i in range(10):
    x,y,z=ll.player.getTilePos()
    z=z+i
    for j in range(10):
        c=randrange(0,16)
        x=x+1
        ll.setBlock(x,y,z,35,c)
a=randrange(0,16)
while True:
    hs=ll.events.pollBlockHits()
    if len(hs)>0:
        h=hs[0]
        block=ll.getBlockWithData(h.pos)
        data=block.data
        
        if data==a:
            ll.postToChat("恭喜你找到了")
            ll.setBlock(h.pos,57)
            break
        elif data<a:
            ll.postToChat("找錯了!!!!找大一點的吧!")
        
        elif data>a:
            ll.postToChat("找錯了!!!!找小一點的吧!")    
        
        
        
        
        
        