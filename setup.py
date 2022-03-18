from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="puff",
    description="Simple and fast web fuzzer written in python.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sagaryadav8742/puff",
    author="sagaryadav8742",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["puff"],
    include_package_data=True,
    install_requires=["aiohttp", "asyncio", "argparse", "clint", "beautifulsoup4", "datetime"],
    entry_points={
        "console_scripts": [
            "puff=puff.main:main",
        ]
    },
)
