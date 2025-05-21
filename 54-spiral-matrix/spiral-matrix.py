from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Left to Right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Top to Bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Right to Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Bottom to Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
