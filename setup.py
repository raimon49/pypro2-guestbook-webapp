from setuptools import setup


setup(
    name='raimon49.guestbook',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)
