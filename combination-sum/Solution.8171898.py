class Solution:

    def find_all_solutions(self, target, candidates, start, current_solution, solution_set):
        if target == 0:
            solution_set.append(current_solution[:])
            return

        if start >= len(candidates):
            return

        if candidates[start] > target:
            return

        for i in xrange(start, len(candidates)):
            current_solution.append(candidates[i])
            self.find_all_solutions(target - candidates[i], candidates, i, current_solution, solution_set)
            current_solution.pop()

    def combinationSum(self, candidates, target):
        candidates.sort()
        solution_set = []
        self.find_all_solutions(target, candidates, 0, [], solution_set)
        return solution_set
