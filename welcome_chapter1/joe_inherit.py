##########
# ******** Simulate Ducks game ********
##########
# Add function, to make all the duck can fly.

#Superclass
class Duck():
    def __init__(self, mode):
        self.mode = mode

    def quack(self):
        print(self.__class__.__name__ + ": Ga Ga Ga")

    def swim(self):
        print(self.__class__.__name__ + ": Swim in a pool")

    def display(self):       #self method can be reload in subclass.
        print(self.__class__.__name__)

    def fly(self):
        print(self.__class__.__name__ + ": fly in the sky")



#subclass
class MallardDuck(Duck):
    def display(self):      #Green head
        print(self.__class__.__name__ + ": display as " + self.mode)


class RedheadDuck(Duck):
    def display(self):       #Red head
        print(self.__class__.__name__ + ": display as " + self.mode)


class RubberDuck(Duck):
    def display(self):
        print(self.__class__.__name__ + ": display as " + self.mode)

if __name__ == '__main__':
    greenduck = MallardDuck("Mallard")
    redduck = RedheadDuck("Redhead")
    rubberduck = RubberDuck("Rubber")

    greenduck.quack()
    greenduck.swim()
    greenduck.display()
    greenduck.fly()

    redduck.quack()
    redduck.swim()
    redduck.display()
    redduck.fly()

    rubberduck.quack()
    rubberduck.swim()
    rubberduck.display()
    rubberduck.fly()         #Question: Rubberduck should not fly in the sky. So inherit reuse cannot resolve self problem.