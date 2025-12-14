total = 0
with open("Day3/input.txt", "r") as f:
    for line in f:
        l = line[:-1]
        current = []
        current_index = 0
        size = 12
        for _ in range(size):
            if size != 1:
                first_max = max(l[:-size+1])
            else:
                first_max = max(l)
            current_index = l.index(first_max) + 1
            l = l[current_index:]
            current.insert(len(current), first_max)
            size -= 1

        total += int(''.join(current))