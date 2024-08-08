# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN

import pygame as py

class Screen():
 
    # INITIALIZATION OF WINDOW HAVING TITLE,
    # WIDTH, HEIGHT AND COLOUR
    # HERE (0,0,255) IS A COLOUR CODE
    def __init__(self, title, width=440, height=445, fill=(0, 0, 255)):
        
        self.height = height        # HEIGHT OF A WINDOW
        self.title = title          # TITLE OF A WINDOW
        self.width = width          # WIDTH OF A WINDOW
        self.fill = fill            # COLOUR CODE
        self.CurrentState = False   # CURRENT STATE OF A SCREEN
        self.numeroState = 0        # NUMERO DU STATE OF A SCREEN
        print("Screen height:",height)
 
    # DISPLAY THE CURRENT SCREEN OF
    # A WINDOW AT THE CURRENT STATE
    def makeCurrentScreen(self):
       
        # SET THE TITLE FOR THE CURRENT STATE OF A SCREEN
        py.display.set_caption(self.title)
        # SET THE STATE TO ACTIVE
        self.CurrentState = True
        # ACTIVE SCREEN SIZE
        self.screen = py.display.set_mode((self.width, self.height))
                
        #print("screen", screen)         
 
    # THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
    def endCurrentScreen(self):
        print("endCurrentScreen")
        self.CurrentState = False
 
    # THIS WILL CONFIRM WHETHER THE NAVIGATION OCCURS
    def checkUpdate(self, fill):
        # HERE FILL IS THE COLOR CODE
        self.fill = fill
        return self.CurrentState
 
    # THIS WILL UPDATE THE SCREEN WITH
    # THE NEW NAVIGATION TAB
    def screenUpdate(self):
        print("SCreen Update")
        if self.CurrentState:
            self.screen.fill(self.fill)


 
    # RETURNS THE TITLE OF THE SCREEN
    def returnTitle(self):
        return self.screen

    def checkState(self) :
        if (self.CurrentState) :
            return True, 0
        else :
            return False,  self.numeroState   


    def changeCurrentState(self, num) :
        print("CHANGE CURRENT STATE")
        self.numeroState = num 


