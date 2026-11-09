class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(numRows - 1):
            row = triangle[-1]
            new_row = [1]
            for j in range(1, len(row)):
                new_row.append(row[j-1] + row[j])
            new_row.append(1)
            triangle.append(new_row)
        return triangle 
