from setuptools import setup

version = '1.0.0'

setup(
    name='pypeak',
    version=version,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    packages=[
        'pypeak',
    ],
    include_package_data=True,
    author='TkachoFF',
    author_email='artsiom.tkachou@gmail.com',
    url='https://github.com/tkachoff/pypeak',
    description='Webium is a Page Object pattern implementation library for Python '
                '(http://martinfowler.com/bliki/PageObject.html). '
                'It allows you to extend WebElement class to your custom controls '
                'like Link, Button and group them as pages.',
    install_requires=[
        'selenium',
        'waiting>=1.2.1',
    ]
)
