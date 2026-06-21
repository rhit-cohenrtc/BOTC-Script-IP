f = open("var_lookup.txt")
id_to_name = f.readlines()
id_to_name = [""] + list(map(str.strip, id_to_name))
f.close()


f = open("LP_output.txt", "r", encoding="utf-16")
lines = list(map(str.strip, f.readlines()))
f.close()


# for line in lines:
#     if line.find("Variables") != -1:
#         print(line)

info = lines[4].split(",")
num_vars = info[0].split("=")
num_vars = int(num_vars[1])

for i in range(6, 6+num_vars):
    line = lines[i].split(":")
    val = float(line[2])
    if val > 0.75:
        print(id_to_name[i + 1 - 6] + ",")