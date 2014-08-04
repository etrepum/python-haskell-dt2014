"""Breadth-first traversal"""
from typing import List, Dict, Set, Iterator
from collections import deque

def breadth_first(starting_node: int,
                  edges: Dict[int, List[int]]) -> Iterator[int]:
    """Yield all nodes reachable from starting_node"""
    visited = Set[int]()
    queue = deque([starting_node])
    while queue:
        node = queue.pop(0)
        if node not in visited:
            yield node
            visited.append(node)
            queue.extend(edges[node])

GRAPH = {
    1: [1, 2, 3],
    2: [5],
    3: [4],
    4: [2],
    5: List[int]()
}

if __name__ == '__main__':
    print(list(breadth_first(1, GRAPH)))
