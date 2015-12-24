try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name='curlc',
    version='0.0.1',
    description="Borrow cookies from your browser's authenticated session for"
                "use in curl.",
    author='William Casarin',
    author_email='bill@casarin.me',
    url='https://github.com/jb55/curlc',
    include_package_data=True,
    install_requires=requirements,
    license="GPLv2",
    keywords='curlc',
    classifiers=[
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.1',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'Topic :: Internet :: WWW/HTTP',
      'Topic :: Software Development',
      'Topic :: System :: Networking',
      'Topic :: Terminals',
      'Topic :: Text Processing',
      'Topic :: Utilities'
    ],
)
