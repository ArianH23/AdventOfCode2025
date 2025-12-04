lock = 50
zeroCounter = 0
with open("Day1/input.txt", "r") as f:
    for line in f:
        numRotation = int(line[1:])
        numMod = numRotation % 100
        addRotation = numRotation // 100

        if numMod > 0:
            if line[0] == "L":
                lock -= numMod
                if lock <= 0 and lock != -numMod:
                    zeroCounter = zeroCounter + 1

            else:
                lock += numMod
                if lock >= 100:
                    zeroCounter = zeroCounter + 1

            lock %= 100

        zeroCounter = zeroCounter + addRotation

    print(zeroCounter)
