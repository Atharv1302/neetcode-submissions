class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        front = 0
        back = len(nums) - 1

        while front <= back:
            if nums[back] == val:
                back = back - 1
            elif nums[front] == val:
                temp = nums[front]
                nums[front] = nums[back]
                nums[back] = temp
                front = front + 1
                back = back - 1
            else:
                front = front + 1

        return front
        