import pydash
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

# 1. add hobbies if not exists
if 'hobbies' not in data:
    data['hobbies'] = ['reading', 'developing']
    # print(data)

# 2. add a friend if it is not already there
if 'friends' in data:
    if 'ahmed' not in data['friends']: 
        data['friends'].append('ahmed')


# 3. deep nested list
# get the list if exsists, default it to empty list if it 
# doesn't exist, read docs here: http://bit.ly/2SEF6HX
children_names = pydash.get(data, 'parent.child.names', [])

# the following like assumes that `parent.child.names` is either
# a list or None, otherwise you will get an error if you tried to 
# append a value to none-list type.
children_names.append('lolo')

# set the newly modifed list of names
pydash.set_(data,  'parent.child.names', children_names)

# save the newly modified yaml data to different file
dump(data, output_file)
