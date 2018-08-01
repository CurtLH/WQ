from setuptools import setup
import versioneer

setup(
    name='WQ',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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
    install_requires=[],
    keywords='WQ',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
