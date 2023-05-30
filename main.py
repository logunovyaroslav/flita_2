import networkx as nx
import matplotlib.pyplot as plt

try:
    # Запрос количества вершин и ребер у пользователя
    n = int(input("Введите количество вершин: "))
    while n < 0:
        print("Количество вершин не может быть отрицательным")
        n = int(input("Введите количество вершин: "))

    # Создание пустого графа
    G = nx.Graph()

    # Добавление вершин в граф
    for i in range(n):
        G.add_node(i+1)
    while True:
        action = input("Для создания нового соединения напишите - 'add'; для отображения графа напишите - 'draw'; "
                       "для того что бы закончить напишите - 'end': \n")
        match action:
            case 'add':
                x = int(input("Введите исходящую вершину графа: "))
                while x > n or x <= 0:
                    print("Невозможное значение")
                    x = int(input("Введите исходящую вершину графа: "))
                y = int(input("Введите приходящую вершину графа: "))
                while y > n or y <= 0:
                    print("Невозможное значение")
                    y = int(input("Введите исходящую вершину графа: "))
                G.add_edge(x, y)
            case 'draw':
                # Отображение графа
                nx.draw(G, with_labels=True)
                plt.show()
            case 'end':
                break
            case _:
                print("Неизвестное действие")
except ValueError:
    print("Неправильное значение. Перезапуск программы...")
