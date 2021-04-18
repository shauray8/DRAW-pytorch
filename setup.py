import sys
from setuptools import setup, find_packages

sys.path[0:0] = ['Draw-pytorch']
#from version import __version__

setup(
  name = 'Draw-pytorch',
  packages = find_packages(),
  #version = __version__,
  license='Unlicienced Licence',
  description = 'implimenting Draw in Pytorch',
  author = 'Shauray Singh',
  author_email = 'shauray9@gmail.com',
  url = 'https://github.com/shauray8/Draw-pytorch',
  keywords = ["RNN","Deep Learning". 'machine learning'],
  install_requires=[
      'numpy',
      'tqdm',
      'torch',
      'torchvision',
      'pillow',
      "matplotlib",
  ],
)
