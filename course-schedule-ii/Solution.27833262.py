class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        in_degree = [0] * numCourses
        graph = {x: set() for x in range(numCourses)}
        for after, before in prerequisites:
            if after in graph[before]:
                continue
            graph[before].add(after)
            in_degree[after] += 1
            
        courses = [x for x in range(numCourses) if in_degree[x] == 0]
        order = []
        
        while courses:
            course = courses.pop()
            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    courses.append(c)
                    
            order.append(course)
            
        if len(order) != numCourses:
            return []
            
        return order
