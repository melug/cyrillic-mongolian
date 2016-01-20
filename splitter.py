#!/usr/bin/python
# -*- coding: utf8 -*-
import re
from alphabets import Egsh, Giig, Temd, Alph

Egsh_Pattern = re.compile(u'[{}]'.format(Egsh+Egsh.upper()), flags=re.U)
Temd_Pattern = re.compile(u'[{}]'.format(Temd+Temd.upper()), flags=re.U)
Giig_Pattern = re.compile(u'[{}]'.format(Giig+Giig.upper()), flags=re.U)
Alph_Pattern_I = re.compile(u'[{}]+'.format(Alph+Alph.upper()), flags=re.U)

def word2egi(w):
    return Temd_Pattern.sub('i', Giig_Pattern.sub('G', Egsh_Pattern.sub('E', w)))


def split(w):
    start = 0
    for text in split2(word2egi(w)):
        yield w[start:start+len(text)]
        start += len(text)


def split2(w):
    ''' G is consonant 
    E is vowel 
    i is one of "Temd"'''
    for s in re.findall(r'(G?E+Gi)|(G?E+G*\Z)|(G*E+G*(?=G))|([GEi]+\Z)', w):
        for c in s:
            if c:
                yield c

def tokenize(w):
    for s in Alph_Pattern_I.finditer(w):
        yield s.group(0)

def test1():
    tests = [
        ('GEEGE', 'GEE-GE'),
        ('GEGGEEGGEG', 'GEG-GEEG-GEG'),
        ('GEEGGEGEG', 'GEEG-GE-GEG'),
        ('GEGGEGGEGGEE', 'GEG-GEG-GEG-GEE'),
        ('GEGGGEEGEE', 'GEGG-GEE-GEE'),
        ('GEGEG', 'GE-GEG'),
        ('EGGEG', 'EG-GEG'),
        ('EGGGEG', 'EGG-GEG'),
        ('GEGEGGGGEE', 'GE-GEGGG-GEE'),
        ('GEGiE', 'GEGi-E'),
        ('EGiE', 'EGi-E'),
        ('GEGEEGiE', 'GE-GEEGi-E'),
        ('GEGiGEEGEG', 'GEGi-GEE-GEG'),
    ]
    for w, p in tests:
        j = '-'.join(split2(w))
        if p != j:
            print 'F', p, j
        else:
            print 'P', p, j

def test2():
    words = [
        [ u'мандуулсан', u'ман-дуул-сан' ],
        [ u'хойно', u'хой-но' ],
        [ u'хойшлоход', u'хойш-ло-ход' ],
        [ u'тэмдэглэгдэхдээ', u'тэм-дэг-лэг-дэх-дээ' ],
        [ u'суртлаараа', u'сурт-лаа-раа' ],
        [ u'хонь', u'хонь' ],
        [ u'морь', u'морь' ],
        [ u'голын', u'го-лын' ],
        [ u'олдох', u'ол-дох' ],
        [ u'үлдсэн', u'үлд-сэн' ],
        [ u'төрөлхтний', u'тө-рөлхт-ний' ],
        [ u'үзье', u'үзь-е' ],
        [ u'харуулъя', u'ха-руулъ-я' ]
    ]
    for w, p in words:
        j = '-'.join(split(w))
        if p == j:
            print 'P', w, j
        else:
            print 'F', w, p, j

def test3():
    sentence = u'Зарим нэр үг хоёр өөр утгыг илтгэх болоод тийн ялгалаар хувилахдаа ч ялгавартай болжээ. Жишээлбэл: Шөнө од (нэрлэхийн тийн ялгал) гялалзана. Алтан гадас одон Лувсангийн энгэр дээр гялалзана. Ард Насангийн соёолон насны морь наадамд түрүүлэв. Өвлийн эхэн сарын (харьяалах) арван тавны шөнө сарны гэрэл тооноор орно. Сард авах, цалин, саранд нисэж очих гэх мэт. Зарим үг тийн ялгалаар хоёр өөр хувирч хоёр өөр утгыг илтгэх явдал байна. Жишээлбэл: адуугаар баян нэгдэл, танай адуунаар миний морь явчлаа гэх мэт.'
    sentence2 = ' '.join([ u'-'.join(split(w)) for w in tokenize(sentence) ])
    print sentence
    print sentence2


if __name__ == '__main__':
    test1()
    test2()
    test3()

