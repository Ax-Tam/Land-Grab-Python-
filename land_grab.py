
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10906673
#    Student name: Alex Tam
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LAND GRAB
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "process_moves".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various rectangular icons, using data stored in a
#  list to determine which icons to place and where.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *

# Define constant values for setting up the drawing canvas
cell_width = 120 # pixels (default is 120)
cell_height = 90 # pixels (default is 90)
grid_size = 7 # width and height of the grid (default is 7)
x_margin = cell_width * 2.4 # pixels, the size of the margin left/right of the board
y_margin = cell_height // 2.1 # pixels, the size of the margin below/above the board
canvas_height = grid_size * cell_height + y_margin * 2
canvas_width = grid_size * cell_width + x_margin * 2

# Validity checks on grid size
assert cell_width >= 100, 'Cells must be at least 100 pixels wide'
assert cell_height >= 75, 'Cells must be at least 75 pixels high'
assert grid_size >= 5, 'Grid must be at least 5x5'
assert grid_size % 2 == 1, 'Grid size must be odd'
assert cell_width / cell_height >= 4 / 3, 'Cells must be much wider than high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You may NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(show_instructions = False, # show Part B instructions
                          label_locations = True, # label axes and home coord
                          bg_colour = 'light grey', # background colour
                          line_colour = 'grey'): # line colour for grid
    
    # Set up the drawing canvas with enough space for the grid
    setup(canvas_width, canvas_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coordinate of the grid
    left_edge = -(grid_size * cell_width) // 2 
    bottom_edge = -(grid_size * cell_height) // 2

    # Draw the horizontal grid lines
    setheading(0) # face east
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge, bottom_edge + line_no * cell_height)
        pendown()
        forward(grid_size * cell_width)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge + line_no * cell_width, bottom_edge)
        pendown()
        forward(grid_size * cell_height)

    # Optionally label the axes and centre point
    if label_locations:

        # Mark the centre of the board (coordinate [0, 0])
        penup()
        home()
        dot(30)
        pencolor(bg_colour)
        dot(20)
        pencolor(line_colour)
        dot(10)

        # Define the font and position for the axis labels
        small_font = ('Arial', (18 * cell_width) // 100, 'normal')
        y_offset = (32 * cell_height) // 100 # pixels

        # Draw each of the labels on the x axis
        penup()
        for x_label in range(0, grid_size):
            goto(left_edge + (x_label * cell_width) + (cell_width // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_size):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_height) + (cell_height // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

    # Optionally write the instructions 
    if show_instructions:
        # Font for the instructions
        big_font = ('Arial', (20 * cell_width) // 100, 'normal')
        # Text to the right of the grid
        penup()
        goto((grid_size * cell_width) // 2 + 50, -cell_height // 3)
        write('This space\nreserved for\nPart B', align = 'left', font = big_font)
        
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    # Ensure any drawing still in progress is displayed
    update()
    tracer(True)
    # Optionally hide the cursor
    if hide_cursor:
        hideturtle()
    # Release the drawing canvas
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The data sets in this section are provided to help you develop and
# test your code.  You can use them as the argument to the
# "process_moves" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_moves" function appearing below.
# Your program must work correctly for any data set that can be
# generated by calling "random_moves()" with no argument.
#
# Each of the data sets is a list of moves, each specifying which
# competitor is attempting to move and in which direction.  The
# general form of each move is
#
#     [competitor_identity, direction]
#
# where the competitor identities range from 'Competitor A' to
# 'Competitor D' and the directions are 'Up', 'Down', 'Left' and
# 'Right'.
#
# Note that all the data sets below assume the second argument
# to "random_moves" has its default value.
#

# The following data set makes no moves at all and can be used
# when developing the code to draw the competitors in their
# starting positions.
fixed_data_set_00 = []

# The following data sets each move one of the competitors
# several times but do not attempt to go outside the margins
# of the grid or overwrite previous moves
fixed_data_set_01 = [['Competitor A', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor A', 'Up']]
fixed_data_set_02 = [['Competitor B', 'Left'],
                     ['Competitor B', 'Left'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Right'],
                     ['Competitor B', 'Up']]
fixed_data_set_03 = [['Competitor C', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Left']]
fixed_data_set_04 = [['Competitor D', 'Left'],
                     ['Competitor D', 'Left'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Right'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Right'],
                     ['Competitor D', 'Down']]

# The following data set moves all four competitors and
# will cause them all to go outside the grid unless such
# moves are prevented by your code
fixed_data_set_05 = [['Competitor C', 'Right'],
                     ['Competitor B', 'Up'],
                     ['Competitor D', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor C', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor D', 'Left'],
                     ['Competitor A', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor B', 'Right'],
                     ['Competitor D', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor C', 'Right'],
                     ['Competitor B', 'Down'],
                     ['Competitor D', 'Right'],
                     ['Competitor A', 'Right']]

# We can also control the random moves by providing a "seed"
# value N to the random number generator by using
# "random_moves(N)" as the argument to function "process_moves".
# You can copy the following function calls into the main
# program to force the program to produce a fixed sequence of
# moves while debugging your code.

# The following seeds all produce moves in which each
# competitor captures a small number of squares in their
# own corner, but do not interfere with one another.
#
#   random_moves(39) - Only one round occurs
#   random_moves(58) - Only two rounds
#   random_moves(12)
#   random_moves(27)
#   random_moves(38)
#   random_moves(41)

# The following seeds all produce moves in which two or
# more competitors overlap one another's territory.
#
#   random_moves(20) - Competitors C and D touch but don't overlap
#   random_moves(23) - Competitors A and B overlap
#   random_moves(15) - Competitors A and D overlap
#   random_moves(29) - Competitors B and D overlap slightly
#   random_moves(18) - Competitors B, C and D overlap
#   random_moves(31) - A and C overlap slightly, B and D touch but don't overlap
#   random_moves(36) - Competitor D overlaps Competitor C
#
# We haven't yet found a seed that causes a player to
# be completely eliminated - can you find one?

# The following seeds all produce very long sequences of
# moves which result in most of the grid being filled.
#
#   random_moves(19)
#   random_moves(75)
#   random_moves(43) - Competitor D reaches opposite corner
#   random_moves(87) - C occupies A's corner and A occupies B's corner
#   random_moves(90) - Only 4 squares left unoccupied
#
# We haven't yet found a seed that causes every cell
# to be occupied - can you find one?

# The following seeds produce data sets which have a special
# meaning in the second part of the assignment. Their
# significance will be explained in the Part B instructions.
#
#   random_moves(21)
#   random_moves(26)
#   random_moves(24)
#   random_moves(35)
#
#   random_moves(52)
#   random_moves(51)
#   random_moves(47)
#   random_moves(46)
#
#   random_moves(53)
#   random_moves(62)
#   random_moves(81)
#   random_moves(48)
#
#   random_moves(54)
#   random_moves(98)

# If you want to create your own test data sets put them here.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.

# The following function creates a random data set as a list
# of moves.  Your program must work for any data set that
# can be returned by this function.  The results returned by
# calling "random_moves()" will be used as the argument to your
# "process_moves" function during marking.  For convenience during
# code development and marking this function also prints each move
# to the shell window.
#
# NB: As a matter of style your code should not print anything else
# to the shell.  Make sure any debugging calls to the "print"
# function are disabled before you submit your solution.
#
# The function makes no attempt to avoid moves that will go
# outside the grid.  It is your responsibility to detect and
# ignore such moves.
#
def random_moves(the_seed = None, max_rounds = 35):
    # Welcoming message
    print('\nWelcome to Land Grab!')
    print('Here are the randomly-generated moves:')
    # Set up the random number generator
    seed(the_seed)
    # Randomise the order in which competitors move
    competitors = ['Competitor A', 'Competitor B', 'Competitor C', 'Competitor D']
    shuffle(competitors)
    # Decide how many rounds of moves to make
    num_rounds = randint(0, max_rounds)
    # For each round generate a random move for each competitor
    # and save and print it
    moves = []
    for round_no in range(num_rounds):
        print()
        for competitor in competitors:
            # Create a random move
            move = [competitor, choice(['Left', 'Right', 'Up', 'Down'])]
            # Print it to the shell and remember it
            print(move)
            moves.extend(move)
    # Print a final message and return the list of moves
    print('\nThere were', len(competitors) * num_rounds,
          'moves generated in', num_rounds,
          ('round' if num_rounds == 1 else 'rounds'))
    return moves
             
#
#--------------------------------------------------------------------#





#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "process_moves" function.
#

# Draw competitors on the grid as per the provided data set
#Constant Values (ADDED)
left_edge1  = -(grid_size * cell_width) // 2
left_edge2  = -(grid_size * cell_width) // 2

right_edge1 = (grid_size * cell_width) // 2
right_edge2 = (grid_size * cell_width) // 2

bottom_line1 = -(grid_size * cell_height) // 2
bottom_line2 = -(grid_size * cell_height) // 2

top_line1 = (grid_size * cell_height) // 2
top_line2 = (grid_size * cell_height) // 2

speed("fastest")



#Part B of Assigment
#Moves the competitor to the left and state if they reached middle (home)
medium_font = ('Time New Roman', 15, 'normal')
def winner():
    penup()
    color('black')
    goto((grid_size * cell_width) // 2 + 50, -cell_height // 3 + 120)
    write('First competitor \n to reach home:', align = 'left', font = medium_font)
    goto((grid_size * cell_width) // 2 + 50, -cell_height // 3 + 60)
    setheading(0)
#States if none of the competitor reached middle (home)
def none():
    penup()
    color('black')
    goto((grid_size * cell_width) // 2 + 50, -cell_height // 3 + 120)
    write('First competitor \n to reach home: \n NONE', align = 'left', font = medium_font)



def process_moves(data_set):
    #Taking values from Constant Values 
    global left_edge1, left_edge2, right_edge1, right_edge2, bottom_line1, bottom_line2, top_line1, top_line2

    A_reached_home = False
    B_reached_home = False
    C_reached_home = False
    D_reached_home = False

    winners = []
    
    #Setting Competitors in their corners
    competitors = [cat(), turtle(), panda(), starfish()]
    direction = 0
    #Setting turtle's direction with each moves (Up, Down, Right, Left)
    for data in data_set:
        if data[1] == 'Up':
            direction = 90
        elif data[1] == 'Down':
            direction = 270
        elif data[1] == 'Right':
            direction = 0
        elif data[1] == 'Left':
            direction = 180
            
        #For Competitor A
        if data[0] == 'Competitor A':
            #UP (90 Pixels = cell height)
            if direction == 90:
                    top_line1 += cell_height
                    setheading(0)
                    #Stops it from going out of top border
                    if top_line1 <= 315:
                        cat()
                        distance(0,0)
                        #States if Competitor A reaches home square
                        if distance(0, 0) < 45:
                            winners.append("cat") 
                            A_reached_home = True
                    else:
                        top_line1 = 315
            #DOWN (-90 Pixels = -cell height)
            elif direction == 270:
                    top_line1 -= cell_height
                    setheading(0)
                    #Stops it from going out of bottom border
                    if top_line1 >= -225:
                        cat()
                        distance(0,0)
                        #States if Competitor A reaches home square
                        if distance(0, 0) < 45:
                            winners.append("cat") 
                            A_reached_home = True
                    else:
                        top_line1 = -225
            #RIGHT (120 Pixels = cell width)
            if direction == 0: 
                    left_edge1 += cell_width
                    setheading(0)
                    #Stops it from going out of right border 
                    if left_edge1 <= 300: 
                        cat()
                        distance(0,0)
                        #States if Competitor A reaches home square
                        if distance(0, 0) < 45:
                            winners.append("cat") 
                            A_reached_home = True
                    else:
                        left_edge1 = 300
                    
            #LEFT   (-120 Pixels = -cell width)
            elif direction == 180:
                    left_edge1 -= cell_width
                    setheading(0)
                    
                    #Stops it from going out of left border
                    if left_edge1 > -420:
                        cat()
                        distance(0,0)
                        #States if Competitor A reaches home square
                        if distance(0, 0) < 45:
                            winners.append("cat") 
                            A_reached_home = True
                    else:
                        left_edge1 = -420
                        
        #For Competitor B
        elif data[0] == 'Competitor B':
            #UP (90 Pixels = cell height)
            if direction == 90:
                    top_line2 += cell_height
                    setheading(0)
                    #Stops it from going out of top border
                    if top_line2 <= 315:
                        turtle()
                        distance(0,0)
                        #States if Competitor B reaches home square
                        if distance(0, 0) < 45:
                            winners.append("turtle") 
                            A_reached_home = True
                    else:
                        top_line2 = 315

            #DOWN (-90 Pixels = -cell height)
            elif direction == 270:
                    top_line2 -= cell_height
                    setheading(0)
                    #Stops it from going out of bottom border
                    if top_line2 >= -225:
                        turtle()
                        distance(0,0)
                        #States if Competitor B reaches home square
                        if distance(0, 0) < 45:
                            winners.append("turtle") 
                            A_reached_home = True
                    else:
                        top_line2 = - -225
            #RIGHT (120 Pixels = cell width)
            if direction == 0: 
                    right_edge1 += cell_width
                    setheading(0)
                    #Stops it from going out of right border
                    if right_edge1 <= 420:
                        turtle()
                        distance(0,0)
                        #States if Competitor B reaches home square
                        if distance(0, 0) < 45:
                            winners.append("turtle") 
                            A_reached_home = True
                    else:
                        right_edge1 = 420
            #LEFT   (-120 Pixels = -cell width)
            elif direction == 180:
                    right_edge1 -= cell_width
                    setheading(0)
                    #Stops it from going out of left border
                    if right_edge1 >= -300:
                        turtle()
                        distance(0,0)
                        #States if Competitor B reaches home square
                        if distance(0, 0) < 45:
                            winners.append("turtle") 
                            A_reached_home = True
                    else:
                        right_edge1 = -300

        #For Competitor C
        elif data[0] == 'Competitor C':
            setheading(direction)
            #UP (90 Pixels = cell height)
            if direction == 90:
                    bottom_line1 += cell_height
                    setheading(0)
                    #Stops it from going out of top border
                    if bottom_line1 <= 225:
                        panda()
                        distance(0,0)
                        #States if Competitor C reaches home square
                        if distance(0, 0) < 45:
                            winners.append("panda") 
                            A_reached_home = True
                    else:
                        bottom_line1 = 225
            #DOWN (-90 Pixels = -cell height)
            elif direction == 270:
                    bottom_line1 -= cell_height
                    setheading(0)
                    #Stops it from going out of bottom border
                    if bottom_line1 >= -315:
                        panda()
                        distance(0,0)
                        #States if Competitor C reaches home square
                        if distance(0, 0) < 45:
                            winners.append("panda") 
                            A_reached_home = True
                    else:
                        bottom_line1 = -315
            #RIGHT (120 Pixels = cell width)
            if direction == 0: 
                    left_edge2 += cell_width
                    setheading(0)
                    #Stops it from going out of right border
                    if left_edge2 <= 300:
                        panda()
                        distance(0,0)
                        #States if Competitor C reaches home square
                        if distance(0, 0) < 45:
                            winners.append("panda") 
                            A_reached_home = True
                    else:
                        left_edge2 = 300
            #LEFT   (-120 Pixels = -cell width)
            elif direction == 180:
                    left_edge2 -= cell_width
                    setheading(0)
                    #Stops it from going out of left border
                    if left_edge2 >= -420:
                        panda()
                        distance(0,0)
                        #States if Competitor C reaches home square
                        if distance(0, 0) < 45:
                            winners.append("panda") 
                            A_reached_home = True
                    else:
                        left_edge2 = -420
        #For Competitor D
        else:
            #UP (90 Pixels = cell height)
            if direction == 90:
                    bottom_line2 += cell_height
                    setheading(0)
                    #Stops it from going out of top border
                    if bottom_line2 <= 225:
                        starfish()
                        distance(0,0)
                        #States if Competitor D reaches home square
                        if distance(0, 0) < 45:
                            winners.append("starfish") 
                            A_reached_home = True
                    else:
                        bottom_line2 = 225
            #DOWN (-90 Pixels = -cell height)
            elif direction == 270:
                    bottom_line2 -= cell_height
                    setheading(0)
                    #Stops it from going out of bottom border
                    if bottom_line2 >= -315:
                        starfish()
                        distance(0,0)
                        #States if Competitor D reaches home square
                        if distance(0, 0) < 45:
                            winners.append("starfish") 
                            A_reached_home = True
                    else:
                        bottom_line2 = -315
            #RIGHT (120 Pixels = cell width)
            if direction == 0: 
                    right_edge2 += cell_width
                    setheading(0)
                    #Stops it from going out of right border
                    if right_edge2 <= 420:
                        starfish()
                        distance(0,0)
                        #States if Competitor D reaches home square
                        if distance(0, 0) < 45:
                            winners.append("starfish") 
                            A_reached_home = True
                    else:
                        right_edge2 = 420
            #LEFT   (-120 Pixels = -cell width)
            elif direction == 180:
                    right_edge2 -= cell_width
                    setheading(0)
                    #Stops it from going out of left border
                    if right_edge2 >= -300:
                        starfish()
                        distance(0,0)
                        #States if Competitor D reaches home square
                        if distance(0, 0) < 45:
                            winners.append("starfish") 
                            A_reached_home = True
                    else:
                        right_edge2 = -300
            
     #States if none of the Competitors reaches home square                   
    if A_reached_home == B_reached_home == C_reached_home == D_reached_home == False:
            none()
    #States/Visualises the winner on the right
    if len(winners) > 0:
        if winners[0] == "cat":
            winner()
            left_edge1 = 470
            top_line1 = 50
            cat()
        elif winners[0] == "turtle":
            winner()
            right_edge1 = 570
            top_line2 = 50
            turtle()
        elif winners[0] == "panda":
            winner()
            left_edge2 = 470
            bottom_line1 = 0
            panda()
        elif winners[0] == "starfish":
            winner()
            right_edge2 = 590
            bottom_line2 = 0
            starfish()
        

                
#Writing Competitors on board
penup()
#Competitor A
tracer(False)
goto(left_edge1 - cell_width, top_line1 - (cell_height/2))
pencolor('black')
write('Competitor A:\nCats', font=("Time New Roman", 12 ,"normal"))
#Competitor B
tracer(False)
goto(right_edge1 + (cell_width/4), top_line2 - (cell_height/2))
pencolor('black')
write('Competitor B:\nTurtles', font=("Time New Roman", 12 ,"normal"))
#Competitor C
tracer(False)
goto(left_edge2 - cell_width, bottom_line1 + (cell_height/2))
pencolor('black')
write('Competitor C:\nPandas', font=("Time New Roman", 12 ,"normal"))
#Competitor D
tracer(False)
goto(right_edge2 + (cell_width/4), bottom_line2 + (cell_height/2))
pencolor('black')
write('Competitor D:\nStarfishes', font=("Time New Roman", 12 ,"normal"))


cat = 'Competitor A'
def cat():
    tracer(False)
    #setting default pen settings
    pencolor('black')
    width(1)
    penup()
    #Colouring top left cell brown
    goto(left_edge1, top_line1)
    pendown()
    begin_fill()
    for brown_square in range(2):
        forward(cell_width)
        right(90)
        forward(cell_height)
        right(90)
    color('brown')
    end_fill()
    #Drawing a cat
    penup()
    #Centering the cat in the middle of the top left cell
    goto(left_edge1+60, top_line1-67.5) 
    pensize(3)
    #Draw head
    color('black')
    pendown()
    circle(25)
    #Draw right ear
    penup()
    goto(left_edge1+82.5, top_line1-32.5)
    left(90)
    pendown()
    forward(25)
    left(120)
    forward(18.75)
    #Draw left ear
    penup()
    goto(left_edge1+36, top_line1-32.5)
    pendown()
    setheading(84)
    forward(25)
    right(120)
    forward(18.75)
    #Draw left eye
    penup()
    goto(left_edge1+45,top_line1-35)
    pendown()
    left(90)
    for left_eye in range(12):
        forward(1)
        right(10)
    #Draw right eye
    penup()
    setheading(0)
    goto(left_edge1+65, top_line1-35)
    pendown()
    left(45)
    for right_eye in range(12):
        forward(1)
        right(10)
    #Draw nose
    penup()
    goto(left_edge1+55, top_line1-42.5)
    pendown()
    width(0.1)
    color('black')
    begin_fill()
    setheading(0)
    for nose in range(3):
        forward(6.25)
        right(120)
    end_fill()
    #Draw mouth
    penup()
    setheading(270)
    goto(left_edge1+60, top_line1-47)
    pendown()
    width(2)
    circle(5, 180)
    penup()
    goto(left_edge1+60, top_line1-47)
    pendown()
    circle(5, -180)
    #Draw tongue
    penup()
    setheading(270)
    goto(left_edge1+55, top_line1-53)
    pendown()
    for tongue in range(8):
        forward(2.5)
        left(25)
    #Draw left whisker 1
    penup()
    goto(left_edge1+45, top_line1-45)
    pendown()
    goto(left_edge1+30, top_line1-40)
    #Draw left whisker 2
    penup()
    goto(left_edge1+45, top_line1-45)
    pendown()
    goto(left_edge1+30, top_line1-50)
    #Draw right whisker 1
    penup()
    goto(left_edge1+75, top_line1-45)
    pendown()
    goto(left_edge1+90, top_line1-40)
    #Draw right whisker 2
    penup()
    goto(left_edge1+75, top_line1-45)
    pendown()
    goto(left_edge1+90, top_line1-50)
    penup()

    
turtle = 'Competitor B'
def turtle():
    tracer(False)
    #setting default pen settings
    pencolor('black')
    width(1)
    penup()
    #Colouring top right cell green
    goto(right_edge1, top_line2)
    setheading(180)
    pendown()
    begin_fill()
    for green_square in range(2):
        forward(cell_width)
        left(90)
        forward(cell_height)
        left(90)
    color('green') 
    end_fill()
    #Drawing a turtle
    penup()
    #Centering the turtle in the middle of the top right cell
    pendown()
    goto(right_edge1-60, top_line2-45)
    #Draw body
    dot(50, 'black')
    penup()
    #Draw neck and head
    color('black')
    width(3)
    goto(right_edge1-35, top_line2-42)
    begin_fill()
    setheading(45)
    pendown()
    forward(10)
    setheading(-45)
    forward(15)
    setheading(225)
    forward(15)
    setheading(135)
    forward(10)
    end_fill()
    penup()
    #Draw left leg 1
    goto(right_edge1-47.5, top_line2-20)
    pendown()
    dot(12)
    #Draw left leg 2
    penup()
    goto(right_edge1-72.5, top_line2-20)
    pendown()
    dot(12)
    #Draw right leg 1
    goto(right_edge1-47.5, top_line2-70)
    pendown()
    dot(12)
    #Draw right leg 2
    penup()
    goto(right_edge1-72.5, top_line2-70)
    pendown()
    dot(12)
    #Draw tail
    penup()
    goto(right_edge1-85, top_line2-42)
    pendown()
    begin_fill()
    setheading(225)
    forward(6)
    setheading(315)
    forward(7)
    end_fill()
    penup()



panda = 'Competitor C'
def panda():
    tracer(False)
    #setting default pen settings
    pencolor('black')
    width(1)
    penup()
    #Colouring the bottom left cell white
    goto(left_edge2, bottom_line1)
    setheading(0)
    pendown()
    begin_fill()
    for white_square in range(2):
        forward(cell_width)
        left(90)
        forward(cell_height)
        left(90)
    color('white')
    end_fill()
    #Drawing a panda
    penup()
    #Centering the panda in the middle of the bottom left cell
    goto(left_edge2+60, bottom_line1+22.5)
    pensize(3)
    #Draw head
    color('black')
    pendown()
    circle(25)
    #Draw right ear
    penup()
    goto(left_edge2+72.5, bottom_line1+68.75)
    pendown()
    begin_fill()
    right(90)
    circle(7.5, -260)
    end_fill()
    #Draw left ear
    penup()
    goto(left_edge2+47.5, bottom_line1+68.75)
    pendown()
    left(170)
    begin_fill()
    right(90)
    circle(7.5, 260)
    end_fill()
    #Draw left eye
    penup()
    goto(left_edge2+50, bottom_line1+45)
    pendown()
    begin_fill()
    circle(7.5)
    end_fill()
    left(10)
    penup()
    goto(left_edge2+52.5, bottom_line1+50)
    pendown()
    color('white')
    begin_fill()
    circle(3.75)
    end_fill()
    penup()
    goto(left_edge2+52.5, bottom_line1+51.25)
    pendown()
    color('black')
    begin_fill()
    circle(1)
    end_fill()
    #Draw right eye
    penup()
    goto(left_edge2+70, bottom_line1+45)
    pendown()
    color('black')
    begin_fill()
    circle(7.5)
    end_fill()
    penup()
    goto(left_edge2+67.5, bottom_line1+50)
    pendown()
    color('white')
    begin_fill()
    circle(3.75)
    end_fill()
    penup()
    goto(left_edge2+67.5, bottom_line1+51.75)
    pendown()
    color('black')
    begin_fill()
    circle(1)
    end_fill()
    #Draw nose
    color('black')
    penup()
    goto(left_edge2+60, bottom_line1+35)
    pendown()
    begin_fill()
    circle(2.5)
    end_fill()
    #Draw mouth
    right(90)
    circle(5, 180) 
    penup()
    goto(left_edge2+60, bottom_line1+35)
    pendown()
    circle(5, -180)
    penup()
    

starfish = 'Competitor D'
def starfish():
    tracer(False)
    #setting default pen settings
    pencolor('black')
    width(1)
    penup()
    #Colouring bottom right cell blue
    goto(right_edge2, bottom_line2)
    setheading(180)
    pendown()
    begin_fill()
    for blue_square in range(2):
        forward(cell_width)
        right(90)
        forward(cell_height)
        right(90)
    color('blue')
    end_fill()
    #Drawing a starfish
    penup()
    #Centering the starfish in the middle of the bottom right cell
    goto(right_edge2-75, bottom_line2+22.5)
    pensize(3)
    #Draw stars
    color('orange')
    setheading(74)
    pendown()
    begin_fill()
    for starfish in range(5): 
        forward(50)
        right(144)
    end_fill()
    #Drawing details for the starfish
    penup()
    goto(right_edge2-60, bottom_line2+45)
    dot(3, 'black')
    pendown()
    penup()
    #top line for starfish
    setheading(90)
    color('black')
    width(1.5)
    pendown()
    forward(22)
    pendown()
    penup()
    #right line for starfish
    goto(right_edge2-60, bottom_line2+45)
    setheading(20)
    pendown()
    forward(22)
    #left line for starfish
    goto(right_edge2-60, bottom_line2+45)
    setheading(165)
    pendown()
    forward(22)
    #bottom-right line for starfish
    goto(right_edge2-60, bottom_line2+45)
    setheading(310)
    pendown()
    forward(22)
    #bottom-left line for starfish
    goto(right_edge2-60, bottom_line2+45)
    setheading(235)
    pendown()
    forward(22)
    penup()

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution, and calls your solution.  Do not change
# any of this code except as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, choose
# ***** whether or not to label the axes, etc, by providing
# ***** arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its competitors
title('One Island Four Animals')


### Call the student's function to process the moves
### ***** While developing your program you can call the
### ***** "random_moves" function with a fixed seed for the random
### ***** number generator, but your final solution must work with
### ***** "random_moves()" as the argument to "process_moves", i.e.,
### ***** for any data set that can be returned by calling
### ***** "random_moves" with no seed.
process_moves(random_moves()) # <-- this will be used for assessment

### Alternative function call to help debug your code
### ***** The following function call can be used instead of
### ***** the one above while debugging your code, but will
### ***** not be used for assessment. Comment out the call
### ***** above and uncomment the one below if you want to
### ***** call your "process_moves" function with one of the
### ***** "fixed" data sets above, so that you know in advance
### ***** what the moves are.
#process_moves(data_set_06) # <-- not used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid.
release_drawing_canvas()

#
#--------------------------------------------------------------------#
