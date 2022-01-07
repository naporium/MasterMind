import random
import statistics

"""
testar "randomness" da funcao random.choice
"""


FILE = "data.txt"
NUMERO_TESTES = 100
TAMANHO_LISTA = 10000000


def write_data_on_file(file=FILE, numero_testes=NUMERO_TESTES, tamanho=TAMANHO_LISTA):

    zeros_data = []
    uns_data = []
    dois_data = []
    tres_data = []
    quatros_data = []

    for i in range(numero_testes):
        # CREATE A LIST WITH ELEMENTS
        l = (0, 1, 2, 3, 4)
        lista = []
        for j in range(0, tamanho):
            char = random.choice(l)
            lista.append(char)

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

    def write_file(f, data_to_write) -> None:
        with open(f, "at") as fstream:
            fstream.writelines("%s\n" % number for number in data_to_write)

    file_names = ("0", "1", "2", "3", "4")
    write_file(file_names[0] + file, zeros_data)
    write_file(file_names[1] + file, zeros_data)
    write_file(file_names[2] + file, zeros_data)
    write_file(file_names[3] + file, zeros_data)
    write_file(file_names[4] + file, zeros_data)


def read_data() -> None:
    file_names = ["0data.txt", "1data.txt", "2data.txt", "3data.txt", "4data.txt"]
    output_data = []
    for fn in file_names:
        print("!READING FILE", fn)
        data = []
        with open(fn, "rt") as fstream:
            while True:
                # Get next line from file
                line = fstream.readline()
                # if line is empty
                # end of file is reached

                if not line:
                    break
                line = float(line.strip())
                data.append(line)

            mean = statistics.mean(data)
            median = statistics.mean(data)
            _max = max(data)
            _min = min(data)
            output_data.append((mean, median, _max, _min))

    for index, data in enumerate(output_data):
        print("=" * 70)
        print(f"[ data {index} ]")
        print(f"mean:{data[0]}")
        print(f"median:{data[1]}")
        print(f"max:{data[2]}")
        print(f"min:{data[3]}")


# write_data_on_file()
read_data()
