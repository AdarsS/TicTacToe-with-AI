"""
 Made By u/CamaroBro18
 GitHub CamaroBro180
 A simple single player tic tac toe game
 Player = rectangle or rect
 Computer = circle

"""
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 500))
run = True

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
font = pygame.font.SysFont("comicsansms", 22)

while run:
    # Initialize Board
    screen.fill(black)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    a1 = pygame.draw.rect(screen, white, (25, 25, 100, 100))
    a2 = pygame.draw.rect(screen, white, (150, 25, 100, 100))
    a3 = pygame.draw.rect(screen, white, (275, 25, 100, 100))
    b1 = pygame.draw.rect(screen, white, (25, 150, 100, 100))
    b2 = pygame.draw.rect(screen, white, (150, 150, 100, 100))
    b3 = pygame.draw.rect(screen, white, (275, 150, 100, 100))
    c1 = pygame.draw.rect(screen, white, (25, 275, 100, 100))
    c2 = pygame.draw.rect(screen, white, (150, 275, 100, 100))
    c3 = pygame.draw.rect(screen, white, (275, 275, 100, 100))
    draw_object = 'rect'  # Change whether the computer or player goes first by changing the draw object to rect or circle
    running = True

    # Draw the rectangles
    def draw_rect(r1, r2, r11, r22, p11, p12):
        pygame.draw.rect(screen, red, (r1, r2, r11, r22))
        global draw_object
        draw_object = 'circle'
        board[p11][p12] = 1

    # Draw the circles
    def draw_circle(c10, c20, c11, c22, p12, p22):
        pygame.draw.circle(screen, green, (c10, c20), c11, c22)
        global draw_object
        draw_object = 'rect'
        board[p12][p22] = 2

    # Display the winner
    def display_win():
        if draw_object == 'rect':
            screen.blit(font.render("Computer Won", True, (255, 255, 255)), (50, 400))
            screen.blit(font.render("Press Space to reset", True, (255, 255, 255)), (50, 440))
        else:
            screen.blit(font.render("Player Won", True, (255, 255, 255)), (50, 400))
            screen.blit(font.render("Press Space to reset", True, (255, 255, 255)), (50, 440))

    # Display Draw
    def display_draw():
        screen.blit(font.render("Draw", True, (255, 255, 255)), (50, 400))
        screen.blit(font.render("Press space to reset", True, (255, 255, 255)), (50, 440))

    # Record player moves
    def player_move(pos):
        if draw_object == 'rect':
            if a1.collidepoint(pos) and board[0][0] == 0:
                draw_rect(50, 50, 50, 50, 0, 0)
            if a2.collidepoint(pos) and board[0][1] == 0:
                draw_rect(175, 50, 50, 50, 0, 1)
            if a3.collidepoint(pos) and board[0][2] == 0:
                draw_rect(300, 50, 50, 50, 0, 2)
            if b1.collidepoint(pos) and board[1][0] == 0:
                draw_rect(50, 175, 50, 50, 1, 0)
            if b2.collidepoint(pos) and board[1][1] == 0:
                draw_rect(175, 175, 50, 50, 1, 1)
            if b3.collidepoint(pos) and board[1][2] == 0:
                draw_rect(300, 175, 50, 50, 1, 2)
            if c1.collidepoint(pos) and board[2][0] == 0:
                draw_rect(50, 300, 50, 50, 2, 0)
            if c2.collidepoint(pos) and board[2][1] == 0:
                draw_rect(175, 300, 50, 50, 2, 1)
            if c3.collidepoint(pos) and board[2][2] == 0:
                draw_rect(300, 300, 50, 50, 2, 2)

    # Record computer moves
    def computer_move():
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 9 choices for the computer to make
        x = random.choice(choices)  # x picks a choice from the choices list
        while draw_object == 'circle' and not check_player_won():
            if board[1][1] == 0:  # if the player first move isn't the centre spot the computer will make the move
                draw_circle(200, 200, 35, 35, 1, 1)
                break
            for i in range(0, 3):  # Checks for the winning move. If no winning move is present the computer will choose a random move
                for j in range(0, 3):
                    if board[i][j] == 0:
                        board[i][j] = 2  # 2 - Computer
                        if check_computer_won():
                            if i == 0 and j == 0:
                                draw_circle(75, 75, 35, 35, 0, 0)
                                return False
                            if i == 0 and j == 1:
                                draw_circle(200, 75, 35, 35, 0, 1)
                                return False
                            if i == 0 and j == 2:
                                draw_circle(325, 75, 35, 35, 0, 2)
                                return False
                            if i == 1 and j == 0:
                                draw_circle(75, 200, 35, 35, 1, 0)
                                return False
                            if i == 1 and j == 1:  # Centre spot
                                draw_circle(200, 200, 35, 35, 1, 1)
                                return False
                            if i == 1 and j == 2:
                                draw_circle(325, 200, 35, 35, 1, 2)
                                return False
                            if i == 2 and j == 0:
                                draw_circle(75, 325, 35, 35, 2, 0)
                                return False
                            if i == 2 and j == 1:
                                draw_circle(200, 325, 35, 35, 2, 1)
                                return False
                            if i == 2 and j == 2:
                                draw_circle(325, 325, 35, 35, 2, 2)
                                return False
                        else:
                            board[i][j] = 0
            for i in range(0, 3):  # Checks if the player is going to win. If it returns True, the following statements is going to block the move
                for j in range(0, 3):
                    if board[i][j] == 0:
                        board[i][j] = 1  # 1 - Player
                        if block_player_won():
                            if i == 0 and j == 0:
                                draw_circle(75, 75, 35, 35, 0, 0)
                                return False
                            if i == 0 and j == 1:
                                draw_circle(200, 75, 35, 35, 0, 1)
                                return False
                            if i == 0 and j == 2:
                                draw_circle(325, 75, 35, 35, 0, 2)
                                return False
                            if i == 1 and j == 0:
                                draw_circle(75, 200, 35, 35, 1, 0)
                                return False
                            if i == 1 and j == 1:  # Centre spot
                                draw_circle(200, 200, 35, 35, 1, 1)
                                return False
                            if i == 1 and j == 2:
                                draw_circle(325, 200, 35, 35, 1, 2)
                                return False
                            if i == 2 and j == 0:
                                draw_circle(75, 325, 35, 35, 2, 0)
                                return False
                            if i == 2 and j == 1:
                                draw_circle(200, 325, 35, 35, 2, 1)
                                return False
                            if i == 2 and j == 2:
                                draw_circle(325, 325, 35, 35, 2, 2)
                                return False
                        else:
                            board[i][j] = 0
            if x == 1 and board[0][0] == 0:
                draw_circle(75, 75, 35, 35, 0, 0)
            if x == 2 and board[0][1] == 0:
                draw_circle(200, 75, 35, 35, 0, 1)
            if x == 3 and board[0][2] == 0:
                draw_circle(325, 75, 35, 35, 0, 2)
            if x == 4 and board[1][0] == 0:
                draw_circle(75, 200, 35, 35, 1, 0)
            if x == 6 and board[1][2] == 0:
                draw_circle(325, 200, 35, 35, 1, 2)
            if x == 7 and board[2][0] == 0:
                draw_circle(75, 325, 35, 35, 2, 0)
            if x == 8 and board[2][1] == 0:
                draw_circle(200, 325, 35, 35, 2, 1)
            if x == 9 and board[2][2] == 0:
                draw_circle(325, 325, 35, 35, 2, 2)
            if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:  # check if any positions available if not break out of loop
                break
            else:
                computer_move()  # If in case of repeated choice this will enable it to loop again

    # Check the computer move one step ahead
    def check_computer_won():  # Return true if when the computer gets a win from any of the statements
        global board
        # Row wise
        if board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
            return True
        elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
            return True
        elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
            return True
            # Column wise
        elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
            return True
        elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
            return True
        elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
            return True
            # Diagonally
        elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
            return True
        elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
            return True

    # Check the player move one step ahead
    def block_player_won():  # Return true if when the computer checks and the player gets a win from any of the statements
        global board
        # Row wise
        if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
            return True
        elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
            return True
        elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
            return True
            # Column wise
        elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
            return True
        elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
            return True
        elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
            return True
            # Diagonally
        elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
            return True
        elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
            return True

    #  Check if the player or computer won or Draw
    def check_player_won():
        global board
        # Row wise
        if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or (
                board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]  # To make sure after win player cannot input anymore
            display_win()
            return False
        elif (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or (
                board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
        elif (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or (
                board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
            # Column wise
        elif (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (
                board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
        elif (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (
                board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
        elif (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or (
                board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
            # Diagonally
        elif (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (
                board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
        elif (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1) or (
                board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2):
            board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            display_win()
            return False
            # Draw
        elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 3 not in board[0]:
            display_draw()
            return False


    # Main Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                player_move(position)
                computer_move()
                check_player_won()
            computer_move()
        pygame.display.update()
