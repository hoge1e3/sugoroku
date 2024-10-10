import tkinter as tk
from inspect import getsource
import threading

def boardLen(start):
    c=1
    s=start
    while True:
        s=s.next
        if s==start:
            return c
        c+=1
W=800
H=400
class BoardWindow:
    def __init__(self,start,players):
        self.start=start
        self.players=players
        self.window = tk.Tk()
        self.window.title("Board Status")
        self.window.geometry(f"{W}x{H}")
    def show(self):
        start=self.start
        n=boardLen(start)
        s=start
        x=0
        y=0
        h=(n+1)//2
        for i in range(h):
            self.showCell(s, x, y)
            x+=1
            s=s.next
        y+=1
        for i in range(n-h):
            x-=1
            self.showCell(s, x, y)
            s=s.next

    def showCell(self, cell, x,y):
        text=getsource(type(cell))
        cell=tk.Frame(self.window, borderwidth=1, relief=tk.SOLID )
        source=tk.Label(cell, text=text, font=("Arial", 10),
                       borderwidth=1, relief=tk.SOLID , justify="left")
        source.grid(row=0,column=0)
        players=tk.Label(cell, text="players", font=("Arial", 10),)
        players.grid(row=1,column=0)
        cell.grid(row=y, column=x)
        return cell
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
def start(start, players):
    board_window=BoardWindow(start, players)
    gui_thread_instance = threading.Thread(target=gui_thread, args=(board_window.window,))
    gui_thread_instance.start()
    return board_window
