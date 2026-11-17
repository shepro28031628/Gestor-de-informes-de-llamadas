import csv

with open('g:/Unidades compartidas/Gestion de Tecnologia/Gestor de informes de Llamadas/abril.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(f"Headers: {headers}")
    for i, row in enumerate(reader):
        if '7110' in row or '7112' in row or '7114' in row:
            print(f"Row {i+2}:")
            for idx, (h, val) in enumerate(zip(headers, row)):
                if val:
                    print(f"  [{idx}] {h}: {val}")
        if i > 500: break
