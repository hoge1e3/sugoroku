import tkinter as tk
from inspect import getsource
import threading

W=800
H=400
class GCell:
    def __init__(self, cell, players, source):
        self.cell=cell
        self.players=players
        self.source=source
class BoardWindow:
    def __init__(self, map, players):
        self.map=map
        self.players=players
        self.window = tk.Tk()
        self.window.title("Board Status")
        self.window.geometry(f"{W}x{H}")
        self.gcells=[]
    def show(self):
        self.seed=tk.Label(self.window,borderwidth=1, relief=tk.SOLID)
        self.seed.grid(row=0,column=0)
        self.main=tk.Frame(self.window,borderwidth=1, relief=tk.SOLID)
        self.main.grid(row=1,column=0)
        self.status=tk.Label(self.window,borderwidth=1, relief=tk.SOLID)
        self.status.grid(row=2,column=0)
        self.message=tk.Label(self.window,borderwidth=1, relief=tk.SOLID)
        self.message.grid(row=3,column=0)
        for y in range(len(self.map)):
            row=self.map[y]
            for x in range(len(row)):
                cell=row[x]
                if not cell: continue
                self.showCell(cell, x, y)
        self.drawPlayer()
    def setSeed(self, val):
        self.seed["text"]=val
    def setStatus(self, val):
        self.status["text"]=val
    def drawPlayer(self):
        for c in self.gcells:
            c.players["text"]=""
            for p in self.players:
                if c.cell==p.cell:
                    c.players["text"]+=p.name
        self.message["text"]=""
        for p in self.players:
            self.message["text"]+=f" [{p.name} point={p.point} x={p.x} y={p.y}] "
    def showCell(self, cell, x,y):
        text=getsource(type(cell))
        gcell=tk.Frame(self.main, borderwidth=1, relief=tk.SOLID )
        source=tk.Label(gcell, text=text, font=("Arial", 10),
                       borderwidth=1, relief=tk.SOLID , justify="left")
        source.grid(row=0,column=0)
        players=tk.Label(gcell, text="players", font=("Arial", 10),)
        players.grid(row=1,column=0)
        gcell.grid(row=y, column=x)
        gc=GCell(cell, players, source)
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
