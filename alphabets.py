#!/usr/bin/python
# -*- coding: utf8 -*-

# ҮСГИЙН ТОДОРХОЙЛОЛТ

# Үндсэн эгшиг
Avia = u'аэиоуөү'
# Туслах эгшиг
Tusl = u'яеёюйы'
# Эгшиг үсэг
Egsh = Avia + Tusl
Egsh_Giig = u'мнглбвр'
Zari_Giig = u'цжзсдтшчх'
Onts_Giig = u'кфпщ'
# Гийгүүлэгч авиа
Giig = Egsh_Giig + Zari_Giig + Onts_Giig
# Тэмдэг үсэг
Temd = u'ъь'
Alph = Egsh+Giig+Temd

# ЭГШГИЙН ТОДОРХОЙЛОЛТ

# Урт эгшиг
Urte = [ c*2 for c in Avia if c != u'и' ] + \
        [ u'яа', u'яу', u'еэ', u'еү', u'еө', u'ёо', u'ёу', u'юу', u'юү' ] + \
        [ u'иа', u'ио', u'иу' ] + \
        [ u'ы', u'ий' ]
# Хос эгшиг
Hose = [ c+u'й'for c in Avia if c not in [ u'и', u'ө' ]] + \
        [ u'уа', u'ау' ]

# Эр эгшиг
Ereg = [u'а', u'о', u'у', u'ё', u'юу']
# Эм эгшиг
Emeg = [u'э', u'ө', u'ү', u'е', u'юү']
# Саармаг эгшиг
Saar = [u'и', u'й']

