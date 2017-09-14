from setuptools import setup

setup(name='NeighborCompare',
      version='0.1',
      description='A method for comparing and visualizing '
                  'dimensionality reduction algorithm solutions.',
      url='http://github.com/mrJeppard/neighborplot',
      author='Duncan McColl',
      author_email='duncmc831@gmail.com',
      license='None',
      packages=['neighborplot'],
      install_requires=["numpy",
                        "scipy",
                        "matplotlib",
                        "pandas"],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False
      )
