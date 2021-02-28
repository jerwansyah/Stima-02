# Tugas Kecil 2 IF2211 Strategi Algoritma

## About
Program pemecah masalah _topological sort_ menggunakan algoritma _decrease and conquer_.

Algoritma _Decrease and Conquer_
> Algoritma _Decrease and Conquer_ (DnC) yang diimplementasikan untuk melakukan  _topological sort_ adalah mengurangi node dengan derajat masuk 0 dan menghapus node yang bertetangga dengan node tersebut secara rekursif hingga graf tidak memiliki node. Node hasil pengurangan bertahap dari graf merupakan hasil dari _topological sorting_ graf. Algoritma DnC yang diimplementasikan merupakan variasi DnC pengurangan dengan ukuran berubah.

Masalah yang ingin sortir haruslah berupa _Directed Acyclic Graph_ (DAG).

Tested on WSL2 (Distro: Ubuntu 20.04.1 LTS).

## Requirement
Memiliki Python3.

## Cara Menggunakan
1. Buka terminal.
2. Masukkan file yang ingin diuji ke dalam folder test.
3. Buka path folder src dan jalankan `python3 13519116.py <nama test file>` atau `./13519116.py <nama test file>`
```sh
$ cd src
$ python3 13519116.py test.txt
```
```sh
$ cd src
$ ./13519116.py test.txt
```
### Author
Jeane Mikha Erwansyah/13519116
***
