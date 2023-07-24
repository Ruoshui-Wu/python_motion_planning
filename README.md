
# Introduction

`Motion planning` plans the state sequence of the robot without conflict between the start and goal. 

`Motion planning` mainly includes `Path planning` and `Trajectory planning`.

* `Path Planning`: It's based on path constraints (such as obstacles), planning the optimal path sequence for the robot to travel without conflict between the start and goal.
* `Trajectory planning`: It plans the motion state to approach the global path based on kinematics, dynamics constraints and path sequence.

This repository provides the implement of common `Motion planning` algorithm, welcome your star & fork & PR.

The theory analysis can be found at [motion-planning](https://blog.csdn.net/frigidwinter/category_11410243.html)

We also provide ROS C++ version at [https://github.com/ai-winter/ros_motion_planning](https://github.com/ai-winter/ros_motion_planning) and Matlab Version at [https://github.com/ai-winter/matlab_motion_planning](https://github.com/ai-winter/matlab_motion_planning)

# Quick Start
The file structure is shown below

```
├─gif
├─example
└─global_planner
│   ├─graph_search
│   ├─sample_search
│   └─evolutionary_search
├─local_planner
├─utils
└─main.py
```
The global planning algorithm implementation is in the folder `global_planner` with `graph_search`, `sample_search` and `evolutionary search`; The local planning algorithm implementation is in the folder `local_planner`.

To start simulation, open the folder `example` and select the algorithm, for example

```python
if __name__ == '__main__':
    '''
    path searcher constructor
    '''
    search_factory = SearchFactory()
    
    '''
    graph search
    '''
    # build environment
    start = (5, 5)
    goal = (45, 25)
    env = Grid(51, 31)

    # creat planner
    planner = search_factory("a_star", start=start, goal=goal, env=env)
    # animation
    planner.run()
```

# Version
## Global Planner

Planner      |   Version   | Animation
------------ | --------- | --------- 
**GBFS**              | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/gbfs.py)   | ![gbfs_python.png](gif/gbfs_python.png) 
**Dijkstra**                 | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/dijkstra.py) | ![dijkstra_python.png](gif/dijkstra_python.png)
**A***               | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/a_star.py) |  ![a_star_python.png](gif/a_star_python.png) 
**JPS**                 | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/jps.py) | ![jps_python.png](gif/jps_python.png)
**D***                  | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/d_star.py) | ![d_star_python.png](gif/d_star_python.png)
**LPA***                 | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/lpa_star.py) | ![lpa_star_python.png](gif/lpa_star_python.png) 
**D\* Lite**                | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/d_star_lite.py) | ![d_star_lite_python.png](gif/d_star_lite_python.png)
**Voronoi**                | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/graph_search/voronoi.py) | ![voronoi_python.png](gif/voronoi_python.png) 
**RRT**                 | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/sample_search/rrt.py) | ![rrt_python.png](gif/rrt_python.png)
**RRT***                 | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/sample_search/rrt_star.py) | ![rrt_star_python.png](gif/rrt_star_python.png)
**Informed RRT**                 | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/sample_search/informed_rrt.py) | ![informed_rrt_python.png](gif/informed_rrt_python.png)
**RRT-Connect**                | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/sample_search/rrt_connect.py) | ![rrt_connect_python.png](gif/rrt_connect_python.png)

## Local Planner
| Planner |  Version   | Animation                                     
| ------- | ---------------------------------------- | -------------------------------------------------- 
| **PID** | ![Status](https://img.shields.io/badge/develop-v1.0-red) |![Status](https://img.shields.io/badge/gif-none-yellow) 
| **APF** | ![Status](https://img.shields.io/badge/develop-v1.0-red) |![Status](https://img.shields.io/badge/gif-none-yellow) 
| **DWA** |  ![Status](https://img.shields.io/badge/develop-v1.0-red) | ![Status](https://img.shields.io/badge/gif-none-yellow) 
| **TEB** | ![Status](https://img.shields.io/badge/develop-v1.0-red) | ![Status](https://img.shields.io/badge/gif-none-yellow) 
| **MPC** | ![Status](https://img.shields.io/badge/develop-v1.0-red) | ![Status](https://img.shields.io/badge/gif-none-yellow) 
| **Lattice** | ![Status](https://img.shields.io/badge/develop-v1.0-red) |![Status](https://img.shields.io/badge/gif-none-yellow) 

## Intelligent Algorithm

| Planner | Version   | Animation                                |
| ------- | -------------------------------------------------------- | -------------------------------------------------------- 
| **ACO** | [![Status](https://img.shields.io/badge/done-v1.0-brightgreen)](https://github.com/ai-winter/python_motion_planning/blob/master/global_planner/evolutionary_search/aco.py) | ![aco_python.png](gif/aco_python.png)
| **GA**  | ![Status](https://img.shields.io/badge/develop-v1.0-red) | ![Status](https://img.shields.io/badge/gif-none-yellow) 
| **PSO**  | ![Status](https://img.shields.io/badge/develop-v1.0-red) | ![Status](https://img.shields.io/badge/gif-none-yellow) 
| **ABC** | ![Status](https://img.shields.io/badge/develop-v1.0-red) | ![Status](https://img.shields.io/badge/gif-none-yellow) 





# Papers
## Search-based Planning
* [A*: ](https://ieeexplore.ieee.org/document/4082128) A Formal Basis for the heuristic Determination of Minimum Cost Paths
* [JPS:](https://ojs.aaai.org/index.php/AAAI/article/view/7994) Online Graph Pruning for Pathfinding On Grid Maps
* [Lifelong Planning A*: ](https://www.cs.cmu.edu/~maxim/files/aij04.pdf) Lifelong Planning A*
* [D*: ](http://web.mit.edu/16.412j/www/html/papers/original_dstar_icra94.pdf) Optimal and Efficient Path Planning for Partially-Known Environments
* [D* Lite: ](http://idm-lab.org/bib/abstracts/papers/aaai02b.pdf) D* Lite

## Sample-based Planning
* [RRT: ](http://msl.cs.uiuc.edu/~lavalle/papers/Lav98c.pdf) Rapidly-Exploring Random Trees: A New Tool for Path Planning
* [RRT-Connect: ](http://www-cgi.cs.cmu.edu/afs/cs/academic/class/15494-s12/readings/kuffner_icra2000.pdf) RRT-Connect: An Efficient Approach to Single-Query Path Planning
* [RRT*: ](https://journals.sagepub.com/doi/abs/10.1177/0278364911406761) Sampling-based algorithms for optimal motion planning
* [Informed RRT*: ](https://arxiv.org/abs/1404.2334) Optimal Sampling-based Path Planning Focused via Direct Sampling of an Admissible Ellipsoidal heuristic

## Evolutionary-based Planning
* [ACO: ](http://www.cs.yale.edu/homes/lans/readings/routing/dorigo-ants-1999.pdf) Ant Colony Optimization: A New Meta-Heuristic

## Local Planning

* [DWA: ](https://www.ri.cmu.edu/pub_files/pub1/fox_dieter_1997_1/fox_dieter_1997_1.pdf) The Dynamic Window Approach to Collision Avoidance




# Acknowledgment
* Our visualization and animation framework of Python Version refers to [https://github.com/zhm-real/PathPlanning](https://github.com/zhm-real/PathPlanning). Thanks sincerely.