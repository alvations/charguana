from distutils.core import setup

setup(
  name = 'charguana',
  packages = ['charguana'],
  version = '0.1.15',
  description = 'A character vomiting library.',
  author = 'Liling Tan',
  license = 'MIT',
  package_data={'charguana': ['data/perluniprops/*.txt', 'data/strokecounter/*.txt']},
  url = 'https://github.com/alvations/charguana',
  download_url = 'https://github.com/alvations/charguana/tarball/0.1.15',
  keywords = ['unicode', 'character', 'vommit', 'linguistics' ],
  classifiers = [],
)
