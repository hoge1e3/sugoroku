cell_ID=0
# Cellはマス目。
class Cell:
    def __init__(self):
        global cell_ID
        cell_ID += 1
        self.number = cell_ID
        self.next = None
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

    def stop(self, p):#止まった時
        if self.field == "x":
            p.x *= self.value#xの値をvalueの値の分掛けた値にする
        elif self.field == "y":
            p.y *= self.value




class GateCell1(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "{}番目のGateCell1".format(self.number)

    def stop(self, player):#マスに止まったとき、「通り過ぎたとき」になる。
        if player.point>=12 or player.point<=-12:
            player.win = 1
        else:
            player.point-=1
    def over(self, player):#通り過ぎたとき
        pass


class GateCell2(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "{}番目のGateCell2".format(self.number)

    def stop(self, player):#マスに止まったとき、「通り過ぎたとき」になる。
        if player.point%2==1:
            player.win=1
        else:
            pass
    def over(self, player):#通り過ぎたとき
        pass


class GateCell3(Cell):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "{}番目のGateCell3".format(self.number)

    def stop(self, player):#マスに止まったとき、「通り過ぎたとき」になる。

        player.win=1

    def over(self, player):#通り過ぎた時
        pass

class cell1(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point+=1
    def over(self, player):
        pass

class cell2(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point-=2
    def over(self, player):
        pass

class cell3(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point=3
    def over(self, player):
        pass

class cell4(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point+=3
    def over(self, player):
        pass
class cell5(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point-=1
    def over(self, player):
        pass
class cell6(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point=2
    def over(self, player):
        pass
class cell7(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point-=3
    def over(self, player):
        pass
class cell8(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point+=-2
    def over(self, player):
        pass
class cell9(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point-=-2
    def over(self, player):
        pass
class cell10(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point+=-2
    def over(self, player):
        pass
class cell11(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point+=2
    def over(self, player):
        pass
class cell12(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        player.point-=-1
    def over(self, player):
        pass
class cell13(Cell):
    def __init__(self):
        super().__init__()
    def stop(self, player):
        if player.input_YN("宝箱があります開けますか？")=="y":  #"y","n","!="
            print("罠でした")
            player.point-=1
        else:
            print("見なかったことにしました")
            player.point+=2
    def over(self, player):
        pass
