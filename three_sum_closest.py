class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Pehle hum list ko sort kar dete hain
        closest_sum = float("inf")  # Initially, closest sum ko infinity set karte hain

        for i in range(len(nums)-2):  # Har element ke liye loop chalaate hain
            l, r = i+1, len(nums)-1  # Do pointers set karte hain: left (l) aur right (r)
            while l < r:  # Jab tak left pointer right se chhota hai
                total = nums[i] + nums[l] + nums[r]  # Teen numbers ka sum nikalte hain
                
                if  total == target:  # Agar sum target ke barabar hai
                    return total  # Toh wahi sum return kar dete hain

                # Agar current sum target se kitna door hai, yeh check karte hain
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total  # Agar current sum closer hai, toh usko update kar dete hain
                
                if total < target:  # Agar sum target se chhota hai
                    l += 1  # Left pointer ko aage badha dete hain
                else:  # Agar sum target se bada hai
                    r -= 1  # Right pointer ko peeche le aate hain
        return closest_sum  # Finally, closest sum return karte hain