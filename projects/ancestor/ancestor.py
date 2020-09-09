def earliest_ancestor(ancestors, starting_node, isChild=False):
    for parent, child in ancestors:
        if child == starting_node:
            return earliest_ancestor(ancestors, parent, True)

    if isChild:
        return starting_node
    else:
        return -1

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 1)) # 10
    print(earliest_ancestor(test_ancestors, 2)) # -1
    print(earliest_ancestor(test_ancestors, 3)) # 10
    print(earliest_ancestor(test_ancestors, 4)) # -1
    print(earliest_ancestor(test_ancestors, 5)) # 4
    print(earliest_ancestor(test_ancestors, 6)) # 10
    print(earliest_ancestor(test_ancestors, 7)) # 4
    print(earliest_ancestor(test_ancestors, 8)) # 4
    print(earliest_ancestor(test_ancestors, 9)) # 4
    print(earliest_ancestor(test_ancestors, 10)) # -1
    print(earliest_ancestor(test_ancestors, 11)) # -1