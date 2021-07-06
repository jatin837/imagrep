class Word(object):
    def __init__(self, content, x, y, width, height):
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{self.content} at ({self.x}, {self.y}) with width = {self.width} and height = {self.height}"

class Text(object):
    def __init__(self, words):
        self.words = words
    
    def to_text(self):
        return ' '.join([word.content for word in self.words])

