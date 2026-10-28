def reverse_list(items):
    resolved = []
    
    for item in items:
        resolved.insert(0, item)
    return resolved
print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))