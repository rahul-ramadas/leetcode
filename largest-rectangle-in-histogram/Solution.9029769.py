class Solution:

    def largestRectangleArea(self, height):
        if not height:
            return 0

        stack = []
        max_area = 0

        for i, h in enumerate(height):
            if not stack or height[stack[-1]] <= h:
                stack.append(i)
                continue

            while stack and height[stack[-1]] > h:
                ind = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i
                trial = height[ind] * (right - left)
                max_area = max(max_area, trial)

            stack.append(i)

        right = len(height)
        while stack:
            ind = stack.pop()
            left = stack[-1] + 1 if stack else 0
            trial = height[ind] * (right - left)
            max_area = max(max_area, trial)

        return max_area
