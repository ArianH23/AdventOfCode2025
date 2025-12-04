lock = 50
zeroCounter = 0
with open("Day1/input.txt", "r") as f:
    for line in f:
        if line[0] == "L":
            lock -= int(line[1:])
        else:
            lock += int(line[1:])

        lock %= 100
        if lock == 0:
            zeroCounter += 1
    print(zeroCounter)
