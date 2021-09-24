import pygame, sys, random

#Mouse over all six buttons
def maze_hover():
    if 420 <= pygame.mouse.get_pos()[0] <= 660 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, yellow_hi, pygame.Rect(420, 10, 240, 90)) 
        screen.blit(maze_surface1, maze_rect1)
        screen.blit(maze_surface2, maze_rect2)
    else:
        pygame.draw.rect(screen, yellow, pygame.Rect(420, 10, 240, 90)) 
        screen.blit(maze_surface1, maze_rect1)
        screen.blit(maze_surface2, maze_rect2)

def randompattern_hover():
    if 670 <= pygame.mouse.get_pos()[0] <= 910 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, purple_hi, pygame.Rect(670, 10, 240, 90)) 
        screen.blit(randompattern_surface1, randompattern_rect1)
        screen.blit(randompattern_surface2, randompattern_rect2)
    else:
        pygame.draw.rect(screen, purple, pygame.Rect(670, 10, 240, 90)) 
        screen.blit(randompattern_surface1, randompattern_rect1)
        screen.blit(randompattern_surface2, randompattern_rect2)

def clear_hover():
    if 920 <= pygame.mouse.get_pos()[0] <= 1160 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, green_hi, pygame.Rect(920, 10, 240, 90)) 
        screen.blit(clear_surface1, clear_rect1)
        screen.blit(clear_surface2, clear_rect2)
    else:
        pygame.draw.rect(screen, green, pygame.Rect(920, 10, 240, 90)) 
        screen.blit(clear_surface1, clear_rect1)
        screen.blit(clear_surface2, clear_rect2)

def astar_hover():
    if 1170 <= pygame.mouse.get_pos()[0] <= 1410 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, orange_hi, pygame.Rect(1170, 10, 240, 90)) 
        screen.blit(astar_surface1, astar_rect1)
        screen.blit(astar_surface2, astar_rect2)
    else:
        pygame.draw.rect(screen, orange, pygame.Rect(1170, 10, 240, 90)) 
        screen.blit(astar_surface1, astar_rect1)
        screen.blit(astar_surface2, astar_rect2)

def dijkstra_hover():
    if 1420 <= pygame.mouse.get_pos()[0] <= 1660 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, blue_hi, pygame.Rect(1420, 10, 240, 90)) 
        screen.blit(dijkstra_surface1, dijkstra_rect1)
        screen.blit(dijkstra_surface2, dijkstra_rect2)
    else:
        pygame.draw.rect(screen, blue, pygame.Rect(1420, 10, 240, 90)) 
        screen.blit(dijkstra_surface1, dijkstra_rect1)
        screen.blit(dijkstra_surface2, dijkstra_rect2)

def depthfirst_hover():
    if 1670 <= pygame.mouse.get_pos()[0] <= 1910 and 10 <= pygame.mouse.get_pos()[1] <= 100:
        pygame.draw.rect(screen, pink_hi, pygame.Rect(1670, 10, 240, 90)) 
        screen.blit(depthfirst_surface1, depthfirst_rect1)
        screen.blit(depthfirst_surface2, depthfirst_rect2)
    else:
        pygame.draw.rect(screen, pink, pygame.Rect(1670, 10, 240, 90)) 
        screen.blit(depthfirst_surface1, depthfirst_rect1)
        screen.blit(depthfirst_surface2, depthfirst_rect2)

def draw_board():
    
    #Drawing blank board

    timeleft = 0

    while timeleft < 900:
        clock.tick(36)
        timeleft += 18

        row_num = int(timeleft/36-1)
        for i in range(0,50):
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+i*38, 120+row_num*38, 37, 37))

        pygame.display.update()

    timeleft = 18

    while timeleft > -1:

        #Starting point
        pygame.draw.rect(screen, (int(((236-200)/18)*timeleft+200), int(((236-22)/18)*timeleft+22), int(((236-28)/18)*timeleft+28)), pygame.Rect(10+starting_point[0]*38, 120+starting_point[1]*38, 37, 37))
        pygame.draw.rect(screen, panelcolour, pygame.Rect(10+starting_point[0]*38+12, 120+starting_point[1]*38+12, 13, 13))

        #Goal
        pygame.draw.rect(screen, (int(((236-16)/18)*timeleft+16), int(((236-138)/18)*timeleft+138), int(((236-150)/18)*timeleft+150)), pygame.Rect(10+goal_point[0]*38, 120+goal_point[1]*38, 37, 37))
        pygame.draw.rect(screen, panelcolour, pygame.Rect(10+goal_point[0]*38+12, 120+goal_point[1]*38+12, 13, 13))

        pygame.display.update()

        clock.tick(18)
        timeleft -= 1
    
def initialize_maze():

    #Build maze
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(cell)
        maze.append(line)

    maze[starting_point[1]][starting_point[0]] = "s"
    maze[goal_point[1]][goal_point[0]] = "g"

    return maze

def draw_maze():

    clear_board()

    div_sq = [[0, 49, 0, 24]]
    holes = []
    sections = []

    while len(div_sq) > 0:

        for i in div_sq:

            just_added = ""

            #If possible to draw a wall
            if i[1] - i[0] >= 2 or i[3] - i[2] >= 2:
                #Drawing first wall with full board
                if div_sq == [[0, 49, 0, 24]]:
                    h_or_v = 1
                else:
                    h_or_v = random.randint(0, 1)
            
            #Horizontal wall
            if h_or_v == 0:
                
                rand_wall = random.randint(i[2]+1,i[3]-1)
                rand_hole = random.randint(i[0], i[1])

                for w1 in range(i[0], i[1]+1):
                    if w1 != rand_hole: 
                        if maze[rand_wall][w1] != "s" and maze[rand_wall][w1] != "g":
                            maze[rand_wall][w1] = "w"
                    else:
                        if maze[rand_wall][w1] != "s" and maze[rand_wall][w1] != "g":
                            maze[rand_wall][w1] = "h"
                            holes.append([rand_wall, w1])

                just_added = "hor"

            #Vertical wall
            if h_or_v == 1:
                
                #First wall
                if div_sq == [[0, 49, 0, 24]] and starting_point[0] < 12 and goal_point[0] > 38:
                    rand_wall = random.randint(16, 34)
                else:
                    rand_wall = random.randint(i[0]+1, i[1]-1)
                rand_hole = random.randint(i[2], i[3])

                for w2 in range(i[2], i[3]+1):
                    if w2 != rand_hole: # and maze[rand_wall][w2] != "s" and maze[rand_wall][w2] != "g":
                        if maze[w2][rand_wall] != "s" and maze[w2][rand_wall] != "g":
                            maze[w2][rand_wall] = "w"
                            
                    else:
                        if maze[w2][rand_wall] != "s" and maze[w2][rand_wall] != "g":
                            maze[w2][rand_wall] = "v"
                            holes.append([w2, rand_wall])

                just_added = "ver"

            #Divide remaining part of board into two after every wall

            if just_added == "hor":
                if rand_wall - i[2] > 2:
                    div_sq.append([i[0], i[1], i[2], rand_wall-1])
                if i[3] - rand_wall > 2:
                    div_sq.append([i[0], i[1], rand_wall+1, i[3]])

            if just_added == "ver":
                if rand_wall - i[0] > 2:
                    div_sq.append([i[0], rand_wall-1, i[2], i[3]])
                if i[1] - rand_wall > 2:
                    div_sq.append([rand_wall+1, i[1], i[2], i[3]])

            div_sq.remove(i)
    
    #Find all leftover 2*2 blank areas
    for i in range(0, 24):
        for j in range(0, 49):
            if maze[i][j] == maze[i][j+1] == maze[i+1][j] == maze[i+1][j+1]== "c":
                sections.append([i,j])
                sections.append([i, j+1])
                sections.append([i+1, j])
                sections.append([i+1, j+1])

    #For all blank parts if it's not blocking a passage, add one wall in every 2*2 area
    for s in sections:
        #Up down left right
        udlr_wall_count = 0
        if maze[s[0]][s[1]] != "s" and maze[s[0]][s[1]] != "g":
            for (xs, ys) in ((s[0]-1, s[1]), (s[0]+1, s[1]), (s[0], s[1]-1), (s[0], s[1]+1)):
                if 0 <= xs <= 24 and 0 <= ys <= 49:
                    if maze[xs][ys] == "w":
                        udlr_wall_count += 1
            if udlr_wall_count == 1:
                if s[0] % 2 == 1 and s[1] % 2 == 1:
                    maze[s[0]][s[1]] = "w"

    #If next to a hole on a wall                
    for sn in sections:
        for hn in holes:
            if abs(sn[0] - hn[0]) + abs(sn[1] - hn[1]) == 1:
                maze[sn[0]][sn[1]] == "c"
    
    #Horizontal holes shouldn't be blocked above and below
    for i2 in range(0, height): 
        for j2 in range(0, width):
            if maze[i2][j2] == "h":
                maze[i2][j2] = "c"
                
                if i2 > 0 and maze[i2-1][j2] != "s" and maze[i2-1][j2] != "g":
                    if maze[i2-1][j2] == "w":
                        maze[i2-1][j2] = "c"
                        holes.append([i2-1, j2])
                
                if i2 < 24 and maze[i2+1][j2] != "s" and maze[i2+1][j2] != "g":
                    if maze[i2+1][j2] == "w":
                        maze[i2+1][j2] = "c"
                        holes.append([i2+1, j2])
                    
    #Vertical holes shouldn't be blocked left and right
    for i2 in range(0, height): 
        for j2 in range(0, width):
            if maze[i2][j2] == "v":
                maze[i2][j2] = "c"
                
                if j2 > 0 and maze[i2][j2-1] != "s" and maze[i2][j2-1] != "g":
                    if maze[i2][j2-1] == "w":
                        maze[i2][j2-1] = "c"
                        holes.append([i2, j2-1])
                    
                if j2 < 49 and maze[i2][j2+1] != "s" and maze[i2][j2+1] != "g":
                    if maze[i2][j2+1] == "w":
                        maze[i2][j2+1] = "c"
                        holes.append([i2, j2+1])
                    

    timeleft = -1
    while timeleft < 1249:
        
        clock.tick(820)
        timeleft += 1
        row_num = timeleft//50
        column_num = timeleft%50

        if maze[row_num][column_num] == "w":
            pygame.draw.rect(screen, darkgrey, pygame.Rect(10+column_num*38, 120+row_num*38, 37, 37)) #(0, 62, 116)
            pygame.display.update()

def click_square(ini_sq): 
    
    #Recognize square clicked
    row1 = (pygame.mouse.get_pos()[1] - 120 + 38)// 38 - 1
    column1 = (pygame.mouse.get_pos()[0] - 10 + 38) // 38 - 1
    
    if ini_sq == "c":
        if maze[row1][column1] == "c":
            maze[row1][column1] = "w"
            pygame.draw.rect(screen, darkgrey, pygame.Rect(10+column1*38, 120+row1*38, 37, 37))

def click_wall():

    #Recognize wall clicked
    row1 = (pygame.mouse.get_pos()[1] - 120 + 38)// 38 - 1
    column1 = (pygame.mouse.get_pos()[0] - 10 + 38) // 38 - 1
    if maze[row1][column1] == "w":
        maze[row1][column1] = "c"
        pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column1*38, 120+row1*38, 37, 37))

def click_endpoints(ini_sq, starting_point, goal_point):

    #Clicking either starting point or goal point

    row1 = (pygame.mouse.get_pos()[1] - 120 + 38)// 38 - 1
    column1 = (pygame.mouse.get_pos()[0] - 10 + 38) // 38 - 1
    cur_sq = []
    cur_sq.append(row1)
    cur_sq.append(column1)

    if ini_sq == "s":

        for i in clicked_route:
            if i[0] != row1 or i[1] != column1:
                maze[i[0]][i[1]] = "c"
                pygame.draw.rect(screen, panelcolour, pygame.Rect(10+i[1]*38, 120+i[0]*38, 37, 37))
        
        if maze[row1][column1] != "g":
            maze[row1][column1] = "s"
            for jj in range(0,1250):
                row_jj = jj//50
                column_jj = jj%50
                if maze[row_jj][column_jj] == "c":
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_jj*38, 120+row_jj*38, 37, 37))

            pygame.draw.rect(screen, (192, 46, 32), pygame.Rect(10+column1*38, 120+row1*38, 37, 37)) 
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column1*38+12, 120+row1*38+12, 13, 13))
            starting_point = [column1, row1]
        else:
            maze[row1][column1] = "g"
            
            pygame.draw.rect(screen, (132, 168, 42), pygame.Rect(10+column1*38, 120+row1*38, 37, 37))
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column1*38+12, 120+row1*38+12, 13, 13))
            
            goal_point = [column1, row1]

    elif ini_sq == "g":

        for jj in range(0,1250):
            row_jj = jj//50
            column_jj = jj%50
            if maze[row_jj][column_jj] == "c":
                pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_jj*38, 120+row_jj*38, 37, 37))

        for i in clicked_route:
            if i[0] != row1 or i[1] != column1:
                maze[i[0]][i[1]] = "c"
                pygame.draw.rect(screen, panelcolour, pygame.Rect(10+i[1]*38, 120+i[0]*38, 37, 37))

        maze[row1][column1] = "g"
        pygame.draw.rect(screen, teal, pygame.Rect(10+column1*38, 120+row1*38, 37, 37)) #62, 142, 134
        pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column1*38+12, 120+row1*38+12, 13, 13))
        goal_point = [column1, row1]

    return starting_point, goal_point

def clear_board():

    #Clean everything

    #First the path found
    for i in range(0, 1250):
        row_i = i//50
        column_i = i%50
        if maze[row_i][column_i] == "v":
            maze[row_i][column_i] = "c"
        if maze[row_i][column_i] == "c":
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_i*38, 120+row_i*38, 37, 37))

    #Then the walls
    timeleft = -1
    while timeleft < 1249:
        
        clock.tick(1520)
        timeleft += 1
        row_num = timeleft//50
        column_num = timeleft%50

        if maze[row_num][column_num] == "w":
            maze[row_num][column_num] = "c"
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_num*38, 120+row_num*38, 37, 37))        
            pygame.display.update()

def random_pattern():

    #Generate random walls

    timeleft = -1
    while timeleft < 1249:
        
        clock.tick(3020)
        timeleft += 1
        row_num = timeleft//50
        column_num = timeleft%50

        if maze[row_num][column_num] != "s" and maze[row_num][column_num] != "g":
            temp_random = random.randint(1, 10)
            if temp_random > 7:
                maze[row_num][column_num] = "w"
                pygame.draw.rect(screen, darkgrey, pygame.Rect(10+column_num*38, 120+row_num*38, 37, 37))
            else:
                maze[row_num][column_num] = "c"
                pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_num*38, 120+row_num*38, 37, 37))
            
            pygame.display.update()

def astar():

    #A* algorithm

    #Clean up any previous path first
    for i8 in range(0, 1250):
        row_i8 = i8//50
        column_i8 = i8%50
        if maze[row_i8][column_i8] == "v":
            maze[row_i8][column_i8] = "c"
        if maze[row_i8][column_i8] == "c":
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_i8*38, 120+row_i8*38, 37, 37))

    #Set up all three distance costs/steps
    g_cost_list = []
    h_cost_list = []
    f_cost_list = []

    g_cost_list.append([])
    h_cost_list.append([])
    f_cost_list.append([])

    #Set up initial values - all Manhattan distances ignoring walls, will be updated later
    for j in range(0, height):
        for i in range(0, width):

            if maze[j][i] == "c":
                temp_g_cost = abs(i-starting_point[0]) + abs(j-starting_point[1])
                temp_h_cost = abs(i-goal_point[0]) + abs(j-goal_point[1])
                
            elif maze[j][i] == "s":
                temp_g_cost = abs(i-starting_point[0]) + abs(j-starting_point[1])
                temp_h_cost = abs(i-goal_point[0]) + abs(j-goal_point[1]) 
                
            elif maze[j][i] == "w":
                temp_g_cost = -1
                temp_h_cost = -1
                
            elif maze[j][i] == "g":
                temp_g_cost = abs(i-starting_point[0]) + abs(j-starting_point[1]) 
                temp_h_cost = abs(i-goal_point[0]) + abs(j-goal_point[1])
                
            else:
                print("Error: more variety than c w s g")
                temp_g_cost = "Error"
                temp_h_cost = "Error"
                temp_f_cost = "Error"
            
            temp_f_cost = temp_g_cost + temp_h_cost

            temp_maze_size = len(g_cost_list)

            if len(g_cost_list[temp_maze_size-1]) < 50:
                g_cost_list[temp_maze_size-1].append(temp_g_cost) 
                h_cost_list[temp_maze_size-1].append(temp_h_cost)
                f_cost_list[temp_maze_size-1].append(temp_f_cost)
            else:
                g_cost_list.append([])
                g_cost_list[temp_maze_size].append(temp_g_cost) 

                h_cost_list.append([])
                h_cost_list[temp_maze_size].append(temp_h_cost)

                f_cost_list.append([])
                f_cost_list[temp_maze_size].append(temp_f_cost)   

    open_list = []
    closed_list = []

    oc_list = []
    oc_counter = -1

    open_list.append(starting_point)

    parent_dict = {}

    o_length = []
    c_length = []

    #Open list empty means no path possible, goal point in closed list means goal found
    while len(open_list) > 0 and goal_point not in closed_list:

        if open_list == [starting_point]:
            o_length_b = len(open_list) - 1
        else:
            o_length_b = len(open_list)

        c_length_b = len(closed_list)

        cur_sq = open_list[0]

        for index, item in enumerate(open_list):
            if f_cost_list[item[1]][item[0]] < f_cost_list[cur_sq[1]][cur_sq[0]]:
                cur_sq = item

        #Found goal
        if cur_sq == goal_point:
            path = []

            #Build the path found
            current = cur_sq
            while current is not starting_point:
                path.append(current)
                current = parent_dict.get(tuple(current))

            #Reverse to the right sequence
            path = path[::-1]
            
            oc_len = len(oc_list) - 1

            timeleft = -1
            while timeleft < oc_len:

                #Various speeds depending on the length
                if oc_len > 280:
                    clock.tick(78)
                elif oc_len > 100:
                    clock.tick(28)
                else:
                    clock.tick(16)

                timeleft += 1

                #Each particular step
                temp_oc_list = oc_list[timeleft]

                for oc in temp_oc_list:
                    if oc != starting_point and oc != goal_point:
                        pygame.draw.rect(screen, (int((166-210)*((oc_len-timeleft)/oc_len)+210), int((126-72)*((oc_len-timeleft)/oc_len)+72), int((182-52)*((oc_len-timeleft)/oc_len)+52)), pygame.Rect(10+oc[0]*38, 120+oc[1]*38, 37, 37))
                        pygame.display.update()

            #Don't draw over the two end points
            if starting_point in path:
                path.remove(starting_point)
            if goal_point in path:
                path.remove(goal_point)

            #Draw the path
            p_len = len(path) - 1

            timeleft = -1
            while timeleft < p_len:
                
                #Various speeds depending on the length
                if p_len > 100:
                    clock.tick(32)
                else:
                    clock.tick(18)
                timeleft += 1

                p_sq = path[timeleft]

                if p_sq != starting_point and p_sq != goal_point:
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(10+p_sq[0]*38+13, 120+p_sq[1]*38+13, 11, 11))
                    pygame.display.update()
            
            for ad in path:
                pygame.draw.rect(screen, (252, 252, 252), pygame.Rect(10+ad[0]*38+13, 120+ad[1]*38+13, 11, 11))

        open_list.remove(cur_sq)
        closed_list.append(cur_sq)

        neighbour_list = []

        #Four neighbours of the current square
        for (yy,xx) in ((cur_sq[1]-1, cur_sq[0]), (cur_sq[1]+1, cur_sq[0]), (cur_sq[1], cur_sq[0]-1), (cur_sq[1], cur_sq[0]+1)):
            if 0 <= xx < 50 and 0 <= yy < 25:
                if (maze[yy][xx] == "c" or maze[yy][xx] == "g") and [xx, yy] not in closed_list:
                    neighbour_list.append([xx, yy])
        
        if cur_sq in neighbour_list:
            neighbour_list.remove(cur_sq)

        if len(neighbour_list) > 0:
            
            for i2 in neighbour_list:

                #"Real" g cost by adding one to previous square, based on the real route
                temp_g = g_cost_list[cur_sq[1]][cur_sq[0]] + 1

                #If the square in question is already in open list, only update the g cost
                if i2 in open_list:
                    if temp_g < g_cost_list[i2[1]][i2[0]]:
                        g_cost_list[i2[1]][i2[0]] = temp_g

                #Add the square into open list and update the g cost as well
                else:
                    open_list.append(i2)
                    g_cost_list[i2[1]][i2[0]] = temp_g

                #Update f cost
                f_cost_list[i2[1]][i2[0]] = g_cost_list[i2[1]][i2[0]] + h_cost_list[i2[1]][i2[0]]

                #Add the parent-child relationship
                parent_dict[tuple(i2)] = cur_sq

        oc_counter += 1
        oc_list.append([])

        c_length_e = len(closed_list)

        c_length.append(c_length_e-c_length_b)

        for cx in range(0, c_length_e-c_length_b+1):
            oc_list[oc_counter].append(closed_list[-cx])

    #No path possible only drawing the attempt
    else:
        if open_list == []:
            
            oc_len = len(oc_list) - 1
            timeleft = -1
            while timeleft < oc_len:
                
                clock.tick(22)

                timeleft += 1

                temp_oc_list = oc_list[timeleft]

                for oc in temp_oc_list:
                    if oc != starting_point and oc != goal_point:
                        pygame.draw.rect(screen, (int((214-204)*((oc_len-timeleft)/oc_len)+204), int((188-92)*((oc_len-timeleft)/oc_len)+92), int((70-32)*((oc_len-timeleft)/oc_len)+32)), pygame.Rect(10+oc[0]*38, 120+oc[1]*38, 37, 37)) # 222, 176, 122 to 216, 136, 52

                        pygame.display.update()

def dijkstra():

    #Dijkstra algorithm

    #Clean up any previous path first
    for i8 in range(0, 1250):
        row_i8 = i8//50
        column_i8 = i8%50
        if maze[row_i8][column_i8] == "v":
            maze[row_i8][column_i8] = "c"
        if maze[row_i8][column_i8] == "c":
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_i8*38, 120+row_i8*38, 37, 37))

    #Set up g cost
    g_cost_list = []
    g_cost_list.append([])

    #Manhattan distances only to the starting point
    for j in range(0, height):
        for i in range(0, width):

            if maze[j][i] == "c":
                temp_g_cost = abs(i-starting_point[0]) + abs(j-starting_point[1])
                
            elif maze[j][i] == "s":
                temp_g_cost = abs(i-starting_point[0]) + abs(j-starting_point[1])
                
            elif maze[j][i] == "w":
                temp_g_cost = -1
                
            elif maze[j][i] == "g":
                temp_g_cost = abs(i-starting_point[0]) + abs(j-starting_point[1])
                
            else:
                print("Error: more variety than c w s g")
                temp_g_cost = "Error"
            
            temp_maze_size = len(g_cost_list)

            if len(g_cost_list[temp_maze_size-1]) < 50:
                g_cost_list[temp_maze_size-1].append(temp_g_cost) 
            else:
                g_cost_list.append([])
                g_cost_list[temp_maze_size].append(temp_g_cost) 

    open_list = []
    closed_list = []

    oc_list = []
    oc_counter = -1

    open_list.append(starting_point)

    parent_dict = {}

    o_length = []
    c_length = []

    #Very similar to A*
    while len(open_list) > 0 and goal_point not in closed_list:

        if open_list == [starting_point]:
            o_length_b = len(open_list) - 1
        else:
            o_length_b = len(open_list)

        c_length_b = len(closed_list)

        cur_sq = open_list[0]

        for index, item in enumerate(open_list):
            if g_cost_list[item[1]][item[0]] < g_cost_list[cur_sq[1]][cur_sq[0]]:
                cur_sq = item

        #Found goal
        if cur_sq == goal_point:
            path = []

            current = cur_sq
            while current is not starting_point:
                path.append(current)
                current = parent_dict.get(tuple(current))

            path = path[::-1]
            
            oc_len = len(oc_list) - 1

            timeleft = -1
            while timeleft < oc_len:

                #Various speeds depending on the length
                if oc_len > 280:
                    clock.tick(88)
                elif oc_len > 100:
                    clock.tick(36)
                else:
                    clock.tick(18)

                timeleft += 1

                temp_oc_list = oc_list[timeleft]

                for oc in temp_oc_list:
                    if oc != starting_point and oc != goal_point:
                        pygame.draw.rect(screen, (int((142-202)*((oc_len-timeleft)/oc_len)+202), int((170-182)*((oc_len-timeleft)/oc_len)+182), int((92-28)*((oc_len-timeleft)/oc_len)+28)), pygame.Rect(10+oc[0]*38, 120+oc[1]*38, 37, 37)) # 222, 176, 122 to 216, 136, 52
                        pygame.display.update()

            if starting_point in path:
                path.remove(starting_point)
            if goal_point in path:
                path.remove(goal_point)

            #Draw the path
            p_len = len(path) - 1

            timeleft = -1
            while timeleft < p_len:
                
                #Various speeds depending on the length
                if p_len > 100:
                    clock.tick(32)
                else:
                    clock.tick(18)
                timeleft += 1

                p_sq = path[timeleft]

                if p_sq != starting_point and p_sq != goal_point:
                    pygame.draw.rect(screen, panelcolour, pygame.Rect(10+p_sq[0]*38+13, 120+p_sq[1]*38+13, 11, 11))

                    pygame.display.update()
            
            for ad in path:
                pygame.draw.rect(screen, (252, 252, 252), pygame.Rect(10+ad[0]*38+13, 120+ad[1]*38+13, 11, 11))

        open_list.remove(cur_sq)
        closed_list.append(cur_sq)

        neighbour_list = []

        for (yy,xx) in ((cur_sq[1]-1, cur_sq[0]), (cur_sq[1]+1, cur_sq[0]), (cur_sq[1], cur_sq[0]-1), (cur_sq[1], cur_sq[0]+1)):
            if 0 <= xx < 50 and 0 <= yy < 25:
                if (maze[yy][xx] == "c" or maze[yy][xx] == "g") and [xx, yy] not in closed_list:#:
                    neighbour_list.append([xx, yy])
        
        if cur_sq in neighbour_list:
            neighbour_list.remove(cur_sq)

        if len(neighbour_list) > 0:
            
            for i2 in neighbour_list:

                temp_g = g_cost_list[cur_sq[1]][cur_sq[0]] + 1

                if i2 in open_list:
                    if temp_g < g_cost_list[i2[1]][i2[0]]:
                        g_cost_list[i2[1]][i2[0]] = temp_g
                else:
                    open_list.append(i2)
                    g_cost_list[i2[1]][i2[0]] = temp_g

                parent_dict[tuple(i2)] = cur_sq

        oc_counter += 1
        oc_list.append([])

        c_length_e = len(closed_list)

        c_length.append(c_length_e-c_length_b)

        for cx in range(0, c_length_e-c_length_b+1):
            oc_list[oc_counter].append(closed_list[-cx])

    #No path possible only drawing the attempt
    else:
        if open_list == []:
            
            oc_len = len(oc_list) - 1
            timeleft = -1
            while timeleft < oc_len:
                
                clock.tick(22)

                timeleft += 1

                temp_oc_list = oc_list[timeleft]

                for oc in temp_oc_list:
                    if oc != starting_point and oc != goal_point:
                        pygame.draw.rect(screen, (int((88-46)*((oc_len-timeleft)/oc_len)+46), int((166-88)*((oc_len-timeleft)/oc_len)+88), int((140-168)*((oc_len-timeleft)/oc_len)+168)), pygame.Rect(10+oc[0]*38, 120+oc[1]*38, 37, 37)) # 222, 176, 122 to 216, 136, 52
                        pygame.display.update()

def depth_first():

    #Depth first search algorithm

    #Clean up any previous path first
    for i8 in range(0, 1250):
        row_i8 = i8//50
        column_i8 = i8%50
        if maze[row_i8][column_i8] == "v":
            maze[row_i8][column_i8] = "c"
        if maze[row_i8][column_i8] == "c":
            pygame.draw.rect(screen, panelcolour, pygame.Rect(10+column_i8*38, 120+row_i8*38, 37, 37))

    not_visited_list = deque()
    not_visited_list.append(starting_point)
    visited_list = []
    parent_dict = {}

    #Only going forward until impossible, needs minimal information to start
    while len(not_visited_list) > 0:

        cur_sq = not_visited_list.pop()

        if cur_sq == goal_point:
            path = []
            current = goal_point

            current = cur_sq
            while current is not starting_point:
                path.append(current)
                current = parent_dict.get(tuple(current))

            path = path[::-1]

            #Don't draw over the end points
            if starting_point in visited_list:
                visited_list.remove(starting_point)
            if goal_point in visited_list:
                visited_list.remove(goal_point)

            if starting_point in path:
                path.remove(starting_point)
            if goal_point in path:
                path.remove(goal_point)

            v_len = len(visited_list) - 1

            timeleft = -1
            while timeleft < v_len:

                #Various speeds depending on the length
                #A little faster since this algorithm tends to be long
                if v_len > 280:
                    clock.tick(82)
                elif v_len > 100:
                    clock.tick(28)
                else:
                    clock.tick(8)

                timeleft += 1

                pygame.draw.rect(screen, (int((136-0)*((v_len-timeleft)/v_len)+0), int((172-108)*((v_len-timeleft)/v_len)+108), int((218-136)*((v_len-timeleft)/v_len)+136)), pygame.Rect(10+visited_list[timeleft][0]*38, 120+visited_list[timeleft][1]*38, 37, 37))
                pygame.display.update()

            #Draw the path
            p_len = len(path) - 1
            timeleft = -1
            while timeleft < p_len:

                #Various speeds depending on the length
                #A little faster since this algorithm tends to be long
                if p_len > 200:
                    clock.tick(88)
                elif p_len > 100:
                    clock.tick(32)
                else:
                    clock.tick(16)
                timeleft += 1

                pygame.draw.rect(screen, panelcolour, pygame.Rect(10+path[timeleft][0]*38+13, 120+path[timeleft][1]*38+13, 11, 11))
                pygame.display.update()

            for ad in path:
                pygame.draw.rect(screen, (252, 252, 252), pygame.Rect(10+ad[0]*38+13, 120+ad[1]*38+13, 11, 11))

            #Clean up maze for the next task
            for rs in range(0, 1250):
                row_rs = rs//50
                column_rs = rs%50
                if maze[row_rs][column_rs] == "v":
                    maze[row_rs][column_rs] = "c"

            break

        if maze[cur_sq[1]][cur_sq[0]] == "w":
            continue

        if cur_sq not in visited_list:

            visited_list.append(cur_sq)
            
            maze[cur_sq[1]][cur_sq[0]] = "v"

            if cur_sq != starting_point:
                pass
            else:
                maze[cur_sq[1]][cur_sq[0]] = "s"

            for (yy, xx) in ((cur_sq[1]-1, cur_sq[0]), (cur_sq[1]+1, cur_sq[0]), (cur_sq[1], cur_sq[0]-1), (cur_sq[1], cur_sq[0]+1)):
                if 0 <= xx <= 49 and 0 <= yy <= 24:
                    not_visited_list.append([xx, yy])

                    if [xx, yy] not in visited_list:
                        parent_dict[tuple([xx, yy])] = cur_sq
    
    #No path possible only drawing the attempt
    else:

        #Don't draw over the two end points
        if starting_point in visited_list:
            visited_list.remove(starting_point)
        if goal_point in visited_list:
            visited_list.remove(goal_point)

        v_len = len(visited_list) - 1

        timeleft = -1
        while timeleft < v_len:

            #Various speeds depending on the length
            #A little faster since this algorithm tends to be long
            if v_len > 280:
                clock.tick(88)
            elif v_len > 100:
                clock.tick(52)
            else:
                clock.tick(18)

            timeleft += 1

            pygame.draw.rect(screen, (int((16-196)*((v_len-timeleft)/v_len)+196), int((104-92)*((v_len-timeleft)/v_len)+92), int((152-92)*((v_len-timeleft)/v_len)+92)), pygame.Rect(10+visited_list[timeleft][0]*38, 120+visited_list[timeleft][1]*38, 37, 37))
            pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption('Path Finder')

panelcolour = (232, 232, 222)#(236, 236, 236)
lightgrey = (202, 202, 196)#(212, 212, 212)

darkgrey = (88, 98, 98)#(52, 78, 108)#(18, 58, 62)#(118, 118, 118)

ruyaoqing = (128, 164, 146)

yellow = (0, 62, 116)#(198, 178, 38)
yellow_hi = (16, 82, 132)
orange = (210, 72, 52)#(204, 92, 32)
orange_hi = (206, 96, 66)#(192, 112, 36)
green = (42, 110, 62)#(132, 168, 42)
green_hi = (82, 122, 72)#(152, 182, 22)
purple = (76, 76, 156)#(82, 42, 96)
purple_hi = (92, 92, 162)#(92, 52, 102)
blue = (202, 182, 28)#(46, 88, 168)
blue_hi = (206, 192, 62)#(72, 102, 172)
pink = (0, 108, 136)#(196, 92, 92)
pink_hi = (52, 122, 142)#(212, 98, 122)

red = (168, 34, 38)
teal = (66, 152, 162)#(16, 138, 150)

starting_point = [9, 12]
goal_point = [40, 12]

moving_point = False

dragging = False
clicked_wall = False
clicked_start = False
clicked_goal = False
clicked_route = []

showing_points = False

empty = 0
wall = "w"
cell = "c"
start = "s"
goal = "g"
height = 25
width = 50
maze = []

logo_font = pygame.font.Font('freesansbold.ttf', 38)
button_font = pygame.font.Font('freesansbold.ttf', 30)

pygame.draw.rect(screen, panelcolour, pygame.Rect(0, 0, 1920, 110))

pygame.draw.rect(screen, lightgrey, pygame.Rect(0, 110, 1920, 970))

title_surface1 = button_font.render("PATH", True, (252, 252, 252)) 
title_rect1 = title_surface1.get_rect(midleft = (14, 60)) 
title_surface2 = button_font.render("FINDER", True, (252, 252, 252)) 
title_rect2 = title_surface2.get_rect(midleft = (14, 86)) 
pygame.draw.rect(screen, ruyaoqing, pygame.Rect(10, 10, 400, 90))
screen.blit(title_surface1, title_rect1)
screen.blit(title_surface2, title_rect2)

astar_surface1 = button_font.render("A*", True, panelcolour) 
astar_rect1 = astar_surface1.get_rect(midleft = (1174, 60)) 
astar_surface2 = button_font.render("ALGORITHM", True, panelcolour) 
astar_rect2 = astar_surface1.get_rect(midleft = (1174, 86)) 
pygame.draw.rect(screen, orange, pygame.Rect(1170, 10, 240, 90))
screen.blit(astar_surface1, astar_rect1)
screen.blit(astar_surface2, astar_rect2)

maze_surface1 = button_font.render("GENERATE", True, panelcolour) 
maze_rect1 = maze_surface1.get_rect(midleft = (424, 60)) 
maze_surface2 = button_font.render("MAZE", True, panelcolour) 
maze_rect2 = maze_surface1.get_rect(midleft = (424, 86)) 
pygame.draw.rect(screen, yellow, pygame.Rect(420, 10, 240, 90))
screen.blit(maze_surface1, maze_rect1)
screen.blit(maze_surface2, maze_rect2)

randompattern_surface1 = button_font.render("RANDOM", True, panelcolour) 
randompattern_rect1 = randompattern_surface1.get_rect(midleft = (674, 60)) 
randompattern_surface2 = button_font.render("PATTERN", True, panelcolour) 
randompattern_rect2 = randompattern_surface1.get_rect(midleft = (674, 86)) 
pygame.draw.rect(screen, purple, pygame.Rect(670, 10, 240, 90))
screen.blit(randompattern_surface1, randompattern_rect1)
screen.blit(randompattern_surface2, randompattern_rect2)

clear_surface1 = button_font.render("CLEAR", True, panelcolour) 
clear_rect1 = clear_surface1.get_rect(midleft = (924, 60)) 
clear_surface2 = button_font.render("BOARD", True, panelcolour) 
clear_rect2 = clear_surface1.get_rect(midleft = (924, 86)) 
pygame.draw.rect(screen, green, pygame.Rect(920, 10, 240, 90))
screen.blit(clear_surface1, clear_rect1)
screen.blit(clear_surface2, clear_rect2)

dijkstra_surface1 = button_font.render("DIJKSTRA", True, panelcolour)
dijkstra_rect1 = dijkstra_surface1.get_rect(midleft = (1424, 60)) 
dijkstra_surface2 = button_font.render("ALGORITHM", True, panelcolour) 
dijkstra_rect2 = dijkstra_surface1.get_rect(midleft = (1424, 86)) 
pygame.draw.rect(screen, blue, pygame.Rect(1420, 10, 240, 90))
screen.blit(dijkstra_surface1, dijkstra_rect1)
screen.blit(dijkstra_surface2, dijkstra_rect2)

depthfirst_surface1 = button_font.render("DEPTH-FIRST", True, panelcolour)
depthfirst_rect1 = depthfirst_surface1.get_rect(midleft = (1674, 60)) 
depthfirst_surface2 = button_font.render("SEARCH", True, panelcolour) 
depthfirst_rect2 = depthfirst_surface1.get_rect(midleft = (1674, 86)) 
pygame.draw.rect(screen, pink, pygame.Rect(1670, 10, 240, 90))
screen.blit(depthfirst_surface1, depthfirst_rect1)
screen.blit(depthfirst_surface2, depthfirst_rect2)

draw_board()
initialize_maze()

while True:

    #Mouse over a square
    if 10 <= pygame.mouse.get_pos()[0] <= 1909 and 120 <= pygame.mouse.get_pos()[1] < 1070:

        row1 = (pygame.mouse.get_pos()[1] - 120 + 38)// 38 - 1
        column1 = (pygame.mouse.get_pos()[0] - 10 + 38) // 38 - 1

        sq1 = [row1, column1]

        if dragging == True:
            if ini_sq == "s":
                #Collision of two endpoints
                if column1 == goal_point[0] and row1 == goal_point[1]:
                    dragging = False
                else:
                    click_endpoints("s", starting_point, goal_point)
                    starting_point = click_endpoints("s", starting_point, goal_point)[0]
                    goal_point = click_endpoints("s", starting_point, goal_point)[1]

                if sq1 not in clicked_route:
                    clicked_route.append(sq1)
                    
            elif ini_sq == "g":
                if column1 == starting_point[0] and row1 == starting_point[1]:
                    dragging = False
                else:
                    click_endpoints("g", starting_point, goal_point)
                    starting_point = click_endpoints("g", starting_point, goal_point)[0]
                    goal_point = click_endpoints("g", starting_point, goal_point)[1]

                if sq1 not in clicked_route:
                    clicked_route.append(sq1)

            if clicked_wall == False:
                click_square(ini_sq) #
            elif clicked_wall == True:
                click_wall()

    else:
        dragging = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if 10 <= pygame.mouse.get_pos()[1] <= 100:

                if 420 <= pygame.mouse.get_pos()[0] <= 660:
                    draw_maze()
                
                if 670 <= pygame.mouse.get_pos()[0] <= 910:
                    random_pattern()

                if 920 <= pygame.mouse.get_pos()[0] <= 1160:
                    clear_board()

                if 1170 <= pygame.mouse.get_pos()[0] <= 1410:
                    astar()

                if 1420 <= pygame.mouse.get_pos()[0] <= 1660:
                    dijkstra()
                
                if 1670 <= pygame.mouse.get_pos()[0] <= 1910:
                    depth_first()

            #Clicking a square
            if 10 <= pygame.mouse.get_pos()[0] <= 1909 and 120 <= pygame.mouse.get_pos()[1] < 1070:
                
                row1 = (pygame.mouse.get_pos()[1] - 120 + 38)// 38 - 1
                column1 = (pygame.mouse.get_pos()[0] - 10 + 38) // 38 - 1

                #Clicked starting point
                if maze[row1][column1] == "s":
                    ini_sq = "s"
                    dragging = True

                #Clicked goal point
                if maze[row1][column1] == "g":
                    ini_sq = "g"
                    dragging = True

                #Clicked other points
                if maze[row1][column1] == "c" or maze[row1][column1] == "w" or maze[row1][column1] == "v":
                    ini_sq = "c"
                    dragging = True
        
        #Right click - only to remove walls
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            row1 = (pygame.mouse.get_pos()[1] - 120 + 38)// 38 - 1
            column1 = (pygame.mouse.get_pos()[0] - 10 + 38) // 38 - 1
            if maze[row1][column1] == "w":
                clicked_wall = True
                dragging = True
                ini_sq = "w"

        #Left or right button released
        if event.type == pygame.MOUSEBUTTONUP and (event.button == 1 or event.button == 3):
            dragging = False
            clicked_wall = False
            clicked_start = False
            clicked_goal = False
            clicked_route = []
        
    astar_hover()
    dijkstra_hover()
    maze_hover()
    clear_hover()
    randompattern_hover()
    depthfirst_hover()

    pygame.display.update()

    clock.tick(32)
    
