from setuptools import setup, find_packages

from treemenus import __version__

setup(
    name='django-treemenus',
    version=__version__,
    description='Tree-structured menuing application for Django.',
    author='Julien Phalip',
    author_email='jphalip@gmail.com',
    url='http://github.com/jphalip/django-treemenus/',
    license='BSD',
    packages=find_packages(),
    package_data={
        'treemenus': [
            'static/img/treemenus/*.gif',
            'templates/admin/treemenus/menu/*.html',
            'templates/admin/treemenus/menuitem/*.html',
        ]
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
