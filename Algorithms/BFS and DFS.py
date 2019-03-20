visited = set()


def BFS(graph, start, end):
    queue = []
    queue.append([start])
    # 被访问结点的集合
    visited.add(start)

    while queue:
        node = queue.pop()
        # 标记被访问
        visited.add(node)
        # 数据操作
        # process(node)
        # 找出后继结点，并判断没被访问过
        # nodes = generate_related_nodes(node)
        # 拿出后继结点
        queue.push(nodes)


def DFS(node, visited):
    # 标记被访问
    visited.add(node)
    # 数据操作
    # process(node)

    for next_node in node.children():
        if not next_node in visited:
            DFS(next_node, visited)
