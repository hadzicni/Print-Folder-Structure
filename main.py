import os

def print_directory_contents(path, indent=0):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print('    ' * indent + item) 
            print_directory_contents(full_path, indent + 1)

root_path = 'C:/Users/hadzicni/Documents/Projects'
print_directory_contents(root_path)
