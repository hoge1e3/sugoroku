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
        if (player.point>=12 or
                player.point<=-12):
            player.win = 1
        else:
            player.point-=1


class GateCell2(Cell):
    def stop(self, player):
        if player.point>15:
            player.win=1
        else:
            player.point+=-1


class GateCell3(Cell):
    def stop(self, player):
        if player.point>10 and player.point%2==1:
            player.win=1
        else:
            player.point+=1
class GateCell4(Cell):
    def stop(self, player):
        if player.x+player.point>100:
            player.win = 1

class GateCell5(Cell):
    def stop(self, player):

        player.win = 1

class GateCell6(Cell):
    def stop(self, player):
        if player.point>10:
            player.win=1
        else:
            player.x+=1


class cell1(Cell):
    def stop(self, player):
        player.point+=1


class cell2(Cell):
    def stop(self, player):
        player.point-=1


class cell3(Cell):
    def stop(self, player):
        player.point+=3


class cell4(Cell):
    def stop(self, player):
        player.point+=3

class cell5(Cell):
    def stop(self, player):
        player.point-=1

class cell6(Cell):
    def stop(self, player):
        player.point*=2

class cell7(Cell):
    def stop(self, player):
        player.point-=3

class cell8(Cell):
    def stop(self, player):
        player.point+=-2

class cell9(Cell):
    def stop(self, player):
        player.point-=-2

class cell10(Cell):
    def stop(self, player):
        player.point+=-3

class cell11(Cell):
    def stop(self, player):
        player.point=player.other.point

class cell12(Cell):
    def stop(self, player):
        player.point-=-1

class cell13(Cell):
    def stop(self, player):
        if player.input_YN("y/n")=="y":
            player.point-=1
        else:
            player.point+=2

class cell14(Cell):
    def stop(self,player):
        player.x+=1

class cell15(Cell):
    def stop(self,player):
        player.other.point-=player.x

class cell16(Cell):
    def stop(self,player):
        player.other.point-=5

class cell17(Cell):
    def stop(self, player):
        player.point+=player.x

class cell18(Cell):
    def stop(self, player):
        player.point-=player.x
class cell19(Cell):
    def stop(self, player):
        player.other.point+=player.x

class cell20(Cell):
    def stop(self, player):
        player.other.x-=4

class cell21(Cell):
    def stop(self, player):
        player.point+=5

class cell22(Cell):
    def stop(self,player):
        player.x+=player.other.x

class cell23(Cell):
    def stop(self, player):
        player.point+=player.other.other.x

class cell24(Cell):
    def stop(self, player):
        player.other.x-=player.x

class cell25(Cell):
    def stop(self, player):
        player.point+=player.other.point

class cell26(Cell):
    def stop(self, player):
        player.other.point-=3

class cell27(Cell):
    def stop(self, player):
        player.other.x=player.x

class cell28(Cell):
    def stop(self, player):
        player.other.point=player.point
