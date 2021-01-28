from mcpi.minecraft import  Minecraft
ll=Minecraft.create()
l2=[12,14,41],[35,73,86]
m=ll.getPlayerEntityId("APE_44")
x,y,z,=ll.entity.getTilePos(m)
sx=x
for i in l2:
    for j in i:
        ll.setBlock(x,y,z,j)
        x=x+1
    x=sx
    z=z-1



