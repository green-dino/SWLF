import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go   

# Create a list of relationships
relationships = [
    ('A', 'Change Control Record', 'has', 'B', 'Change request number'),
    ('A', 'Change Control Record', 'has', 'C', 'Change request date'),
    ('A', 'Change Control Record', 'has', 'D', 'Requested by - name and position'),
    ('A', 'Change Control Record', 'has', 'E', 'Description of the change'),
    ('A', 'Change Control Record', 'has', 'F', 'Justification for the change'),
    ('A', 'Change Control Record', 'has', 'G', 'Impact assessment - including potential risks and mitigation measures'),
    ('A', 'Change Control Record', 'has', 'H', 'Change priority - e.g., low, medium, high'),
    ('A', 'Change Control Record', 'has', 'I', 'Change category - e.g., hardware, software, procedural'),
    ('A', 'Change Control Record', 'has', 'J', 'Change implementation date/time'),
    ('A', 'Change Control Record', 'has', 'K', 'Change approver and approval date'),
    ('L', 'Document Control Information', 'has', 'M', 'Document title'),
    ('L', 'Document Control Information', 'has', 'N', 'Document number'),
    ('L', 'Document Control Information', 'has', 'O', 'Revision history'),
    ('L', 'Document Control Information', 'has', 'P', 'Date of last revision'),
    ('L', 'Document Control Information', 'has', 'Q', 'Document owner'),
    ('L', 'Document Control Information', 'has', 'R', 'Distribution list'),
    ('A', 'Change Control Record', 'has', 'L', 'Document Control Information'),
    ('X', 'Change Implementation Plan', 'has', 'Y', 'Scope of the change'),
    ('X', 'Change Implementation Plan', 'has', 'Z', 'Steps involved in implementing the change'),
    ('X', 'Change Implementation Plan', 'has', 'A1', 'Resources required for the change'),
    ('X', 'Change Implementation Plan', 'has', 'B1', 'Timeline for each step'),
    ('X', 'Change Implementation Plan', 'has', 'C1', 'Testing and validation procedures'),
    ('X', 'Change Implementation Plan', 'has', 'D1', 'Rollback plan'),
    ('A', 'Change Control Record', 'has', 'X', 'Change Implementation Plan'),
    ('E1', 'Communication and Notification', 'has', 'F1', 'Stakeholders affected by the change'),
    ('E1', 'Communication and Notification', 'has', 'G1', 'Communication plan'),
    ('E1', 'Communication and Notification', 'has', 'H1', 'Notification process for impacted parties'),
    ('E1', 'Communication and Notification', 'has', 'I1', 'Training requirements for personnel involved in the change'),
    ('A', 'Change Control Record', 'has', 'E1', 'Communication and Notification'),
    ('A2', 'Risk Assessment and Control', 'has', 'B2', 'Risk assessment of the change'),
    ('A2', 'Risk Assessment and Control', 'has', 'C2', 'Identification of potential risks and vulnerabilities'),
    ('A2', 'Risk Assessment and Control', 'has', 'D2', 'Risk mitigation measures'),
    ('A2', 'Risk Assessment and Control', 'has', 'E2', 'Contingency plans for unforeseen issues or failures'),
    ('A2', 'Risk Assessment and Control', 'has', 'F2', 'Monitoring and reporting mechanisms during the change implementation'),
    ('A', 'Change Control Record', 'has', 'A2', 'Risk Assessment and Control'),
    ('A3', 'Document references', 'has', 'B3', 'Documented evidence and artifacts'),
    ('A3', 'Document references', 'has', 'C3', 'Record keeping requirements'),
    ('A3', 'Document references', 'has', 'D3', 'Retention period'),
    ('A', 'Change Control Record', 'has', 'A3', 'Document references'),
    ('A', 'Change Control Record', 'has', 'B', 'Change request number'),
    ('A', 'Change Control Record', 'has', 'C', 'Change request date'),
    ('A', 'Change Control Record', 'has', 'D', 'Requested by - name and position')
]

# Create a pandas DataFrame
pb_relations_df = pd.DataFrame(relationships, columns=['From Node', 'From Entity', 'Relationship', 'To Node', 'To Entity'])

while True:
    # Print menu for user options
    print("\nOptions:")
    print("1. View all relationships")
    print("2. View relationships related to a specific entity")
    print("3. Exit")

    # Get user's choice
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # Option 1: View all relationships
        print(pb_relations_df)

    elif choice == '2':
        # Option 2: View relationships related to a specific entity
        entity_name = input("Enter the name of the entity you want to view relationships for: ")
        entity_filter = (pb_relations_df['From Entity'] == entity_name) | (pb_relations_df['To Entity'] == entity_name)
        filtered_df = pb_relations_df[entity_filter]
        if not filtered_df.empty:
            print(f"Relationships related to {entity_name}:")
            print(filtered_df)
        else:
            print(f"No relationships found for {entity_name}.")

    elif choice == '3':
        # Option 3: Exit
        break

    else:
        print("Invalid choice. Please select a valid option.")

# Display the DataFrame
print(pb_relations_df)


rows = pb_relations_df.shape[0]
cols = pb_relations_df.shape[1]

print(f'{pb_relations_df.shape} --> {rows} rows and {cols} columns')

# Create a NetworkX graph
G = nx.Graph()

# Iterate through the DataFrame and add nodes and edges
for index, row in pb_relations_df.iterrows():
    G.add_node(row['From Node'], label=row['From Entity'])
    G.add_node(row['To Node'], label=row['To Entity'])
    G.add_edge(row['From Node'], row['To Node'], label=row['Relationship'])

# Calculate node positions using a layout algorithm (e.g., Kamada-Kawai)
pos = nx.kamada_kawai_layout(G)

# Create a Plotly figure
fig = go.Figure()

# Create nodes
for node in G.nodes:
    fig.add_trace(go.Scatter(x=[pos[node][0]], y=[pos[node][1]], mode='markers+text', marker=dict(size=20), text=[G.nodes[node]['label'], node], textposition='bottom center'))

# Create edges
edge_x = []
edge_y = []
for edge in G.edges:
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5, color='#888')))

# Update the layout
fig.update_layout(
    showlegend=False,
    hovermode='closest',
    title='Interactive Network Graph',
    title_x=0.5,
)

# Show the interactive graph
fig.show(renderer='browser')