#This is a fork of https://bitbucket.org/sardarnl/apns-client/

import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='apns-client',
    version='0.1.5',
    author='Sardar Yumatov, Colin Bean',
    author_email='ccbean@gmail.com',
    url='https://github.com/socialize/apns-utils',
    description='Python client for Apple Push Notification service (APNs)',
    long_description="Fork of https://bitbucket.org/sardarnl/apns-client/",
    packages=['apnsclient'],
    license="Apache 2.0",
    keywords='apns push notification apple messaging iOS',
    install_requires=['pyOpenSSL'],
    test_require=['mock'],
    classifiers = [ 'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Programming Language :: Python',
                    'Topic :: Software Development :: Libraries :: Python Modules']
)
