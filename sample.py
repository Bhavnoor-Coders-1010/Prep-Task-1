import numpy as np
import time
import pygame

def game(finalArr, r, c):
    for i in range(r):
        for j in range(c):
            count = 0
            if(i>0):
                if(j>0 and finalArr[i-1][j-1] in [1,-2]):
                    count+=1
                if(j<cols-1 and finalArr[i-1][j+1] in [1,-2]):
                    count+=1
                if(finalArr[i-1][j] in [1,-2]):
                    count+=1
            if(i<rows-1):
                if(j>0 and finalArr[i+1][j-1] in [1,-2]):
                    count+=1
                if(j<cols-1 and finalArr[i+1][j+1] in [1,-2]):
                    count+=1
                if(finalArr[i+1][j] in [1,-2]):
                    count+=1
            if(j>0 and finalArr[i][j-1] in [1,-2]):
                count+=1
            if(j<cols-1 and finalArr[i][j+1] in [1,-2]):
                count+=1
            # print(count)

            if finalArr[i][j]==1:
                if count<2 or count>3:
                    finalArr[i][j]=-2
                else:
                    continue
            elif finalArr[i][j]==0:
                if count==3:
                    finalArr[i][j]=-1

    for i in range(r):
        for j in range(c):
            if finalArr[i][j]==-1:
                finalArr[i][j]=1
            elif finalArr[i][j]==-2:
                finalArr[i][j]=0
    
    
    return finalArr

def call(array, numRows, numCols):
    array = game(array, numRows, numCols)
    print(menu)
    print(f"Updated\n",array, sep='')

def changeMatrix(arr, template):
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                template[i][j] = pygame.draw.rect(win, (50+5*((i+j)%2),50+5*((i+j)%2),50+5*((i+j)%2)), (j*50, i*50, 50, 50))
            else:
                template[i][j] = pygame.draw.rect(win, (255-10*((i+j)%2),255-10*((i+j)%2),0), (j*50, i*50, 50, 50))

def changeOnClick(arr, template, pos):
    
    for i in range(rows):
        for j in range(cols):
            if(template[i][j].collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and clicked[i][j] == False):
                if(arr[i][j] == 1):
                    arr[i][j] = 0
                    template[i][j] = pygame.draw.rect(win, (50+5*((i+j)%2),50+5*((i+j)%2),50+5*((i+j)%2)), (j*50, i*50, 50, 50))
                else:
                    arr[i][j] = 1
                    template[i][j] = pygame.draw.rect(win, (255-10*((i+j)%2),255-10*((i+j)%2),0), (j*50, i*50, 50, 50))
                clicked[i][j] = True
                print(menu)
                print(f"Updated\n",arr, sep='')

                
            if pygame.mouse.get_pressed()[0] == 0:
                clicked[i][j] = False
                
    
def resetGrid(arr):
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = 0

rows = int(input("Enter number of Rows: "))
cols = int(input("Enter number of Columns: "))

lst = []
clicked = []
for i in range(rows):
    lst.append([0]*cols)
    clicked.append([False]*cols)
finalArr = np.array(lst)

menu = '''
Press "s" to change(1 step) onto the next result
Press "b" to begin automatic simulation 
Press "p" to pause the automatic simulation
Press "r" to reset the grid
(Click on the cells to change their state)'''
if(rows>15 or cols>25):
    print("Please re-run the program with rows<=15 and columns<=25")
    exit()
randomDist = input("Do you want to assign the matrix randomly?(Please enter yes or no)")

if(randomDist.lower() == "yes"):
    for i in range(rows):
        for j in range(cols):
            finalArr[i][j] = round(np.random.random())

print(menu)
print("Intial Array\n",finalArr, sep='')



running = False
pygame.init()
win = pygame.display.set_mode((cols*50,rows*50))
pygame.display.set_caption("Conway's Game of Life")
while True:
    win.fill((0,0,0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_s:
                call(finalArr, rows, cols)
            if events.key == pygame.K_b:
                running = True
            if events.key == pygame.K_p:
                running = False
            if events.key == pygame.K_r:
                resetGrid(finalArr)
    
    
    if running:
        call(finalArr, rows, cols)
        time.sleep(1)
            
    for i in range(rows):
        for j in range(cols):
            lst[i][j] = pygame.draw.rect(win, (50+5*((i+j)%2),50+5*((i+j)%2),50+5*((i+j)%2)), (j*50, i*50, 50, 50))
    
    changeOnClick(finalArr, lst,  pygame.mouse.get_pos())
    changeMatrix(finalArr, lst)
        
    pygame.display.update()