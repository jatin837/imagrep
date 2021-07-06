class Word(object):
    def __init__(self, x:int, y:int, dx:int, dy:int, content:str):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.content = content
    def __repr__(self):
        return f"{self.content} at ({self.x}, {self,y}), dim = ({self.l}X{self.w})"

class Text(object):
    def __init__(self, words:list = []):
        self.words = words
    def __repr__(self):
        return ' '.join([f"{word.content}" for word in self.words])
    def __add__(self, word):
        self.words.append(word)
    def __len__(self):
        return len(self.words)

