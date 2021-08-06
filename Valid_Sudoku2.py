'''
See "Did I finish my Sudoku?" - 5 Kyu

'''
def done_or_not(board):

    # Check rows
    def check_rows():
        seen_in_row = set()
        for row in board:
            for number in row:
                if number not in seen_in_row:
                    seen_in_row.add(number)
                else:
                    return False
            seen_in_row.clear()

    # Check columns
    def check_columns():
        seen_in_column = set()
        row = 0
        col = 0
        while col < 9:
            while row < 9:
                if board[row][col] not in seen_in_column:
                    seen_in_column.add(board[row][col])

                else:
                    return False
                row += 1

            row = 0
            col += 1
            seen_in_column.clear()



    # Check 3x3 Boxes in a 'row'

    def check_boxes_in_row():
        start = 0
        begin = 0
        end = 3

        seen_nums = set()

        count = 0
        checked_box_row = 0

        while checked_box_row < 3:
            seen_nums.clear()

            while count < 3:
                for num in board[start][begin:end]:
                    if num not in seen_nums:
                        seen_nums.add(num)
                    else:
                        return False
                start += 1
                count += 1
                print(seen_nums)
            start = 0
            count = 0
            checked_box_row += 1
            begin += 3
            end += 3
        return True

    # Driver code
    valid_box_rows = 0

    if check_rows() == False:
        print("rows fail")
        return "Try again!"
    if check_columns() is False:
        print("cols fail")
        return "Try again!"

    while valid_box_rows < 3:
        if check_boxes_in_row() == True:
            del board[:3]
        else:
            print("boxes fail")
            return "Try again!"
        valid_box_rows += 1
    return "Finished!"
