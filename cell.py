cell_ID=0
# Cellはマス目。
class Cell:
    def __init__(self):
        global cell_ID
        cell_ID += 1
        self.number = cell_ID
        self.x=0
        self.y=0
    def __str__(self):
        return "{}番のマス".format(self.number)
    def fields(self):
        return f"x={self.x} y={self.y}"
    def stop(self, player):
        pass
    def over(self, player):
        pass

class GateCell1(Cell):
    def stop(self, player):
        if (player.point>=12000 or
                player.point<=-12000):
            player.win = 1
        else:
            player.x+=1
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell2(Cell):
    def stop(self, player):
        if player.point>15000:
            player.win=1
        else:
            player.point+=1000
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell3(Cell):
    def stop(self, player):
        if player.point>10000:
            player.win=1
        else:
            player.point+=1000
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell4(Cell):
    def stop(self, player):#check
        if player.x*player.point>10000:
            player.win = 1
        else:
            player.x+=1
    def over(self,player):
        if player.x*player.point>=500000:
            player.win=1
class GateCell5(Cell):
    def stop(self, player):
        if int((player.point*player.x)/1000)%2!=0:
           player.win = 1
        else:
            player.x+=1
    def over(self,player):
        if player.point>=50000:
            player.win=1
class GateCell6(Cell):
    def stop(self, player):
        if player.point>10000:
            player.win=1
        else:
            player.x+=1
    def over(self,player):
        if player.point>=50000:
            player.win=1

class cell1(Cell):
    def stop(self, player):
        player.point+=1000


class cell2(Cell):
    def stop(self, player):
        player.point-=1000


class cell3(Cell):
    def stop(self, player):
        player.point+=3000


class cell4(Cell):
    def stop(self, player):
        player.point+=4000

class cell5(Cell):
    def stop(self, player):
        player.point+=5000

class cell6(Cell):
    def stop(self, player):
        player.point*=2

class cell7(Cell):
    def stop(self, player):
        player.point-=3000

class cell8(Cell):
    def stop(self, player):
        player.point+=-1000

class cell9(Cell):
    def stop(self, player):
        player.point-=-2000

class cell10(Cell):
    def stop(self, player):
        player.point+=-1000

class cell11(Cell):
    def stop(self, player):
        player.point=player.other.point

class cell12(Cell):
    def stop(self, player):
        player.point-=-4000

class cell13(Cell):
    def stop(self, player):
        if player.input_YN("y/n")=="y":
            player.point-=1000
        else:
            player.point+=10000

class cell14(Cell):
    def stop(self,player):
        player.x+=int(player.point/1000)

class cell15(Cell):
    def stop(self,player):
        player.other.point-=player.x*1000

class cell16(Cell):
    def stop(self,player):
        player.other.point-=1000

class cell17(Cell):
    def stop(self, player):
        player.point+=player.x*2000

class cell18(Cell):
    def stop(self, player):
        player.point+=1500*player.x
class cell19(Cell):
    def stop(self, player):
        player.other.point-=1000*player.x

class cell20(Cell):
    def stop(self, player):
        player.other.x+=4

class cell21(Cell):
    def stop(self, player):
        player.point+=1000*player.x

class cell22(Cell):
    def stop(self,player):
        player.x+=player.other.x

class cell23(Cell):
    def stop(self, player):
        if player.x%2==0:
            player.point+=5000

class cell24(Cell):
    def stop(self, player):
        player.other.x+=player.x

class cell25(Cell):
    def stop(self, player):
        if player.x%3==0:
            player.point+=player.other.point

class cell26(Cell):
    def stop(self, player):
        player.other.point-=(player.point-player.other.point)

class cell27(Cell):
    def stop(self, player):
        if player.x%2!=0:
            player.x+=10
class cell28(Cell):
    def stop(self, player):
        player.other.x-=int(player.point/1000)

class cell29(Cell):
    def stop(self, player):
        player.point+=2000*player.x

class cell30(Cell):
    def stop(self,player):
        player.x+=3

class cell31(Cell):
    def stop(self, player):
        player.point+=self.y*1000
        self.y=0
    def over(self,player):
        self.y+=1

class cell32(Cell):
    def stop(self, player):
        player.point+=self.y
        self.y=0
    def over(self,player):
        player.point-=1000
        self.y+=1000

class cell33(Cell):
    def stop(self, player):
        self.y+=1000
        player.point+=self.y
class cell50(Cell):
    def stop(self, player):
        self.x+=1
        if self.x>=3:
            player.point+=5000
