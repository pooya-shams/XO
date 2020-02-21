#                        In the name of god                      #
# The XO game : easy                                             #
# Author : Pooya.Sh.K                                            #

import pygame, sys, time, random
from pygame.locals import *
pygame.init ()

# VARIABLES

WINDOWWIDTH  = 640 # the width of the games window
WINDOWHEIGHT = 690 # the height of the games window
LINELENGHT = 540 # lenght of the board lines
SIDEGAP = 50 # the gaps between the window and the board
LINEWIDTH = 3 # the width of the board line in pixels
LINEGAPS = 178 # the gaps between lines
XSCORES = 0 # the games X won
OSCORES = 0 # the games O won
DSCORES = 0 # the draw games
FONT = pygame.font.Font('freesansbold.ttf', 40) # the font object

# lines coordinates

LINECORS_START_POS = ((228, 50 ), (409, 50 ), (50 , 228), (50 , 409))
LINECORS_END_POS   = ((228, 590), (409, 590), (590, 228), (590, 409))

#           R    G    B
WHITE   = (255, 255, 255)
BLACK   = ( 0 ,  0 ,  0 )
RED     = (255,  0 ,  0 )
GREEN   = ( 0 , 255,  0 )
BLUE    = ( 0 ,  0 , 255)
CYAN    = ( 0 , 255, 255)
MAGENTA = (255,  0 , 255)
YELLOW  = (255, 255,  0 )
ORANGE  = (128, 128,  0 )

BGCOLOR = GREEN
LINECOLOR = MAGENTA
XCOLOR = RED
OCOLOR = BLUE
POINT_FG_COLOR = YELLOW
POINT_BG_COLOR = CYAN

X = "X"
O = "O"
E = "EMPTY"

# box features
#         x ,  y  ,(XOE)
BOX1 = [(139, 139),  E]
BOX2 = [(320, 139),  E]
BOX3 = [(501, 139),  E]
BOX4 = [(139, 320),  E]
BOX5 = [(320, 320),  E]
BOX6 = [(501, 320),  E]
BOX7 = [(139, 501),  E]
BOX8 = [(320, 501),  E]
BOX9 = [(501, 501),  E]

ALLBOXES = (BOX1, BOX2, BOX3,
            BOX4, BOX5, BOX6,
            BOX7, BOX8, BOX9)

CORNER_BOXES = (BOX1, BOX3, BOX9, BOX7)
SIDE_BOXES = (BOX2, BOX4, BOX8, BOX6)

ALLROWS = ((BOX1, BOX2, BOX3),
           (BOX4, BOX5, BOX6),
           (BOX7, BOX8, BOX9),
           (BOX1, BOX4, BOX7),
           (BOX2, BOX5, BOX8),
           (BOX3, BOX6, BOX9),
           (BOX1, BOX5, BOX9),
           (BOX3, BOX5, BOX7))

ROW_MAKERS = ((BOX1, BOX3, BOX9),
              (BOX3, BOX9, BOX7),
              (BOX9, BOX7, BOX1),
              (BOX7, BOX1, BOX3))


class base:
    """ class for making the bases """

    def make_window ():
        """ makes a window """
        DISPLAYSURF = pygame.display.set_mode ((WINDOWWIDTH, WINDOWHEIGHT))
        DISPLAYSURF.fill (BGCOLOR)
        pygame.display.update ()
        return DISPLAYSURF

    def draw_board ():
        """ draws a (#) shaped board """
        for i in range (4):
            pygame.draw.line (DISPLAYSURF, LINECOLOR, LINECORS_START_POS[i],
                              LINECORS_END_POS [i],LINEWIDTH)
        pygame.display.update ()

    def reset ():
        """ resets the screen """
        DISPLAYSURF.fill (GREEN)
        base.draw_board ()
        for box in ALLBOXES:
            box [1] = E
        pygame.display.update ()


class check_all_rows:
    """ class for checking all rows """

    def winner ():
        """ checks if any row is full of X or O & ++ the players score"""
        for row in ALLROWS:
            a = row[0][1]
            b = row[1][1]
            c = row[2][1]
            if a == b == c != E:
                if a == b == c == X:
                    pygame.draw.line (DISPLAYSURF, ORANGE, row[0][0], row[2][0], LINEWIDTH+5)
                    pygame.display.update ()
                    draw.winner (X)
                    return X
                if a == b == c == O:
                    pygame.draw.line (DISPLAYSURF, ORANGE, row[0][0], row[2][0], LINEWIDTH+5)
                    pygame.display.update ()
                    draw.winner (O)
                    return O
        return None


class draw :
    """ class for drawing X or O in a BOX """

    def X (box):
        """ draws X in the givven box """
        x = box[0][0]
        y = box[0][1]
        rlline = ((x+70, y-70), (x-70, y+70))
        lrline = ((x-70, y-70), (x+70, y+70))
        pygame.draw.line (DISPLAYSURF, XCOLOR, rlline[0], rlline[1], LINEWIDTH)
        pygame.draw.line (DISPLAYSURF, XCOLOR, lrline[0], lrline[1], LINEWIDTH)
        pygame.display.update ()
        return

    def O (box):
        """ draws O in the givven box """
        x = box[0][0]
        y = box[0][1]
        pygame.draw.circle (DISPLAYSURF, OCOLOR, (x, y), 70, 10)
        pygame.display.update ()
        return

    def scores ():
        """ draws the players scores """
        printxscores = FONT.render("X:"+str(XSCORES), True, RED   , CYAN    )
        printoscores = FONT.render("O:"+str(OSCORES), True, BLUE  , YELLOW  )
        printdscores = FONT.render("D:"+str(DSCORES), True, GREEN , MAGENTA )
        xrect = printxscores.get_rect ()
        orect = printoscores.get_rect ()
        drect = printdscores.get_rect ()
        xrect.center = (100, 640)
        orect.center = (540, 640)
        drect.center = (330, 640)
        DISPLAYSURF.blit (printxscores, xrect)
        DISPLAYSURF.blit (printoscores, orect)
        DISPLAYSURF.blit (printdscores, drect)

    def winner (w):
        if w == X:
            fon = FONT.render("Sorry but 'I' scored! :P", True, BLUE, YELLOW)
        if w == O:
            fon = FONT.render("congrats! 'you' could score!! :O", True, BLUE, YELLOW)
        if w == E:
            fon = FONT.render("this game was 'draw'. :|", True, BLUE, YELLOW)
        rec = fon.get_rect ()
        rec.center = (320, 345)
        DISPLAYSURF.blit (fon, rec)
        pygame.display.update ()
        time.sleep (1)
        return None


def random_move ():
    """ if there is no possible boxes to win, we
    just make a random decision to continue the game """
    boxes = list ()
    for box in ALLBOXES:
        if box [1] == E:
            boxes.append(box)
    return boxes[random.randint(0, len(boxes)-1)]

def take_players_choice (mousex, mousey):
    """ if the event is mouse click, returns the clicked box """
    x = mousex
    y = mousey
    for box in ALLBOXES:
        bx = range(box[0][0]-89, box[0][0]+90)
        by = range(box[0][1]-89, box[0][1]+90)
        if (x in bx) and (y in by):
            return box

    return None


def main (): # the main game function #
    global XSCORES, OSCORES, DSCORES, DISPLAYSURF
    DISPLAYSURF = base.make_window ()
    base.draw_board ()
    XSTART = True
    OSTART = False
    runing = True
    TURN = 0
    while runing: # the main game loop
        if XSTART == True and OSTART == False:
            for e in pygame.event.get ():
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    runing = False
                    pygame.quit ()
                    sys.exit ()
                if e.type == MOUSEBUTTONUP and TURN % 2 == 1:
                    box = take_players_choice (pygame.mouse.get_pos()[0],
                                               pygame.mouse.get_pos()[1])
                    if box in ALLBOXES:
                        if box [1] == E:
                            box [1] = O
                            draw.O (box)
                            TURN += 1

            if TURN == 9 or check_all_rows.winner ()!=None:
                if check_all_rows.winner () == X:
                    XSCORES += 1
                    XSTART, OSTART = True, False
                    base.reset ()
                    TURN = 0
                    continue
                elif check_all_rows.winner () == O:
                    OSCORES += 1
                    XSTART, OSTART = False, True
                    base.reset ()
                    TURN = 0
                    continue
                elif TURN == 9:
                    draw.winner (E)
                    DSCORES += 1
                    XSTART, OSTART = OSTART, XSTART
                    base.reset ()
                    TURN = 0
                    continue

            if TURN % 2 == 0: 
                box = None
                box = random_move ()
                if box in ALLBOXES:
                    box [1] = X
                    draw.X (box)
                    TURN += 1

            if TURN == 9 or check_all_rows.winner ()!=None:
                if check_all_rows.winner () == X:
                    XSCORES += 1
                    XSTART, OSTART = True, False
                    base.reset ()
                    TURN = 0
                    continue
                elif check_all_rows.winner () == O:
                    OSCORES += 1
                    XSTART, OSTART = False, True
                    base.reset ()
                    TURN = 0
                    continue
                elif TURN == 9:
                    draw.winner (E)
                    DSCORES += 1
                    XSTART, OSTART = OSTART, XSTART
                    base.reset ()
                    TURN = 0
                    continue

        if XSTART == False and OSTART == True:
            for e in pygame.event.get ():
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    runing = False
                    pygame.quit ()
                    sys.exit ()
                if e.type == MOUSEBUTTONUP and TURN % 2 == 0:
                    box = take_players_choice (pygame.mouse.get_pos()[0],
                                               pygame.mouse.get_pos()[1])
                    if box in ALLBOXES:
                        if box [1] == E:
                            box [1] = O
                            draw.O (box)
                            TURN += 1

            if TURN == 9 or check_all_rows.winner ()!=None:
                if check_all_rows.winner () == X:
                    XSCORES += 1
                    XSTART, OSTART = True, False
                    base.reset ()
                    TURN = 0
                    continue
                elif check_all_rows.winner () == O:
                    OSCORES += 1
                    XSTART, OSTART = False, True
                    base.reset ()
                    TURN = 0
                    continue
                elif TURN == 9:
                    draw.winner (E)
                    DSCORES += 1
                    XSTART, OSTART = OSTART, XSTART
                    base.reset ()
                    TURN = 0
                    continue

            if TURN % 2 == 1:
                box = random_move ()
                if box in ALLBOXES:
                    if box[1] == E:
                        box [1] = X
                        draw.X (box)
                        TURN += 1

            if TURN == 9 or check_all_rows.winner ()!=None:
                if check_all_rows.winner () == X:
                    XSCORES += 1
                    XSTART, OSTART = True, False
                    base.reset ()
                    TURN = 0
                    continue
                elif check_all_rows.winner () == O:
                    OSCORES += 1
                    XSTART, OSTART = False, True
                    base.reset ()
                    TURN = 0
                    continue
                elif TURN == 9:
                    draw.winner (E)
                    DSCORES += 1
                    XSTART, OSTART = OSTART, XSTART
                    base.reset ()
                    TURN = 0
                    continue


        if TURN == 9 or check_all_rows.winner ()!=None:
            if check_all_rows.winner () == X:
                XSCORES += 1
                XSTART, OSTART = True, False
                TURN = 0
                base.reset ()
                continue
            elif check_all_rows.winner () == O:
                OSCORES += 1
                XSTART, OSTART = False, True
                TURN = 0
                base.reset ()
                continue
            elif TURN == 9:
                draw.winner (E)
                DSCORES += 1
                XSTART, OSTART = OSTART, XSTART
                TURN = 0
                base.reset ()
                continue


        draw.scores ()
        pygame.display.update ()


if __name__ == "__main__":
    main ()
