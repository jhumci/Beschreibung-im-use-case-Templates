first_experiment_id = int(1000)
gerade_ids = 0

for id in range(10):
    exp_id = first_experiment_id + id
    print(f"Experiment ID: {exp_id}")
    
    if id < 5:
        print(f"Erstes Experiment {id + 1}: {exp_id}")
    
    if exp_id % 2 == 0:
        gerade_ids += 1

print(f"\nAnzahl der Experimente mit gerader ID: {gerade_ids}")
