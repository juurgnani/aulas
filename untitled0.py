# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BQcl27fXLtV7ya1tLgtign3QGrfVWE_b
"""

from sklearn.linear_model import LinearRegression

X= [[1],[2],[3],[4],[5]]
Y= [2000000,3000000, 4000000,5000000,6000000]

model = LinearRegression()

model.fit(X, Y)

num_quartos = 7
preco_previsto = model.predict([[num_quartos]])
print(f"O valor previsto para uma casa de {num_quartos} quartos é de: ${preco_previsto [0]:.2f}")