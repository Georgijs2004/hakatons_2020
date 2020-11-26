import csv



def read_cell(x, y):
    with open('ispv_pasvaldibas_iedzivotaju_skaits_20200701.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1


print('Rēzeknes novads: ', read_cell(5, 8))
print('Ventspils novads: ', read_cell(5, 11))
print('Madonas novads: ', read_cell(5, 80))
print('Daugavpils novads: ', read_cell(5, 46))
print('Gulbenes novads: ', read_cell(5, 54))
print('Talsu novads: ', read_cell(5, 118))
print('Kuldīgas novads: ', read_cell(5, 71))
print('Alūksnes novads: ', read_cell(5, 28))
print('Saldus novads: ', read_cell(5, 109))
print('Jelgavas novads: ', read_cell(5, 62))
print('Rīgas novads: ', read_cell(5, 9))
print('Jūrmalas novads: ', read_cell(5, 6))