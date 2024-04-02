import random

def choose_initial_solution():
    choice = input("Random initial solution or user input? (random/user): ").lower()
    return random.uniform(-10,10) if choice == 'random' else float(input("Enter initial solution: "))

def evaluate_objective_function(solution):
    return solution ** 2

def generate_neighbour(solution):
    return solution + random.uniform(-1,1)

max_iterations = 100

current_solution = choose_initial_solution()
current_value = evaluate_objective_function(current_solution)

for _ in range(max_iterations):
    neighbour = generate_neighbour(current_solution)
    neighbour_value = evaluate_objective_function(neighbour)

    if neighbour_value > current_value:
        current_solution,current_value = neighbour,neighbour_value

print("Best Solution: ",current_solution)
print("Objective Value: ",current_value)