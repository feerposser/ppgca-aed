
class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.lista_adjacente = []

    def add_adjacente(self, destino, custo):
        self.lista_adjacente.append([destino, custo])


class Grafo:
    vertices = {}

    def add_vertice(self, vertice):
        self.vertices[vertice.nome] = vertice
        return

    def add_aresta(self, origem, destino, custo):
        self.vertices[origem].add_adjacente(destino=destino, custo=custo)
        return

    def mostra_grafo(self):
        for chave, valor in self.vertices.items():
            print(valor.nome, valor.lista_adjacente)


g = Grafo()
cidades = ["passo fundo", "uruguaiana", "tapejara", "carazinho", "marau"]
b = []
for i in cidades:
    b.append(Vertice(i))

print([i.nome for i in b])

g.add_vertice(b[0])
g.add_vertice(b[2])
g.add_aresta(origem="passo fundo", destino="tapejara", custo=10)
g.add_aresta(origem="passo fundo", destino="carazinho", custo=5)

g.mostra_grafo()