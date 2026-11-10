class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros_count = 0
        for num in nums:
            if num == 0:
                zeros_count += 1
            
            if num!=0:
                product *= num

        print(zeros_count)

        result = []
        for num in nums:
            if zeros_count == 0:
                result.append(int(product/num))
            elif zeros_count == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(0)


        return result