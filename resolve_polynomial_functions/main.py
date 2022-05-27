import random


def calculate_functions(index_list, var_list, sol, des_sol):
    result = 0
    for pos, i in enumerate(index_list):
        result += var_list[pos] * (sol[pos]**i)

    return result - des_sol


def fitness(index_list, var_list, sol, des_sol):
    answer = calculate_functions(index_list, var_list, sol, des_sol)
    print(answer)
    if answer == 0: return 99_999
    else: return abs(1/answer)



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
for pos, i in enumerate(range(num_of_polynoms, 0, -1)):
    polynom = chr(97 + pos)

    result = int(input(f"Multiplicity of {polynom}**{i}: "))

    if result != 0:
        variables_list.append(result)

    index_list.append(i)
    polynom_dict[polynom] = []


print(index_list)
print(variables_list)
print(polynom_dict)

solutions = generate_solutions(num_of_polynoms)
print(solutions)

desired_solution = int(input("Desired solution: "))

for i in range(10000):
    rankedsolutions = []
    for solution in solutions:
        weight = fitness(index_list, variables_list, solution, desired_solution)
        print(weight)
        rankedsolutions.append([weight, solution])
    
    rankedsolutions.sort()
    rankedsolutions.reverse()

    print(f"=== Gen {i} best solutions ===")
    print(rankedsolutions[0])

    if rankedsolutions[0][0] > 9999:
        break

    bestsolutions = rankedsolutions[:100]

    elements = []
    for b_sol in bestsolutions:
        for i in b_sol[1]:
            elements.append(i)
    
    new_generation = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)

        new_generation.append([e1, e2, e3])
    
    solutions = new_generation

print("Final result:")
print(calculate_functions(index_list, variables_list, solution, desired_solution) + desired_solution)