# Importa o método copy() e o módulo random().
import copy
import random

# Cria a classe Hat e acrescenta a ela uma
# função interna (__init__()) e outra externa
# (draw()).
class Hat:
    # Cria __init__ e atribui a função self
    # e **kwargs. Usamos kwargs por ser uma
    # convensão que representa Keyword Arguments.
    # Usamos ** na frente de kwargs para aceitar
    # diferentes argumentos e organiza-los em
    # um dicionario, ou seja, {}.
    def __init__(self, **kwargs):
        # Usamos .contents para retornar uma
        # lista com os itens presentes em self.
        self.contents = []
        # Usa a iteração for sobre os utens em
        # kwargs para apensar (usando .append())
        # as bolas com base nas cores. Então se
        # temos "vermelho = 2", será apensado a
        # lista duas vezes vermelho, ou seja
        # (vermelho, vermelho).
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    # Cria a função draw() e atribui a ela
    # self e num, e cria a variavel draw e
    # atribui uma lista a ela. 
    def draw(self, num):
        drawn = []
        # Usa a condicional if para verificar
        # se num é maior ou igual à self.contents.
        # Caso seja devolve a lista em self e caso
        # não apensa a lista de draw uma bola
        # aleatória em self.contents e a remove
        # de self.contents. Para isso usamos
        # alguns metodos, o metodo .pop() remove
        # um item da lista especificada nesse caso
        # self.contents. O metodo .index() retorna
        # a primeira ocorrencia dos parametros usados,
        # nesse caso usamos random.choice() em
        # self.contents para selecionar de forma
        # aleatória dentro da lista. Depois de
        # tirar as bolas de self.contents e
        # adiciona-las a lista de draw, retorna
        # a lista de draw.
        if num >= len(self.contents):
            return self.contents
        else:
            for i in range(num):
                drawn.append(
                    self.contents.pop(
                        self.contents.index(
                          random.choice(self.contents))))
        return drawn

# Cria a função experiment() e atribui a ela
# a classe hat e outros 3 parametros:
# expected_balls, num_balls_drawn e num_experiments.
# Cria também a variavel hits e atribui valor 0 a ela.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hits = 0
    # Usa iteração for com base no parametro
    # num_experiments e para cada iteração
    # estabelece is_hit como true, copia hat
    # na variavel experiment_hat usando o
    # método copy.deepcopy() e cria também a
    # variavel experiment_list recebendo o
    # valor de experiment_hat com a função
    # draw() com base no valor do parametro
    # num_balls_drawn.
    for i in range(num_experiments):
        is_hit = True
        experiment_hat = copy.deepcopy(hat)
        experiment_list = experiment_hat.draw(num_balls_drawn)
        # Cria uma nova iteração usando o
        # parametro expected_balls e verifica
        # os itens dela. Se não existir a bola
        # na variavel experiment_list is_hit
        # vira falso, invoca break para parar
        # a iteração e caso exista segue.
        # Cria também uma variavel count e atribui 0.
        for key, value in expected_balls.items():
            count = 0
            if key not in experiment_list:
                is_hit = False
                break
            # Aqui temos mais uma iteração for,
            # dessa vez ela percorrerá as bolas
            # em experiment_list e caso corresponda
            # adiciona mais 1 à variavel count.
            for ball in experiment_list:
                if ball == key: count += 1
            # Usa a condicional if para verificar
            # se count é menor do que o valor
            # apresentado no parametro expected_balls.
            # Caso seja trasforma is_hit em falso e
            # corta a iteração. Caso não seja segue.
            if count < value:
                is_hit = False
                break
        # Usa uma nova condicional if, caso is_hit
        # seja verdadeiro (True) acrescenta mais um
        # a hits e caso seja falso (False) segue.
        if is_hit: hits += 1
    # Por fim retornamos a divisão do número de hits
    # pelo parametro num_experiments, ou seja, retorna
    # o número de vezes que a bola apareceu pelo número
    # de experimentos realizados.
    return hits / num_experiments