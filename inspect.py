#!/usr/bin/python
# -*- coding: utf8 -*-

import re
import time
from alphabets import Ereg, Emeg, Saar
from splitter import tokenize, split

def follow_up_char(w):
    ''' Rule 9, Defines character of suffixes or vowels.
    а, у        ->  а
    э, ү, и     ->  э
    о           ->  о
    ө           ->  ө
    Exception, following alphabets changes follow up character
    уу, үү, юу, юү, яу, ёу, еү, иу
    Following alphabets may go in the middle word but doesn't change follow up character.
    и, ий, ы, эй
    '''
    dd = {
        u'а': u'а',
        u'у': u'а',
        u'э': u'э',
        u'ү': u'э',
        u'и': u'э',
        u'о': u'о',
        u'ө': u'ө',
    }
    ee = [ u'уу', u'үү', u'юу', u'юү', u'яу', u'ёу', u'еү', u'иу' ]
    ii = [ u'и', u'ий', u'ы', u'эй' ]
    fu = None
    for u in split(w.lower()):
        found = False
        for e in ee:
            if e in u:
                fu = dd[e[-1]]
                found = True
        if not found and fu is None:
            for k in dd.keys():
                if k in u:
                    fu = dd[k]
    return fu

def gender(w):
    ''' Rule 8, Mongolian words shouldn't be male and female at the same time. 
    Only exceptions are:
        1. Words combined
        2. Ends with double vowel
    Returns general gender of the word, and number of male, female alphabets.
    '''
    Ms, Fs = 0, 0
    G = None
    i = 0
    while i<len(w):
        pw = w[i:].lower()
        c, g = gender2(pw)
        if c == -1:
            break
        i += c+1
        # if the word is already male and followed by Saar, it shouldn't count
        if G and any([ pw[c:].startswith(saar) for saar in Saar ]):
            continue
        if G is None:
            G = g
        if g == 'M': 
            Ms += 1
        elif g == 'F':
            Fs += 1
    return G, Ms, Fs

def gender2(w):
    for i in range(len(w)):
        sub = w[i:].lower()
        if any([ sub.startswith(e) for e in Ereg ]):
            return i, 'M'
        if any([ sub.startswith(e) for e in Emeg+Saar ]):
            return i, 'F'
    return -1, 'X'

def test1():
    sentence = u'Улсын Прокурорын ерөнхий газарт “Прокурорын удирдах ажилтны зөвлөгөөн” өнөөдөр эхэлж байна. Тус зөвлөгөөнөөр аймаг, сум, дүүргийн прокурорууд өнгөрсөн онд хэчнээн хэргийг, хэрхэн яаж шийдвэрлэсэн тоон мэдээллээ нэгтгэж, энэ онд ямар арга ажиллагаагаар ажиллах вэ. Цаашид прокурорын байгууллагын үйл ажиллагаа буюу прокурорын хяналт дор эрүүгийн хэрэг үүсгэгдэн шалгагдаж буй хэргийн талаарх мэдээллийг нээлттэйгээр хэрхэн олон нийтэд мэдээлэх вэ зэргээ ярилцаж, тодорхойлох юм байна. Ингэж тогтсон дүрэм, журмын дагуу мэдээллийг олон нийтэд түгээхгүй бол шүүхээр гэм буруутай нь тогтоогдоогүй, сэжигтнээр татагдан шалгагдаж буй тодорхой хүмүүсийн нэр төр, эрх чөлөөтэй амьдрахад халдах эрсдэлтэй үйл ажиллагааг прокурорын байгууллага явуулдаг гэж Улсын Прокурорын ерөнхий газрын орлогч Г.Эрдэнэбат тайлбарлалаа. Мөн ирэх есдүгээр сараас Улсын Их хурлаар шинэчлэгдэн батлагдсан Эрүүгийн хууль хэрэгжиж эхэлнэ. Үүнтэй холбоотойгоор прокурорын байгууллага цаашид гэмт хэрэгтэй тэмцэхдээ шинэ хуулийнхаа хэрэгжилтийг хэрхэн хангаж ажиллах вэ гэдгээ энэхүү удирдах ажилтны зөвлөгөөнөөрөө хэлэлцэх юм байна. Эрүүгийн хууль шинэчлэгдэн батлагдсантай холбоотойгоор прокурорын байгууллагад бүтэц, орон тооны өөрчлөлт хийх шаардлага тулгарчээ.'
    sentence2 = u'юуны юүний ишиг илүү'
    for w in tokenize(sentence):
        print gender(w), w
    for w in tokenize(sentence):
        print follow_up_char(w), w

def test2():
    words = [
        [ u'авдартай', u'а' ],
        [ u'уламжлахад', u'а' ],
        [ u'хамгаалахаараа', u'а' ],
        [ u'уулзвар', u'а' ],
        [ u'эрдэм', u'э' ],
        [ u'үзэгдэхэд', u'э' ],
        [ u'жинхэнэ', u'э' ],
        [ u'онгоцоор', u'о' ],
        [ u'оролцоход', u'о' ],
        [ u'мөнгө', u'ө' ],
        [ u'өргөдөл', u'ө' ],
        [ u'ёндон', u'о' ],
        [ u'олъё', u'о' ],
        [ u'уралдаантайгаар', u'а' ],
        [ u'үдэшлэгтэй', u'э' ],
        [ u'инээдэм', u'э' ],
        [ u'уяатай', u'а' ],
        [ u'орчуулагч', u'а' ],
        [ u'өрнүүлсэн', u'э' ],
        [ u'оёулахдаа', u'а' ],
        [ u'үеүдэд', u'э' ],
        [ u'хориулан', u'а' ],
        [ u'ажиллах', u'а' ],
        [ u'хөгжилдөнө', u'ө' ],
        [ u'онийсон', u'о' ],
        [ u'нөхөдтэйгөө', u'ө' ],
        [ u'өвстэйхөн', u'ө' ],
        [ u'доёийсон', u'о' ],
        [ u'тулга', u'а' ],
        [ u'эрдэнэзул', u'а' ],
    ]
    for w, f in words:
        fuc = follow_up_char(w)
        if fuc != f:
            print 'F', w, fuc, f
        if fuc == f:
            print 'P', w, fuc, f
        
if __name__ == '__main__':
    test1()
    test2()
