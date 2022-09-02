class Animal:

    def __init__(self, theNumLegs, theCall, theName):
        self.numLegs = theNumLegs
        self.call = theCall
        self.name = theName

    def speak(self):
        print("Implement method first in the in derived class!")