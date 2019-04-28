from setuptools import setup


setup(
    name='deduplication',
    version='0.1',
    description='Algorithm for items(images) deduplication',
    author='Habiboulaye A.B',
    author_email='habiboulaye@gmail.com',
    packages=['algo_deduplicate'],
    install_requires=['numpy',
                      'keras',
                      'argparse']
)