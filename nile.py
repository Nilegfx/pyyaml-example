from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

file = open('data_without_hobbies.yaml', 'r')
output_file = open(r'data_without_hobbies_output.yaml', 'w')
# file = open('data.yaml', 'r')
data = load(file.read(), Loader=Loader)

if 'hobbies' not in data:
    data['hobbies'] = ['reading', 'developing']
    print(data)

output = dump(data, output_file)