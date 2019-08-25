import sys

def hour_to_seg(value):
    return value*3600


def min_to_seg(value):
    return value*60


def segundos_to_hour(value):
    return value/3600


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.lista_adjacente = []
        self.visitado = False

    def add_adjacente(self, destino, custo):
        self.lista_adjacente.append([destino, custo])

    def pai(self):
        pass


class Grafo:
    vertices = {}
    dijkstra_matriz = {}
    dijkstra_visitas = []

    def add_vertice(self, vertice):
        self.vertices[vertice.nome] = vertice

    def add_aresta(self, origem, destino, custo):
        if origem in self.vertices:
            self.vertices[origem].add_adjacente(destino=destino, custo=custo)
        if origem not in self.vertices:
            vertice = Vertice(origem)
            self.add_vertice(vertice=vertice)
            self.vertices[origem].add_adjacente(destino=destino, custo=custo)
        if destino not in self.vertices:
            vertice = Vertice(destino)
            self.add_vertice(vertice=vertice)

    def mostra_grafo(self):
        print('mostra grafo', self.vertices)
        for chave, valor in self.vertices.items():
            print(valor.nome, valor.lista_adjacente, valor.visitado)

    def limpa_grafo(self):
        self.vertices.clear()
        self.dijkstra_matriz.clear()
        # self.dijkstra_matriz = {"varzea": [0, "varzea"]}
        # self.dijkstra_visitas.append(['varzea', 0])
        self.dijkstra_matriz = {"varzea": [0, "varzea"]}
        self.dijkstra_visitas.append(['varzea', 0])

    def mostra_matriz_dijkstra(self):
        for chave, valor in self.dijkstra_matriz.items():
            print(chave)
            print('\t', valor)

    def quicksort(self, lista):
        return sorted(lista, key=lambda lista: lista[1])

    def dijkstra(self):

        # Inicia a matriz do dijkstra. O valor de distância é 61 porque o tempo máximo no exercício é 60
        for i in self.vertices:
            if i not in self.dijkstra_matriz:
                self.dijkstra_matriz[i] = [sys.maxsize, ""]

        # Lista para visitar
        # print("dijkstra visitas:", self.dijkstra_visitas)

        # Enquanto houver vertices para serem visitados
        while self.dijkstra_visitas:

            # Mostra o vértice que será analisado, orientando-se pela lista de visitas
            # print("\nvértice atual:", self.vertices[self.dijkstra_visitas[0][0]].nome)

            # Se o vértice ainda não foi visitado
            if not self.vertices[self.dijkstra_visitas[0][0]].visitado:
                # print("\tlista de adjacencia do", self.vertices[self.dijkstra_visitas[0][0]].nome, '-',
                #       self.vertices[self.dijkstra_visitas[0][0]].lista_adjacente)

                lista_adjacente_elemento_visitado = self.vertices[self.dijkstra_visitas[0][0]].lista_adjacente

                for i_lista_adjacente in range(0, len(lista_adjacente_elemento_visitado)):
                    # elemento_adjacente = ['nome_vertice', custo]
                    elemento_adjacente = lista_adjacente_elemento_visitado[i_lista_adjacente]

                    # Se o elemento da adjacencia ainda não foi visitado
                    if not self.vertices[elemento_adjacente[0]].visitado:
                        # print("\t", elemento_adjacente[0], "não foi visitado")
                        # Adiciona ele à lista de visitas
                        self.dijkstra_visitas.append([elemento_adjacente[0], elemento_adjacente[1]])

                        # print("\tdistancia do vértice atual", self.dijkstra_matriz[self.dijkstra_visitas[0][0]][0])
                        # print("\tdistancia para o próximo vértice (adj)", elemento_adjacente[0], '=', elemento_adjacente[1])
                        soma_distancias = self.dijkstra_matriz[self.dijkstra_visitas[0][0]][0] + elemento_adjacente[1]
                        # print("\tsoma distancias", soma_distancias)

                        if soma_distancias < self.dijkstra_matriz[elemento_adjacente[0]][0]:
                            # print("\tsomou distancias")
                            self.dijkstra_matriz[elemento_adjacente[0]][0] = soma_distancias
                            self.dijkstra_matriz[elemento_adjacente[0]][1] = self.dijkstra_visitas[0][0]
                            # print("\t atualizou matriz dijkstra de ", elemento_adjacente[0])
                            # print("\t", self.dijkstra_matriz[elemento_adjacente[0]])
                    # else:
                    #     print("\tJá foi visitado", self.vertices[elemento_adjacente[0]].nome)

                self.vertices[self.dijkstra_visitas[0][0]].visitado = True
            self.dijkstra_visitas.pop(0)
            if self.dijkstra_visitas:
                # print("@@@@@@@@@", self.dijkstra_visitas)
                self.dijkstra_visitas = self.quicksort(self.dijkstra_visitas)
            #     print("@@@@@@@@@", self.dijkstra_visitas)
            # print(".dijkstra visitas", self.dijkstra_visitas)
            # print("matriz dijkstra", self.dijkstra_matriz)
            # import time
            # time.sleep(5)
        # self.mostra_matriz_dijkstra()
        return self.dijkstra_matriz['alto'][0]

g = Grafo()
# print(hora)
# print(sys.maxsize, type(sys.maxsize))

while True:
    hora = hour_to_seg(17)
    g.limpa_grafo()
    x, n, v = input().split()
    x, n, v = int(x), int(n), int(v)

    hora += min_to_seg(x)

    if hora <= 63000:
        hora = 63000
    else:
        hora = 64200

    # print('--', hora)

    if x + n + v == 0:
        break

    for i in range(0, n):
        vertice1, vertice2, peso = input().split()
        peso = int(peso)

        g.add_aresta(origem=vertice1, destino=vertice2, custo=peso)

    hora += min_to_seg(g.dijkstra())

    # print(50*"=====")

    # g.mostra_matriz_dijkstra()

    h = hora // 3600
    minuto = (hora % 3600) // 60

    # print(h, minuto)

    controle_hora = 0

    if h == 24:
        # print('24')
        h = "00"
    elif h > 24:
        # print('maior que 24')
        h -= 24
        if h < 10:
            h = "0"+str(h)

    if minuto == 0:
        minuto = "00"
    elif minuto < 10:
        minuto = "0"+str(minuto)

    print("%s:%s" % (h, minuto))

    if hora <= 64800:
        print("Nao ira se atrasar")
    else:
        print("Ira se atrasar")


# print("--- %s  seconds ---" % (time.time() - start_time))