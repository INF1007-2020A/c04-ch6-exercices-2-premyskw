#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    return dict(zip(some_list,range(len(some_list))))


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    i = 0
    couleur = []
    for i in colors:
        couleur.append((i, cnames[i]))
    return couleur


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    nombres =[]
    compteur = 0
    while not compteur >= 10000:
        if compteur < 15 or compteur > 350:
            nombres.append(compteur)
        compteur += 1           
    return nombres


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    dnn_tous, lr_tous, rf_tous = model_dict["DNN"], model_dict["LR"], model_dict["RF"]
    dnn_tou2, lr_tou2, rf_tou2 = list(zip(*dnn_tous)), list(zip(*lr_tous)), list(zip(*rf_tous))
    mse_dnn, mse_lr, mse_rf = mse(dnn_tou2), mse(lr_tou2), mse(rf_tou2)
    return {"DNN": mse_dnn, "LR": mse_lr, "RF": mse_rf}

def mse(bucke):
    attendu = 0
    calculé = 0
    n=0
    i=0
    diff_carré = 0
    différence =0
    attendu = bucke[0]
    calculé = bucke[1]
    print(attendu)
    somme = 0
    n = len(attendu)
    for i in range(0,n):
        différence = attendu[i]-calculé[i]
        diff_carré = différence**2
        sommme = somme + diff_carré
    mse1 = somme/n
    return mse1

def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
