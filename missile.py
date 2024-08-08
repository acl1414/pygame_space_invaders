import pygame as py

from constantes import Constantes

 
class Missile():
 
    # INITIALIZATION 
    def __init__(self, x, y, delta_y):
        
        self.x = x
        self.y = y
        self.delta_y = delta_y

        self.height=15
        self.wifth=5
        imageTemp=py.image.load('assets/missile.png')
        self.image=py.transform.scale(imageTemp,(5,15))
        self.is_to_delete= False
      
        
      
 
    # DRAW THE BUTTON FOR THE TWO
    # TABS MENU_SCREEN AND CONTROL TABS MENU
    def display(self, screen):

        screen.blit(self.image , (self.x, self.y))
    
    def update(self):

        self.y=self.y - self.delta_y
        if (self.y<0) :
            self.is_to_delete = True

    def is_to_deleted (self):
        return self.is_to_delete       

    
     
 
    