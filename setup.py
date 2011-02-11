from setuptools import setup, find_packages
 
setup(
    name='django-typogrify',
    version='1.2',
    description='Make type not look like crap (for django apps)',
    author='Christian Metts, Chris Drackett',
    author_email='chris@shelfworthy.com',
    url='http://github.com/chrisdrackett/django-typogrify',
    packages = [
        "typogrify",
        "typogrify.templatetags",
    ],
    install_requires = [
        'textile',
    ],
    classifiers=[
        'Development Status :: 1',
        'Environment :: Web Environment',
        'Intended Audience :: Developers :: Designers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)