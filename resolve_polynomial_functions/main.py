import random


def calculate_functions(index_list, var_list, pol_list):
    function_result = 0
    for pos, i in enumerate(index_list):
        function += var_list[pos] * pol_list**i

    return function_result


def generate_solutions(num):
    solutions = []
    for _ in range(1000):
        sol = []
        for _ in range(num):
            sol.append(random.uniform(0, 10_000))

        solutions.append(sol)

    return solutions


# * Adding the parameters
index_list = []
variables_list = []
polynom_dict = {}

num_of_polynoms = int(input("Number of polynoms:"))
for pos, i in enumerate(range(num_of_polynoms - 1, -1, -1)):
    polynom = chr(97 + pos)

    result = int(input(f"Multiplicity of {polynom}**{i}: "))

    index_list.append(i)
    variables_list.append(result)
    polynom_dict[polynom] = []


print(index_list)
print(variables_list)
print(polynom_dict)

solutions = generate_solutions(num_of_polynoms)


print(solutions)
