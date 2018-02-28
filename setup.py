import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-inscrybmde',
    version='0.1',
    description='django-inscrybmde is a WYSIWYG markdown editor for Django',
    long_description=readme,
    author="Siyuan Zhang, Thierry BOULOGNE",
    author_email='onepill@gmail.com',
    url='https://github.com/tboulogne/django-inscrybmde',
    license='MIT',
    packages=['inscrybmde'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django,admin,wysiwyg,markdown,editor,inscrybmde',
)
