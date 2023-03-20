from fsm import *
#import state
#Implementation av controllen (i vårat fall ps4 kontroll va?)
#Input till konstruktorn är bara exempel
class controller:
    def __init__(self, fsm, type):
        self.myfsm = fsm
        self.type = type

    #Exempel på funktioner som kan bli kallade när en specifik knapp trycks på
    def cross_pressed(self):
        #exempel method när x trycks på.
        #Förslagsvis kan detta skicka en signal till fsm att byta state till mobile?
        print("cross pressed")
        self.myfsm.change_state("mobile")
        
    def circle_pressed(self):
        #exempel method när o trycks på.
        #Förslagsvis kan detta skicka en signal till fsm att byta state till idle?
        print("circle pressed")
        self.myfsm.change_state("idle")
        
    def triangle_pressed(self):
        #exempel method när triangel trycks på.
        #Förslagsvis kan detta skicka en signal till fsm att byta state till recon?
        print("triangle pressed")
        self.myfsm.change_state("recon")

