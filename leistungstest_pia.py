import datetime

#Als Erstes: Definition der Fahrradergometer Experiment und der ID
#Schleife für ID mit try and except
#2.Dictionarie mit
# - Versuchsleiterin
# - Erstellungsdatum
# - ID_Nummer -> muss sich um 1 Erhöhen

def fahrradergometer_experiment(first_experiment_ID):
    try:
        first_experiment_ID : int(first_experiment_ID)
    except ValueError:
        print("Nur ganze Zahlen erlaubt")
        return[]

#Erstellen einer Liste von Experimenten
    experiment_list = []
    today = datetime.date.today()

#1.Schleife -> 10 Experimente, Versuchsleiterin, Erstellungsdatum, ID_Nummer
    for i in range(11):
        experiment = {
            "Versuchsleiterin": "Pia Schratt",
            "Erstellungsdatum": today,
            "ID_Nummer": first_experiment_ID + i  # Erhöhung der ID um 1
        }
        experiment_list.append(experiment)  # Experiment zur Liste hinzufügen
    return experiment_list  # Rückgabe der Liste
#print(experiment_list)

#Aufruf und Speicherung
experiment_list = fahrradergometer_experiment(1)

# 2.Schleife
# -> die ersten 5 Experimente anzeigen
def Auswertung_experiment(experiment_list):
    for i in range(min(5, len(experiment_list))):
        print(experiment_list[i])

even_count = sum(1 for exp in experiment_list if exp["ID_Nummer"] % 2 == 0)
print("Anzahl der Experimente mit gerader ID:", even_count)
