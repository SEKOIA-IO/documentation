import setuptools


setuptools.setup(
    name='redoc',
    version='0.0.1',
    description='Plugin for adding redoc in Mkdocs.',
    long_description='redoc plugin on mkdocs',  # noqa: E501
    keywords='redoc',
    url='',
    author='Mickael Découflet',
    author_email='mickael.decouflet@sekoia.fr',
    license='Apache-2.0',
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'mkdocs.plugins': [
            "redoc = plugins.redoc:RedocPlugin"
        ]
    }
)