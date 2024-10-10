import sys
import random

import threading
from time import sleep
import tkinter as tk
from inspect import getsource
from cell import *

GOAL_POINT=1
loop=0
mode=[0,1,2]

# プレイヤーのステータス
class Player:
    def __init__(self, name, cell,players,humans):
        self.name = name
        self.cell = cell
        self.point = 0
        self.others=players
        self.win = 0
        self.dice = 1
        self.x = 0
        self.y = 0
        self.human=humans

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

    def cast_dice(self):
        # マニュアルモードの処理
        if self.human:
            while 1:
                try:
                    i = int(input("サイコロを振って，出た数字を入れてください({}-{})?".format(1, 6)))
                except:
                    i=0
                if i>=1 and i<=6:
                    break
        else:
            i = random.randint(1, 6)
            print("サイコロを振って{}が出ました".format(i))
        return i

    def input_YN(self,message):
        if not self.human:
            i=random.randint(0,1)
            return "yn"[i]#["y","n"][i]
        else:
            while True:
                i = input(message + "y/n")
                if i == "y" or i == "n":
                    return i
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
    p_step = p.cast_dice()
    if p_step!=0:
        steps(p, p_step)
    print(p.name, "step:", p_step)



def create_chain(cell_array):
    for i in range(1, len(cell_array)):
        cell_array[i - 1].next = cell_array[i]
    return cell_array[0]

def last_cell(cell):
    while cell.next != None:
        cell = cell.next
    return cell

# １～６と決まってるから引数なし

# 手動にしたいならmanualを実行時引数に
args = sys.argv
if len(args) > 1:
    auto_play = args[1]
else:
    auto_play = "manual"
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
for i in range(len(main_route)):
    main_route[i].number=i+1

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
humans=int(input("人数を入力してください（0~2）"))
p1 = Player("p1", start,players, humans>=1)
p2 = Player("p2", start,players, humans>=2)
players.append(p1)
players.append(p2)
p1.other=p2
p2.other=p1
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
