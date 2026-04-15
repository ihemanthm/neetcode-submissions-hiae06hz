class Solution:
    def validator(self, nums: List[str]) -> bool:
        unique_nums = set()
        for each in nums:
            if each == '.':
                continue
            if each in unique_nums:
                return False
            unique_nums.add(each)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        rows_valid = True
        for row in board:
            rows_valid &= self.validator(row)
        if not rows_valid:
            print("rows invalid")
            return False
        
        cols_valid = True
        for j in range(cols):
            col_as_row = []
            for i in range(rows):
                col_as_row.append(board[i][j])
            cols_valid &= self.validator(col_as_row)
        
        if not cols_valid:
            print("cols invalid")
            return False
        sub_boxes_valid = True
        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                sub_box_as_list = []
                for k in range(3):
                    sub_box_as_list.extend(board[i+k][j:j+3])
                sub_boxes_valid &= self.validator(sub_box_as_list) 
        print("sub boxes invalid")
        return sub_boxes_valid
        
        

        
