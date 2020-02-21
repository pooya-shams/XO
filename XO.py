#                        In the name of god                      #
# The XO game : extreme                                          #
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

    def defence_or_end ():
        """ checks if any row is going to be full of X|O """
        rows = list ()
        for row in ALLROWS:
            a = row [0][1]
            b = row [1][1]
            c = row [2][1]
            if a == b != c == E:
                rows.append (row)
            if a == c != b == E:
                rows.append (row)
            if b == c != a == E:
                rows.append (row)
        if len (rows) == 0:
            return None
        elif len (rows) == 1:
            row = rows[0]
            a = row [0][1]
            b = row [1][1]
            c = row [2][1]
            if a == b != c == E:
                return row [2]
            elif a == c != b == E:
                return row [1]
            elif b == c != a == E:
                return row [0]
        elif len (rows) >= 2:
            for row in rows:
                a = row[0][1]
                b = row[1][1]
                c = row[2][1]
                if a == b == X != c == E:
                    return row [2]
                elif a == c == X != b == E:
                    return row [1]
                elif b == c == X != a == E:
                    return row [0]

        return None

    def rowmaker ():
        """ cheks if there is any row maker that we could full it """
        for row in ROW_MAKERS:
            a = row[0][1]
            b = row[1][1]
            c = row[2][1]
            if a == b != c == E:
                return row [2]
            elif a == c != b == E:
                return row [1]
            elif b == c != a == E:
                return row [0]
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

class X_start:
    """ the first three moves when X starts """

    def first_move ():
        """ the best choice in the firs move is one of the corner boxes """
        return CORNER_BOXES [random.randint (0, 3)]

    def sec_move (first_move):
        """ returns the box in the opposite corner of the board """
        try:
            p = CORNER_BOXES.index (first_move)
            return CORNER_BOXES [(p+2)%4]
        except TypeError:
            raise RuntimeError ("somthing bad happened") from None


    def second_move (x_first_move, o_first_move):
        """ if the next box to the first move is full the best move is another cornerbox"""
        global TMOVE_B5
        xf = x_first_move
        of = o_first_move
        p = CORNER_BOXES.index (xf)
        if of != BOX5 and of != CORNER_BOXES [(p-1)%4] and of != CORNER_BOXES [(p+1)%4]:
            if of in SIDE_BOXES:
                TMOVE_B5 = True
                for row in ALLROWS:
                    if xf in row and of in row and CORNER_BOXES[(p-1)%4] in row:
                        return CORNER_BOXES [(p+1)%4]
                    elif xf in row and of in row and CORNER_BOXES[(p+1)%4] in row:
                        return CORNER_BOXES [(p-1)%4]
                return CORNER_BOXES [[(p-1)%4,(p+1)%4][random.randint(0,1)]]

            TMOVE_B5 = False
            return CORNER_BOXES [[(p-1)%4,(p+1)%4][random.randint(0,1)]]

        elif of == BOX5 or of == CORNER_BOXES [(p-1)%4] or of == CORNER_BOXES [(p+1)%4]:
            return X_start.sec_move (xf)

    def third_move ():
        """ the third move is the best time to make a dilemma """
        if TMOVE_B5:
            return BOX5
        elif not (TMOVE_B5):
            return check_all_rows.rowmaker ()

    def random_move ():
        """ if there is no possible boxes to win, we
        just make a random decision to continue the game """
        boxes = list ()
        for box in ALLBOXES:
            if box [1] == E:
                boxes.append(box)
        return boxes [random.randint(0, len(boxes)-1)]


class O_start :
    """ the first moves when O starts """

    def first_move ():
        """ the best move is BOX5, if it is full one of the corner boxes is the best"""
        if BOX5 [1] == E:
            return BOX5
        elif BOX5 [1] != E:
            return CORNER_BOXES [random.randint (0, 3)]

    def second_move (xfirst_move, ofirst_move):
        xf = xfirst_move
        of = ofirst_move
        if xf == BOX5:
            if of in CORNER_BOXES :
                if X_start.sec_move (of)[1] == E:
                    return X_start.sec_move (of)
                elif X_start.sec_move (of)[1] != E:
                    return SIDE_BOXES [random.randint (0, 3)]
            elif not (of in CORNER_BOXES) :
                boxes = list ()
                for row in ALLROWS:
                    if of in row:
                        for box in row:
                            if box[1] == E and box in CORNER_BOXES:
                                boxes.append(box)
                            else:
                                pass
                return boxes [random.randint(0, len(boxes)-1)]


        elif xf != BOX5:
            if X_start.sec_move (xf)[1] == E:
                return check_all_rows.defence_or_end ()
            elif X_start.sec_move (xf)[1] != E:
                for box in CORNER_BOXES:
                    if box[1] == E:
                        return box
        return None

    def random_move ():
        """ if there is no possible boxes to win, we
        just make a random decision to continue the game """
        boxes = list ()
        for box in ALLBOXES:
            if box [1] == E:
                boxes.append(box)
        return boxes [random.randint(0, len(boxes)-1)]

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
    global XSCORES, OSCORES, DSCORES, DISPLAYSURF, TMOVE_B5
    DISPLAYSURF = base.make_window ()
    base.draw_board ()
    XSTART = True
    OSTART = False
    runing = True
    TURN = 0
    TMOVE_B5 = False
    pygame.display.set_caption("XO")
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
                            if TURN == 2:
                                O_FIRST_MOVE = box

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
                if TURN == 0:
                    box = X_start.first_move ()
                    X_FIRST_MOVE = box

                if TURN == 2:
                    box = X_start.second_move (X_FIRST_MOVE, O_FIRST_MOVE)

                if TURN == 4:
                    box = X_start.third_move ()

                if check_all_rows.defence_or_end()!=None:
                    box = check_all_rows.defence_or_end ()

                if box == None :
                    box = X_start.random_move ()

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
                            if TURN == 1:
                                O_FIRST_MOVE = box

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
                box = None
                if TURN == 1:
                    box = O_start.first_move ()
                    X_FIRST_MOVE = box

                if TURN == 3:
                    box = O_start.second_move (X_FIRST_MOVE, O_FIRST_MOVE)

                if check_all_rows.defence_or_end () != None:
                    box = check_all_rows.defence_or_end ()

                if box == None:
                    box = O_start.random_move ()

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
