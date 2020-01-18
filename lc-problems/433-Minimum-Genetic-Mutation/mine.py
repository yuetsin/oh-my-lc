#!/usr/bin/env python

from functools import lru_cache


class Gene:
    def __init__(self, gene):
        self.gene = gene
        self.can_be = []
        self.nucbases = ['A', 'C', 'G', 'T']

    def build_mutation(self, bank_set):
        for i in range(len(self.gene)):
            char = self.gene[i]
            for nucbase in self.nucbases:
                if nucbase == char:
                    continue
                new_str = self.gene[:i] + nucbase + self.gene[i + 1:]
                # print("new_str = %s" % new_str)
                if new_str in bank_set:
                    self.can_be.append(new_str)

        # print("%s's mutation_list is %s" % (self.gene, self.can_be))


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # WORD LADDER 变种……
        bank_set = set(bank)

        start_gene = Gene(start)
        start_gene.build_mutation(bank_set)

        genes = {
            start: start_gene
        }

        for item in bank:
            gene_item = Gene(item)
            gene_item.build_mutation(bank_set)
            genes.update({item: gene_item})

        # @lru_cache(maxsize=None)
        def findMutationPath(since: str, visited_set: set) -> int:
            # print("called fMP %s" % since)
            if since == end:
                return 0
            min_path = float('+inf')
            gene = genes[since]
            for next_step in gene.can_be:
                if next_step in visited_set:
                    continue
                new_set = copy.deepcopy(visited_set)
                new_set.add(next_step)
                step_cnt = findMutationPath(next_step, new_set)
                if step_cnt != -1:
                    min_path = min(min_path, step_cnt)

            return min_path + 1 if min_path != float('+inf') else -1

        return findMutationPath(start, set())
