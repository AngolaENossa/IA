# ricochet_robots.py: Template para implementação do 1º projeto de Inteligência Artificial 2020/2021.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 36:
# 93748 Rafael António Fernandes e Costa Marques Candeias
# 93749 Rafael de Melo Pereira

from search import Problem, Node, astar_search, breadth_first_tree_search, depth_first_tree_search, greedy_search

r1 = []
r2 = []
r3 = []
r4 = []
obj = []


class RRState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = RRState.state_id
        RRState.state_id += 1

    def __lt__(self, other):
        """ Este método é utilizado em caso de empate na gestão da lista
        de abertos nas procuras informadas."""
        return self.id < other.id


class Board:
    """ Representacao interna de um tabuleiro de Ricochet Robots. """

    def robot_position(self, robot: str):
        """ Devolve a posição atual do robô passado como argumento. """
        if (r1[0] == robot):
            return r1[1], r1[2]
        elif (r2[0] == robot):
            return r2[1], r2[2]
        elif (r3[0] == robot):
            return r3[1], r3[2]
        else:
            return r4[1], r4[2]

    def objective_position(self):
        """ Devolve a côr e a posição do objetivo do tabuleiro. """
        return obj[0], obj[1], obj[2]

    # TODO: outros metodos da classe


def parse_instance(filename: str) -> Board:
    """ Lê o ficheiro cujo caminho é passado como argumento e retorna
    uma instância da classe Board. """
    f = open(filename, "r")

    n1 = int(f.readline())
    a = f.readline()
    b = f.readline()
    c = f.readline()
    d = f.readline()
    e = f.readline()

    for word in a:
        if word != " ":
            r1.append(word)
    for word in b:
        if word != " ":
            r2.append(word)
    for word in c:
        if word != " ":
            r3.append(word)
    for word in d:
        if word != " ":
            r4.append(word)
    for word in e:
        if word != " ":
            obj.append(word)

    f.close()


class RicochetRobots(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        # TODO: self.initial = ...
        pass

    def actions(self, state: RRState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        # TODO
        pass

    def result(self, state: RRState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação retornada deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state). """
        # TODO
        pass

    def goal_test(self, state: RRState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se o alvo e o robô da
        mesma cor ocupam a mesma célula no tabuleiro. """
        # TODO
        pass

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """
        # TODO
        pass


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de inumpyut de sys.argv[1],
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
