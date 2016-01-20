#!/usr/bin/python
# -*- coding: utf8 -*-

import re
import time
from alphabets import Ereg, Emeg, Saar
from splitter import tokenize, word2egi

def word_gender_validity(w):
    ''' Rule 8, Mongolian words shouldn't be male and female at the same time. 
    Only exceptions are:
        1. Words combined
        2. Ends with double vowel
    '''
    Ms, Fs = 0, 0
    i = 0
    while i<len(w):
        c, g = word_gender2(w[i:])
        if c == -1:
            break
        i += c+1
        if g == 'M': 
            Ms += 1
        elif g == 'F':
            Fs += 1
    return Ms, Fs

def follow_up_rule(w):
    ''' Rule 9, defines suffix vowels.
    а, у        ->        а
    э, ү, и     ->        э
    о           ->        о
    ө           ->        ө
    Exceptions:
    уу, үү, юу, юү, яу, ёу, еү, иу Redefines the vowels.
    и, ий, ы, эй. These alphabets can break and get in the middle of word. 
    '''

def word_gender2(w):
    for i in range(len(w)):
        sub = w[i:].lower()
        if any([ sub.startswith(e) for e in Ereg ]):
            return i, 'M'
        if any([ sub.startswith(e) for e in Emeg+Saar ]):
            return i, 'F'
    return -1, 'X'

def word_gender(w):
    ''' returns 'M' for male, 'F' for female '''
    return word_gender2(w)[1]

def test1():
    sentence = u'Улсын Прокурорын ерөнхий газарт “Прокурорын удирдах ажилтны зөвлөгөөн” өнөөдөр эхэлж байна. Тус зөвлөгөөнөөр аймаг, сум, дүүргийн прокурорууд өнгөрсөн онд хэчнээн хэргийг, хэрхэн яаж шийдвэрлэсэн тоон мэдээллээ нэгтгэж, энэ онд ямар арга ажиллагаагаар ажиллах вэ. Цаашид прокурорын байгууллагын үйл ажиллагаа буюу прокурорын хяналт дор эрүүгийн хэрэг үүсгэгдэн шалгагдаж буй хэргийн талаарх мэдээллийг нээлттэйгээр хэрхэн олон нийтэд мэдээлэх вэ зэргээ ярилцаж, тодорхойлох юм байна. Ингэж тогтсон дүрэм, журмын дагуу мэдээллийг олон нийтэд түгээхгүй бол шүүхээр гэм буруутай нь тогтоогдоогүй, сэжигтнээр татагдан шалгагдаж буй тодорхой хүмүүсийн нэр төр, эрх чөлөөтэй амьдрахад халдах эрсдэлтэй үйл ажиллагааг прокурорын байгууллага явуулдаг гэж Улсын Прокурорын ерөнхий газрын орлогч Г.Эрдэнэбат тайлбарлалаа. Мөн ирэх есдүгээр сараас Улсын Их хурлаар шинэчлэгдэн батлагдсан Эрүүгийн хууль хэрэгжиж эхэлнэ. Үүнтэй холбоотойгоор прокурорын байгууллага цаашид гэмт хэрэгтэй тэмцэхдээ шинэ хуулийнхаа хэрэгжилтийг хэрхэн хангаж ажиллах вэ гэдгээ энэхүү удирдах ажилтны зөвлөгөөнөөрөө хэлэлцэх юм байна. Эрүүгийн хууль шинэчлэгдэн батлагдсантай холбоотойгоор прокурорын байгууллагад бүтэц, орон тооны өөрчлөлт хийх шаардлага тулгарчээ.'
    sentence2 = u'юуны юүний ишиг илүү'
    print u' '.join([ u'{}({})'.format(w, word_gender(w)) for w in tokenize(sentence) ])
    print u' '.join([ u'{}({})'.format(w, word_gender(w)) for w in tokenize(sentence2) ])
    for w in tokenize(sentence):
        print word_gender_validity(w), w
        
if __name__ == '__main__':
    test1()
    #print word_gender_validity(u'Прокурорын')
    #print word_gender_validity(u'эрдэнэбат тайлбарлалаа')
