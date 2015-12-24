from setuptools import setup

version = '0.0.2'

setup(
    name='curlc',
    version=version,
    packages = ['curlc'],
    description="curl wrapper to borrow cookies from your browser's authenticated session",
    author='William Casarin',
    author_email='bill@casarin.me',
    url='https://github.com/jb55/curlc',
    include_package_data=True,
    install_requires=[ "pycookiecheat >= 0.2.0" ],
    entry_points = {'console_scripts': ['curlc=curlc.curlc:main'] },
    license="GPLv2",
    keywords='curlc',
    classifiers=[
      'Programming Language :: Python :: 3',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'Topic :: Internet :: WWW/HTTP',
      'Topic :: Software Development',
      'Topic :: System :: Networking',
      'Topic :: Terminals',
      'Topic :: Utilities'
    ],
)
