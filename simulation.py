import matplotlib.pyplot as plt
import math
from Creature import Creature

population_init = 100000
birth_rate = 0.45
death_rate = 0.40
mutation_factor = 0.01
disease_factor = 0.005
insane_disease_factor = Creature.MODERATE

deer = Creature(population_init, birth_rate, death_rate, mutation_factor, disease_factor, insane_disease_factor)

x, y = [], []
# simulate out for 1000 steps
x.append(0)
y.append(deer.get_current_population())
for n in range(1, 1000):
    x.append(n)
    deer.calculate_new_population()
    y.append(deer.get_current_population())
    #print(deer.get_current_population())

print(y)

fig = plt.figure(figsize=(10, 6))
plt.xlim(0, 1000)
plt.ylim(5000, 2000000)
plt.yscale('log')
plt.xlabel('Years', fontsize=20)
plt.ylabel('Population', fontsize=20)
plt.title('Population Simulation over 1000 years', fontsize=20)
plt.plot(x, y, label="ee")
plt.show()
