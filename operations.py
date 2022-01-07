from enum import Enum
from Color import bold
from json import dumps


class Color(Enum):
    """
    Estrutura para cores
    """
    RED = "R"
    GREEN = "G"
    BLUE = "B"
    YELLOW = "Y"
    MAGENTA = "M"


def get_number_of_colors_in_common(_sc, _user_colors):
    """
        Conta o numero de vezes que uma cor aparece numa lista com elementos do tipo <Color>

    :param _sc: <list> lista de cores : enumerator Color
    :param _user_colors: <list> lista de cores : enumerator Color
    :return: <tuple> dois dicionários com o numero de vezes que uma cor se repete
    """

    tabela_cores_secret = {
        f"{str(Color.RED)}": _sc.count(Color.RED),
        f"{str(Color.GREEN)}": _sc.count(Color.GREEN),
        f"{str(Color.BLUE)}": _sc.count(Color.BLUE),
        f"{str(Color.YELLOW)}": _sc.count(Color.YELLOW),
        f"{str(Color.MAGENTA)}": _sc.count(Color.MAGENTA),
    }
    tabela_cores_utilizador = {
        str(Color.RED): _user_colors.count(Color.RED),
        str(Color.GREEN): _user_colors.count(Color.GREEN),
        str(Color.BLUE): _user_colors.count(Color.BLUE),
        str(Color.YELLOW): _user_colors.count(Color.YELLOW),
        str(Color.MAGENTA): _user_colors.count(Color.MAGENTA),
    }

    # print(f"tabela_cores_secret: {dumps(tabela_cores_secret, indent=4)}")
    # print(f"tabela_cores_utilizador: {dumps(tabela_cores_utilizador, indent=4)}")

    return tabela_cores_utilizador, tabela_cores_secret


def validate(sc, user_colors):
    """
    esta funcao devolve as "dicas" para as cores.
    O numero de cores certas no sitio certo, comparando a chave escolhida
     pelo utilizador e a chave secreta, e o numero de cores certas mas no local errado
    :param sc: <list> chave secreta com 4 cores: type <Color enum>
    :param user_colors: <list>  cores escolhida pelo utilizador 4 cores: type <Color enum>
    :return: <tuple> tuple com dois inteiros
    """

    # print(bold(f"         sc: {sc}"))
    # print(bold(f"user_colors: {user_colors}"))
    correct_color_correct_position = 0
    correct_color_different_position = 0

    # create at temporary copy , of the secret color list
    tmp_sc_list = sc.copy()
    tmp_user_color_list = user_colors.copy()

    for index, secret_color in enumerate(sc):
        if user_colors[index] == sc[index]:
            # delete item in tmp lists
            del tmp_sc_list[index - correct_color_correct_position]
            del tmp_user_color_list[index - correct_color_correct_position]
            # Increment counter
            correct_color_correct_position = correct_color_correct_position + 1

    # print(f"tmp_sc_list: {tmp_sc_list}")
    # print(f"tmp_user_color_list: {tmp_user_color_list}")
    table_user_colors, table_sc = get_number_of_colors_in_common(tmp_sc_list, tmp_user_color_list)
    # print(f"table_sc: {table_sc}")
    # print(f"table_user_colors: {table_user_colors}")

    # COUNT THE NUMBER OF COLORS THAT ARE CORRECT BUT IN DIFFERENT POSITIONS
    counter = 0
    counter1 = 0
    counter2 = 0
    for color in Color:
        if table_sc[str(color)] >= 1 and table_user_colors[str(color)] >= 1:
            # CASO tabela 1 == tabela 2
            if table_sc[str(color)] == table_user_colors[str(color)]:
                correct_color_different_position = correct_color_different_position + table_sc[str(color)]
                counter = counter + 1
            # CASO (tabela 2 > tabela 1) &  tabela2 >= 1
            if table_user_colors[str(color)] > table_sc[str(color)]  and table_user_colors[str(color)] >= 1:
                correct_color_different_position = correct_color_different_position + table_sc[str(color)]
                counter1 = counter1 + 1
            # CASO (tabela 2 < tabela 1) & tabela2 > 1
            if table_user_colors[str(color)] < table_sc[str(color)] and table_user_colors[str(color)] >= 1:
                correct_color_different_position = correct_color_different_position + table_user_colors[str(color)]
                counter2 = counter2 + 1

    # print(f"counter: {counter}")
    # print(f"counter1: {counter1}")
    # print(f"counte2: {counter2}")
    # print(bold(f"S: {sc}"))
    # print(bold(f"U: {user_colors}"))
    # print(f"correct_color_correct_position {correct_color_correct_position}")
    # print(f"correct_color_different_position: {correct_color_different_position} ")
    # print("-------------------------------------------------")
    return correct_color_correct_position, correct_color_different_position
