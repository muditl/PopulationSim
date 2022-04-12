import matplotlib.pyplot as plt
import math
from Creature import Creature

population_init = 10000
birth_rate = 0.1
mutation_factor = 0.0001
disease_factor = 0.0
insane_disease_factor = Creature.HIGH

deer = Creature(population_init, birth_rate, mutation_factor, disease_factor, insane_disease_factor)

x, y = [], []
# simulate out for 1000 steps
x.append(0)
y.append(deer.get_current_population())
for n in range(1, 1000):
    x.append(n)
    deer.calculate_new_population()
    y.append(deer.get_current_population())
    # print(deer.get_current_population())

print(y)
fig = plt.figure(figsize=(10, 6))
plt.xlim(0, 1000)
plt.ylim(100, 2000000)
plt.yscale('log')
plt.xlabel('Years', fontsize=20)
plt.ylabel('Population', fontsize=20)
plt.title('Population Simulation over 1000 years', fontsize=20)
plt.plot(x, y, label="ee")
plt.show()
