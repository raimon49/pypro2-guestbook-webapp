import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup(
    name='raimon49.guestbook',
    version='1.1.1',
    description='A guestbook web application.',
    long_description=read_file('README.rst'),
    author='raimon49',
    author_email='raimon49@hotmail.com',
    url='https://github.com/raimon49/pypro2-guestbook-webapp',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords=['web', 'guestbook'],
    license='BSD License',
    install_requires=[
        'Flask',
        'bpmappers',
    ],
    entry_points="""
        [console_scripts]
        guestbook = guestbook:main
    """
)
