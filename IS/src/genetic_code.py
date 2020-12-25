import random


class GeneticCode:
    def __init__(self, dnk: str, goal: str, genes):
        if not dnk:
            self.dnk = ''.join(
                random.choices(genes, k=len(goal))
            )
        else:
            self.dnk = dnk
        self.__goal = goal
        self.__genes = genes

    def measure(self) -> int:
        score = 0
        for index, gene in enumerate(self.dnk):
            if gene != self.__goal[index]:
                score -= 1
        return score

    def mutate(self, number_of_changes: int = 5) -> None:
        new_dnk = list(self.dnk)
        for _ in range(number_of_changes):
            random_index = random.randint(0, len(new_dnk) - 1)
            if self.dnk[random_index] != self.__goal[random_index]:
                new_dnk[random_index] = random.choice(self.__genes)
        self.dnk = "".join(new_dnk)

    def crossing_over(self, another_dnk: str) -> str:
        random_slice = random.randint(
            0,
            len(self.dnk) - 1
        )
        return "".join(self.dnk[:random_slice] + another_dnk[random_slice:])
