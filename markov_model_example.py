#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import defaultdict

# Länge der verwendeten N-Gramme
L = 3


ngramfreq = {("das", "rote", "buch"): 5,
             ("dieses", "rote", "buch"): 2,
             ("gute", "rote", "buch"): 4,
             ("das", "gelbe", "buch"): 1,
             ("das", "rote", "kleid"): 2,
             ("dieses", "rote", "kleid"): 2,
             ("das", "rote", "haus"): 8, }

kneser = True

# Wahrscheinlichkeiten für alle NGramm-Längen berechnen
prob = {}
n = L
for i in range(L):
    print("................")

    print("ngram", n)
    print("ngramfreq")
    for ngram, freq in ngramfreq.items():
        print(ngram, freq)
    n = n - 1

    # Berechnung des Discounts
    N1 = sum(1 for v in ngramfreq.values() if v == 1)
    N2 = sum(1 for v in ngramfreq.values() if v == 2)

    if N1 <= 0:
        N1 = 1
    if True: #N1 > 100:
        discount = N1 / (N1 + (2.0 * N2))
    else:
        # Defaultwert für den Discount verwenden, falls die Zahl
        # der einmal aufgetretenen N-Gramme zu klein ist.
        discount = 0.5

    print("\nN1", N1)
    print("N2", N2)
    print("discount", discount)

    # Berechnung aller Kontexthäufigkeiten
    contextfreq = defaultdict(int)
    for ngram, freq in ngramfreq.items():
        context = ngram[:-1]
        contextfreq[context] += freq

    print("\ncontextfreq")
    for context, f in contextfreq.items():
        print(context, f)

    # Berechnung der relativen Häufigkeiten mit Discount
    for ngram, f in ngramfreq.items():
        context = ngram[:-1]
        prob[ngram] = (ngramfreq[ngram] - discount) / contextfreq[context]

    # Berechnung der N-1Gramm-Häufigkeiten
    sngramfreq = defaultdict(int)
    for ngram, freq in ngramfreq.items():

        if kneser:
            sngramfreq[ngram[1:]] += 1
        else:
            sngramfreq[ngram[1:]] += freq
    ngramfreq = sngramfreq


print("prob")
for ngram, prob in prob.items():
    print(ngram, prob)



