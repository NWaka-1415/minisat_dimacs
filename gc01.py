import itertools
import math


def cmb(n: int, r: int):
    return list(itertools.combinations(range(1, n + 1), r))


class GCP:
    def __init__(self, nodes: int, edges: list, colors: int):
        self.nodes = nodes
        self.edges = edges
        self.colors = colors
        self.val = nodes * colors
        self.clauses = math.floor(nodes * (1 + colors * (colors - 1) / 2) + len(edges) * colors)

    def p(self, i: int, a: int):
        return (i - 1) * self.colors + a

    def printClause(self, lits: list):
        litsStr = ""
        for i in lits:
            litsStr += "{}".format(i) + " "
        litsStr += "0"
        print(litsStr)

    def encode(self):
        print("p cnf {0} {1}".format(self.val, self.clauses))
        for i in range(1, self.nodes + 1):
            self.printClause([self.p(i, a) for a in range(1, self.colors + 1)])
            for tuples in cmb(self.colors, 2):
                self.printClause([-self.p(i, tuples[0]), -self.p(i, tuples[1])])
        for edge in self.edges:
            for t in range(1, self.colors + 1):
                self.printClause([-self.p(edge[0], t), -self.p(edge[1], t)])


if __name__ == '__main__':
    gcp = GCP(4, [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)], 3)
    gcp.encode()
