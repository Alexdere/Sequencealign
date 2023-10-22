import blosum as bl
#from uib_inf100_graphics.event_app import run_app
from uib_inf100_graphics.simple import canvas, display

from kladd4 import blosum62 
# Define input sequences
sequence1 = "AGTACG"
sequence2 = "AGCTCG"
sequence1 = "GATTACA"
sequence2 = "GCATGCT"

#scoresystem = input("enter 1 or 2")
# i want the matrix to have green colors on the letters part of the allignment
def create_matrix(sequence1, sequence2, gap):  # Renamed the function
    mat = [[0] * (len(sequence2) + 2) for i in range(len(sequence1) + 2)]  # Renamed the variable

    mat[0][2:] = list(sequence2)
    mat[0][1] = "d"
    mat[1][0] = "q"
    for i in range(1, len(sequence1) + 1):  # Changed index to start at 1
        mat[i+1][0] = sequence1[i - 1]
        

    # Fill the second row with gap penalties
    for j in range(2, len(mat[1])):
        mat[1][j] = j * gap+1

    # Fill the second element in other rows with gap penalties
    for i in range(2, len(mat)):
        mat[i][1] = (i - 1) * gap

    return mat
def score_blosum(a, b):
    score = blosum62.get((a, b), None)
    if score is None:
        score = blosum62.get((b, a), 0)  # Try the reverse pair, default to 0 if not found
    return score

def score(a, b, match_score=1, mismatch_score=-1):
    if a == b:
       return match_score
    else:
        return mismatch_score
    
#gap_penalty = -1  # change score to score_blosum in score_values and backtrack!
def score_values(sequence1, sequence2, mat, gap):
    for i in range(2, len(sequence1) + 2):
        for j in range(2, len(sequence2) + 2):
            #diagonal = mat[i-1][j-1] + score(sequence1[i-2], sequence2[j-2])
            diagonal = mat[i-1][j-1] + score(sequence1[i-2], sequence2[j-2])
            top = mat[i-1][j] + gap
            left = mat[i][j-1] + gap
            
            mat[i][j] = max(diagonal, top, left)
    return mat
#a = score_values(sequence1, sequence2, mat, gap)

def draw_board(canvas, x1, y1, x2, y2, mat,boolean, path ):
    rows = len(mat)
    cols = len(mat[0])
    t = False
    cell_width = (x2 - x1) / cols
    cell_height = (y2 - y1) / rows
    debug_mode = boolean

    # Initialize list to hold the current sublist
    current_sublist = []
    # Initialize list to hold all sublists
    all_sublists = []
    

    aligned = backtrack(sequence1, sequence2, mat, -1)
    canvas.create_text(200, 15, anchor = "center", text = aligned[0:-2], font = "Arial 15",fill = "black" )
    canvas.create_text(200, 35, anchor = "center", text = aligned[1:-1], font = "Arial 15",fill = "black" )
    
    # Initialize list to hold the current sublist
    current_sublist = []
    # Initialize list to hold all sublists
    all_sublists = []
    # Iterate through path
    for i in range(len(path) - 1):
        row1, col1 = path[i]
        row2, col2 = path[i + 1]
        
        # Check if the current and next cells are adjacent and in the same column
        if col1 == col2 and row1 == row2 + 1:
            # If the current sublist is empty, add both cells to it
            if not current_sublist:
                current_sublist.extend([path[i], path[i + 1]])
            else:
                # If the current sublist is not empty, just add the next cell
                current_sublist.append(path[i + 1])
        else:
            # If the cells are not adjacent in the same column, 
            # add the current sublist to all_sublists and reset current_sublist
            if current_sublist:
                all_sublists+=current_sublist
                current_sublist = []

    # Handle the case where the last sublist goes up to the last element in path
    if current_sublist:
        all_sublists.append(current_sublist)
  
    for row in range(rows):
        n=0
       
        for col in range(cols):
            
            path2 = []
            path2.append([row,col]) # lagrer alle ruter
            

            cell_left = x1 + col * cell_width
            cell_top = y1 + row * cell_height
            cell_right = cell_left + cell_width
            cell_bottom = cell_top + cell_height
            color = mat[row][col]
        
            cell_center_x = (cell_left + cell_right) / 2
            cell_center_y = (cell_top + cell_bottom) / 2
            
            for rowcol in path2:
                if rowcol in path:  # fargelegg ruter som er regnet ut i backtrack
                    co = "red"
                    n +=1
                    if rowcol in path and n>1:
                        t = True
                        if t ==True:
                            r = row
                ###[ grønne bokstaver
                elif row == 0 and col >1:
                    co = "#00FF00"
                elif row >1 and col == 0:
                    co = "#00FF00" ##]
                else:
                    co = get_color(color)
            
            canvas.create_rectangle( #################################### plasere inn piler?
                cell_left, cell_top, cell_right, cell_bottom,
            
                fill=co, 
            )
            if debug_mode == True:
                canvas.create_text(cell_center_x-7, cell_center_y,
                        text=str(color),
                        font='Arial 12')
                # Draw the cell number text
           
    for row in range(rows):
        for col in range(cols):
            col_exists = any(col == col_idx for row_idx, col_idx in all_sublists)
            stop_column = []
            
            for i in all_sublists:
                stop_column.append(i[1])

            #print(col_exists)
            #print(col)
            if (r == row  or (row < r and row >1))and col == 0: ######### Fargelegg lilla før første gap for q
                co = "#BA55D3"
                cell_left = x1 + col * cell_width
                cell_top = y1 + row * cell_height
                cell_right = cell_left + cell_width
                cell_bottom = cell_top + cell_height
                color = mat[row][col]
            
                cell_center_x = (cell_left + cell_right) / 2
                cell_center_y = (cell_top + cell_bottom) / 2
                canvas.create_rectangle(
                cell_left, cell_top, cell_right, cell_bottom,
            
                fill=co,) 
                if debug_mode == True:
                    canvas.create_text(cell_center_x-7, cell_center_y,
                            text=str(color),
                            font='Arial 12')
                    
        
            if row == 0 and col < min(stop_column) and col >1 : ############# fargelegg lilla før første gap d
                    
                    co = "#BA55D3"
                    cell_left = x1 + col * cell_width
                    cell_top = y1 + row * cell_height
                    cell_right = cell_left + cell_width
                    cell_bottom = cell_top + cell_height
                    color = mat[row][col]
                
                    cell_center_x = (cell_left + cell_right) / 2
                    cell_center_y = (cell_top + cell_bottom) / 2
                    canvas.create_rectangle(
                    cell_left, cell_top, cell_right, cell_bottom,
                
                    fill=co,) 
                    if debug_mode == True:
                        canvas.create_text(cell_center_x-7, cell_center_y,
                                text=str(color),
                                font='Arial 12') 
                        
            
            elif col_exists and row == 0:
                co = "#BA55D3"
                
                cell_left = x1 + col * cell_width
                cell_top = y1 + row * cell_height
                cell_right = cell_left + cell_width
                cell_bottom = cell_top + cell_height
                color = mat[row][col]
            
                cell_center_x = (cell_left + cell_right) / 2
                cell_center_y = (cell_top + cell_bottom) / 2
                canvas.create_rectangle(
                cell_left, cell_top, cell_right, cell_bottom,
            
                fill=co,) 
                if debug_mode == True:
                    canvas.create_text(cell_center_x-7, cell_center_y,
                            text=str(color),
                            font='Arial 12') #### ]
    print(min(stop_column))
            
            #else:
                #break
   

def backtrack(sequence1, sequence2, mat, gap): #need to add code that checks if the path has the lowest possible score, and finds multiple pathways if there
    i = len(sequence1)  # initialize i at the length of sequence1
    j = len(sequence2) # initialize j at the length of sequence2
    path = []
    aligned_seq1 = []
    aligned_seq2 = []

    while i > 0 and j > 0:
        #path.append([i+1,j+1])
        #print(path)
        current = mat[i+1][j+1]  # +1 due to the extra row and column in your matrix
        diagonal = mat[i][j]
        up = mat[i][j+1]
        left = mat[i+1][j]
        
        if current == diagonal + score(sequence1[i-1], sequence2[j-1]):
            path.append([i+1,j+1])
            aligned_seq1.append(sequence1[i-1])
            aligned_seq2.append(sequence2[j-1])
            i -= 1
            j -= 1
        elif current == up + gap:
            path.append([i+1,j+1])
            aligned_seq1.append(sequence1[i-1])
            aligned_seq2.append('-')
            i -= 1
        else:
            path.append([i+1,j+1])
            aligned_seq1.append('-')
            aligned_seq2.append(sequence2[j-1])
            j -= 1

    while i > 0:
        aligned_seq1.append(sequence1[i-1])
        aligned_seq2.append('-')
        i -= 1

    while j > 0:
        aligned_seq1.append('-')
        aligned_seq2.append(sequence2[j-1])
        j -= 1

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)),path

def get_color(value): #regn ut fargen basert på regler
    while True:
        try:
            if int(value) == 0:
                return "lightgray"
            elif int(value) >0: 
                    
                return "orange"
                    
                
            elif int(value) <0:
                return "cyan"
        except:
            break


aligned_seq1, aligned_seq2, path = backtrack(sequence1, sequence2, score_values(sequence1, sequence2, create_matrix(sequence1, sequence2, -1), -1), -1)
draw_board(canvas, 10, 50, 390, 390, score_values(sequence1, sequence2,create_matrix(sequence1, sequence2, -1), -1), True, path)
display(canvas)
print(aligned_seq1, aligned_seq2) 

