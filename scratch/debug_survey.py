import csv

target_file = 'g:/Unidades compartidas/Gestion de Tecnologia/Gestor de informes de Llamadas/abril.csv'
completed_surveys_uids = set()

with open(target_file, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)
    for row in rows:
        if '7114' in row:
            completed_surveys_uids.add(row[20])

print(f"Found {len(completed_surveys_uids)} completed surveys.")

for uid in list(completed_surveys_uids)[:3]:
    print(f"\n--- Survey UID: {uid} ---")
    for row in rows:
        if row[20] == uid:
            print(f"CDR: {row[0]}, Dst: {row[5]}, App: {row[11]}, Data: {row[12]}, Duration: {row[16]}")
