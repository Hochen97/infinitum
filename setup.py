from setuptools import setup

setup(name='infinitum',
      version='0.0.5',
      description='A package for making working with databases not suck',
      url='http://github.com/hochen97/infinitum',
      author='Jacob Hochendoner',
      author_email='hochen97@gmail.com',
      license='MIT',
      packages=['infinitum'],
      install_requires=[
          'psycopg2-binary'
      ],
      zip_safe=False)