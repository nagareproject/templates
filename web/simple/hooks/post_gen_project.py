import os
import sys

name = '{{ cookiecutter.project_name }}'
here = os.getcwd()

print('')
print('-' * 10)
print("Application '{}' created.\n".format(name))

print("""Note:
  1. Edit the file '{}' to set informations about your new application.
  2. Register your application with:
     - {} install -e {}
""".format(
    os.path.join(here, 'setup.py'),
    os.path.join(os.path.dirname(sys.executable), 'pip'),
    here
))

