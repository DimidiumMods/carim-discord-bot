from setuptools import setup

setup(
    install_requires=[
        'discord.py>=2.7.1',
        'requests'
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-timeout',
            'pytest-asyncio'
        ]
    }
)
