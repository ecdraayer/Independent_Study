import lace
import csv

with open('example.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list()
    for line in reader:
        data.append(line)

attribute_names = header
data_matrix = data
independent_attrs = ['ADM_RATE', 'SAT_AVG', 'TUITFTE', 'RET_FT4', 'PCTFLOAN', 'PCTPELL', 'DEBT_MDN', 'C150_4', 'CDR3']
objective_attr = 'mn_earn_wne_p7'

aftercliff = lace.cliff(attribute_names, data_matrix, independent_attrs, objective_attr, False, 0.4)
assert len(aftercliff) < 600

aftermorph = lace.morph(attribute_names, aftercliff, independent_attrs, objective_attr, False, False, 0.15, 0.35)
assert len(aftermorph)==len(aftercliff) and aftermorph[0] != aftercliff[0]


lace1res = lace.lace1(attribute_names, data_matrix, independent_attrs, objective_attr, False, 0.4, 0.15,0.35)
assert len(lace1res) < len(data)*0.5

bins = [header] + data[:50]
try2add_data_matrix = data[200:700]
bins = lace.add_to_bin(attribute_names, try2add_data_matrix, independent_attrs, objective_attr, False, 0.4, 0.15, 0.35, bins)
assert len(bins) < 550


lace2res = lace.lace2_simulator(attribute_names, data_matrix, independent_attrs, objective_attr, False, 0.4, 0.15, 0.35, number_of_holder=5)
assert len(lace2res)<len(lace1res)
print(lace2res)

