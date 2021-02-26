#!/usr/bin/env python3
# topo.py
# 13519116 Jeane Mikha Erwansyah

import sys

if len(sys.argv) != 2:
    exit(1)
file = sys.argv[1]

global graph;

class node:
    # Kelas node dengan atribut nama dan array node yang masuk ke node
    def __init__(self, name, in_degree):
        self.name = name
        self.in_degree = in_degree

def roman_value(num):
    # Fungsi untu mengubah angka ke angka romawi, maksimal 39
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
    graph = list();
    f = open('../test/' + file, 'r')
    for line in f:
        if line != '\n':
            line = line.replace('.','').replace('\n','').split(', ');
            graph.append(node(line[0], list(line[1:])))
    f.close()

def pop_zero_in_degree_nodes():
    # Fungsi untuk mencari (array) node dengan derajat nol
    global graph
    temp = list()
    temp1 = list()
    for node in graph:
        if len(node.in_degree) == 0:
            temp.append(node.name)
            temp1.append(node)
    for node in temp1:
        for _ in graph:
            try:
                graph.remove(node)
            except ValueError:
                continue
    for node in graph:
        for course in temp:
            try:
                node.in_degree.remove(course)
            except ValueError:
                continue
    return temp;

def toposort():
    # Fungsi untuk melakukan topological sort
    global graph
    topo_sorted = list()
    while (len(graph) > 0):
        topo_sorted.append(pop_zero_in_degree_nodes())
    return topo_sorted

def print_output(sorted_list):
    # Fungsi untuk mencetak hasil sorting
    print("Solusi dari " + file + " adalah: ")
    i = 1
    for course in sorted_list:
        print("Semester " + roman_value(i) + "\t: " + ', '.join(course), end=".\n")
        i += 1

if __name__ == '__main__':
    parsefile()
    print_output(toposort())
