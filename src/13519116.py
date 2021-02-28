#!/usr/bin/env python3
# 13519116.py
# 13519116 Jeane Mikha Erwansyah

import sys

if len(sys.argv) != 2:
    exit(1)
file = sys.argv[1]

graph = list()
answer = list()

class node:
    # Kelas node dengan atribut nama node dan array node yang masuk ke node
    def __init__(self, name, in_degree):
        self.name = name
        self.in_degree = in_degree

def roman_value(num):
    # Fungsi untuk mengubah angka ke angka romawi
    roman = ''
    if (num // 10 >= 1):
        num = num % 10
        roman += 'X'
    if (num // 9 >= 1):
        num = num % 9
        roman += 'IX'
    if (num // 5 >= 1):
        num = num % 5
        roman += 'V'
    if (num // 4 >= 1):
        num = num % 4
        roman += 'IV'
    if (num != 0 and num // 1 >= 1):
        for i in range(num):
            roman += 'I'
    return roman

def parsefile():
    # Prosedur membaca satu file
    global graph
    f = open('../test/' + file, 'r')
    for line in f:
        if line != '\n':
            line = line.replace('.','').replace('\n','').split(', ');
            graph.append(node(line[0], list(line[1:])))
    f.close()

def dnc():
    # Prosedur untuk melakukan topological sorting dengan decrease and conquer
    global graph, answer
    temp1 = list()
    temp2 = list()
    if (len(graph) != 0):
        for node in graph:
            if len(node.in_degree) == 0:
                temp1.append(node.name)
                temp2.append(node)
        answer.append(list(temp1))
        for node in temp2:
            for _ in graph:
                try:
                    graph.remove(node)
                except ValueError:
                    continue
        for node in graph:
            for course in temp1:
                try:
                    node.in_degree.remove(course)
                except ValueError:
                    continue
        dnc()

def print_output():
    # Fungsi untuk mencetak hasil sorting
    print("Solusi dari " + file + " adalah: ")
    i = 1
    for course in answer:
        print("Semester " + roman_value(i) + "\t: " + ', '.join(course), end=".\n")
        i += 1

if __name__ == '__main__':
    parsefile()
    dnc()
    print_output()
