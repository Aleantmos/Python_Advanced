def set_cover(universe, sets):
    covered = set()
    selected_sets = []

    while covered != set(universe):
        best_set = max(sets, key=lambda s: len(s - covered))
        covered.update(best_set)
        selected_sets.append(best_set)
        sets.remove(best_set)

    return selected_sets


universe = set(map(int, input().split(", ")))
cnt = int(input())
sets = []

for _ in range(cnt):
    sets.append(set(map(int, input().split(", "))))

result = set_cover(universe, sets)

formatted_result = ["{" + ", ".join(map(str, s)) + "}" for s in result]
print("\n".join(formatted_result))
