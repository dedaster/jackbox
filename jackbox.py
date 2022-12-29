# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:54:50 2022

@author: Дедок
"""

import pandas as pd
import random

def game():
    if n <=2 or n > 100:
        print('Игроков должно быть от 3 до 100')
        print()
    else:
        num = (games['Игроки'] >= n)
        res = games.sort_values(['Игроки', 'Часть']).loc[num]
        res_l = len(res)
        res_r = random.randint(0, (res_l)-1)
        result = res.iloc[res_r]
    
        print()
        print("Всего подходящих игр: ", res_l)
        print()
        print(res)
    
        print()
        print()
        print('Случайная подходящая игра:')
        print()
        print(result)
        print()

while True:
    games = pd.read_csv('/Git/jackbox/jackbox.csv')
    games.columns = ['Часть', 'Название', 'Игроки']
    try:
        n = int(input('Введите количество игроков от 3 до 100: '))
        game()
    except ValueError:
        print('Введите число от 3 до 100')
        print()