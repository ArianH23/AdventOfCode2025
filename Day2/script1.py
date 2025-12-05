total=0
with open("Day2/input.txt", "r") as f:
    line = f.readline()
    limits = line.split(',')

    for limit in limits:
        ini = limit.split('-')[0]
        fin = limit.split('-')[1]

        for i in range(int(ini), int(fin) + 1):
            num_string = str(i)
            len_string = len(num_string)

            if num_string[len_string//2:] == num_string[:len_string//2]:
                total += i
                print(num_string)
                input()

    print(total)
