import sys
import random
import threading
import gui
import time

map_seed=int(time.time()/100)
#map_seed=17298475
#17298481
#17301936
#17301950　マスが5種類
random.seed(map_seed)

from time import sleep
import tkinter as tk
from inspect import getsource
from cell import *

GOAL_POINT=1
loop=0
mode=[0,1,2]
noSleep=False
trial=0
max_turns=0

dirs=[(1,0),(0,1),(-1,0),(0,-1)]
def sleep2(s):
    if not noSleep:
        sleep(s)
def dir2name(dir):
    return "?u?l?r?d?"[dir[0]+dir[1]*3+4]
def name2dir(n):
    return {"u":(0,-1), "d":(0,1), "l":(-1,0), "r":(1,0)}[n]
def opposite_dir(a,b):
    return a[0]==-b[0] and a[1]==-b[1]
def add_dir(a,b):
    return (a[0]+b[0], a[1]+b[1])
def cell_at(pos):
    (x,y)=pos
    if not 0<=y<len(map):return None
    row=map[y]
    if not 0<=x<len(row):return None
    return row[x]
        
# プレイヤーのステータス
class Player:
    def __init__(self, name, pos,humans):
        self.name = name
        #self.cell = cell
        self.pos=pos
        self.dir=(1,0)
        self.point = 0
        self.win = 0
        self.x = 0
        self.y = 0
        self.human=humans

    def __str__(self):
        return self.name
    def dir_candidates(self):
        cands=[]
        for d in dirs:
            if opposite_dir(self.dir, d): continue
            n=add_dir(self.pos, d)
            cell=cell_at(n)
            if not cell: continue
            cands.append(d)
        return cands
    def select_dir(self):
        candidates=self.dir_candidates()
        if len(candidates)==1:
            return candidates[0]
        if not self.human:
            return candidates[random.randint(0,len(candidates)-1)]
        candNames=list(dir2name(c) for c in candidates)
        return name2dir(board_window.seldir(candNames))

        while True:
            d=input2("どの方向に行きますか:("+"/".join(candNames)+")?")
            if d=="50000":
                exit()
            if d in candNames:
                return name2dir(d)
    
    def step(self):
        self.dir=self.select_dir()
        self.pos=add_dir(self.pos, self.dir)
        board_window.drawPlayer(self)
        sleep2(0.2)
    @property
    def cell(self):
        return cell_at(self.pos)
    def add_point(self, point):
        self.point += point
        if self.point >= GOAL_POINT:
            self.win = 1

    def cast_dice(self):
        # マニュアルモードの処理
        if self.human:
            i=board_window.cast_dice()
            return i
            while 1:
                try:
                    i = int(input2("サイコロを振って，出た数字を入れてください({}-{})?".format(1, 6)))
                except:
                    i=0
                if i==50000:
                    exit()
                if i>=1 and i<=6:
                    break
        else:
            sleep2(1)
            i = random.randint(1, 6)
            print("サイコロを振って{}が出ました".format(i))
        return i

    def input_YN(self,message):
        if not self.human:
            i=random.randint(0,1)
            return "yn"[i]#["y","n"][i]
        else:
            while True:
                i = input2(message + "y/n")
                if i == "y" or i == "n":
                    return i
                else:
                    print("YかNを入力してください")

# 進む処理
def steps(p, p_step):
    for i in range(p_step,1,-1):
        board_window.setDiceLeft(i)
        p.step()
        board_window.setDiceLeft(i-1)
        print(p.cell.number)
        p.cell.over(p)
    board_window.setDiceLeft(1)
    p.step()
    print(p.cell,"に止まりました")
    c = p.cell
    print(getsource(type(c)))
    p.cell.stop(p)


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
middleCellClasses=[
    cell14,cell15,cell16,cell17,cell18,cell19,cell20,cell21,cell22,cell23,cell24,cell25,cell26
]
gateCellClasses=[
    GateCell1,GateCell2,GateCell3,
]
middleGateCellClasses=[
    GateCell4,GateCell5,GateCell6
]
def selectFrom(cellClasses):
    i=random.randint(0, len(cellClasses)-1)
    return cellClasses[i]()

for i in range(13):
    main_route.append(selectFrom(middleCellClasses))
i=random.randint(0,12)
main_route[i]=selectFrom(gateCellClasses)
for i in range(len(main_route)):
    main_route[i].number=i+1
map=[
    [0, 1, 2, 3, 4],
    [5,-1, 6,-1, 7],
    [8, 9,10,11,12]
]
map=list( 
    list(main_route[i] if i>=0 else None for i in row) 
    for row in map)
#print(map)
#exit()

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
humans=int(input("人数を入力してください（0~2）"))
if humans>=100:
    noSleep=True
    trial=humans
    humans=0
    max_turns=100
players=[]
def init_players():
    global p1,p2,players
    for i in range(len(players)):
        del players[0]
    p1 = Player("p1", (0,0), humans>=1)
    p2 = Player("p2", (0,0), humans>=2)
    players.append(p1)
    players.append(p2)
    p1.other=p2
    p2.other=p1
    p1.others=[p1,p2]
    p2.others=[p2,p1]
init_players()

def mainRept():
    play_seed=int(time.time()/100)
    if not trial:
        main(play_seed)
    else:
        sum_turn_count=0
        for i in range(trial):
            sum_turn_count+=main(play_seed)
            play_seed+=100
            init_players()
        print("Average turn count",sum_turn_count/trial)
    exit()
def main(play_seed):
    random.seed(play_seed)
    global turn_count
    turn_count=0
    while 1:
        # 表示を更新
        #status_window.update_display(players)
        board_window.drawPlayer(p1)
        turn(p1)
        if p1.win != 0:
            winner = p1.name
            break
        # 表示を更新
        #status_window.update_display(players)
        board_window.drawPlayer(p2)
        turn(p2)
        if p2.win != 0:
            winner = p2.name
            break
        turn_count += 1
        print("turn:", turn_count)
        print("Loop:",loop)
        if max_turns and turn_count>=max_turns:
            winner = None
            break
    print(winner, " is win")
    print("map_seed= ", map_seed, "play_seed", play_seed, "Turn count",turn_count)
    return turn_count
    
def input2(mesg):
    return board_window.input(mesg)
    #return input(mesg)
board_window=gui.start(map, players)
board_window.show()
board_window.setSeed(map_seed)
gui_thread_instance = threading.Thread(target=mainRept, args=())
gui_thread_instance.start()
board_window.run()
