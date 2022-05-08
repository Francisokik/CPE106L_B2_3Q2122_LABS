
myfont = pygame.font.SysFont("Comic Sans MS", 70)
 
while not gameOver:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, boxSize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, LIGHTBLUE, (posx, int(boxSize/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, BEIGE, (posx, int(boxSize/2)), RADIUS)
        pygame.display.update()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, boxSize))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/boxSize))
 
                if validLoc(board, col):
                    row = nextRow(board, col)
                    piecePlayed(board, row, col, 1)
 
                    if winCondition(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, LIGHTBLUE)
                        screen.blit(label, (40,10))
                        gameOver = True

            # # Ask for Player 2 Input and Tie
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/boxSize))
 
                if validLoc(board, col):
                    row = nextRow(board, col)
                    piecePlayed(board, row, col, 2)
 
                    if winCondition(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, BEIGE)
                        screen.blit(label, (40,10))
                        gameOver = True
                    
                    if checkTie(board, 1, 2):
                        label = myfont.render("TIE/DRAW", 1, WHITE)
                        screen.blit(label, (40,10))
                        gameOver = True 
                    

            printBoard(board)
            makeBoard(board)

            #players are taking turns
            turn += 1
            turn = turn % 2

        #Game over 
        if gameOver:
            pygame.time.wait(3000)
            
                
                
                        