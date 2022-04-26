class Solution:
    def plusOne(self, digits : list) -> list:
        digits = [y for y in digits if y % 2 == 0 if y % 5 == 0]
        return digits

Obj = Solution()
List = [10,5,20,4,200,12]
print(Obj.plusOne(List))
