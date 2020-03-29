from pathlib import Path

# Create a directory
Path('/home/%user_name%/dir_name').mkdir(exist_ok=True)

# Delete a directory
Path('/home/%user_name%/dir_name').rmdir()

##########
# Rename files or directories
Path('old_file_name.csv').rename('new_file_name.csv')

# Get current working directory
current_dir = Path.cwd()

# Create path
file_path = Path('/home/%user_name%/dir_name/file_name.csv')

# Joining paths
dir_path = Path('/home/%user_name%/dir_name/')
join_path = dir_path / 'file_name.csv'

# Get absolute path
# current file
absolute_current_path = Path(__file__).resolve()
# selected file
absolute_selected_path = Path('file_name.csv').resolve()

# Check if path is a file
check_file = Path('/home/%user_name%/dir_name/file_name.csv').is_file()

# Check if path is a directory
check_dir = Path('/home/%user_name%/dir_name').is_dir()

# Check if a path exists
check_exists = Path('/home/%user_name%/dir_name/file_name.csv').exists()

# Get path to folder containing a file
dir_path = Path('/home/%user_name%/dir_name/file_name.csv').parent

# Get the path to the home directory
home_dir_path = Path.home()
# '/home/%user_name%'

# Get the path to the Desktop directory
desktop_path = Path('~/Desktop').expanduser()
# '/home/%user_name%/Desktop'

# Get size in bytes of a file
file_size = Path('/home/%user_name%/dir_name/file_name.csv').stat().st_size

# Get file extension
ext = Path('/home/%user_name%/dir_name/file_name.csv').suffix
# .csv

# Get file name without directory
file_name = Path('/home/%user_name%/dir_name/file_name.csv').name
# file_name.csv

# List contents of a directory
iter_dir = Path().iterdir()
print(list(iter_dir))

# Change permission of a file
Path('key.pem').chmod(0o400)

###########################################################################
# Reading a file

# В новых версиях python можно напрямую передать Path в open().
path = Path('/home/%user_name%/dir_name/') / 'file_name.csv'
with open(path) as in_f:
    data_a = in_f.read()

# В старых версиях можно преобразовать Path в str и передать в open().
path = Path('/home/%user_name%/dir_name/') / 'file_name.csv'
with open(str(path)) as in_f:
    data_b = in_f.read()
