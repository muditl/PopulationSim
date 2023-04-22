import math
import random

import np as np
import numpy as np
from scipy.stats import norm

random_num = random.random()
print(random_num)

# defining consts
LOW = "LOW"
MODERATE = "MODERATE"
HIGH = "HIGH"

# defining vars
current_population_male = np.absolute(np.random.normal(20, 20, 10000))
current_population_female = np.absolute(np.random.normal(20, 20, 10000))
capacity = 100000

sex_ratio = 0.5
birth_ratio = 0.3
min_birth_age = 14
max_birth_age = 45
print(abs(-11524))


# helper functions
# return population in given range
def age_range_population(lower, upper, _cur_pop):
    return np.count_nonzero((lower < _cur_pop) & (_cur_pop < upper))


# defining factors
def birth_rate():
    pass


def get_number_of_births():
    of_age = age_range_population(min_birth_age, max_birth_age, current_population_female)
    number_of_births = int(of_age * birth_ratio)
    return np.zeros(number_of_births)


def get_births_male_female(_sex_ratio, _no_births):
    sex_ratio = _sex_ratio + (random.random() * 0.01)
    males = np.zeros(int(current_population_male * sex_ratio))
    females = np.zeros(int(current_population_female * (1 - sex_ratio)))
    return males, females



def combine_populations(current_population, to_add):
    return np.append(current_population, to_add)
