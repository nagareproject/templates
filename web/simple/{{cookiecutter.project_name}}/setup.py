from setuptools import setup, find_packages

VERSION = '{{context.version}}'


setup(
    name='{{context.__project_slug}}',
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
    install_requires=['nagare>=0.6b2', 'nagare-publishers-gunicorn', 'nagare-sessions-memory'],
    extras_require={'dev': ['nagare-services-reloader']},
    entry_points="""
    [nagare.applications]
    {{context.__project_slug}} = {{context.__project_slug}}.app:App
    """,
)
