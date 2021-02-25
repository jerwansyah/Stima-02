#!/usr/bin/env python3
# topo.py
# 13519116 Jeane Mikha Erwansyah

import sys

if len(sys.argv) < 1:
    exit(1)
file = sys.argv[1]

global graph;

class node:
    def __init__(self, name, in_degree):
        self.name = name
        self.in_degree = in_degree

def roman_value(num):
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
    global graph
    graph = list();
    f = open('../test/' + file, 'r')
    for line in f:
        line = line.replace(' ','').replace('.','').replace('\n','').split(',');
        graph.append(node(str(line[0]), list(line[1:])))
    f.close()

def pop_zero_in_degree_nodes():
    global graph
    temp = list()
    temp1 = list()
    for node in graph:
        if len(node.in_degree) == 0:
            temp.append(node.name)
            temp1.append(node)
    for node in temp1:
        for node2 in graph:
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
    global graph
    topo_sorted = list()
    while (len(graph) > 0):
        topo_sorted.append(pop_zero_in_degree_nodes())
    return topo_sorted

def print_output(sorted_list):
    i = 1
    for course in sorted_list:
        print("Semester " + roman_value(i) + "\t: " + ', '.join(course))
        i += 1

if __name__ == '__main__':
    parsefile()
    print_output(toposort())
