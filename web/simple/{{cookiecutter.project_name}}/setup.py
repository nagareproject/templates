from setuptools import setup, find_packages

VERSION = '{{ cookiecutter.version }}'


setup(
    name='{{ cookiecutter.project_name }}',
    version=VERSION,
    author='',
    author_email='',
    description='',
    license='',
    keywords='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.cfg']},
    zip_safe=False,
    install_requires=[
        'nagare>=0.6.*',
        'nagare-publishers-gunicorn',
        'nagare-sessions-memory'
    ],
    entry_points="""
    [nagare.applications]
    {{ cookiecutter.project_name }} = {{ cookiecutter.project_name }}.app:App
    """
)

