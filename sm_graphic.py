matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 2, 1, 0, 1],
[0, 0, 0, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 2, 1, 0, 0, 0]] 
matrix2 = [[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 6, 5, 4, 3, 6, 5, 4],
 [0, 5, 6, 9, 8, 7, 6, 5],
 [0, 4, 5, 8, 14, 13, 12, 11],
 [0, 3, 4, 7, 13, 12, 12, 17],
 [0, 2, 3, 8, 12, 13, 12, 16],
 [0, 1, 11, 10, 11, 12, 22, 21],
 [0, 0, 10, 15, 14, 13, 21, 21]]
matrix3 =[[0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 2, 1, 0, 0, 1],
 [0, 0, 1, 1, 2, 1, 0],
 [0, 1, 0, 0, 1, 1, 0],
 [0, 0, 0, 1, 0, 2, 1],
 [0, 0, 1, 0, 0, 1, 3]]
matrix4 = [[0, 0, 0, 0, 0, 0, 0],
 [0, 4, 3, 2, 1, 0, 0],
 [0, 3, 10, 9, 8, 7, 6],
 [0, 2, 9, 10, 14, 13, 12],
 [0, 4, 8, 9, 13, 13, 12],
 [0, 3, 7, 17, 16, 22, 21],
 [0, 2, 9, 16, 15, 21, 28]]

#sequence1 = "AGTACG"
#sequence2 = "AGCTCG"
sequence1 = "GATTACA"
sequence2 = "GCATGCT"

from uib_inf100_graphics.simple import canvas, display

def draw_board(canvas, x1, y1, x2, y2, matrix2):

    rows = len(matrix2)
    cols = len(matrix2[0])
    cell_width = (x2 - x1) / (cols + 1)  # Add one more cell width for the new column
    cell_height = (y2 - y1) / (rows + 1)  # Add one more cell height for the new row
    title_x = x1 + (x2 - x1) / 2  # Center of the board width-wise
    title_y = y1 - 20  # 20 pixels above the board

    # Draw the title
    canvas.create_text(title_x, title_y, anchor="center", text=' G-ATTAC/GCA-TGC  ', font="Arial 14", fill="black")
    # Draw the empty rectangles in the new row and column
    for col in range(1, cols + 1):  # Start from 1 to leave the top-left corner empty
        canvas.create_rectangle(
            x1 + col * cell_width, y1,
            x1 + (col + 1) * cell_width, y1 + cell_height,
            fill="white"
        )
        # Add letters for sequence2 above
        if col<9 and col >1:
            canvas.create_text(
                x1 + col * cell_width + cell_width / 2, y1 + cell_height / 2,
                anchor="center", text=sequence2[col-2], font="Arial 10", fill="black"
            )
    
    for row in range(1, rows + 1):  # Start from 1 to leave the top-left corner empty
        canvas.create_rectangle(
            x1, y1 + row * cell_height,
            x1 + cell_width, y1 + (row + 1) * cell_height,
            fill="white"
        )
        # Add letters for sequence1 to the left
        if row<9 and row >1:
            canvas.create_text(
                x1 + cell_width / 2, y1 + row * cell_height + cell_height / 2,
                anchor="center", text=sequence1[row-2], font="Arial 10", fill="black"
            )
        

    # Draw the board as before, but offset by one row and one column
    for row in range(rows):
        for col in range(cols):
            cell_left = x1 + (col + 1) * cell_width  # Offset by one for the new column
            cell_top = y1 + (row + 1) * cell_height  # Offset by one for the new row
            cell_right = cell_left + cell_width
            cell_bottom = cell_top + cell_height

            # Draw the cell rectangle
            canvas.create_rectangle(
                cell_left, cell_top, cell_right, cell_bottom, fill="white"
            )

            # Draw the cell value
            cell_center_x = (cell_left + cell_right) / 2
            cell_center_y = (cell_top + cell_bottom) / 2
            canvas.create_text(
                cell_center_x, cell_center_y, anchor="center",
                text=str(matrix2[row][col]), font="Arial 10", fill="black"
            )

draw_board(canvas, 10, 50, 390, 390, matrix2)
display(canvas)
                
