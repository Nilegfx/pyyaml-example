from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# open yaml file
file = open('data.yaml', 'r')

# prepare output file
output_file = open('data_modified.yaml', 'w')

# read and parse the yaml data
data = load(file.read(), Loader=Loader)

# add hobbies if not exists
if 'hobbies' not in data:
    data['hobbies'] = ['reading', 'developing']
    print(data)

# add a friend if it is not already there
if 'friends' in data:
    if 'ahmed' not in data['friends']: 
        data['friends'].append('ahmed')

# save the newly modified yaml data to different file
dump(data, output_file)
