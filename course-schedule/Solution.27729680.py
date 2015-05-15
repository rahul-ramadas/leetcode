class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        graph = {i: set() for i in range(numCourses)}
        for after, before in prerequisites:
            graph[before].add(after)
            
        visited = set()
        cycle = set()
        
        for course in range(numCourses):
            has_cycle = self.visit(graph, course, visited, cycle)
            if has_cycle:
                return False
                
        return True
        
    def visit(self, graph, course, visited, cycle):
        if course in cycle:
            return True
            
        if course in visited:
            return False
            
        visited.add(course)
        cycle.add(course)
        
        for after_course in graph[course]:
            has_cycle = self.visit(graph, after_course, visited, cycle)
            if has_cycle:
                return True
                
        cycle.remove(course)
        return False
