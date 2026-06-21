import csv

min_a = 1
max_a = 4

min_b = 4
max_b = 5

min_c = 4
max_c = 5

min_d = 13
max_d = 13

min_total = 22
max_total = 27

data_sheet = open("BOTC_Jinxes_v1.csv", "r")

data = csv.reader(data_sheet)
data = [row for row in data]

data_sheet.close()

num_characters = len(data) - 2

adjacency_matrix = [[0] * num_characters for _ in range(num_characters)] 

type_sets = [[], [], [], []]

out_arr = []
type_id = -1
for char_i in range(len(data[2:])):
    char_data = data[2 + char_i]
    if char_data[0] != "":
        type_id += 1
    out_arr.append(f"{char_data[1]}\n")
    
    type_sets[type_id].append(char_i + 1)
    for char_j in range(len(char_data) - 2):
        if char_data[2 + char_j] == "":
            adjacency_matrix[char_i][char_j] = 0
        else:
            adjacency_matrix[char_i][char_j] = int(char_data[2+char_j])
            
f = open("var_lookup.txt", "w")
f.write("".join(out_arr))
f.close()



for i in range(len(adjacency_matrix)):
   for j in range(len(adjacency_matrix)):
       if adjacency_matrix[i][j] != adjacency_matrix[j][i]:
           print("NOT SYMMETRIC", i, j)
           print(data[i+2][1])
           print(data[j+2][1])
           exit()


type_sets[0] = list(map(str, type_sets[0]))
type_sets[1] = list(map(str, type_sets[1]))
type_sets[2] = list(map(str, type_sets[2]))
type_sets[3] = list(map(str, type_sets[3]))

out_arr = []

out_arr.append(f"param NumCharacters := {num_characters};\n")
for i in [("A", 0), ("B", 1), ("C", 2), ("D", 3)]:
    out_arr.append(f"set {i[0]} := {" ".join(type_sets[i[1]])};\n")

out_arr.append("\n")

out_arr.append(f"param MinA := {min_a};\n")
out_arr.append(f"param MinB := {min_b};\n")
out_arr.append(f"param MinC := {min_c};\n")
out_arr.append(f"param MinD := {min_d};\n\n")

out_arr.append(f"param MaxA := {max_a};\n")
out_arr.append(f"param MaxB := {max_b};\n")
out_arr.append(f"param MaxC := {max_c};\n")
out_arr.append(f"param MaxD := {max_d};\n\n")

out_arr.append(f"param MinTotal := {min_total};\n")
out_arr.append(f"param MaxTotal := {max_total};\n")

out_arr.append("\n")

out_arr.append("param ValidJinx :=\n")
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix)):
        out_arr.append(f"    {i+1:<4d} {j+1:<4d} {adjacency_matrix[i][j]}")
        out_arr.append("\n")
out_arr[-1] = ";"

f = open("data_file.dat", "w")
f.write("".join(out_arr))
f.close()