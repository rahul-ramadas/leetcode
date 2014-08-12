class Solution:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        deficit = 0
        tank = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:
                start = i + 1
                deficit -= tank
                tank = 0

        return start if tank >= deficit else -1
