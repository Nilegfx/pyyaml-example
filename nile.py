from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# open yaml file
file = open('data_without_hobbies.yaml', 'r')

# prepare output file
output_file = open(r'data_without_hobbies_output.yaml', 'w')

# read and parse the yaml data
data = load(file.read(), Loader=Loader)

# add hobbies if not exists
if 'hobbies' not in data:
    data['hobbies'] = ['reading', 'developing']
    print(data)

# save the newly modified yaml data to different file
dump(data, output_file)