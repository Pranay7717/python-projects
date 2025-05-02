class Plant:
      def __init__(self, name, height):
        self.name = name
        self.height = height
      def grow(self):
        print(f"{self.name} is growing")
      def description(self):
        print(f"{self.name} has grown {self.height} cm tall")
class FloweringPlant(Plant):
      def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
      def bloom(self):
        print(f"{self.name} plant is blooming with beautiful {self.flower_color} flowers")
rose = FloweringPlant("Rose", 50, "red")
rose.grow()
rose.description()
rose.bloom()