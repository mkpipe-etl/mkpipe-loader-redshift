from setuptools import setup, find_packages

setup(
    name='mkpipe-loader-redshift',
    version='0.5.0',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=['mkpipe'],
    include_package_data=True,
    entry_points={
        'mkpipe.loaders': [
            'redshift = mkpipe_loader_redshift:RedshiftLoader',
        ],
    },
    description='Amazon Redshift loader for mkpipe.',
    author='Metin Karakus',
    author_email='metin_karakus@yahoo.com',
    python_requires='>=3.9',
)
