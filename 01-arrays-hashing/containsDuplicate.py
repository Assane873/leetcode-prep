from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        un_set = set()
        for i in range(len(nums)):
            if nums[i] in un_set:
                return True
            un_set.add(nums[i])     
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 1]))
    print(sol.hasDuplicate([1, 2, 3, 4]))
    
           




