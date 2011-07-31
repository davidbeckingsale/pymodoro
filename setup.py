try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'description': 'Pymodoro - Pomodoro app in Python',
    'author': 'David Beckingsale',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'davidbeckingsale@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'] ,
    'packages': ['pymodoro'],
    'scripts': [],
    'name': 'pymodoro'
    }

setup(**config)
