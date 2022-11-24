Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Saisir une annee : ")
Saisir une annee : 
>>> annee=input()
2022
>>> print(annee)
2022
>>> print(annee+1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(annee+1)
TypeError: can only concatenate str (not "int") to str
>>> print(annee)+1
2022
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(annee)+1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> annee=int(annee)
>>> print(annee+1)
2023
