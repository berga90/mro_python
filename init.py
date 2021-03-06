#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *

#Initialisation des variables et des matrices utlisés en test 
#TODO matrice dans un fichier en lecture ? (pas ma priorité @timsade)

INF = 9999

intro = "------- MRO PYTHON ------ \n \
1 - Programmation dynamique  \n \
2 - Floyd-WHarshall\n \
3 - Méthode des potentiels \n \
4 - Johnson \n \
5 - Ford-Fulkerson\n \
6 - Procédures Branch et Bound \n \
7 - Simplexe \n \
0 - Exit\n"

num=-10

tab_floyd_cours = \
	[[INF ,  3  ,  8  ,  6  , INF , INF ],\
	[ INF , INF , INF ,  2  ,  6  , INF ],\
	[ INF , INF , INF , INF ,  1  , INF ],\
	[ INF , INF ,  2  , INF , INF ,  7  ],\
	[ INF , INF , INF , INF , INF ,  2  ],\
	[ INF , INF , INF , INF , INF , INF ]]

tab_floyd_autre = \
	[[ 0  , 5   , INF , 10 ],\
	[ INF , 0   , 3   , INF],\
	[ INF , INF , 0   , 1  ],\
	[ INF , INF , INF , 0  ]]

floyd_cours = Matrice(tab_floyd_cours)
floyd_autre = Matrice(tab_floyd_autre)

tab_johnson_cours = \
	[[5,7],\
	 [6,4],\
	 [9,8],\
	 [7,5],\
	 [8,10],\
	 [6,6],\
	 [4,3],\
	 [5,6]]

tab_johnson_autre = \
	[[50,60],\
	 [150,50],\
	 [80,150],\
	 [200,70],\
	 [30,200]]

johnson_cours = Matrice(tab_johnson_cours)
johnson_autre = Matrice(tab_johnson_autre)

tab_fulkerson_cours = \
	[[INF,35,35,40,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,20,INF,10,INF],\
	 [INF,INF,INF,INF,15,25,5,INF],\
	 [INF,INF,INF,INF,INF,20,20,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,20],\
	 [INF,INF,INF,INF,INF,INF,INF,30],\
	 [INF,INF,INF,INF,INF,INF,INF,60],\
	 [85,INF,INF,INF,INF,INF,INF,INF]]



tab_fulkerson_autre = \
	[[INF,20,15,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],\
	 [INF,INF,10,8,6,INF,INF,INF,INF,INF,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,20,INF,INF,INF,INF,INF,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,4,3,5,INF,INF,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,7,10,INF,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,4,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,2,INF,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,4,6,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,12,INF,INF,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,8,6,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,10,7,INF],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,10],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,10],\
	 [INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF]]

fulkerson_cours = Matrice(tab_fulkerson_cours)
fulkerson_autre = Matrice(tab_fulkerson_autre)

rep_mpm_cours = \
 	[[INF ,  0  ,  0  ,  0  , INF , INF , INF , INF , INF], 
	[ INF , INF , INF , INF , INF , INF ,  6  , INF , INF],
	 [INF , INF , INF , INF ,  3  ,  3  , INF , INF , INF], 
   	 [INF , INF , INF , INF , INF , INF , INF ,  6  , INF], 
	 [INF , INF , INF , INF , INF , INF ,  2  , INF , INF], 
	 [INF , INF , INF , INF , INF , INF , INF ,  4  , INF], 
	 [INF , INF , INF , INF , INF , INF , INF ,  3  , INF], 
	 [INF , INF , INF , INF , INF , INF , INF , INF ,  1 ], 
	 [INF , INF , INF , INF , INF , INF , INF , INF , INF ]]  
#        Debut,  A  ,  B  ,  C  ,  D  ,  E  ,  F  ,  G  , Fin


mpm_cours = Matrice(rep_mpm_cours)
