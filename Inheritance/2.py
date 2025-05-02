class Plant:
    def __init__(self):
        print("This is a plant")
    def grow(self):
        print("Plant is growing")
class Flower(Plant):
    def __init__(self):
        super().__init__()
        print("This is a flower")
    def bloom(self):
        print("Flower is blooming")
class Rose(Flower):
    def __init__(self):
        super().__init__()
        print("This is a rose")
    def smell(self):
        print("Rose smells good")
my_rose = Rose()
my_rose.grow()
my_rose.bloom()
my_rose.smell()