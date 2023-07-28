import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import GraphProblem


class GraphGUI:
    def __init__(self, master):
        self.master = master
        master.title("Graph")
        master.configure(bg="#D6CACA")
        self.graph_problem = GraphProblem()

        # Add a frame for the title
        title_frame = tk.Frame(master, bg="#D6CACA")
        title_frame.grid(row=0, column=0, columnspan=3)

        # Create a label for the title
        self.title_label = tk.Label(title_frame, text="Graph Solver", font=(
            "Belleza Regular", 24, "bold"), bg="#D6CACA")
        self.title_label.pack(pady=10)

        self.figure = plt.figure(figsize=(7, 5))
        self.subplot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=master)

        # Left section (25% width)
        left_frame = tk.Frame(master, bg="#D6CACA")
        left_frame.grid(row=1, column=0, rowspan=13, sticky="nsew")
        left_frame.grid_columnconfigure(0, weight=1)

        self.graphgen_label = tk.Label(
            left_frame, text="Generate a Graph:", font=("Arial", 18), bg="#D6CACA")
        self.graphgen_label.grid(row=0, column=0, sticky="ew", padx=10, pady=4)

        self.addnode_label = tk.Label(
            left_frame, text="Add a Node:", font=("Arial", 14), bg="#D6CACA")
        self.addnode_label.grid(row=1, column=0, sticky="w", padx=10, pady=2)

        self.addnode_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.addnode_entry.grid(row=1, column=2, sticky="w", padx=10, pady=2)

        self.add_node_button = tk.Button(
            left_frame, text="Add Node", font=("Arial", 12), bg="#474747", fg="white", command=self.add_node)
        self.add_node_button.grid(row=2, column=0, columnspan=3,
                                  sticky="ew", padx=10, pady=2)

        self.addedge_label = tk.Label(
            left_frame, text="Add an Edge between:", font=("Arial", 14), bg="#D6CACA")
        self.addedge_label.grid(
            row=3, column=0, sticky="ew", padx=10, pady=(10, 2))

        self.from_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.from_entry.grid(row=4, column=0, sticky="w", padx=10, pady=2)

        self.from_label = tk.Label(
            left_frame, text="And", font=("Arial"), bg="#D6CACA")
        self.from_label.grid(row=4, column=1, sticky="w", padx=10, pady=2)

        self.to_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.to_entry.grid(row=4, column=2, sticky="w", padx=10, pady=2)

        self.value_label = tk.Label(
            left_frame, text="Path Cost:", font=("Arial", 14), bg="#D6CACA")
        self.value_label.grid(row=5, column=0, sticky="w", padx=10, pady=2)

        self.value_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.value_entry.grid(row=5, column=2, sticky="w", padx=10, pady=2)

        self.add_edge_button = tk.Button(
            left_frame, text="Add Edge", font=("Arial", 12), bg="#474747", fg="white", command=self.add_edge)
        self.add_edge_button.grid(row=6, column=0, columnspan=3,
                                  sticky="ew", padx=10, pady=2)

        self.search_label = tk.Label(
            left_frame, text="Searching:", font=("Arial", 18), bg="#D6CACA")
        self.search_label.grid(
            row=7, column=0, sticky="w", padx=10, pady=(20, 4))

        self.start_label = tk.Label(
            left_frame, text="Initial State:", font=("Arial", 14), bg="#D6CACA")
        self.start_label.grid(row=8, column=0, sticky="w", padx=10, pady=2)

        self.start_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.start_entry.grid(row=8, column=2, sticky="w", padx=10, pady=2)

        self.goal_label = tk.Label(
            left_frame, text="Goal State:", font=("Arial", 14), bg="#D6CACA")
        self.goal_label.grid(row=9, column=0, sticky="w", padx=10, pady=2)

        self.goal_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.goal_entry.grid(row=9, column=2, sticky="w", padx=10, pady=2)

        self.goal_label = tk.Label(
            left_frame, text="Choose an algorithm:", font=("Arial", 14), bg="#D6CACA")
        self.goal_label.grid(row=10, column=0, sticky="w",
                             padx=10, pady=(10, 2))

        self.apply_button = tk.Button(
            left_frame, text="Breadth First Search", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_bfs)
        self.apply_button.grid(row=11, column=0, columnspan=1,
                               sticky="ew", padx=10, pady=2)

        self.apply_button = tk.Button(
            left_frame, text="Iterative Deepening", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_ids)
        self.apply_button.grid(row=11, column=2, columnspan=1,
                               sticky="ew", padx=10, pady=2)

        self.apply_button = tk.Button(
            left_frame, text="Depth First Search", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_dfs)
        self.apply_button.grid(row=12, column=0, columnspan=1,
                               sticky="ew", padx=10, pady=2)
        
        self.apply_button = tk.Button(
            left_frame, text="A* search", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_astar)
        self.apply_button.grid(row=12, column=2, columnspan=1,
                               sticky="ew", padx=10, pady=2)

        self.apply_button = tk.Button(
            left_frame, text="Depth Limited Search", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_dls)
        self.apply_button.grid(row=13, column=0, columnspan=1,
                               sticky="ew", padx=10, pady=2)
        
        self.apply_button = tk.Button(
            left_frame, text="Hill Climbing", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_hillclimbing)
        self.apply_button.grid(row=14, column=2, columnspan=1,
                               sticky="ew", padx=10, pady=2)
        
        self.limit_entry = tk.Entry(left_frame, font=("Arial", 14), width=10)
        self.limit_entry.grid(row=13, column=2, sticky="w", padx=10, pady=2)

        self.apply_button = tk.Button(
            left_frame, text="Uniform Cost Search", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_ucs)
        self.apply_button.grid(row=14, column=0, columnspan=1,
                               sticky="ew", padx=10, pady=2)

        self.apply_button = tk.Button(
            left_frame, text="Bidirectional Search", font=("Arial", 12), bg="#474747", fg="white", command=self.apply_search_bidirectional)
        self.apply_button.grid(row=15, column=0, columnspan=1,
                               sticky="ew", padx=10, pady=2)

        self.result_label = tk.Label(
            left_frame, text="Result Path:", font=("Arial", 14), bg="#D6CACA")
        self.result_label.grid(row=16, column=0, sticky="w", padx=10, pady=2)

        self.path_label = tk.Label(
            left_frame, text="", font=("Arial", 14), bg="#D6CACA")
        self.path_label.grid(row=17, column=0, sticky="ew", padx=10, pady=2)

        # Right section (75% width)
        self.canvas.get_tk_widget().grid(row=1, column=1, rowspan=20, sticky="nsew")

    # generating the graph:
    def add_node(self):
        node = self.addnode_entry.get()
        if node:
            self.graph_problem.add_node(node)
            self.update_display()

    def add_edge(self):
        from_node = self.from_entry.get()
        to_node = self.to_entry.get()
        value = self.value_entry.get()
        if from_node and to_node and value:
            self.graph_problem.add_edge(from_node, to_node, value)
            self.update_display()

    def update_display(self):
        self.subplot.clear()
        pos = nx.spring_layout(self.graph_problem.graph)
        nx.draw(self.graph_problem.graph, pos,
                ax=self.subplot, with_labels=True)
        labels = nx.get_edge_attributes(self.graph_problem.graph, 'weight')
        nx.draw_networkx_edge_labels(
            self.graph_problem.graph, pos, edge_labels=labels, ax=self.subplot)
        self.canvas.draw()

    # applying the search algorithms
    def apply_search_bfs(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()
        if initial_state and goal_state:
            path = self.graph_problem.breadth_first_search(
                initial_state, goal_state)
            if path:
                result_path = " -> ".join(path)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")

    def apply_search_dfs(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()
        # Set a large depth limit for DFS (effectively unlimited)
        depth_limit = 100

        if initial_state and goal_state:
            path = self.graph_problem.depth_first_search(
                initial_state, goal_state)
            if path:
                result_path = " -> ".join(path)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")
            
    def apply_search_dls(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()
        depth_limit = int(self.limit_entry.get())  # Get the depth limit from the limit_entry widget

        if initial_state and goal_state:
            path = self.graph_problem.depth_limited_search(initial_state, goal_state, depth_limit)
            if path:
                result_path = " -> ".join(path)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")
            
    def apply_search_ucs(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()

        if initial_state and goal_state:
            path = self.graph_problem.uniform_cost_search(initial_state, goal_state)
            if path:
                result_path = " -> ".join(path)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")

    def apply_search_bidirectional(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()
        if initial_state and goal_state:
            path = self.graph_problem.bidirectional_search(initial_state, goal_state)
            if path:
                result_path = " -> ".join(path)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")
            
    def apply_search_ids(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()
        if initial_state and goal_state:
            result = self.graph_problem.iterative_deepening_search(initial_state, goal_state)
            if result:
                result_path = " -> ".join(result)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")

    def apply_search_astar(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()

        if initial_state and goal_state:
            result = self.graph_problem.a_star_search(initial_state, goal_state)

            if result:
                result_path = " -> ".join(result)
                self.path_label.config(text=result_path)
            else:
                self.path_label.config(text="No path found")
        else:
            self.path_label.config(text="Enter start and goal states")

    def apply_search_hillclimbing(self):
        initial_state = self.start_entry.get()
        goal_state = self.goal_entry.get()
        
        if initial_state and goal_state:
            result = self.graph_problem.hill_climbing_search(initial_state, goal_state)
            
            if result:
                self.path_label.config(text="Goal reached!")
            else:
                self.path_label.config(text="Stuck at local maximum. No further progress possible.")
        else:
            self.path_label.config(text="Enter start and goal states")