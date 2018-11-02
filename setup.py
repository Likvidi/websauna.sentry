import os
import sys
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()


# trying to run python setup.py install or python setup.py develop
if len(sys.argv) >= 2:
    if sys.argv[0] == "setup.py" and sys.argv[1] in ("install", "develop"):
        # Otherwise so much stuff would be broken later...
        raise RuntimeError("It is not possible to install this package with setup.py. Use pip to install this package as instructed in Websauna tutorial.")


setup(name='websauna.sentry',
      namespace_packages=['websauna'],
      version='0.0',
      description='Sentry integration for Websauna',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web websauna pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='websauna.sentry',
      install_requires=['pyramid_raven'],
      extras_require={
        # Dependencies for running test suite
        'test': ['websauna[test]'],

        # Dependencies to make releases
        'dev': ['websauna[dev]'],
      },

      # Define where this application starts as referred by WSGI web servers
      entry_points="""\
      [paste.app_factory]
      main = websauna.sentry.demo:main
      """,
      )
