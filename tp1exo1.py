Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nom=justin
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    nom=justin
NameError: name 'justin' is not defined
>>> nom = "justin"
>>> nom= "chaleard"
>>> prenom= "justin"
>>> 
>>> math= 9.5
>>> anglais=16
>>> info= 10
>>> promotion=2022
>>> moy=(math+anglais+info)/3
>>> print("L'étudiant {} {} de la promotion {} a une moyenne de {}".format(prenom, nom, promotion, moy))
L'étudiant justin chaleard de la promotion 2022 a une moyenne de 11.833333333333334
>>> print("L'étudiant {} {} de la promotion {} a une moyenne de {:.2f}".format(prenom, nom, promotion, moy))
L'étudiant justin chaleard de la promotion 2022 a une moyenne de 11.83
