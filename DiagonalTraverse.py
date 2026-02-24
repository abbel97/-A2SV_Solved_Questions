class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        result = []

        for diag in range(rows + cols - 1):
            intermediate = []
            r = 0 if diag < cols else diag - cols + 1
            c = diag if diag < cols else cols - 1
            
            while r < rows and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            if diag % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result