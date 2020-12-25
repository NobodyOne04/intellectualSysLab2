import random

from src.genetic_code import GeneticCode


class Pool:
    def __init__(self, pool_size: int, goal: str, genes):
        self.__pool = [GeneticCode('', goal, genes) for _ in range(pool_size)]
        self.__pool_size = pool_size
        self.__genes = genes
        self.__goal = goal

    def get_random(self) -> GeneticCode:
        return self.__pool[random.randint(0, len(self.__pool) - 1)]

    def selection(self, cut_off_percentage: float = 0.1) -> None:
        measure_pool = [(item.measure(), item) for item in self.__pool]
        sorted_pool = [item[1] for item in sorted(measure_pool, key=lambda x: x[0], reverse=True)]
        self.__pool = sorted_pool[:int(round(self.__pool_size * cut_off_percentage))]

        while len(self.__pool) < self.__pool_size:
            new_dnk = self.get_random().crossing_over(self.get_random().dnk)
            new_gene = GeneticCode(
                new_dnk,
                self.__goal,
                self.__genes
            )
            self.__pool.append(new_gene)

    def evolution(self, epoch: int = 1000) -> int:
        for iterations in range(epoch):
            if self.__pool[0].dnk == self.__goal:
                break

            for index, item in enumerate(self.__pool):
                self.__pool[index].mutate()

            self.selection()
            print(self.__pool[0].dnk)

        return iterations
