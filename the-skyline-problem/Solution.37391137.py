INT_MAX = 2 ** 31 - 1


class Solution(object):

    class Building:

        def __init__(self, height, start, end):
            self.height = height
            self.start = start
            self.end = end

        def __lt__(self, other):
            return (self.height, self.end) > (other.height, other.end)

    def getSkyline(self, bldgs):
        buildings = [Solution.Building(h, s, e) for (s, e, h) in bldgs]
        open_buildings = []
        skyline = []
        cur_b = 0
        n = len(buildings)

        while cur_b < n or open_buildings:

            if open_buildings and (cur_b >= n or open_buildings[0].end < buildings[cur_b].start):
                change_point = open_buildings[0].end
                highest_b = heapq.heappop(open_buildings)
                while open_buildings and open_buildings[0].end <= highest_b.end:
                    heapq.heappop(open_buildings)
            else:
                change_point = buildings[cur_b].start
                while cur_b < n and buildings[cur_b].start == change_point:
                    next_b = buildings[cur_b]
                    heapq.heappush(open_buildings, next_b)
                    cur_b += 1

            cur_height = len(open_buildings) and open_buildings[0].height
            if not skyline or skyline[-1][1] != cur_height:
                skyline.append([change_point, cur_height])

        return skyline
