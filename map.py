
from random import randint
import random

class Room(object):

    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self,direction):
        return self.paths.get(direction, None)

    def add_paths(self,paths):
        self.paths.update(paths)

opening_scene = Room("Pilot",
"""You just arrived to the tomb.
        Maria your asistant is giving you any new infomration about the tomb.
        You cant believed it..all of your years of work finally paid of..
        You found Tutanahmon tomb with the legendary tressure..
        the opening gate is too small for a big crew..u can only enter you with Maria,
        or sent someone else with her..what will u do ? """
)


antechamber = Room("antechamber",
"""
you enter the antechamber,u cant see anything...
        you hears bones crushing as you walk..that cant be a good sign..u managed
        to find a torch,but the light is the medical kit Kostas gave u..
        to open the medical kit you need a 3 digit code that kostas yelled at you
        but you didnt catch any of them..u should guess was???
""")


main_chamber = Room("the_main_chamber",
"""
you and maria enter the main chamber..the room is a 3x3
        square of squares..you must find the correct path..u can only go
        forward,left or right.u stand in the middle square of the first row..
        you only have 5 tries.
        if dont find the correct path,nails will come oute the floor..
        which path will you choose?the square is like this
""")

riddles ={
        "There is a certain crime, that if it is attempted, is punishable, but if it is committed, is not punishable. What is the crime?": "suicide",
        "There are four days which start with the letter 'T',tuesday and thursday,name the other two." : "today and tommorow",
        """A boy and his father are caught in a traffic accident, and the father dies.
        Immediately the boy is rushed to a hospital, suffering from injuries.
        But the attending surgeon at the hospital, upon seeing the boy, says
        'I cannot operate. This boy is my son.'

        How is this situation explained ?""" : "she is his mother",
        }
riddle = random.choice(riddles.keys())
last_chamber = Room("the_last_chamber",
"""
you finally reached the last chamber,
        you cant believe what you are witnessing..an army of
        skeletons is front a big gate..their leader speaks..
        I SHALL TELL YOU A RIDDLE IF YOU FIND THE correct ANSWER
        TUTANAHAMON TRESSURE IS YOURS..the riddle is: %s
""" % riddle)


the_end_winner = Room("The_End",
"""
u finally found the tressure,is magnificent..
        you look at maria,she starts cryning..you hug and kiss her..you tell her
        you want to spent the rest of your life with..she said she wants too.
        that was it..THE end
""")


the_end_loser = Room("The_End",
"""
u wasnt able to finish the task..this was a one in a life time
        opportunity...the end
"""
)

corpass = "%s%s%s" %(randint(0,9),randint(0,9), randint(0,9))
antechamber.add_paths({
    corpass: main_chamber,
    '*': the_end_loser
})

correctpath = "forward,left,right"


main_chamber.add_paths({
    correctpath: last_chamber,
    '*': the_end_loser
})

corrans = riddles[riddle]
last_chamber.add_paths({
    corrans: the_end_winner,
    '*': the_end_loser
})

opening_scene.add_paths({
    'go with her': antechamber,
    'sent someone else': the_end_loser,
})

START = opening_scene
