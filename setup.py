from setuptools import setup

with open("README.md","r") as fh:
    long_description=fh.read()

setup(name="tdes",version='0.0.1',
description="encrypting and decrypting files tool using triple DES",
package_dir={'': 'src'}, py_modules=["main","module","module.DES3","module.utils","DES3","utils"],
long_description=long_description,
long_description_content_type="text/markdown",
install_requires=[
    'click',
    'pycryptodomex'],
    entry_points={
        'console_scripts': [
            'tdes = main:cli',
        ]
    },
    classifiers=[
        "Programmig language :: Python :: 3",
        "Programmig language :: Python :: 3.8",
        "Programmig language :: Python :: 3.1",
        "Programmig language :: Python :: 3.2",
        "Programmig language :: Python :: 3.7",
        "Programmig language :: Python :: 3.x",
        "Development Status :: 4 - Beta",
        "Topic :: Security :: Cryptography",

    ],
    url="https://github.com/4bd4ll4h/tdes",
    author="4bd4ll4h",
    author_email="4bd4ll4h.m@gmail.com"
    )