class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2: return False
        mod_k={0:-1}
        # print("Defined mod_k is ",mod_k)
        prefix=0
        # print("Initial value of prefix is ",prefix)
        for i, x in enumerate(nums):
            prefix+=x
            # print(f"prefix value after sum at {i} is {prefix}")
            prefix%=k
            # print(f"prefix value after mod at {i} is {prefix}")
            if prefix in mod_k:
                if i-mod_k[prefix] > 1:
                    # print(f"mod_k value if condition at {i} is {mod_k}")
                    # print("True")
                    return True
            else:
                mod_k[prefix]=i
                # print(f"mod_k value after else at {i} is {mod_k}")
        return False