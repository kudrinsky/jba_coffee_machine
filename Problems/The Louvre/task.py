class Painting:
    museum = 'Louvre'
    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


certain_painting = Painting(input(), input(), int(input()))
print(f'"{certain_painting.title}" by {certain_painting.painter} ({certain_painting.year}) hangs in the {certain_painting.museum}.')
