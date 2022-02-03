import random
import statistics
from os import path, getcwd
import matplotlib.pyplot as plt
from Profiler import profiler
import numpy as np
import math
"""
testar "randomness" da funcao random.choice
"""


FILE = "data.txt"
NUMERO_TESTES = 100
TAMANHO_LISTA = 10000


def write_file(f, data_to_write) -> None:
    with open(f, "at") as fstream:
        #fstream.writelines("%s\n" % number for number in data_to_write)
        fstream.writelines(f"{data_to_write}\n")


def write_data_on_file(file=FILE, numero_testes=NUMERO_TESTES, tamanho=TAMANHO_LISTA):

    zeros_data = []
    uns_data = []
    dois_data = []
    tres_data = []
    quatros_data = []

    count_data_lst = [] # list to store counting
    for i in range(numero_testes):
        # CREATE A LIST WITH ELEMENTS
        l = (0, 1, 2, 3, 4)
        lista = []
        for j in range(0, tamanho):
            char = random.choice(l)
            lista.append(char)

        # #
        # COUNT FREQUENCY
        zeros = lista.count(0)
        uns = lista.count(1)
        dois = lista.count(2)
        tres = lista.count(3)
        quatros = lista.count(4)

        zeros_data.append(zeros)
        uns_data.append(uns)
        dois_data.append(dois)
        tres_data.append(tres)
        quatros_data.append(quatros)

        # count_data_lst.append(zeros_data, uns_data, dois_data, tres_data, quatros_data)
        def get_file_names(f):
            file_names_numbers = ("0", "1", "2", "3", "4")
            files_names = []
            script_basedir = path.abspath(path.dirname(__file__))  # script is running in this path
            for _number in file_names_numbers:
                fn = _number + f
                file_name = path.join(script_basedir, fn)
                files_names.append(file_name)
                fn = ""
                file_name= ""
            return files_names
        f_names = get_file_names(file)
        write_file(f_names[0], zeros)
        write_file(f_names[1], uns)
        write_file(f_names[2], dois)
        write_file(f_names[3], tres)
        write_file(f_names[4], quatros)


def read_data() -> None:
    file_names = ["0data.txt", "1data.txt", "2data.txt", "3data.txt", "4data.txt"]
    output_data = []
    for fn in file_names:
        print("!READING FILE", fn)
        script_basedir = path.abspath(path.dirname(__file__))  # script is running in this path

        file_name = path.join(script_basedir, fn)
        print(script_basedir)
        data = []
        with open(file_name, "rt") as fstream:
            while True:
                # Get next line from file
                line = fstream.readline()
                # if line is empty
                # end of file is reached

                if not line:
                    break
                line = float(line.strip())
                data.append(float(line))
            # TODO
            # CALL HERE
            mean = statistics.mean(data)
            median = statistics.mean(data)
            _max = max(data)
            _min = min(data)
            output_data.append((mean, median, _max, _min))

    for index, data in enumerate(output_data):

        print(f"[ data {index} ]")
        print(f"mean:{data[0]}")
        print(f"median:{data[1]}")
        print(f"max:{data[2]}")
        print(f"min:{data[3]}")
        print("=" * 70)



# write_data_on_file()
# read_data()




def read_data1() -> None:
    file_names = ["0data.txt", "1data.txt", "2data.txt", "3data.txt", "4data.txt"]
    output_data = []
    for fn in file_names:
        print("!READING FILE", fn)
        script_basedir = path.abspath(path.dirname(__file__))  # script is running in this path

        file_name = path.join(script_basedir, fn)
        print(script_basedir)
        data = []
        with open(file_name, "rt") as fstream:
            while True:
                # Get next line from file
                line = fstream.readline()
                # if line is empty
                # end of file is reached

                if not line:
                    break
                line = float(line.strip())
                data.append(int(line))
            # TODO
            # CALL HERE
            mean = statistics.mean(data)
            median = statistics.mean(data)
            _max = max(data)
            _min = min(data)
            output_data.append((data, mean, median, _max, _min))

    return output_data




def desenha_grafico_contagem(t=NUMERO_TESTES):
    # https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
    result = read_data1()
    # print(result)
    contagem_zeros_lst = result[0][0]
    contagem_uns_lst = result[1][0]
    contagem_dois_lst = result[2][0]
    contagem_tres_lst = result[3][0]
    contagem_quatro_lst = result[4][0]
    x = [n for n in range(1, t + 1)]
    plt.title("Contagem de zeros, uns, dois, tres, quatro")
    plt.ylabel("Contagem")

    plt.plot(x, contagem_zeros_lst, label="zero")
    plt.plot(x, contagem_uns_lst, label="uns")
    plt.plot(x, contagem_dois_lst, label="dois")
    plt.plot(x, contagem_tres_lst, label="tres")
    plt.plot(x, contagem_quatro_lst, label="quatro")
    plt.legend(loc=2)
    plt.show()
    script_basedir = path.abspath(path.dirname(__file__))  # script is running in this path
    file_name = path.join(script_basedir, "graph1.png")
    print(file_name)
    plt.savefig(file_name)

    # TODO: change code below. this is not wright!!
    # data = (contagem_zeros_lst, contagem_uns_lst, contagem_dois_lst,
    #         contagem_tres_lst, contagem_quatro_lst)
    # for index, element in enumerate(data):
    #     mean = statistics.mean(data[index])
    #     median = statistics.mean(data[index])
    #     _max = max(data[index])
    #     _min = min(data[index])
    #     print(f"mean:{mean}")
    #     print(f"median:{median}")
    #     print(f"max:{_max}")
    #     print(f"min:{_min}")
    #     print("=" * 70)
    #
    #
    # # A custom function to calculate
    # # probability distribution function
    # def pdf(x):
    #     mean = np.mean(x)
    #     print("..........")
    #     print(f"mean {mean}")
    #     std = np.std(x)
    #     y_out = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std ** 2))
    #     return y_out
    #
    # for index, element in enumerate(data):
    #     x = np.array(data[index])
    #     y = pdf(x)
    #     # Plotting the bell-shaped curve
    #     plt.style.use('seaborn')
    #     plt.figure(figsize=(12, 12))
    #     plt.plot(x, y, color='black',
    #              linestyle='dashed')
    #
    #     plt.scatter(x, y, marker='o', s=25, color='red')
    #     plt.show()


# write_data_on_file()
desenha_grafico_contagem(NUMERO_TESTES)

