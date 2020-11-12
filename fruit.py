class food(object):
 
# init method or constructor
    def __init__(self, fruit, color, tasty):
        self.fruit = fruit
        self.color = color
        self.tasty = tasty 
 
    def show(self): 
        print ("fruit is", self.fruit)
        print ("color is", self.color )
        print ("is it tasty?", self.tasty)
 
apple = food("apple", "red", "yes")
grapes = food("grapes", "green", "no")
orange = food("orange", "orange", "yes")
 
apple.show()
grapes.show()
orange.show()