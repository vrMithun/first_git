# Graph representation as adjacency list
graph = {
    1: [6, 2, 3],
    2: [1],
    3: [1, 7],
    4: [6, 5],
    5: [7,4, 6],
    6: [1, 4, 5],
    7: [3, 8, 5, 10],
    8: [7, 9],
    9: [8],
    10: [7, 11, 12, 13],
    11: [10],
    12: [10, 13],
    13: [10, 12]
}

# Initialize global variables
disc = {}
low = {}
parent = {}
stack = []
time = [0]  # Time variable to keep track of the discovery time
bccs = []  # List to store all BCCs

def dfs(u):
    print(f"visiting node {u}")
    disc[u] = low[u] = time[0]
    time[0] += 1
    print(f"dics[{u}]={disc[u]}")
    print(f"low[{u}]={low[u]}")
    for v in graph[u]:
        if v not in disc:  # If v is unvisited
            parent[v] = u
            stack.append((u, v))  # Push the edge (u, v) onto the stack
            print('stack',stack)
            dfs(v)

            # Check if the subtree rooted at v has a connection back to u or its ancestors
            low[u] = min(low[u], low[v])
            print(f"low[{u}]={low[u]}")
            # If u is an articulation point, pop edges from the stack to form a BCC
            if low[v] >= disc[u]:
                bcc = []
                while stack[-1] != (u, v):
                    bcc.append(stack.pop())
                bcc.append(stack.pop())  # Pop the edge (u, v)
                print(f"bcc is {bcc},current node {u}")
                bccs.append(bcc)  # Add the BCC to the list
        elif v != parent.get(u) and disc[v] < disc[u]:  # Back edge
            low[u] = min(low[u], disc[v])
            print(f"low[{u}]={low[u]}")
            stack.append((u, v))  # Push the back edge (u, v) onto the stack
            print('stack',stack)
        
def find_bccs():
    # Initialize all nodes as unvisited
    for node in graph:
        if node not in disc:
            parent[node] = None
            dfs(node)

    # Print all BCCs
    print("Biconnected Components:")
    for bcc in bccs:
        print(bcc)

# Run the BCC finding function
find_bccs()
