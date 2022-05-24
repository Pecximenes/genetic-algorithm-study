#* Adding the parameters
index_list = []
variables_list = []
polynom_dict = {}

num_of_polynoms = int(input("Number of polynoms:"))-1
for pos, i in enumerate(range(num_of_polynoms, -1, -1)):
    polynom = chr(97 + pos)

    result = int(input(f"Multiplicity of {polynom}**{i}: "))

    index_list.append(i)
    variables_list.append(result)
    polynom_dict[polynom] = []


print(index_list)
print(variables_list)
print(polynom_dict)
solutions = []

