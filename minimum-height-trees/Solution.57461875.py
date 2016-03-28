class Solution:

    def findMinHeightTrees(self, n, edges):
        degrees = [0] * n
        adjacency = {x: set() for x in xrange(n)}

        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            adjacency[edge[0]].add(edge[1])
            adjacency[edge[1]].add(edge[0])

        boundary = {node for node in xrange(n) if degrees[node] == 1}
        roots = set(xrange(n))

        while len(roots) > 2:
            for node in boundary:
                degrees[node] -= 1
                next_node = adjacency[node].pop()
                adjacency[node].clear()
                degrees[next_node] -= 1
                adjacency[next_node].remove(node)
                roots.remove(node)

            boundary = {node for node in xrange(n) if degrees[node] == 1}

        return list(roots)
