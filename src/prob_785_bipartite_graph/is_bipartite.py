from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sets = {True: set(), False: set()}

        visited = lambda x: x in sets[True] or x in sets[False]
        next_vertices = set()
        for vertex in range(len(graph)):
            if visited(vertex):
                continue
            next_vertices.add((vertex, False))

            while len(next_vertices):
                vertex, last_set = next_vertices.pop()
                next_set = not last_set
                if vertex in sets[last_set]:
                    return False
                sets[next_set].add(vertex)
                for next_vertex in graph[vertex]:
                    if not visited(next_vertex):
                        next_vertices.add((next_vertex, next_set))

        return True
