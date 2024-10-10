import sys
import random

import threading
from time import sleep
import tkinter as tk
from inspect import getsource

GOAL_POINT=1
loop=0
# プレイヤーのステータス
class Player:
    def __init__(self, name, cell,players):
        self.name = name
        self.cell = cell
        self.point = 0
        self.other=players
        self.win = 0
        self.dice = 1
        self.x = 0
        self.y = 0
    def my_index(self):
        return self.other.index(self)
    def other_player(self, i):
        ps=len(self.other)
        return self.other[ (self.my_index()+i+ps*100)%ps ]
    def __str__(self):
        return self.name
    def step(self):
        if self.cell.next == None:
            raise ValueError(self.cell.number)
        self.cell = self.cell.next
    def add_point(self, point):
        self.point += point
        if self.point >= GOAL_POINT:
            self.win = 1



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
        if player.point>=12:
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
        if input_YN("宝箱があります開けますか？"):
            print("罠でした")
            player.point-=1
        else:
            print("見なかったことにしました")
            player.point+=2
    def over(self, player):
        pass


def input_YN(message):
    while True:
        i = input(message + "Y/N")
        if i == "Y":
            return True
        elif i == "N":
            return False
        else:
            print("YかNを入力してください")
# 進む処理
def steps(p, p_step):
    for i in range(p_step - 1):
        p.step()
        print(p.cell.number)
        p.cell.over(p)
    p.step()
    print(p.cell,"に止まりました")
    c = p.cell
    print(getsource(type(c)))
    p.cell.stop(p)


# cellからi番目のcellを探す
def cell_by_index(cell, i):
    for j in range(i):
        cell = cell.next

    if cell == None:
        raise ValueError(i)
    return cell


# ターン処理
def turn(p):
    print(" ")
    print("{}のターンです。".format(p))
    print("{}".format(p.cell))
    before_x = p.x
    before_y = p.y
    bnum = p.cell.number
    print(" x:", before_x, "→", p.x, " y:", before_y, "→", p.y)
    print(" points:", p.point, " position:", bnum, "→", p.cell.number)
    p_step = cast_dice()
    if p_step!=0:
        steps(p, p_step)
    print(p.name, "step:", p_step)

cell_ID = 0


def create_chain(cell_array):
    for i in range(1, len(cell_array)):
        cell_array[i - 1].next = cell_array[i]
    return cell_array[0]



def last_cell(cell):
    while cell.next != None:
        cell = cell.next
    return cell


# １～６と決まってるから引数なし
def cast_dice():
    # マニュアルモードの処理
    if auto_play == "manual":
        i = int(input("サイコロを振って，出た数字を入れてください({}-{})?".format(1, 6)))
    else:
        i = random.randint(1, 6)
        print("サイコロを振って{}が出ました".format(i))
    return i


def player_choice(n):
    if auto_play == "manual":
        i = int(input("({}-{})?".format(1, n)))
    else:
        i = random.randint(1, n)
        print("{}が自動で選択されました".format(i))
    return i


# 手動にしたいならmanualを実行時引数に
args = sys.argv
if len(args) > 1:
    auto_play = args[1]
else:
    auto_play = "auto"
main_route = [
]
normalCellClasses=[
    cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9,cell10,cell11,cell12,cell13
]

gateCellClasses=[
    GateCell1,GateCell2,GateCell3,
]
def selectFrom(cellClasses):
    i=random.randint(0, len(cellClasses)-1)
    return cellClasses[i]()

for i in range(12):
    main_route.append(selectFrom(normalCellClasses))
i=random.randint(0,11)
main_route[i]=selectFrom(gateCellClasses)
gate_cell=main_route[i]

for i in range(len(main_route)):
    main_route[i].number=i+1
print("今回の勝利条件：",gate_cell.number," 番目のマス")
print(getsource(type(gate_cell)))


start = create_chain(main_route)
last_cell(start).next = start

def addstr(c, val):
    def s(self):
        return val+" 番号："+str(self.number)
    c.__str__=s
def addstrAll(cellClasses, start):
    for c in cellClasses:
        addstr(c, f"セル種類：{start}")
        start+=1
addstrAll(normalCellClasses, 1)
addstrAll(gateCellClasses, 100)


turn_count = 0
players=[]
p1 = Player("p1", start,players)
p2 = Player("p2", start,players)
players.append(p1)
players.append(p2)

class PlayerStatusWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Player Status")
        self.window.geometry("600x400")
        self.font_size = 50
        self.labels = []
    def initialize_window(self):
        headers = ["Name", "X", "Y", "Point"]
        for col, header in enumerate(headers):
            label = tk.Label(self.window, text=header, font=("Arial", self.font_size))
            label.grid(row=0, column=col, padx=10, pady=10)
        # プレイヤーの情報用のラベルを事前に作成
        for row in range(1, 3):  # 2人分のプレイヤー用
            row_labels = []
            for col in range(4):  # 4つの列（Name, X, Y, Point)
                label = tk.Label(self.window, text="", font=("Arial", self.font_size))
                label.grid(row=row, column=col, padx=10, pady=10)
                row_labels.append(label)
            self.labels.append(row_labels)
    def update_display(self, players):
        for row, player in enumerate(players):
            self.labels[row][0].config(text=player.name)
            self.labels[row][1].config(text=str(player.x))
            self.labels[row][2].config(text=str(player.y))
            self.labels[row][3].config(text=str(player.point))
    def run(self):
        self.window.mainloop()
status_window = PlayerStatusWindow()
status_window.initialize_window()
def gui_thread(status_window):
    status_window.run()
gui_thread_instance = threading.Thread(target=gui_thread, args=(status_window,))
gui_thread_instance.start()
sleep(1)

while 1:
    # 表示を更新
    status_window.update_display(players)
    turn(p1)
    if p1.win != 0:
        winner = p1.name
        break
    # 表示を更新
    status_window.update_display(players)
    turn(p2)
    if p2.win != 0:
        winner = p2.name
        break
    turn_count += 1
    print("turn:", turn_count)
    print("Loop:",loop)

print(winner, " is win")
exit()
