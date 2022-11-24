print("Veuillez saisir le jour du mois: ")
jour=int(input())
print("Veuillez saisir une heure: ")
heure=int(input())
print("Veuillez saisir les minutes: ")
minute=int(input())
total=(jour*24+heure)*60+minute
print("Depuis le début de l'année, il s'est écoulée {} minutes.".format(total)) 
