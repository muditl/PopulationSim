import math
from random import random


# TODO make some limiting factors.
# TODO break up the death factor.


class Creature:
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    COUNTER = 0  # for debugging

    def __init__(self, population_init, birth_rate, mutation_factor, disease_factor, insane_disease_factor):
        self.current_population = population_init
        self.birth_rate = birth_rate
        self.mutation_factor = mutation_factor
        self.disease_factor = disease_factor
        self.insane_disease_factor = insane_disease_factor
        self.food_factor = 0
        self.insane_mutation_factor = 0
        self.EXTINCT = False
        self.carrying_capacity_factors = self.generate_carrying_capacity_factors()

    def get_current_population(self):
        return self.current_population

    def calculate_new_population(self):
        self.current_population = self.current_population + self.rate_of_growth()
        if self.current_population < 4:
            self.EXTINCT = True

    # rate before limiting factors
    def rate_of_growth(self):
        carrying_capacity = self.calculate_carrying_capacity()
        delta = self.cumulative_birth_factors() + self.cumulative_death_factors()
        if self.current_population + delta > carrying_capacity:
            delta = delta * 0.9
        return delta

    # ----------------------------------- B I R T H ---------- F A C T O R S ----------------------------------- #

    def cumulative_birth_factors(self):
        return math.floor(
            max(self.factor_birth_rates() + self.factor_mutations(), (1.5 + random() * 0.5) * self.current_population))

    # for each individual, b more are born.
    def factor_birth_rates(self):
        b = self.birth_rate
        p_0 = self.current_population
        return b * p_0

    # the rate of increase of population increases each year due to mutations
    def factor_mutations(self):
        m = self.mutation_factor
        rand = random()
        if rand > 0.9:
            self.factor_insane_mutations()
        if rand > 0.75:
            self.mutation_factor += self.insane_mutation_factor / 10
        return m * rand * self.current_population

    # the rate of increase of population increases each year due to mutations
    def factor_insane_mutations(self):
        rand = random() * random() * random()
        if rand > 0.5:
            print("INSANE MUTATION")
            self.insane_mutation_factor = self.mutation_factor * 2 * rand

    # ----------------------------------- D E A T H ---------- F A C T O R S ----------------------------------- #

    def cumulative_death_factors(self):
        return math.floor(min(self.factor_accidents() + self.factor_regular_disease() +
                              self.factor_insane_disease(), -1000000))
        # return self.factor_death_rate() + self.factor_regular_disease() + \
        #        self.factor_insane_disease()

    # def factor_death_rate(self):
    #     d = self.death_rate
    #     p_0 = self.current_population
    #     return -d * p_0

    def factor_regular_disease(self):
        p_0 = self.current_population
        rand = random()
        return -p_0 * rand * self.disease_factor

    def factor_accidents(self):
        rand = random()
        return -self.current_population * rand * 0.01

    # 0-d % of population would die due to disease each year
    # typically between 0.05 and 5
    def factor_insane_disease(self):
        p_0 = self.current_population

        rand = random() * random() * random() * random() * random() * random()
        if self.insane_disease_factor == self.HIGH:
            if rand > 0.1:
                print("PANDEMIC")
                return -rand * p_0

            return 0
        rand = rand * random()
        if self.insane_disease_factor == self.MODERATE:
            if rand > 0.1:
                print("PANDEMIC")
                return -rand * p_0
            return 0
        rand = rand * random()
        if self.insane_disease_factor == self.LOW:
            if rand > 0.1:
                print("PANDEMIC")
                return -rand * p_0
            return 0

    # -------------------------------- L I M I T I N G ---------- F A C T O R S -------------------------------- #

    def factor_food(self):
        # TODO
        return

    def calculate_carrying_capacity(self):
        p_0 = self.current_population
        carrying_capacity = min(self.carrying_capacity_factors)
        return carrying_capacity

    @staticmethod
    def generate_carrying_capacity_factors():
        food = 100000
        habitat = 100000
        predators = 100000
        return [food, habitat, predators]
