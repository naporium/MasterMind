# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from time import sleep
from os import system
from enum import Enum
import random
import itertools

from Color.color import blue, red, yellow, green, magenta, bold
from operations import Color
from operations import validate

# # import menus as mn


# DEFAULT
NUMBER_OF_PLAYS = 10


def get_secret():
    """
    Cria uma lista com 4 elementos do tipo <Color>
    :return: <list>
    """
    # leque de cores disponiveis para o jogo
    colors = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.MAGENTA)

    # conjunto com todas as combinacoes possiveis
    color_set = []  # 635 combinacoes possivies
    for nota_tuple in itertools.product(colors, repeat=4):
        color_set.append(nota_tuple)   # todos os conjuntos <-- 625

    # escolher uma combinaçao de cores, dentro do conjunto das 625 possibilidades
    secret_combination = random.choice(color_set)
    # print(secret_combination)
    return secret_combination


def user_color_input():
    """
    Esta funcao devolve a cor escolhida pelo utilizador, depois de mostrada no ecra as possibilidades

    :return: <enum 'Color'> , caso seja uma cor valida.
    <int> -1 , caso a letra escolhida nao corresponda a uma cor Valida
    """

    user_input = input(f"ESCOLHE UMA COR POSSIVEL: "
                       f"{red('R')}\t  {green('G')}\t {yellow('Y')}\t {blue('B')}\t {magenta('M')}\t "
                       f"\t->")
    if user_input == "r" or user_input == "R":
        return Color.RED
    elif user_input == "g" or user_input == "G":
        return Color.GREEN
    elif user_input == "y" or user_input == "Y":
        return Color.YELLOW
    elif user_input == "b" or user_input == "B":
        return Color.BLUE
    elif user_input == "m" or user_input == "M":
        return Color.MAGENTA
    else:
        return -1


def user_play():
    """
    Esta funcoo e responsável por obter 4 inputs válidos de um utilizador.
    Devolve uma lista de 4 elementos.
    Cada elemento, pertence ao tipo <enum Color>
    :return: <list>
    """
    _user_colors = []
    while len(_user_colors) < 4:
        # print(len(user_colors))
        # print(user_colors)
        user_color_ = user_color_input()
        if user_color_ == -1:
            continue
        else:
            _user_colors.append(user_color_)
    return _user_colors


def get_printy_color_message(color):
    """
    Esta funcao devolve uma letra 'Colorida' com base no valor de entrada 'color'
    :param color: <enum Color>
    :return: <str> Uma letra "colorida".
    """
    if color.value == "R":
        return red("R")
    if color.value == "G":
        return green("G")
    if color.value == "B":
        return blue("B")
    if color.value == "Y":
        return yellow("Y")
    if color.value == "M":
        return magenta("M")


def show_user_plays(user_pl):
    """
    Esta funcao mostra o tabuleiro no ecra.

    :param user_pl: <list> Lista com jogadas. Cada item da lista contem um 3 elementos:
        elemento1: <int> numero da jogada jogada.
        elemento2: <list> lista com 4 cores (elementos do tipo <enum Color>)
        elemento3: <tuple> tuple com dois inteiros: (Cor_correcta_posicao_correcta, cor_correct_posicao_errada)

    :return: <None>
    """
    # print(user_plays)
    # print(user_pl)

    # MOSTRAR NO ECRA O HEADER DO TABULEIRO
    # (A ideia é a estrutura para o tabuleiro ser composta de 3 colunas)
    coluna1 = "JOGADA NO"
    coluna2 = "JOGADAS"
    coluna3 = "RESULTADO"
    message_template = f"{coluna1:<20} {coluna2:<45} {coluna3:<30}"
    print()
    print("-" * 100)
    print(" " * 40, end="")
    print("TABULEIRO", end="")
    print(" " * 40)

    print("-" * 100)
    print(message_template)

    # PERCORRER A LISTA DE JOGADAS E POR CADA JOGADA, APRESENTA LA NO ECRA
    for play in user_pl:
        print("-" * 100)
        # print(play)

        # OBTER OS VALORES EM CADA ITEM DO LISTA DE MENSAGENS
        user_color_play = play[0]
        sugestion_tip = play[1]
        play_number = play[2]
        # print(f"JOGADA NUMERO: {play_number}")
        # print(f"JOGADA: {user_color_play}")
        # print(f"TIP: {sugestion_tip}")

        # CONTRUIR MENSAGEM PARA COLUNA 1.
        pretty_collor_elements = []
        for color in user_color_play:
            pretty_collor = get_printy_color_message(color)
            pretty_collor_elements.append(pretty_collor)
        column1_message = f"{pretty_collor_elements[0]}\t {pretty_collor_elements[1]}\t " \
                          f"{pretty_collor_elements[2]}\t {pretty_collor_elements[3]}\t "

        # CONTRUIR MENSAGEM PARA COLUNA 2.
        columns2_message = f"\t\tCCLC: {sugestion_tip[0]} CCLE: {sugestion_tip[1]}"

        # CONTRUIR A MENSAGEM FINAL PARA A JOGADA DO LOOP
        message_template = f"# {play_number:<20} {column1_message:<45} {columns2_message:<30}"
        print(message_template)
        print()


def is_win(_sc_k, user_guess):
    """
    validar se a escolha feita pelo jogador é igual ao combinacao segredo.

    :param _sc_k: <list> game secret combination
    :param user_guess: <list> user combination
    :return:<boolean> True if are equal, False otherwise
    """
    if _sc_k[0] == user_guess[0] and _sc_k[1] == user_guess[1] and \
            _sc_k[2] == user_guess[2] and _sc_k[3] == user_guess[3]:
        return True
    else:
        return False


def final_message():
    # TODO list:
    print("TODO:"
          "\n BUILD MENU, with options."
          "\n Show statistics."
          "\n Computer guesses ... game")


def main():
    global NUMBER_OF_PLAYS
    NUMBER_OF_PLAYS = 10
    current_play = 1

    # OBTER A CHAVE SECRETA DE CORES
    secret_combination = get_secret()
    secret_combination = [Color.BLUE, Color.GREEN, Color.BLUE, Color.YELLOW]
    # TO USE A PRE DETERMINED SECRET COLOR LIST

    system("clear")

    # MOSTRAR NO INICIO A Combinacao secreta
    print("Secret Combination", secret_combination)

    print(bold("Vamos comecar o jogo:"))
    print()

    sleep(2)
    system("clear")

    user_plays_list = []
    #  esta variavel recebe um tuple com (numero_da jogada,  a lista de cores escolhida pelo utilizador, tips)

    # Vamos continuar a jogar enquanto a
    # jogada actual for menor ou igual que o numero maximo de tentativas
    while current_play <= NUMBER_OF_PLAYS:
        print(bold("ESCOLHER UMA COR DE CADA VEZ, ATE AO MAXIMO DE 4. "))
        _user_colors = user_play()
        # print("user_colors", user_colors)

        # TESTAR SE AS CORES ESCOLHIDAS CORRESPONDEM A UMA CHAVE VICTORIOSA
        if is_win(_sc_k=secret_combination, user_guess=_user_colors) is True:
            # system("clear")
            print("ACERTASTE!!!")
            final_message()
            sys.exit(0)

        else:
            system("clear")
            print(f"NAO FOI DESTA. TENS {NUMBER_OF_PLAYS - current_play} TENTATIVAS.")

            # OBTER A RESPOSTA À JOGADA:
            # dois inteiros <- NUMERO_Cores_correct_LOCAL_CERTO, NUMERO_CORES_CORRECTAS_LOCAL_ERRADO
            dark_pink_tip, pink_tip = validate(sc=list(secret_combination), user_colors=_user_colors)

            print(f"NUMERO CORES CORRECTAS, POSICAO CORRECT: {dark_pink_tip}")
            print(f"NUMERO DE CORES CORRECTAS, POSICOES DIFERENTES: {pink_tip}")

        # ADICIONAR JOGADA ACTUAL , a lista de jogadas
        user_plays_list.append((_user_colors, (dark_pink_tip, pink_tip), current_play))
        sleep(3)

        # ACTUALIZAR CONTADOR DE JOGADAS
        current_play += 1

        # MOSTRAR JOGADAS (TABULEIRO )
        show_user_plays(user_pl=user_plays_list)

    final_message()

if __name__ == '__main__':
    system("clear")
    main()
