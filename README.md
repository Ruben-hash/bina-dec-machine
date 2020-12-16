# bina-dec-machine
homework school on a binary machine


Basics Converter decimal -> binary 
                 binary -> decimal
              
    
requirement: using list and loop for i in ...

1. Calcule les entiers dont l’écriture binaire est donnée ci-dessous. Tu peux le faire à la main ou
t’aider de Python. Par exemple 1.0.0.1.1 vaut 2
4
+2
1
+2
0=19 ce que confirme la commande
0b10011 qui renvoie 19.
• 1.1, 1.0.1, 1.0.0.1, 1.1.1.1
• 1.0.0.0.0, 1.0.1.0.1, 1.1.1.1.1
• 1.0.1.1.0.0, 1.0.0.0.1.1
• 1.1.1.0.0.1.0.1
2. Écris une fonction binaire_vers_entier(liste_binaire) qui à partir d’une liste représentant
l’écriture binaire calcule l’entier correspondant.
En Entrée : une liste de bits 0 et 1
En Sortie : l’entier dont l’écriture binaire est la liste.
Exemples :
• entrée [1,1,0], sortie 6
• entrée [1,1,0,1,1,1], sortie 55
• entrée [1,1,0,1,0,0,1,1,0,1,1,1], sortie 3383
Première NSI novembre 2020
3. Voici un algorithme qui effectue le même travail : il permet le calcul de l’entier à partir de
l’écriture binaire, mais il a l’avantage de ne jamais calculer directement des puissances de 2.
Programme cet algorithme en une fonction binaire_vers_entier_bis() qui a les mêmes
caractéristiques que la fonction précédente.
Exercice n°9 :
Objectifs : trouver l’écriture binaire d’un entier.
1. Calcule à la main l’écriture binaire des entiers suivants. Vérifie tes résultats à l’aide de la
fonction bin() de Python.
• 13, 18, 29, 31,
• 44, 48, 63, 64,
• 100, 135, 239, 1023.
2. Programme l’algorithme suivant en une fonction entier_vers_binaire().
Exemple : si l’entrée est 204, la sortie est [1,1,0,0,1,1,0,0].
Vérifie que tes fonctions marchent bien :
• pars d’un entier n,
• calcule son écriture binaire,
• calcule l’entier associé à cette écriture,
• tu dois retrouver l’entier de départ !
