def getnodes(x, y):
    # return [(1, 0), (0, 1)]
    return []


def main(sourcex, sourcey, targetx, targety):
    path = []
    stack = [(sourcex, sourcey, path)]

    visited = set()
    while stack:

        x, y, path = stack.pop()

        childre = getnodes(x, y)

        if (targetx, targety) in childre:
            return path + [(targetx, targety)]

        for a, b in childre:
            if (a, b) not in visited:
                visited.add((a, b))  # not visted, add to stack for dfs
                stack.append((a, b), path + [(a, b)])

    return None
