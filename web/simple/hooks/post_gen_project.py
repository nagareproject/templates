import os
import sys

name = '{{context.project_name}}'
cur_dir = '{{context._cur_dir}}'
output_dir = '{{context._output_dir}}'

setup_py = os.path.join(output_dir, name, 'setup.py')
if '..' not in os.path.relpath(setup_py, cur_dir):
    setup_py = os.path.relpath(setup_py, cur_dir)

directory = os.path.join(output_dir, name)
if '..' not in os.path.relpath(directory, cur_dir):
    directory = os.path.relpath(directory, cur_dir)

print()
print('-' * 10)
print("Application '{}' created.\n".format(name))

print(
    """Note:
  1. Edit the file '{}' to set informations about your new application.
  2. Register your application with:
     - {} install -e {}
""".format(
        setup_py, os.path.join(os.path.dirname(sys.executable), 'pip'), directory
    )
)
