import networkx as nx
import matplotlib.pyplot as plt




class Function:
    def __init__(self, name, code, parameters=None, description=""):
        self.name = name
        self.code = code
        self.parameters = parameters or []
        self.description = description


# Create a directed graph
G = nx.DiGraph()

# Define classes for the nodes
class Node:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name}\n({self.category})"

# Create instances of nodes
B1 = Node("B1", "Problem Identification and Change Initiation")
B2 = Node("B2", "Change Control Record Creation")
B3 = Node("B3", "Communication and Risk Assessment")
B4 = Node("B4", "Documentation and Evaluation")
B5 = Node("B5", "Fulfillment and Closure")

F1 = Node("F1", "Identify and Document")
F2 = Node("F2", "Assess signifigant impact")
F3 = Node("F3", "Validate and Prioritize")
F4 = Node("F4", "Create Change Control Record")
F5 = Node("F5", "Define document Control Information")
F6 = Node("F6", "Develop Change Implementation Plan")
F7 = Node("F7", "Identify Stakeholders and Develop Strategy")
F8 = Node("F8", "Conduct Risk Assessment")
F9 = Node("F9", "Develop Risk Mitigation Strategies")
F10 = Node("F10", "Reference Relevant Documents")
F11 = Node("F11", "Conduct Evaluation Activities")
F12 = Node("F12", "Initiate Fulfillment Process")
F13 = Node("F13", "Assign roles and tasks")
F14 = Node("F14", "Monitor and manage Trouble Tickets")

# Define node data
nodes_data = [
    ("B1", "Problem Identification and Change Initiation"),
    ("B2", "Change Control Record Creation"),
    ("B3", "Communication and Risk Assessment"),
    ("B4", "Documentation and Evaluation"),
    ("B5", "Fulfillment and Closure"),
    ("F1", "Identify and Document"),
    ("F2", "Assess significant impact"),
    ("F3", "Validate and Prioritize"),
    ("F4", "Create Change Control Record"),
    ("F5", "Define Document Control Information"),
    ("F6", "Develop Change Implementation Plan"),
    ("F7", "Identify Stakeholders and Develop Strategy"),
    ("F8", "Conduct Risk Assessment"),
    ("F9", "Develop Risk Mitigation Strategies"),
    ("F10", "Reference Relevant Documents"),
    ("F11", "Conduct Evaluation Activities"),
    ("F12", "Initiate Fulfillment Process"),
    ("F13", "Assign Roles and Tasks"),
    ("F14", "Monitor and Manage Trouble Tickets"),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for node_name, category in nodes_data:
    node = Node(node_name, category)
    G.add_node(node)

# Define edges
edges_data = [
    ("B1", "F1"),
    ("B1", "F2"),
    ("B1", "F3"),
    ("B2", "F4"),
    ("B2", "F5"),
    ("B2", "F6"),
    ("B3", "F7"),
    ("B3", "F8"),
    ("B3", "F9"),
    ("B4", "F10"),
    ("B4", "F11"),
    ("B5", "F12"),
    ("B5", "F13"),
    ("B5", "F14"),
]

# Add edges to the graph
G.add_edges_from(edges_data)

# Create a layout for the graph
pos = nx.spring_layout(G)

# Draw the nodes
node_labels = {node: str(node) for node in G.nodes()}
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_color='black')

# Draw the edges
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

# Set the category as the node label for better visualization
category_labels = {node: node.category for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=category_labels, font_size=8, font_color='black')

# Customize the plot
plt.title("Directed Graph of Functions and Categories")
plt.axis('off')

# Display the graph
plt.show()