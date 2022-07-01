from setuptools import setup
from montyhallsim import __version__ as version, __author__ as author, __license__ as license_

setup(
    name='montyhallsim',
    version=version,
    url='https://github.com/mrwolferinc/montyhallsim',
    license=license_,
    author=author,
    author_email='bluewolf153622@gmail.com',
    description='A command-line interface for simulating the Monty Hall problem.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords=[
        'montyhallsim',
        'monty-hall-problem',
        'montyhallproblem',
        'monty-hall-problem-simulation',
        'monty-hall-simulation',
        'monty-hall-sim',
        'cli'
    ],
    py_modules=['montyhallsim'],
    python_requires='>=3.7',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux'
    ],
    entry_points={
        'console_scripts': [
            'montyhallsim=montyhallsim:run'
        ]
    }
)
