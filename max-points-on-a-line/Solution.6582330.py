class Solution:

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def maxPoints(self, points):
        if not points:
            return 0
        if len(points) == 1:
            return 1

        pointIter = iter(points)
        firstPoint = next(pointIter)
        if all(firstPoint.x == rest.x and firstPoint.y == rest.y for rest in pointIter):
            return len(points)

        def a_b_c_for_point_pair(point1, point2):
            x1 = point1.x
            x2 = point2.x
            y1 = point1.y
            y2 = point2.y

            a = y2 - y1
            b = x1 - x2
            c = x1 * y2 - x2 * y1

            divideBy = reduce(Solution.gcd, (a, b, c))
            a /= divideBy
            b /= divideBy
            c /= divideBy

            return (a, b, c)

        dictOfLines = collections.defaultdict(int)
        for (point1, point2) in itertools.combinations(points, 2):
            if point1.x == point2.x and point1.y == point2.y:
                continue

            abc = a_b_c_for_point_pair(point1, point2)
            dictOfLines[abc] += 1

        if not dictOfLines:
            return 0

        maxABC = max(dictOfLines.iteritems(), key=operator.itemgetter(1))[0]

        def is_point_on_line(point):
            a, b, c = maxABC
            return ((a * point.x + b * point.y) == c)

        maxPointCount = 0
        for point in points:
            if is_point_on_line(point):
                maxPointCount += 1
        return maxPointCount