#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="odoo-bringout-hello-101",
    version="16.0.1.0.0",
    author="Bringout",
    author_email="info@bringout.com",
    description="Hello 101",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.bring.out.ba",
    project_urls={
        "Bug Tracker": "https://www.bring.out.ba/issues",
        "Documentation": "https://www.bring.out.ba/docs",
        "Source Code": "https://www.bring.out.ba",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Odoo",
        "Framework :: Odoo :: 16.0",
    ],
    python_requires=">=3.8",
    install_requires=[
        "odoo>=16.0dev,<16.1dev",
    ],
    include_package_data=True,
    zip_safe=False,
)
