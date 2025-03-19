import csv

class Graph(object):
    def __init__(self, graph=None):
        if graph is None:
            graph = dict()
        self.graph = graph

    def __str__(self):
        temp =''
        for x in self.graph:
            temp += x + ' --> <' + ','.join(self.graph[x]) + '>\n'
        return temp

    def build_graph(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                self.graph[line[0]] = [n.strip() for n in line[1:]]



def main():
    file_name = 'io/g1.csv'

    g1 = Graph()
    g1.build_graph(file_name)
    print(g1)

if __name__ == "__main__":
    main()
