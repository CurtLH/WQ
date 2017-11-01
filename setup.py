from setuptools import setup

requirements = [
python=2.7,
pytest,
pep8,
autopep8,
ipython,
click,
request
]

setup(
    name='WQ',
    version='0.1.0',
    description="Short description",
    author="Curtis Hampton",
    author_email='CurtLHampton@gmail.com',
    url='https://github.com/CurtLH/WQ',
    packages=['wq'],
    entry_points={
        'console_scripts': [
            'wq=wq.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='WQ',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
