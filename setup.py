from setuptools import setup

setup(name="tdes",version='0.0.1',
description="encrypting and decrypting files tool using triple DES",
package_dir={'': 'src'}, py_modules=["main","DES3","utils"],
install_requires=[
    'click',
    'multipledispatch',
    'pycryptodomex'],
    entry_points={
        'console_scripts': [
            'tdes = main:cli',
        ]
    }
    )