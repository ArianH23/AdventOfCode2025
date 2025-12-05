total=0
with open("Day2/input.txt", "r") as f:
    line = f.readline()
    limits = line.split(',')

    for limit in limits:
        ini = limit.split('-')[0]
        fin = limit.split('-')[1]

        # Numbers range
        for i in range(int(ini), int(fin) + 1):
            num_string = str(i)
            len_string = len(num_string)

            # Number substring until the middle
            for j in range(1, (len_string // 2) + 1):
                substring_base = num_string[:j]
                aux_list = num_string.split(substring_base)
                if aux_list == [''] * ((len_string // len(substring_base)) + 1):
                    total = total + i
                    break
    print(total)
