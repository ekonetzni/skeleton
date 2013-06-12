try:
    from setuptools import setup
except:
    from distutils.core import setup
    
config = {
    'description':      '',
    'author':           '',
    'url':              'Where to get it',
    'download_url':     'Where to actually get it',
    'version':          '0.0',
    'install_requires': ['nose', 'nltk'],
    'packages':         [''],
    'scripts':          [],
    'name':             ''
}

setup(**config)