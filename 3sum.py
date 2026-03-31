class solution:
                def threesum(self, nums, target):
                        nums.sort()
                        s = set()

                        for i in range(len(nums)):
                                j = i + 1
                                k = len(nums) - 1
                                while j < k:
                                        sum = nums[i] + nums[j] + nums[k]
                                        if sum == target:
                                                s.add((nums[i], nums[j], nums[k]))
                                                j += 1
                                                k -= 1
                                        elif sum < target:
                                                j += 1
                                        else:
                                                k -= 1
                        return list(s)
nums = [-4, -1, -1, 5, 1, 2]
target = 0
obj = solution()
output = obj.threesum(nums, target)
print(output)