class Solution:
    def searchMatrix(self, matrix, target):
        
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        s = 0 
        e = size - 1


        while s <= e:
            mid = (s + e) // 2

            outterIdx = mid // n
            innerIdx = mid % n
            if target == matrix[outterIdx][innerIdx]:
                return True
            elif target < matrix[outterIdx][innerIdx]:
                e = mid - 1
            elif target > matrix[outterIdx][innerIdx]:
                s = mid + 1
        else:
            return False