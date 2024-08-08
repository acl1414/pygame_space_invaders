# SCREEN CLASS FOR WINDOW HAVING THE FUNCTION OF UPDATING THE ONE SCREEN TO ANOTHER SCREEN

import pygame as py

from pygame import *

from screen import Screen
from button import Button 

class MenuScreen(Screen):
 
    # INITIALIZATION OF WINDOW HAVING TITLE,
    # WIDTH, HEIGHT AND COLOUR
    # HERE (0,0,255) IS A COLOUR CODE
    def __init__(self, title, width, height, fill=(0, 0, 255)):
      super().__init__(title, width, height, fill=(0, 0, 255))

      self.width=width
      # CREATION DES BUTTON
      self.MENU_BUTTON2 = Button((width-150)/2, 200, 150, 50, (255, 250, 250), (255, 0, 0), "TimesNewRoman", (255, 255, 255), "JOUER")
      self.MENU_BUTTON_QUIT = Button((width-150)/2, 270, 150, 50, (255, 250, 250), (255, 10, 10), "TimesNewRoman", (255, 255, 255), "QUITTER")
      
      # Load custom font
      self.custom_font = py.font.Font("assets/PIXEL CRAFT.ttf", 48)

      self.changeS = False



    def screenUpdate(self):

      super()
 
      
 
      mouse_pos = py.mouse.get_pos()          # STORING THE MOUSE EVENT TO CHECK THE POSITION OF THE MOUSE
      mouse_click = py.mouse.get_pressed()    # CHECKING THE MOUSE CLICK EVENT
      keys = py.key.get_pressed()             # KEY PRESSED OR NOT

    

      button_play_Pressed = self.MENU_BUTTON2.focusCheck(mouse_pos, mouse_click)
      button_quit_Pressed = self.MENU_BUTTON_QUIT.focusCheck(mouse_pos, mouse_click)
      
      if (button_play_Pressed) :
          super().endCurrentScreen()
          super().changeCurrentState(1)

      if (button_quit_Pressed) :
          py.quit()


    def screenDisplay(self):
      
      text_menu_width, text_height = self.custom_font.size("MENU")   # recupération with of text
      text_menu_posX = (self.width - (text_menu_width) ) / 2                          # récupération x pour centrer text

      text = self.custom_font.render('MENU', True, (0, 255, 0), (0, 0, 0))
      self.screen.blit(text, (text_menu_posX, 20))

      self.MENU_BUTTON2.showButton(self.returnTitle())
      self.MENU_BUTTON_QUIT.showButton(self.returnTitle()) 







  
