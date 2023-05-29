from setuptools import find_packages, setup

VERSION = "0.0.1"

with open("README.md", "r") as readme:
    long_description = readme.read()

with open("LICENSE", "r") as license_file:
    license = license_file.read()

setup(
    name="aioemit",
    version=VERSION,
    description="A minimalistic async event bus implementation",
    author="iunary",
    license=license,
    author_email="contact@yusuf.im",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "emitter",
        "event bus",
        "pubsub",
        "async",
        "subscribe",
        "emit",
        "publish",
        "aioemit",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
