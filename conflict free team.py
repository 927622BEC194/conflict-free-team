def dfs(node, adj_list, visited, expertise):
    """DFS to find all nodes in the current connected component."""
    stack = [node]
    total_expertise = 0
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            total_expertise += expertise[curr]
            for neighbor in adj_list[curr]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return total_expertise

def solve(n, c, conflicts, expertise):
    # Step 1: Create the adjacency list
    adj_list = [[] for _ in range(n)]
    for u, v in conflicts:
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    # Step 2: Use DFS to find all connected components and calculate expertise sum for each component
    visited = [False] * n
    max_expertise = 0
    for i in range(n):
        if not visited[i]:
            # Find total expertise for the connected component starting from node i
            component_expertise = dfs(i, adj_list, visited, expertise)
            max_expertise = max(max_expertise, component_expertise)

    # Step 3: Output the result
    print(max_expertise)

# Input reading
n, c = map(int, input().split())  # n is number of employees, c is number of conflict pairs
conflicts = [tuple(map(int, input().split())) for _ in range(c)]  # c lines of conflict pairs
expertise = list(map(int, input().split()))  # Expertise levels of employees

solve(n, c, conflicts, expertise)
