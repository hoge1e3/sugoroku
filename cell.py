cell_ID=0
# Cellはマス目。
class Cell:
    def __init__(self):
        global cell_ID
        cell_ID += 1
        self.number = cell_ID
    def __str__(self):
        return "{}番のマス".format(self.number)
    def stop(self, player):
        pass
    def over(self, player):
        pass


class SetCell(Cell):
    def __init__(self, field, value):
        super().__init__()
        self.field = field
        self.value = value

    def __str__(self):
        return "{}に{}をSetする{}番目のマス".format(self.field, self.value, self.number)

    def stop(self, p):#止まった時
        if self.field == "x":
            p.x = self.value#xの値をvalueの値にする
        elif self.field == "y":
            p.y = self.value


class AddCell(Cell):
    def __init__(self, field, value):
        super().__init__()
        self.field = field
        self.value = value
    def __str__(self):
        return "{}に{}をAddする{}番目のマス".format(self.field, self.value, self.number)
    def stop(self, p):#止まった時
        if self.field == "x":
            p.x += self.value#xの値をvalueの値の分増やす
        elif self.field == "y":
            p.y += self.value


class SubCell(Cell):
    def __init__(self, field, value):
        super().__init__()
        self.field = field
        self.value = value

    def __str__(self):
        return "{}に{}をSubする{}番目のマス".format(self.field, self.value, self.number)

    def stop(self, p):#止まった時
        if self.field == "x":
            p.x -= self.value#xの値をvalueの値の分減らす
        elif self.field == "y":
            p.y -= self.value

class MulCell(Cell):
    def __init__(self, field, value):
        super().__init__()
        self.field = field
        self.value = value

    def __str__(self):
        return "{}に{}をMulする{}番目のマス".format(self.field, self.value, self.number)

    def stop(self, p):
        if self.field == "x":
            p.x *= self.value
        elif self.field == "y":
            p.y *= self.value

class GateCell1(Cell):
    def stop(self, player):
        if (player.point>=12000 or
                player.point<=-12000):
            player.win = 1
class GateCell2(Cell):
    def stop(self, player):
        if player.point>15000:
            player.win=1
        else:
            player.point+=1000
class GateCell3(Cell):
    def stop(self, player):
        if player.point>10000:
            player.win=1
        else:
            player.point+=1000
class GateCell4(Cell):
    def stop(self, player):#check
        if player.x*player.point>10000:
            player.win = 1

class GateCell5(Cell):
    def stop(self, player):

        player.win = 1

class GateCell6(Cell):
    def stop(self, player):
        if player.point>10000:
            player.win=1
        else:
            player.x+=1


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
        player.x+=player.point/1000

class cell15(Cell):
    def stop(self,player):
        player.other.point-=player.x

class cell16(Cell):
    def stop(self,player):
        player.other.point-=1000

class cell17(Cell):
    def stop(self, player):
        player.point+=player.x

class cell18(Cell):
    def stop(self, player):
        player.point-=player.x
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
        player.point+=player.other.point

class cell26(Cell):
    def stop(self, player):
        player.other.point-=3000

class cell27(Cell):
    def stop(self, player):
        player.other.x=player.x

class cell28(Cell):
    def stop(self, player):
        player.other.point=player.point

class cell29(Cell):
    def stop(self, player):
        player.point+=2000*player.x

class cell30(Cell):
    def stop(self,player):
        player.x+=3
