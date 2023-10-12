class Block:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.functions = []
        self.tasks = []

    def add_function(self, func):
        self.functions.append(func)

    def add_task(self, task):
        self.tasks.append(task)

class ProcessNode:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, node):
        self.connections.append(node)

    def __str__(self):
        return self.name

class ProcessFlow:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node.name not in self.nodes:
            self.nodes[node.name] = node

    def add_connection(self, from_node_name, to_node_name):
        from_node = self.nodes.get(from_node_name)
        to_node = self.nodes.get(to_node_name)
        if from_node and to_node:
            from_node.add_connection(to_node)

    def __str__(self):
        result = ""
        for node_name, node in self.nodes.items():
            result += f"{node} --> " + ', '.join(node.connections) + '\n'
        return result

# Create the nodes
b1 = ProcessNode("B1(Problem Identification and Change Initiation)")
b2 = ProcessNode("B2(Change Control Record Creation)")
b3 = ProcessNode("B3(Communication and Risk Assessment)")
b4 = ProcessNode("B4(Documentation and Evaluation)")
b5 = ProcessNode("B5(Fulfillment and Closure)")

# Create the process flow and add nodes
process_flow = ProcessFlow()
nodes_data = [("B1", "B2"), ("B2", "B3"), ("B3", "B4"), ("B4", "B5")]

for node_data in nodes_data:
    node_name, connections = node_data
    node = ProcessNode(f"{node_name}({BlockNames[node_name]})")
    process_flow.add_node(node)

    if connections:
        connection_list = connections.split(", ")
        for connection in connection_list:
            process_flow.add_connection(node_name, connection)

# Print the process flow
print(process_flow)