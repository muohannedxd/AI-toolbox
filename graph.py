from collections import deque
from queue import PriorityQueue
import heapq
import math
import networkx as nx


class GraphProblem:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        if node not in self.graph.nodes:
            self.graph.add_node(node)

    def add_edge(self, from_node, to_node, value):
        if (from_node, to_node) not in self.graph.edges:
            self.graph.add_edge(from_node, to_node, weight=value)

    def get_successors(self, state):
        return list(self.graph.neighbors(state))

    def get_edge_cost(self, from_node, to_node):
        return int(self.graph[from_node][to_node]['weight'])

    # breadth first search
    def breadth_first_search(self, start, goal):
        found, fringe, visited, came_from = False, deque(
            [start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))

        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')

            if current == goal:
                found = True
                break

            # Use get_successors() method to retrieve the neighbors
            for node in self.get_successors(current):
                if node not in visited:
                    visited.add(node)
                    fringe.appendleft(node)
                    came_from[node] = current
            print(', '.join(fringe))

        if found:
            print()
            # Trace the path from goal to start
            path = []
            node = goal
            while node != start:
                path.insert(0, node)
                node = came_from[node]
            path.insert(0, start)

            return path
        else:
            print('No path from {} to {}'.format(start, goal))

    # depth first search    
    def depth_first_search(self, start, goal):
        found, fringe, visited, came_from = False, [start], set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))

        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')

            if current == goal:
                found = True
                break

            # Use get_successors() method to retrieve the neighbors
            for node in self.get_successors(current):
                if node not in visited:
                    visited.add(node)
                    fringe.append(node)
                    came_from[node] = current

            print(', '.join(fringe))

        if found:
            print()
            # Trace the path from goal to start
            path = []
            node = goal
            while node != start:
                path.insert(0, node)
                node = came_from[node]
            path.insert(0, start)

            return path
        else:
            print('No path from {} to {}'.format(start, goal))
    # depth limited search
    def depth_limited_search(self, start, goal, depth_limit):
        found, fringe, visited, came_from = False, [(start, 0)], set([start]), {start: None}
        print('{:11s} | {:7s} | {}'.format('Expand Node', 'Depth', 'Fringe'))
        print('----------------------------------')
        print('{:11s} | {:7s} | {}'.format('-', '0', start))

        while not found and len(fringe):
            current, depth = fringe.pop()
            print('{:11s} | {:7d}'.format(current, depth), end=' | ')

            if current == goal:
                found = True
                break

            if depth < depth_limit:
                for node in self.get_successors(current):  # Use get_successors() method to retrieve the neighbors
                    if node not in visited:
                        visited.add(node)
                        fringe.append((node, depth + 1))
                        came_from[node] = current
                print(', '.join([n for n, _ in fringe]))

        if found:
            print()
            # Trace the path from goal to start
            path = []
            node = goal
            while node != start:
                path.insert(0, node)
                node = came_from[node]
            path.insert(0, start)

            return path
        else:
            print('No path from {} to {} within depth limit {}'.format(start, goal, depth_limit))
            
    # uniform cost search
    def uniform_cost_search(self, start, goal):
        found, heap, visited, came_from, cost_so_far = False, [(0, start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {:8s} | {}'.format('Expand Node', 'Cost', 'Fringe'))
        print('----------------------------------')
        print('{:11s} | {:8s} | {}'.format('-', '0', start))

        while not found and heap:
            current_cost, current = heapq.heappop(heap)
            print('{:11s} | {:8d}'.format(current, current_cost), end=' | ')

            if current == goal:
                found = True
                break

            for node in self.get_successors(current):
                new_cost = cost_so_far[current] + self.get_edge_cost(current, node)  # Calculate the cost of the new path
                if node not in visited or new_cost < cost_so_far[node]:
                    visited.add(node)
                    heapq.heappush(heap, (new_cost, node))
                    came_from[node] = current
                    cost_so_far[node] = new_cost
            fringe = [node[1] for node in heap]
            print(', '.join(fringe))

        if found:
            print()
            # Trace the path from goal to start
            path = []
            node = goal
            while node != start:
                path.insert(0, node)
                node = came_from[node]
            path.insert(0, start)

            return path
        else:
            print('No path from {} to {}'.format(start, goal))
    
    # bidirectional search
    def bidirectional_search(self, start, goal):
        found = False
        forward_fringe = deque([start])
        backward_fringe = deque([goal])
        forward_visited = set([start])
        backward_visited = set([goal])
        forward_came_from = {start: None}
        backward_came_from = {goal: None}

        print('{:15s} | {:15s}'.format('Forward Fringe', 'Backward Fringe'))
        print('-------------------------------------------')
        print('{:15s} | {:15s}'.format(start, goal))

        while not found and forward_fringe and backward_fringe:
            forward_current = forward_fringe.pop()
            backward_current = backward_fringe.pop()
            print('{:15s} | {:15s}'.format(forward_current, backward_current), end=' | ')

            if forward_current in backward_visited:
                found = True
                meeting_point = forward_current
                break
            elif backward_current in forward_visited:
                found = True
                meeting_point = backward_current
                break

            forward_successors = self.get_successors(forward_current)
            backward_successors = self.get_successors(backward_current)

            for forward_node in forward_successors:
                if forward_node not in forward_visited:
                    forward_visited.add(forward_node)
                    forward_fringe.appendleft(forward_node)
                    forward_came_from[forward_node] = forward_current

            for backward_node in backward_successors:
                if backward_node not in backward_visited:
                    backward_visited.add(backward_node)
                    backward_fringe.appendleft(backward_node)
                    backward_came_from[backward_node] = backward_current

            print(', '.join(forward_fringe), end=' | ')
            print(', '.join(backward_fringe))

        if found:
            print()
            # Trace the path from start to the meeting point
            forward_path = []
            forward_node = meeting_point
            while forward_node != start:
                forward_path.insert(0, forward_node)
                forward_node = forward_came_from[forward_node]
            forward_path.insert(0, start)

            # Trace the path from the goal to the meeting point
            backward_path = []
            backward_node = meeting_point
            while backward_node != goal:
                backward_path.append(backward_node)
                backward_node = backward_came_from[backward_node]
            backward_path.append(goal)

            path = forward_path + backward_path
            return path
        else:
            print('No path from {} to {}'.format(start, goal))
            
    # iterative deepening search
    def iterative_deepening_search(self, start, goal):
        found = False
        max_depth = 0
        
        while not found:
            depth_limit = max_depth + 1
            result = self.depth_limited_search(start, goal, depth_limit)
            
            if result is not None:
                return result
            
            max_depth += 1
        
        print('No path from {} to {}'.format(start, goal))

    # A* with its heuristic
    def a_star_search(self, start, goal):
        found = False
        fringe = PriorityQueue()
        visited = set()
        came_from = {start: None}
        cost_so_far = {start: 0}
        fringe.put((cost_so_far[start], start))

        print('{:11s} | {:8s} | {}'.format('Expand Node', 'Cost', 'Fringe'))
        print('----------------------------------')
        print('{:11s} | {:8s} | {}'.format('-', '0', start))

        while not found and not fringe.empty():
            current_cost, current = fringe.get()
            visited.add(current)
            print('{:11s} | {:8d}'.format(current, current_cost), end=' | ')

            if current == goal:
                found = True
                break

            for node in self.get_successors(current):  # Use get_successors() method to retrieve the neighbors
                if node in visited:
                    continue

                new_cost = cost_so_far[current] + self.get_cost(current, node)
                if node not in cost_so_far or new_cost < cost_so_far[node]:
                    came_from[node] = current
                    cost_so_far[node] = new_cost
                    priority = new_cost + heuristic(node, goal)
                    fringe.put((priority, node))

            print(', '.join([node[1] for node in fringe.queue]))

        if found:
            print()
            # Trace the path from goal to start
            path = []
            node = goal
            while node != start:
                path.insert(0, node)
                node = came_from[node]
            path.insert(0, start)

            return path
        else:
            print('No path from {} to {}'.format(start, goal))

    # A STAR
    def a_star_search(self, start, goal):
        found = False
        fringe = PriorityQueue()
        visited = set()
        came_from = {start: None}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}
        fringe.put((f_score[start], start))

        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))

        while not found and not fringe.empty():
            current = fringe.get()[1]
            visited.add(current)
            print('{:11s}'.format(current), end=' | ')

            if current == goal:
                found = True
                break

            for node in self.get_successors(current):  # Use get_successors() method to retrieve the neighbors
                if node in visited:
                    continue

                new_g_score = g_score[current] + self.get_cost(current, node)
                if node not in g_score or new_g_score < g_score[node]:
                    came_from[node] = current
                    g_score[node] = new_g_score
                    f_score[node] = g_score[node] + heuristic(node, goal)
                    fringe.put((f_score[node], node))

            print(', '.join([node[1] for node in fringe.queue]))

        if found:
            print()
            # Trace the path from goal to start
            path = []
            node = goal
            while node != start:
                path.insert(0, node)
                node = came_from[node]
            path.insert(0, start)

            return path
        else:
            print('No path from {} to {}'.format(start, goal))
            
    # HILL CLIMBING
    def hill_climbing_search(self, start, goal):
        current = start
        while True:
            print('Current Node: {}'.format(current))
            
            if current == goal:
                print('Goal reached!')
                return current
            
            successors = self.get_successors(current)
            best_successor = None
            
            for successor in successors:
                if self.get_cost(current, successor) < self.get_cost(current, best_successor):
                    best_successor = successor
            
            if not best_successor:
                print('Stuck at local maximum. No further progress possible.')
                return None
            
            current = best_successor



def heuristic(self, node, goal):
    # Assume nodes are coordinates (x, y)
    return 1