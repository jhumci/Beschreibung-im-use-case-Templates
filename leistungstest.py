from datetime import date

def create_experiments(first_experiment_id):
    try:
        first_experiment_id = int(first_experiment_id)
    except ValueError:
        print("Fehler: Die first_experiment_id muss eine ganze Zahl sein.")
        return []

    versuchsleiter = "Ihr Name"
    erstellungsdatum = date.today().isoformat()
    experimente = []

    for i in range(10):
        experiment = {
            "Id_": first_experiment_id + i,
            "Versuchsleiter": versuchsleiter,
            "Erstellungsdatum": erstellungsdatum,
            "Testname": f"Leistungstest {i+1}"
        }
        experimente.append(experiment)

    return experimente

first_experiment_id = input("Gib eine Start-ID ein: ")
experimente = create_experiments(first_experiment_id)

if experimente:
    print("\nErste fünf Experimente:")
    for experiment in experimente[:5]:
        print(experiment)

    gerade_ids = sum(1 for exp in experimente if exp["Id_"] % 2 == 0)
    print(f"\nAnzahl der Experimente mit gerader ID: {gerade_ids}")
