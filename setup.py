"""setup this"""
import io

from setuptools import setup

import polygonal as polygonal

LICENSE = 'GNU GPLv3'


def read(*filenames, **kwargs):
    """read and concatenate files"""
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as fil:
            buf.append(fil.read())
    return sep.join(buf)


setup(
    name='polygonal',
    version=polygonal.__version__,
    url='http://bitbucket.com/vladekm/polygonal/',
    license=LICENSE,
    author='Vlad Mettler',
    author_email='vlad@liquidant.com',
    tests_require=['nose'],
    description="Framework for implementation of modules using the Hexagonal"
                "architecture",
    long_description=read('README.rst'),
    packages=['polygonal'],
    include_package_data=True,
    platforms='any',
    test_suite='polygonal.tests',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: {}'.format(LICENSE),
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        ],
    extras_require={
        'testing': ['nose']
    }
)
