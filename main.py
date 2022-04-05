from cell import Cell
import tkinter as tk
import random


class Game:
    
    HEIGHT = 800
    WIDTH = 800
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.gen_field(n, m)
        self.gen_entities(self.n * self.m // 4)
        self.level_colors = ['white', '#0b8d00', '#0fbb00', '#11d800','#14ff00']

        
    def gen_field(self, n, m):
        self.field = [[Cell(i, j) for j in range(m)] for i in range(n)]
    
    def gen_entities(self, amount):
        for _ in range(amount):
            while True:
                i = random.randint(0, self.n - 1)
                j = random.randint(0, self.m - 1)
                if not self.field[i][j].level >= 1:
                    self.field[i][j].level = 1
                    break
    
    def step(self):
        for i in self.field:
            for j in i:
                j.discover(self.field, self.n, self.m)
                
        for k in self.field:
            for l in k:
                l.cycle()
    
    def run(self):
        self.block = self.WIDTH / self.m if self.m >= self.n else self.HEIGHT / self.n
        
        self.root = tk.Tk()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.canva = tk.Canvas(self.root, height = self.n * self.block, width = self.m * self.block)
        self.draw()
        
        self.canva.place(relx =0.5, rely = 0.5, anchor="center")
        self.root.mainloop()
    
    def draw(self):
        self.canva.delete('all')
        for i in range(self.n):
            for j in range(self.m):
                self.canva.create_rectangle(j * self.block, i * self.block, self.block + j * self.block, self.block + i * self.block, fill = self.level_colors[self.field[i][j].level])
        self.step()
        self.canva.after(300, self.draw)


g = Game(30, 40)
g.run()
