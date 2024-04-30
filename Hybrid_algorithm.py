def hybrid_color(graph):
    # Initialize an empty color assignment dictionary for each vertex
    color_assignment = {vertex: None for vertex in graph}
    
    # Sort vertices in descending order of their degrees
    sorted_vertices = sorted(graph, key=lambda vertex: len(graph[vertex]), reverse=True)
    
    # Initialize a counter for colors
    color_counter = 0
    
    # Loop through each vertex in the sorted order
    for vertex in sorted_vertices:
        # Initialize a set of available colors for the current vertex
        available_colors = set(range(color_counter + 1))
        
        # Check neighbors of the current vertex
        for neighbor in graph[vertex]:
            # If the neighbor has been assigned a color, remove it from available colors
            if color_assignment[neighbor] is not None:
                available_colors.discard(color_assignment[neighbor])
        
        # If no available colors, increment the color counter and assign a new color
        if not available_colors:
            color_counter += 1
            color_assignment[vertex] = color_counter
        else:
            # Assign the smallest available color to the vertex
            color_assignment[vertex] = min(available_colors)
    
    # Backtracking refinement
    for vertex in sorted_vertices:
        for neighbor in graph[vertex]:
            if color_assignment[neighbor] == color_assignment[vertex]:
                neighbor_neighbors = graph[neighbor]
                available_colors = set(range(color_counter + 1))
                
                # Check neighbors of the neighbor to determine available colors
                for n_neighbor in neighbor_neighbors:
                    if color_assignment[n_neighbor] is not None:
                        available_colors.discard(color_assignment[n_neighbor])
                
                # If available colors exist, swap colors to reduce conflicts
                if available_colors:
                    new_color = min(available_colors)
                    color_assignment[vertex], color_assignment[neighbor] = new_color, color_assignment[vertex]
                    break
    
    return color_assignment

# Example graph represented as an adjacency list
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Call the hybrid_color function with the example graph
coloring_result = hybrid_color(example_graph)

# Print the vertex coloring results
print("Vertex Coloring:")
for vertex, color in coloring_result.items():
    print(f"Vertex {vertex} colored with color {color}")
