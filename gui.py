# show/hide  fields by level
import tkinter as tk
from inspect import getsource
import threading
from random import randint
from time import sleep
from cell import StateCell
W=1000
H=800
class GCell:
    def __init__(self, cell, players, source, fields):
        self.cell=cell
        self.players=players
        self.source=source
        self.fields=fields
dirs=["l","u","d","r"]
dir_label={"l":"←", "u":"↑", "d":"↓", "r":"→"}

class BoardWindow:
    def __init__(self, map, players):
        def ex():
            self.window.destroy()
            self.exited=True
            exit()
        self.exited=False
        self.map=map
        self.players=players
        self.window = tk.Tk()
        self.window.title("Board Status")
        self.window.geometry(f"{W}x{H}")
        self.window.protocol("WM_DELETE_WINDOW", ex)
        self.gcells=[]
        self.dice_status=None
        self.dir_status=None
    def input(self, mesg):
        self.setMessage(mesg)
        self.entered=False
        self.inputE.delete(0,tk.END)
        while not self.entered:
            sleep(0.1)
            if self.exited: break
        return self.inputE.get()
    def do_cast(self):
        self.dice_button["state"]=tk.DISABLED
        self.dice_status="casting"
    def cast_dice(self):
        self.dice_label["text"]="サイコロを振ってください:"
        self.dice_button["state"]=tk.NORMAL
        self.dice_status="waitPush"
        while self.dice_status=="waitPush":
            if self.exited: break
            sleep(0.05)
        for i in range(20):
            res=randint(1,6)
            self.dice_label["text"]=str(res)
            sleep(0.05)
        return res
    def do_seldir(self,d):
        if self.dir_buttons[d]["state"]==tk.DISABLED:
            return
        self.dir_status=d
        self.disable_dirs()
    def disable_dirs(self):
        for d in dirs:
            self.dir_buttons[d]["state"]=tk.DISABLED
    def seldir(self,cands):
        self.dir_label["text"]="どちらに行きますか:"
        self.disable_dirs()
        for c in cands:
            self.dir_buttons[c]["state"]=tk.NORMAL
        self.dir_status="selecting"
        while self.dir_status=="selecting":
            sleep(0.05)
        self.dir_label["text"]=""
        return self.dir_status
    def show(self):
        font=("Arial", 15)
        self.seed=tk.Label(self.window,borderwidth=1, relief=tk.SOLID, font=font)
        self.seed.grid(row=0,column=0)
        self.main=tk.Frame(self.window,borderwidth=1, relief=tk.SOLID)
        self.main.grid(row=1,column=0)
        self.status=tk.Label(self.window,borderwidth=1, relief=tk.SOLID, font=font)
        self.status.grid(row=2,column=0)
        self.dice_frame=tk.Frame(self.window,borderwidth=1, relief=tk.SOLID)
        self.dice_frame.grid(row=3,column=0)
        if self.dice_frame:
            self.dice_label=tk.Label(self.dice_frame,borderwidth=1, relief=tk.SOLID, font=font)
            self.dice_label.grid(row=0,column=0)
            self.dice_button=tk.Button(self.dice_frame,text="サイコロを振る",command=lambda *_:self.do_cast(),state=tk.DISABLED, font=font)
            self.dice_button.grid(row=0,column=1)
        self.dir_frame=tk.Frame(self.window,borderwidth=1, relief=tk.SOLID)
        self.dir_frame.grid(row=4,column=0)
        def db(d,i):
            self.dir_buttons[d]=tk.Button(self.dir_frame,text=dir_label[d],command=lambda *_:self.do_seldir(d),state=tk.DISABLED, font=font)
            self.dir_buttons[d].grid(row=0,column=i)
        self.window.bind("<Left>", lambda _:self.do_seldir("l"))
        self.window.bind("<Right>",lambda _:self.do_seldir("r"))
        self.window.bind("<Up>",   lambda _:self.do_seldir("u"))
        self.window.bind("<Down>", lambda _:self.do_seldir("d"))
        self.window.bind("<space>", lambda _:self.do_cast())
        if self.dir_frame:
            self.dir_label=tk.Label(self.dir_frame,text="", font=font)
            self.dir_label.grid(row=0,column=0)
            self.dir_buttons={}
            i=1
            for d in dirs:
                db(d,i)
                i+=1
        self.messageInput=tk.Frame(self.window,borderwidth=1, relief=tk.SOLID)
        self.messageInput.grid(row=5,column=0)
        if self.messageInput:
            self.message=tk.Label(self.messageInput, borderwidth=1, relief=tk.SOLID)
            self.message.grid(row=0,column=0)
            self.inputE=tk.Entry(self.messageInput)
            self.inputE.grid(row=0,column=1)
        def entered(e):
            self.entered=True
        self.inputE.bind("<Return>", entered)
        for y in range(len(self.map)):
            row=self.map[y]
            for x in range(len(row)):
                cell=row[x]
                if not cell: continue
                self.showCell(cell, x, y)
        self.drawPlayer(self.players[0])
    def setSeed(self, val):
        self.seed["text"]=val
    def setMessage(self, val):
        self.dice_label["text"]=val
    def setDiceLeft(self, c):
        self.dice_label["text"]="残り: "+str(c)
    def drawPlayer(self,turn):
        for c in self.gcells:
            c.source["foreground"]="#000000"
            if c.fields:
                c.fields["text"]=c.cell.fields()
        for c in self.gcells:
            c.players["text"]=""
            for p in self.players:
                if c.cell==p.cell:
                    c.players["text"]+=p.name
                    if p==turn:
                        c.source["foreground"]="#ff0000" if p.name=="p1" else "#0000ff"

        self.status["text"]=""
        for p in self.players:
            if p==turn:
                self.status["text"]+="*"
            self.status["text"]+=f"[{p.name} point= {p.point} x={p.x} y={p.y}]  "
    def showCell(self, cell, x,y):
        font=("Courier New", "9")
        text=getsource(type(cell))
        text=convert_indent_4_to_2(text)
        gcell=tk.Frame(self.main, borderwidth=1, relief=tk.SOLID )
        source=tk.Label(gcell, text=text, font=font,
                       borderwidth=1, relief=tk.SOLID , justify="left")
        source.grid(row=0,column=0)       
        players=tk.Label(gcell, text="players", font=font)
        #    borderwidth=1, relief=tk.SOLID , justify="left")
        fld=cell.fields()
        if fld!=None:
            fields = tk.Label(gcell, font=font, text=fld,
                borderwidth=1, relief=tk.SOLID , justify="left")
            fields.grid(row=1, column=0)
            players.grid(row=2,column=0)
        else: 
            fields=None
            players.grid(row=1,column=0)

        gcell.grid(row=y, column=x)
        gc=GCell(cell, players, source, fields)
        self.gcells.append(gc)
        return gc
    def run(self):
        self.window.mainloop()
class PlayerStatusWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Player Status")
        self.window.geometry("800x400")
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
#status_window = PlayerStatusWindow()
#status_window.initialize_window()
def gui_thread(window):
    window.mainloop()
def start(map, players):
    board_window=BoardWindow(map, players)
    return board_window

def convert_indent_4_to_2(code):
    lines = code.splitlines()
    converted_lines = []
    for line in lines:
        leading_spaces = len(line) - len(line.lstrip())
        new_indent = ' ' * (leading_spaces // 4 * 2)
        content = line.lstrip()
        converted_lines.append(new_indent + content)  
    return '\n'.join(converted_lines)