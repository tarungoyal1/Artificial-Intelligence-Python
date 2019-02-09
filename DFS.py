def main():
    title("Depth First Search")
    print("!--Populate the adjency list--! e.g-> 1 4")

    edges = getEdges()
    for v, adjv in edges.items():
        print(v, ": ", adjv)

    visited = []
    stack = []

    source = input("Enter the source vertex:")

    stack.append(int(source))
    visited.append(int(source))

    top = 0
    while len(stack)>0:
        if set(edges[stack[top]]).issubset(set(visited)) or len(edges[stack[top]])<=0:
            del stack[top]
            top -= 1
            continue

        for v in edges[stack[top]]:
            if v not in visited:
                stack.insert(top+1, v)
                top+=1
                break
        if stack[top] not in visited:
            visited.append(stack[top])

    print(visited)

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

if __name__ == "__main__":
    main()