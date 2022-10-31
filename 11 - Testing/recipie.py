class Recipie:

  def __init__(self):
    self.items = []

  def add_ingredient(self, item):
    self.items.append(item)

  def num_ingredients(self):
    return len(self.items)

  def get_ingredients(self):
    return self.items