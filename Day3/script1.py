total = 0
with open("Day3/input.txt", "r") as f:
    for line in f:
        first_max = max(line[:-2])
        first_max_index = line.index(first_max)
        second_max = max(line[first_max_index+1:])
        total += int(first_max + second_max)
        # input()
    print(total)