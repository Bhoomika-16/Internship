import pygame, sys
from tkinter import *

from button import Button

pygame.init()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


splash_root1 = Tk()
splash_root1.title("jimmy")
splash_root1.geometry("1280x720")
splash_root1.configure(bg='#250218')
# Add image file
bg = PhotoImage(file="assets/title.png")
bg1 = PhotoImage(file="assets/dbit.png")
bg2 = PhotoImage(file="assets/arl.png")
# Show image using label
label1 = Label(splash_root1, image=bg)
label1.place(x=0, y=-50)
label2 = Label(splash_root1, image=bg1)
label2.place(x=300, y=350)
label3 = Label(splash_root1, image=bg2)
label3.place(x=900, y=370)

splash_label = Label(splash_root1, text="""
THIS PROJECT IS DONE IN COLLABRATION WITH

DON BOSCO INSTITUTE OF TECHNOLOGY 
&
AUTOMATA RESEARCH LABORTORY""", font=("arial", 15), fg="white", bg="#250218")
splash_label.place(x=400, y=350)

splash_label2 = Label(splash_root1, text="""DESIGNED AND DEVELOPED BY:
ASHWATH(1DB19CS017)
BHOOMIKA(1DB19CS024)
GAGANA(1DB19CS050)""", font=("arial", 15), fg="white", bg="#250218")
splash_label2.place(x=100, y=600)

splash_label4 = Label(splash_root1, text="""UNDER THE GUIDANCE:
MR RAGHAVENDRA SWAMY H 
AUTOMATA RESEARCH LABORATORIES""", font=("arial", 15), fg="white", bg="#250218")
splash_label4.place(x=500, y=600)

splash_label5 = Label(splash_root1, text="""PROJECT COORDINATOR:
DR VENUGEETHA Y
PROFESSOR AT DBIT""", font=("arial", 15), fg="white", bg="#250218")
splash_label5.place(x=1000, y=600)


def play():
    while True:
        import game 


def help():
    SCREEN = pygame.display.set_mode((1280, 720))
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("aliceblue")
        HELP_TEXT = get_font(40).render("HOW TO PLAY", True, "Black")
        HELP_RECT = HELP_TEXT.get_rect(center=(640, 50))

        HELP_TEXT1 = get_font(20).render("TO AVOID OBSTACLES JUMP OVER THEM USING SPACE KEY", True, "Black")
        HELP_RECT1 = HELP_TEXT1.get_rect(center=(640, 150))
        HELP_TEXT2 = get_font(20).render("COLLECT COINS AS MUCH AS POSSIBLE TO IMPROVE SCORE", True, "Black")
        HELP_RECT2 = HELP_TEXT2.get_rect(center=(640, 250))
        HELP_TEXT3 = get_font(20).render("TO CATCH THE THIEF COLLECT ATTACK POWERUP 5 TIMES ", True, "Black")
        HELP_RECT3 = HELP_TEXT3.get_rect(center=(640, 350))
        HELP_TEXT4 = get_font(20).render("ONLY THREE LIVES WILL BE GIVEN!!!SO PLAY SAFE TO SURVIVE", True, "Black")
        HELP_RECT4 = HELP_TEXT4.get_rect(center=(640, 450))
        SCREEN.blit(HELP_TEXT, HELP_RECT)
        SCREEN.blit(HELP_TEXT1, HELP_RECT1)
        SCREEN.blit(HELP_TEXT2, HELP_RECT2)
        SCREEN.blit(HELP_TEXT3, HELP_RECT3)
        SCREEN.blit(HELP_TEXT4, HELP_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(75), base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def about():
    SCREEN = pygame.display.set_mode((1280, 720))
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        x = 1

        SCREEN.fill("aliceblue")
        HELP_TEXT = get_font(40).render("ABOUT THE GAME", True, "Black")
        HELP_RECT = HELP_TEXT.get_rect(center=(640, 50))
        HELP_TEXT1 = get_font(15).render("THROUGH THIS PROJECT WE HAVE TRIED TO IMPLEMENT AN AI BASED GAMING ENGINE. ",
                                         True, "Black")
        HELP_RECT1 = HELP_TEXT1.get_rect(center=(640, 100))
        HELP_TEXT2 = get_font(13).render("UNDER THE GUIDANCE OF MR.RAGHAVENDRA SWAMY H ,FOUNDER AND PROPRIETOR AT",
                                         True, "Black")
        HELP_RECT2 = HELP_TEXT2.get_rect(center=(640, 150))
        HELP_TEXT5 = get_font(20).render("AUTOMATA RESEARCH LABORATORIES", True, "Black")
        HELP_RECT5 = HELP_TEXT5.get_rect(center=(640, 185))
        logo1 = pygame.transform.scale(pygame.image.load("assets/logo1.jpeg"), (120, 120))
        SCREEN.blit(logo1, (580, 200))

        HELP_TEXT6 = get_font(13).render("PROJECT COORDINATOR:", True, "Black")
        HELP_RECT6 = HELP_TEXT6.get_rect(center=(640, 350))
        HELP_TEXT7 = get_font(13).render("DR.VENUGEETHA Y", True, "Black")
        HELP_RECT7 = HELP_TEXT7.get_rect(center=(640, 370))
        HELP_TEXT9 = get_font(13).render("PROFESSOR", True, "Black")
        HELP_RECT9 = HELP_TEXT9.get_rect(center=(640, 390))
        HELP_TEXT8 = get_font(20).render("DON BOSCO INSTITUTE OF TECHNOLOGY", True, "Black")
        HELP_RECT8 = HELP_TEXT8.get_rect(center=(640, 420))

        logo = pygame.transform.scale(pygame.image.load("assets/logo.png"), (130, 130))
        SCREEN.blit(logo, (580, 430))
        HELP_TEXT3 = get_font(13).render("DESIGNED AND DEVELOPED BY: ", True, "Black")
        HELP_RECT3 = HELP_TEXT3.get_rect(center=(640, 600))
        HELP_TEXT4 = get_font(13).render(
            "ASHWATH D PADUR(1DB19CS017) BHOOMIKA B POOJARI(1DB19CS024) GAGANA(1DB19CS050)", True, "Black")
        HELP_RECT4 = HELP_TEXT4.get_rect(center=(640, 630))
        SCREEN.blit(HELP_TEXT, HELP_RECT)
        SCREEN.blit(HELP_TEXT1, HELP_RECT1)
        SCREEN.blit(HELP_TEXT2, HELP_RECT2)
        SCREEN.blit(HELP_TEXT5, HELP_RECT5)
        SCREEN.blit(HELP_TEXT6, HELP_RECT6)
        SCREEN.blit(HELP_TEXT7, HELP_RECT7)
        SCREEN.blit(HELP_TEXT9, HELP_RECT9)
        SCREEN.blit(HELP_TEXT8, HELP_RECT8)
        SCREEN.blit(HELP_TEXT3, HELP_RECT3)
        SCREEN.blit(HELP_TEXT4, HELP_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(1200, 680), text_input="BACK", font=get_font(30), base_color="Black",
                              hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    splash_root.destroy()
    pygame.display.set_caption("JIMMY-The police dog")
    icon = pygame.image.load('i1.jpeg')
    pygame.display.set_icon(icon)
    TITLE = pygame.image.load("assets/title1.png")
    BG = pygame.transform.scale(pygame.image.load("assets/bg.png"), (1280, 800))
    SCREEN = pygame.display.set_mode((1280, 720))
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(TITLE, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#edad29")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 400))

        PLAY_BUTTON = Button(image=None, pos=(640, 480), text_input="PLAY", font=get_font(40), base_color="#d7fcd4",
                             hovering_color="Red")
        HELP_BUTTON = Button(image=None, pos=(640, 530), text_input="HELP", font=get_font(40), base_color="#d7fcd4",
                             hovering_color="Red")
        ABOUT_BUTTON = Button(image=None, pos=(640, 580), text_input="ABOUT", font=get_font(40), base_color="#d7fcd4",
                              hovering_color="Red")
        QUIT_BUTTON = Button(image=None, pos=(640, 630), text_input="QUIT", font=get_font(40), base_color="#d7fcd4",
                             hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HELP_BUTTON, QUIT_BUTTON, ABOUT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def splash():
    splash_root1.destroy()

    global splash_root
    splash_root= Tk()
    splash_root.title("jimmy")
    splash_root.geometry("1280x720")
    splash_root.configure(bg='#250218')

    splash_label = Label(splash_root, text="DISCLAIMER", font=("TIMES NEW ROMAN", 40), fg="white", bg="#250218")
    splash_label.pack(pady=20)
    splash_label = Label(splash_root, text=
    """Copyright 2022 'DON BOSCO INSTITUTE OF TECHNOLOGY', 'AUTOMATA RESEARCH LABORATORY'


    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated,
    documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:


    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
    Software.


    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE 
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
    CONTRACT,TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
    DEALINGS IN THE SOFTWARE. """, font=("times new roman", 15), fg="white", bg="#250218")
    splash_label.pack(pady=25)

    splash_root.after(5000, main_menu)


splash_root1.after(5000, splash)

mainloop()
