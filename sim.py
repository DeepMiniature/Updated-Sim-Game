import pygame 

pygame.init()
window = pygame.display.set_mode((800, 800))
font = pygame.font.Font('BENGUIAB.ttf', 24)
running = True
run = True 
red = []
blue = []
res = False
count = 0
circle_draw = []
for i in range(49):
    circle_draw.append(False) 

def initial():
    global pos, loc, line, permanent, blue, red, count,freq,countfir,circle_draw
    pos = []
    loc = []
    freq = []
    for i in range(49):
        tup = ((i%7)*100+100,(i//7)*100+100)
        loc.append(tup)
        pos.append(False)
        freq.append(0)
    line = 'no'
    permanent = []
    countfir = -1
    circle_draw = []
    for k in range(49):
            circle_draw.append(False)


def game_over(x):
    global font, run, permanent
    
    if(x == "white"):
        a = (255,255,255)
        winner = font.render('Winner is : White', True, (255,255,255))
    
    if(x == "green"):
        a = (68,214,44)
        winner = font.render('Winner is : Green', True, (68,214,44))
    
    initial()
    
    run = False
    restart = font.render("For Rematch Press : r", True, a)
    exit = font.render("For Exit Press : e",True, a)
    window.blit(winner, (300, 300))
    window.blit(restart, (270, 380))
    window.blit(exit, (300, 460))

initial()

while(running):
    
    window.fill((0,0,0))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if(event.key == pygame.K_r):
                res = True

            if(event.key == pygame.K_e):
                pygame.quit()
        
        if event.type == pygame.KEYUP:
            
            if(event.key == pygame.K_r):
                res = False
    
    if(res):
        initial()
        run = True
        red = []
        blue = []
        count = 0
        
    if(pygame.mouse.get_pressed() == (1,0,0) and run == True):
        for i in range(49):
            if(pygame.mouse.get_pos()[0] < (loc[i][0]+5) and pygame.mouse.get_pos()[0] > (loc[i][0]-5) and pygame.mouse.get_pos()[1] < (loc[i][1]+5) and pygame.mouse.get_pos()[1] > (loc[i][1]-5)):
                pos[i] = True
                circle_draw[i] = True
                if(countfir == -1):
                    countfir = i
    
    colour = 	(135,206,235) 
    circle_x = (150, 50)
    circle_radius = 12
    border_width = 0 
    circle_x = (150, 50)
    
    if(run):
        for i in range(49):
            if (circle_draw[i] == True):
                pygame.draw.circle(window, (255,0,0), loc[i], 5, border_width)
            else:
                pygame.draw.circle(window, colour, loc[i], 5, border_width)
   
    for i in range(49):
        
        if (pos[i] == True):
        
            for j in range(49):
        
                if(i == j):
                    continue
        
                elif(pos[j] == True):
                    add = []
                    
                    pygame.draw.line(window, colour, loc[i], loc[j], 2)
                    count += 1
                    for k in range(49):
                        pos[k] = False 
                    add.append(i)
                    add.append(j)
                
                    if(add not in permanent):
                        permanent.append(add)
                        freq[i] += 1
                        freq[j] += 1                    

    for k in range(len(permanent)):
       
        if(k%2 == 0):
            pygame.draw.line(window, (255,255,255), loc[permanent[k][0]], loc[permanent[k][1]], 2)
       
        if(k%2 == 1):
            pygame.draw.line(window, (68,214,44), loc[permanent[k][0]], loc[permanent[k][1]], 2)

    counter = 0
    for k in freq:
        if (k>1 and counter == countfir):
            if(count%2 == 0):
                game_over("white")
            else:
                game_over("green")
        elif (k>2 and counter != countfir):
            if(count%2 == 0):
                game_over("white")
            else:
                game_over("green")
        
        counter += 1

    if(run == False):
        if(count%2 == 0):
                game_over("white")
        else:
                game_over("green")

    pygame.display.update()