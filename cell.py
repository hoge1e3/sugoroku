from random import randint
cell_ID=0

# Cellはマス目。
class Cell:
    def __init__(self):
        global cell_ID
        cell_ID += 1
        self.number = cell_ID
    def __str__(self):
        return "{}番のマス".format(self.number)
    def fields(self):
        return None
    def stop(self, player):
        pass
    def over(self, player):
        pass
class GateCell(Cell):
    pass
class StateGateCell(Cell):
    def __init__(self):
        super().__init__()
        self.gate="close"
        self.x=0
        self.y=0
    def fields(self):
        return f"x={self.x} y={self.y} gate={self.gate}"

class GateCell1(GateCell):
    def stop(self, player):
        if (player.point>=12000 or
                player.point<=-12000):
            player.win = 1
        else:
            player.x+=1
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell2(GateCell):
    def stop(self, player):
        if player.point>15000:
            player.win=1
        else:
            player.point+=1000
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell3(GateCell):
    def stop(self, player):
        if player.point>10000:
            player.win=1
        else:
            player.point+=1000
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell4(GateCell):
    def stop(self, player):#check
        if player.x*player.point>100000:
            player.win = 1
        else:
            player.x+=1
    def over(self,player):
        if player.x*player.point>=500000:
            player.win=1
class GateCell5(GateCell):
    def stop(self, player):
        if player.point>=15000:
            player.win = 1
        else:
            player.x+=1
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell6(GateCell):
    def stop(self, player):
        if player.point>10000:
            player.win=1
        else:
            player.x+=1
    def over(self,player):
        if player.point>=50000:
            player.win=1

class GateCell7(StateGateCell):
    def stop(self, player):
        if self.gate=="open":
            if player.x>10:
                player.win=1
    def over(self, player):
        self.y+=player.y
        if self.y > 25:
            self.gate = "open"



class Cell1(Cell):
    def stop(self, player):
        player.point+=1000


class Cell2(Cell):
    def stop(self, player):
        player.point-=1000


class Cell3(Cell):
    def stop(self, player):
        player.point+=3000


class Cell4(Cell):
    def stop(self, player):
        player.point+=4000

class Cell5(Cell):
    def stop(self, player):
        player.point+=5000

class Cell6(Cell):
    def stop(self, player):
        player.point*=2

class Cell7(Cell):
    def stop(self, player):
        player.point-=3000
    def over(self, player):
        player.other.point-=1000
class Cell8(Cell):
    def stop(self, player):
        player.point-=5000
    def over(self, player):
        player.point+=1000

class Cell9(Cell):
    def stop(self, player):
        player.point-=2000
    def over(self, player):
        player.other.point-=2000

class Cell10(Cell):
    def stop(self, player):
        player.point+=10000
    def over(self, player):
        player.point-=5000

class Cell11(Cell):
    def stop(self, player):
        player.point+=player.other.point

class Cell12(Cell):
    def stop(self, player):
        player.point-=4000
    def over(self, player):
        player.point+=2000

class Cell13(Cell):
    def stop(self, player):
        if player.point>=10000:
            player.point-=1000
        else:
            player.point+=10000

class Cell14(Cell):
    def stop(self,player):
        player.x+=int(player.point/1000)

class Cell15(Cell):
    def stop(self,player):
        player.other.point-=player.x*1000

class Cell16(Cell):
    def stop(self,player):
        player.other.point-=1000

class Cell17(Cell):
    def stop(self, player):
        player.point+=player.x*2000

class Cell18(Cell):
    def stop(self, player):
        player.point+=1500*player.x
class Cell19(Cell):
    def stop(self, player):
        player.other.point-=1000*player.x

class Cell20(Cell):
    def stop(self, player):
        player.other.x+=4

class Cell21(Cell):
    def stop(self, player):
        player.point+=1000*player.x

class Cell22(Cell):
    def stop(self,player):
        player.x+=player.other.x

class Cell23(Cell):
    def stop(self, player):
        if player.x%2==0:
            player.point+=5000

class Cell24(Cell):
    def stop(self, player):
        player.other.x+=player.x

class Cell25(Cell):
    def stop(self, player):
        if player.x%3==0:
            player.point+=player.other.point

class Cell26(Cell):
    def stop(self, player):
        p=player.other.point
        player.other.point=player.point
        player.point=p

class Cell27(Cell):
    def stop(self, player):
        if player.x%2!=0:
            player.x+=10
class Cell28(Cell):
    def stop(self, player):
        player.other.x-=int(player.point/1000)

class Cell29(Cell):
    def stop(self, player):
        player.point+=2000*player.x

class Cell30(Cell):
    def stop(self,player):
        player.x+=3

class StateCell(Cell):
    def __init__(self):
        super().__init__()
        self.x=randint(0,5)
        self.y=randint(0,5)
    def fields(self):
        return f"x={self.x} y={self.y}"
    
class Cell31(StateCell):
    def stop(self, player):
        player.point+=self.y*1000
        self.y=0
    def over(self,player):
        self.y+=1

class Cell32(StateCell):
    def stop(self, player):
        player.point+=self.y
        self.y=0
    def over(self,player):
        player.point-=1000
        self.y+=1000


class Cell33(StateCell):
    def stop(self, player):
        self.y+=1000
        player.point+=self.y

class Cell34(StateCell):
    def stop(self, player):
        player.other.cell.y=1

class Cell35(StateCell):#GateCell7
    def stop(self, player):
        player.y+=self.y
        self.y=0
    def over(self, player):
        self.y+=1

class Cell36(StateCell):#GateCell7
    def stop(self,player):
        player.x+=self.x
    def over(self, player):
        self.x+=1
        player.x-=1

class Cell37(StateCell):#Gate7
    def stop(self, player):
        x = self.x
        self.x = player.x
        player.x = x
    def over(self, player):
        self.x+=1
class Cell38(StateCell):#gate7
    def stop(self, player):
        player.y+=self.y
        self.x+=1
    def over(self, player):
        player.x+=self.x
        self.x+=1

class Cell39(StateCell):#gate7
    def stop(self, player):
        player.y += self.y
        self.y=0
    def over(self, player):
        self.y += 1
        player.y-=1
class Cell40(StateCell):#gate7
    def stop(self, player):
        player.x+=self.x
        player.y+=self.y
    def over(self, player):
        self.x*=-1
        self.y*=-1

class Cell41(StateCell):
    def stop(self, player):
        player.x+=self.x
    def over(self, player):
        self.x+=1

class GateCell8(StateGateCell):
    def stop(self, player):
        if self.gate=="open":
            player.win=1
        else:
            self.over(player)
    def over(self, player):
        self.x+=player.point
        player.point=0
        if self.x > 100000:
            self.gate="open"

class Cell50(StateCell):
    def stop(self, player):
        if self.x>=30:
            player.point+=500000
            self.x = 0
        elif self.x>=10:
            player.point+=10000
            self.x = 0
    def over(self, player):
        self.x+=5
class Cell51(StateCell):
    def stop(self, player):
        self.x*=-1
    def over(self, player):
        player.point+=1000*self.x

class Cell52(StateCell):
    def stop(self, player):
        player.point+=1000*self.x
    def over(self, player):
        self.x*=-1
class Cell53(StateCell):
    def stop(self, player):
        self.x*=-2
        self.over(player.other)
    def over(self, player):
        player.point+=self.x*1000

class Cell54(StateCell):
    def stop(self, player):
        player.point+=self.y*1000
        self.y=0
    def over(self, player):
        player.y=-1
        self.y+=1
class Cell55(StateCell):
    def stop(self, player):
        d=player.point-player.other.point
        if d<0:
            a=player.point
            player.point=player.other.point
            player.other.point=a
class Cell56(StateCell):
    def stop(self, player):
        player.point+=self.x*2*1000
    def over(self, player):
        self.x*=-1

class Cell57(StateCell):
    def stop(self, player):
        if self.x==0:
            player.point+=player.other.point
        elif self.x==1:
            player.other.point+=player.point
        elif self.x==2:
            a=(player.point+player.other.point)/2
            player.point=a
            player.other.point=a
    def over(self, player):
        self.x=(self.x+1)%3


class Cell60(StateCell):
    def stop(self, player):
        player.point+=self.x*2000
    def over(self,plater):
        self.x*=-1

class Cell61(StateCell):
    def stop(self, player):
        player.point+=self.y*1000
    def over(self, player):
        self.y+=1

class Cell62(StateCell):
    def stop(self, player):
        if self.x==0:
            player.x*=2
        elif self.x==1:
            player.other.x*=2
        elif self.x==2:
            player.point+=10000
            player.other.point+=10000
    def over(self, player):
        self.x=(self.x+1)%3

class Cell63(StateCell):
    def stop(self, player):
        player.y+=self.y
        self.y=0
    def over(self, player):
        self.y+=3

class Cell64(StateCell):
    def stop(self, player):
        if self.x%2==0:
            player.point+=self.y*1000
        else:
           self.y+=1
    def over(self, player):
        self.x+=1

class Cell65(StateCell):
    def stop(self, player):
        self.x+=1
        self.y+=1
        player.x*=self.x
        player.y*=self.y

class Cell66(StateCell):
    def stop(self, player):
        player.x+=self.x
        self.x=0
    def over(self, player):
        self.x+=3