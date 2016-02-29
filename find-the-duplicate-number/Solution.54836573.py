class Solution(object):
    """Solution based on linked-list cycle detection."""

    def findDuplicate(self, nums):
        n = len(nums) - 1

        # Get inside the cycle.
        pos = n
        for i in xrange(n):
            pos = nums[pos] - 1

        # Find the length of the cycle.
        pole_pos = pos
        cycle_length = 0
        while True:
            cycle_length += 1
            pos = nums[pos] - 1
            if pole_pos == pos:
                break

        # Initialize the back and front pointers, separated by the cycle length.
        back = n
        front = n
        for _ in xrange(cycle_length):
            front = nums[front] - 1

        # Move the pointers together, until they meet at the beginning of the cycle.
        while front != back:
            front = nums[front] - 1
            back = nums[back] - 1

        # Position of the beginning of the cycle is a duplicate number.
        return front + 1
