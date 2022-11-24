Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> jour=18
>>> mois=11
>>> annee=2022
>>> heure=8
>>> minute=57
>>> print("Depuis le début du mois il s'est écoulé {} minutes".format((jour*24+heure)*60+minutes))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Depuis le début du mois il s'est écoulé {} minutes".format((jour*24+heure)*60+minutes))
NameError: name 'minutes' is not defined. Did you mean: 'minute'?
>>> print("Depuis le début du mois il s'est écoulé {} minutes".format((jour*24+heure)*60+minute))
Depuis le début du mois il s'est écoulé 26457 minutes
