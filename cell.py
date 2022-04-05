class Cell:
    
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.level = 0
        self.vision = 1
        self.level_up = False
    
    def discover(self, board, n, m):
        neighbors = 0
        for k in range(self.i - self.vision, self.i + self.vision + 1):
            for l in range(self.j - self.vision, self.j + self.vision + 1):
                if 0 <= k < n and 0 <= l < m:
                    if board[k][l] != self:
                        if board[k][l].level >= 1:
                            neighbors += 1
        
        if self.level >= 1:
            if neighbors in [2,3]:
                self.level_up = True
            else:
                self.level_up = False
        else:
            if neighbors == 3:
                self.level_up = True
            else:
                self.level_up = False
    
    def cycle(self):
        if self.level_up:
            if self.level + 1 >= 4:
                self.level = 0
            else:
                self.level += 1
        else:
            if self.level - 1 <= 0:
                self.level = 0
            else:
                self.level -= 1