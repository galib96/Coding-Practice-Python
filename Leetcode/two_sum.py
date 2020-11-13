def twoSum(nums: list, target: int):
        pos_dict = {}
        for i in range(len(nums)):
            
            number = nums[i]
            
            goal = target - nums[i]
            
            if pos_dict.get(goal, -1) != -1:
                return [i, pos_dict[goal]]
            
            pos_dict[number] = i

print(twoSum([1,2,7,11,19],9))