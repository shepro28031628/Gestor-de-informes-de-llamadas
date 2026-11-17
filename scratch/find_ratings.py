import csv

target_file = 'g:/Unidades compartidas/Gestion de Tecnologia/Gestor de informes de Llamadas/abril.csv'
uids_with_7114 = set()

with open(target_file, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)
    for row in rows:
        if row[5] == '7114' or row[22] == '7114':
            uids_with_7114.add(row[20])

print(f"Found {len(uids_with_7114)} UIDs that reached 7114.")

for uid in uids_with_7114:
    print(f"\n--- UID: {uid} ---")
    for row in rows:
        if row[20] == uid:
            # Print columns that might contain the rating
            # Checking Dst, Accountcode, Data, and maybe some others at the end
            print(f"Dst: {row[5]}, Data: {row[12]}, Acc: {row[1]}, Ext: {row[22]}, Agent: {row[24]}")
