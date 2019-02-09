def main():
    title("Breadth First Search")
    print("!--Populate the adjency list--! e.g-> 1 4")

    edges = getEdges()
    for v, adjv in edges.items():
        print(v,": ", adjv)

    visited = []
    queue = []

    source = input("Enter the source vertex:")

    queue.append(int(source))

    while len(queue)>0:

        print("Visited = ", queue[0])

        for n in edges[queue[0]]:
            if n not in visited:
                queue.append(n)
        print("Queue = ", queue)
        if queue[0] not in visited:
            visited.append(queue[0])

        del queue[0]

    print("Queue = ", queue)
    print("BFS traversal = ", visited)

def getEdges():
    edges = {}
    c=0
    while 1:
        edge = str(input("Enter adjacent vertices of v"+str(c)+":")).split()
        if len(edge)>0:
            e = [int(v) for v in sorted(list(set(edge))) if int(v)!=c]
            edges[c] = e
        else:
            break
        c+=1
    return edges

def title(message, border = "*"):
    print(border*len(message))
    print(message)
    print(border*len(message))
    print("\n")

if __name__ == "__main__":
    main()