import math
import random
import numpy as np
import os 
import re
import matplotlib.pyplot as plt

def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j],str(","),end='') 
        print ('\n') 
        
def print_puzzle(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j],str(","),end='') 
        print ('\n') 


def find_empty_squares(sudoku_array,l): 
    for row in range(9): 
        for col in range(9): 
            if(sudoku_array[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False

 
def in_same_row(sudoku_array,row,num): 
    for i in range(9): 
        if(sudoku_array[row][i] == num): 
            return True
    return False


def in_same_col(sudoku_array,col,num): 
    for i in range(9): 
        if(sudoku_array[i][col] == num): 
            return True
    return False


def in_same_grid(sudoku_array,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(sudoku_array[i+row][j+col] == num): 
                return True
    return False


def looks_good(sudoku_array,row,col,num): 

    return not in_same_row(sudoku_array,row,num) and not in_same_col(sudoku_array,col,num) and not in_same_grid(sudoku_array,row - row%3,col - col%3,num) 

class sudoku1():
    def __init__(self):
        self.assignments_1=0
        self.assignments_2=0
        self.assignments_3=0
    def sudoku_bt(self,sudoku_array): 

        l=[0,0] 
        #assignments_1=0
        if(not find_empty_squares(sudoku_array,l)): 
            return True


        row=l[0] 
        col=l[1] 


        for num in range(1,10): 

            if(looks_good(sudoku_array,row,col,num)): 

                sudoku_array[row][col]=num 
                self.assignments_1=self.assignments_1+1
                if(self.assignments_1>10000):
                    return False
                #print("assignments_1",assignments_1)
                if(self.sudoku_bt(sudoku_array)): 
                    return True

                sudoku_array[row][col] = 0

        #print("The assignment_1 is ",assignments_1)

        return False

#########################

#class sudoku2():
    def solve_btfc( self,puzzle ):    

        # get a list of the empty squares (remaining variables)
        empty_squares = get_empty_squares( puzzle )
        #assignments_2=0
        # if there are no remaining empty squares we're done
        if len(empty_squares) == 0: 

            #print_puzzle( puzzle )
            return 1

        square = get_random_square( empty_squares )
        #row = square[0]
        #col = square[1]

        l=[0,0] 
        #assignments_1=0
        if(not find_empty_squares(sudoku_array,l)): 
            return 1


        row=l[0] 
        col=l[1] 
        #print(row,col)
        remaining_values = get_remaining_values( puzzle )
        #print(remaining_values)
        values = list( remaining_values[col+row*9] )
        #print("values")
        #print(values)

        while len( values ) != 0:        
            value = values[ int( math.floor( random.random()*len( values ) ) ) ]
            values.remove(value)        
            if forward_check( remaining_values, value, row, col ):
                puzzle[row][col] = value
                #print("the assignments_2 is", self.assignments_2)
                self.assignments_2=self.assignments_2+1
                if(self.assignments_2>10000):
                        return 0
                
                if(self.solve_btfc( puzzle )):
                    return 1
                else:
                    puzzle[row][col] = 0
        

        return 0
    
    def solve_btfch( self,puzzle ):
         # get a list of the empty squares (remaining variables)
        empty_squares = get_empty_squares( puzzle )
        #assignments_3=0

        # if there are no remaining empty squares we're done
        if len(empty_squares) == 0: 

           # print_puzzle( puzzle )
            return 1

        # find the most constrained square (one with least remaining values)
        remaining_values = get_remaining_values( puzzle )
        mrv_list = []
        [ mrv_list.append( len( remaining_values[ square[0]*9+square[1] ] ) ) for square in empty_squares ]
       # print(square[0],square[1])
        #print("remaining values")
        #print(remaining_values)
        #print("mrv")
        #print(mrv_list)
        # make a list of the squares with the minimum remaining values (mrv)
        mrv_squares = []
        minimum = min( mrv_list )
        for i in range(len(mrv_list)):
            value = mrv_list[i]
            if value == minimum:
                mrv_squares.append( empty_squares[i] )

        # if there are no ties, take the square with the MRV
        if len( mrv_squares ) == 1:
            square = mrv_squares[0]
            #print("taking mrv")
            #print(square)
        else:
            # otherwise, find the most constraining variable (variable with highest degree)
            degree_list = []
            for cell in mrv_squares:  
                degree = get_degree( cell, puzzle )
                degree_list.append( degree )

                max_degree = max( degree_list )
                max_degree_squares = []
                for i in range(len(degree_list)):      
                    value = degree_list[i]
                    if value == max_degree:
                        max_degree_squares.append( mrv_squares[i] )
                # just take the first square as a tie-breaker      
                square = max_degree_squares[0]

            #print("taking most constarint")
            #print(square)


        row = square[0]
        col = square[1]

        values = list( remaining_values[col+row*9] )

        while len( values ) != 0:        

            lcv_list = get_lcv( values, row, col, remaining_values )
            # take the least constraining value
            value = values[ lcv_list.index( min( lcv_list ) ) ]
            values.remove(value)        
            if forward_check( remaining_values, value, row, col ):
                puzzle[row][col] = value
                self.assignments_3=self.assignments_3+1
                if(self.assignments_3>10000):
                    return 0
                if (self.solve_btfch( puzzle )):
                    return 1
                else:
                    puzzle[row][col] = 0

           # print("The assignment_3 is ",assignments_3)

        return 0


def forward_check( remaining_values, value, row, col ):    

    for i in range(9):
        if i == col:
            continue    
            
        x = remaining_values[row*9+i]
                
        if len(x) == 1:
            if x[0] == value:
                return 0
     
    for i in range(9):
        if i == row:
            continue
            
        x = remaining_values[col+9*i]
        if len(x) == 1:
            if x[0] == value:
                return 0

    block_row = math.floor(row/3)
    block_col = math.floor(col/3)  
    for i in range(3):
        for j in range(3):
            
            if [block_row*3+i, block_col*3+j] == [row, col]:
                continue            
            
            x = remaining_values[block_col*3+j+(block_row*3+i)*9]
            if len(x) == 1:
                if x[0] == value:
                    return 0                                  
    return 1                          


# Returns a list of the remaining potential values for each of the 81 squares
# The list is structured row by row with respect to the puzzle
# Only gets called once, at the beginning of the BT-FC search to initialize
def get_remaining_values( puzzle ):
    remaining_values = []
    # initialize all remaining values to the full domain
    [remaining_values.append( list(range(1,10)) ) for i in range(81) ] 
    
    for row in range( len(puzzle) ):
        for col in range( len(puzzle[1]) ):
            if puzzle[row][col] != 0:
                # remove the value from the constrained squares  
                value = puzzle[row][col]  
                remaining_values = remove_values( row, col, value, remaining_values ) 
                #print(remaining_values)
                
    return remaining_values     
                        
                        
# Removes the specified value from constrained squares and returns the new list
def remove_values( row, col, value, remaining_values ):
    #print("the row is and column is")
    #print(row,col)
    # use a value of zero to indicate that the square is assigned
    remaining_values[col+row*9] = [0]
    
    # Remove the specified value from each row, column, and block if it's there
    for x in (remaining_values[row*9:row*9+9]):
        try:
            x.remove( value )
        except ValueError:  
            pass 
            
    for i in range(9):
        try:
            remaining_values[col+9*i].remove( value )
        except ValueError:
            pass

    block_row = math.floor(row/3)
    block_col = math.floor(col/3)  
    for i in range(3):
        for j in range(3):
            try:
                remaining_values[block_col*3+j+(block_row*3+i)*9].remove( value )
            except ValueError:
                pass

    return remaining_values
   
                    
# return a randomly selected square from the list of empties
def get_random_square( empty_squares ):   
    # randomly pick one of the empty squares to expand and return it
    return empty_squares[ int(math.floor(random.random()*len(empty_squares))) ]  
    
    
# return the list of empty squares indices for the puzzle
def get_empty_squares ( puzzle ):
    empty_squares = []
    # scan the whole puzzle for empty cells
    for row in range(len( puzzle )):
        for col in range(len( puzzle[1] )):
            if puzzle[row][col] == 0:
                empty_squares.append( [row,col] ) 
    return empty_squares


# counts the number of times a value appears in constrained cells
def get_lcv( values, row, col, remaining_values ):
    
    lcv_list = []
    
    for value in values: 
        count = 0   
        for i in range(9):
            if i == col:
                continue           
            x = remaining_values[row*9+i]                    
            if value in x:
                count += 1
         
        for i in range(9):
            if i == row:
                continue                
            x = remaining_values[col+9*i]
            if value in x:
                count += 1

        block_row = math.floor(row/3)
        block_col = math.floor(col/3)  
        for i in range(3):
            for j in range(3):                
                if [block_row*3+i, block_col*3+j] == [row, col]:
                    continue            
                x = remaining_values[block_col*3+j+(block_row*3+i)*9]
                if value in x:
                    count += 1 
                     
        lcv_list.append( count )
                                       
    return lcv_list

# returns the number of variables constrained by the specified square
def get_degree( square, puzzle ):
    row = square[0]
    col = square[1]
    
    degree = 0
    
    for i in range(9):
        if i == col:
            continue                
        if puzzle[row][i] == 0:
            degree+=1
     
    for i in range(9):
        if i == row:
            continue
        if puzzle[i][col] == 0:
            degree+=1

    block_row = math.floor(row/3)
    block_col = math.floor(col/3)  
    for i in range(3):
        for j in range(3):            
            if [block_row*3+i, block_col*3+j] == [row, col]:
                continue        
            if puzzle[block_row*3+i][block_col*3+j] == 0:
                degree+=1

    return degree         
    
    
if __name__=="__main__": 
    
    print("solution for normal backtracking")
    dir = 'C:/Users/himan/Downloads/sudoku_problems/sudoku_problems'
    initializations=list(range(1,72))
    assignments=[None]*71
    for folder in os.listdir(dir):
        
        avg_assignments=[None]*10
        print("the folder now is ",folder)
        folder_number=int(folder)
        for instances in os.listdir(os.path.join(dir,folder)):
        
            print("the instance now is ",instances)
            instance_number=re.search(r'\d+', instances).group(0)
            instance_number = int(instance_number)
            fil = os.path.join(dir + '/'+str(folder)+'/', instances)
            with open(fil) as infile:
                sudoku_array=np.fromstring( infile.read().replace("[","").replace("]", ""), sep="   ").reshape(9,9)
    #assignments_1=0
    
                s=sudoku1()
               # g=sudoku2()
                if(s.sudoku_bt(sudoku_array)): 
                    print_grid(sudoku_array) 
                    print("assign1",s.assignments_1)
                    avg_assignments[instance_number-1]=s.assignments_1
                else: 
                    print("No solution exists as it is taking more than 10k steps")
                    avg_assignments[instance_number-1]=s.assignments_1
        print("The avg_assignments to be calculated are",avg_assignments)
        print("the folder that is bieng updated is ",folder_number)
        assignments[folder_number-1]=sum(avg_assignments)/len(avg_assignments)
    print("the list for assignment (y) goes like", assignments)
    plt.scatter(initializations,assignments)
    plt.xlabel("initializations")
    plt.ylabel("assignments")
    plt.show()
    print("solution for backtracking+forward checking")
    
    dir = 'C:/Users/himan/Downloads/sudoku_problems/sudoku_problems'
    initializations=list(range(1,72))
    assignments=[None]*71
    for folder in os.listdir(dir):
        
        avg_assignments=[None]*10
        print("the folder now is ",folder)
        folder_number=int(folder)
        for instances in os.listdir(os.path.join(dir,folder)):
        
            print("the instance now is ",instances)
            instance_number=re.search(r'\d+', instances).group(0)
            instance_number = int(instance_number)
            fil = os.path.join(dir + '/'+str(folder)+'/', instances)
            with open(fil) as infile:
                g=sudoku1()
                sudoku_array=np.fromstring( infile.read().replace("[","").replace("]", ""), sep="   ").reshape(9,9)
                #print(sudoku_array)
                if(g.solve_btfc(sudoku_array)):
                    print_grid(sudoku_array)
                    print("The assignment_2 is ",g.assignments_2)
                    avg_assignments[instance_number-1]=g.assignments_2
                else:
                    print("No solution exists as it is taking more than 10k steps")
                    avg_assignments[instance_number-1]=g.assignments_2
        print("The avg_assignments to be calculated are",avg_assignments)
        print("the folder that is bieng updated is ",folder_number)
        assignments[folder_number-1]=sum(avg_assignments)/len(avg_assignments)
    print("the list for assignment (y) goes like", assignments)
    plt.scatter(initializations,assignments)
    plt.xlabel("initializations")
    plt.ylabel("assignments")
    plt.show()
    print("solution for backtracking+forward checking+heuristics")
    
    with open("C:/Users/himan/Downloads/sudoku_problems/sudoku_problems/1/2.sd") as infile:
       sudoku_array=np.fromstring( infile.read().replace("[","").replace("]", ""), sep="   ").reshape(9,9)

    dir = 'C:/Users/himan/Downloads/sudoku_problems/sudoku_problems'
    initializations=list(range(1,72))
    assignments=[None]*71
    for folder in os.listdir(dir):
        avg_assignments=[None]*10
        print("the folder now is ",folder)
        folder_number=int(folder)
        for instances in os.listdir(os.path.join(dir,folder)):
        
            print("the instance now is ",instances)
            instance_number=re.search(r'\d+', instances).group(0)
            instance_number = int(instance_number)
            fil = os.path.join(dir + '/'+str(folder)+'/', instances)
            with open(fil) as infile:
                h=sudoku1()
                sudoku_array=np.fromstring( infile.read().replace("[","").replace("]", ""), sep="   ").reshape(9,9)
                if(h.solve_btfch(sudoku_array)):
                    print_grid(sudoku_array) 
                    print("The assignment_3 is ",h.assignments_3)
                    avg_assignments[instance_number-1]=h.assignments_3
                else:
                    print("No solution exists as it is taking more thatn 10k steps")
                    avg_assignments[instance_number-1]=h.assignments_3
        print("The avg_assignments to be calculated are",avg_assignments)
        print("the folder that is bieng updated is ",folder_number)
        assignments[folder_number-1]=sum(avg_assignments)/len(avg_assignments)
    print("the list for assignment (y) goes like", assignments)
    print("solution for backtracking+forward checking+heuristics")
    plt.scatter(initializations,assignments)
    plt.xlabel("initializations")
    plt.ylabel("assignments")
    plt.show()

			




