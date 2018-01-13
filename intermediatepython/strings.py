names = ['akash', 'kanika','mahesh','malti']

for name in names :
    statement = 'Hello there '+name
    print(statement)

for name in names :
    statement = ' '.join(['Hello there',name])
    print(statement)

print(', '.join(names))

#             double back-slash for window's nonsense.
location_of_files = 'C:\\Users\\H\\Desktop\\Intermediate Python'
file_name = 'example.txt'

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

who = 'Gary'
how_many = 12

print('{} bought {} apples today!'.format(who, how_many))
