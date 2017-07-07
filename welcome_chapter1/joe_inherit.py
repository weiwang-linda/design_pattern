##########
# ******** Simulate Ducks game ********
##########
# Add function, to make all the duck can fly.

#Superclass
class Duck():
    def __init__(this, mode):
        this.mode = mode

    def quack(this):
        print(this.__class__.__name__ + ": Ga Ga Ga")

    def swim(this):
        print(this.__class__.__name__ + ": Swim in a pool")

    def display(this):       #This method can be reload in subclass.
        print(this.__class__.__name__)

    def fly(this):
        print(this.__class__.__name__ + ": fly in the sky")



#subclass
class MallardDuck(Duck):
    def display(this):      #Green head
        print(this.__class__.__name__ + ": display as " + this.mode)


class RedheadDuck(Duck):
    def display(this):       #Red head
        print(this.__class__.__name__ + ": display as " + this.mode)


class RubberDuck(Duck):
    def display(this):
        print(this.__class__.__name__ + ": display as " + this.mode)

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
    rubberduck.fly()         #Question: Rubberduck should not fly in the sky. So inherit reuse cannot resolve this problem.