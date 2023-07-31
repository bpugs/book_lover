from setuptools import setup, find_packages
setup(
    name='book_lover',
    version='1.0.0',
    url='https://github.com/bpugs/book_lover',
    author='Brendan Puglisi',
    author_email='btp6ht@virginia.edu',
    description='Contains and creates data frames for book lovers',
    packages=find_packages(),    
    install_requires=['pandas'],
)