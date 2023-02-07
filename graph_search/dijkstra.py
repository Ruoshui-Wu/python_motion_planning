'''
@file: dijkstra.py
@breif: Dijkstra motion planning
@author: Winter
@update: 2023.1.13
'''
import os, sys
import heapq

sys.path.append(os.path.abspath(os.path.join(__file__, "../../")))

from .a_star import AStar
from utils import Env

class Dijkstra(AStar):
    def __init__(self, start: tuple, goal: tuple, env: Env, heuristic_type: str = "euclidean") -> None:
        super().__init__(start, goal, env, heuristic_type)
    
    def __str__(self) -> str:
        return "Dijkstra"

    def plan(self):
        '''
        Class for Dijkstra motion planning.

        Parameters
        ----------
        start: tuple
            start point coordinate
        goal: tuple
            goal point coordinate
        env: Env
            environment
        heuristic_type: str
            heuristic function type, default is euclidean

        Examples
        ----------
        >>> from utils import Grid
        >>> from graph_search import Dijkstra
        >>> start = (5, 5)
        >>> goal = (45, 25)
        >>> env = Grid(51, 31)
        >>> planner = Dijkstra(start, goal, env)
        >>> planner.run()
        '''
        # OPEN set with priority and CLOSED set
        OPEN = []
        heapq.heappush(OPEN, self.start)
        CLOSED = []

        while OPEN:
            node = heapq.heappop(OPEN)

            # exists in CLOSED set
            if node in CLOSED:
                continue

            # goal found
            if node == self.goal:
                CLOSED.append(node)
                return self.extractPath(CLOSED), CLOSED

            for node_n in self.getNeighbor(node):
             
                # hit the obstacle
                if node_n.current in self.obstacles:
                    continue
                
                # exists in CLOSED set
                if node_n in CLOSED:
                    continue
                
                node_n.parent = node.current
                node_n.h = 0

                # goal found
                if node_n == self.goal:
                    heapq.heappush(OPEN, node_n)
                    break
                
                # update OPEN set
                heapq.heappush(OPEN, node_n)
            
            CLOSED.append(node)
        return [], []