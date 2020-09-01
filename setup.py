#!/usr/bin/env python

from pathlib import Path
from subprocess import call
import os

try:
    from setuptools.command.install import install
    from setuptools import setup, Extension
    from distutils.command.build import build
except:
    from distutils.command.build import build
    from distutils.command.install import install
    from distutils import setup, Extension
    
swig = Extension(
    "_anitomy",
    swig_opts=["-c++"],
    language="c++",
    sources=["anitomy.i"]
    + [str(e) for e in Path().joinpath("anitomy").iterdir() if e.suffix == ".cpp"],
)

swigless = Extension(
    "_anitomy",
    language="c++",
    sources=["anitomy_wrap.cpp"]
    + [str(e) for e in Path().joinpath("anitomy").iterdir() if e.suffix == ".cpp"],
    include_dirs=["anitomy"]
)

class CustomBuild(build):
    def run(self):
        self.run_command("build_ext")
        super().run()


class CustomInstall(install):
    def run(self):
        self.run_command("build_ext")
        super().run()


setup(
    name="anitomy_py",
    version="1.0.0",
    description="Port of Anitomy from C++ to Python using SWIG.",
    author="Félix Desmaretz",
    author_email="felix.desmaretz@protonmail.com",
    #    url = 'https://docs.python.org/extending/building',
    long_description="""
    Port of Anitomy (https://github.com/erengy/anitomy) to Python using SWIG (http://swig.org/).
    """,
    license="Mozilla Public License 2.0",
    cmdclass={"build": CustomBuild, "install": CustomInstall},
    ext_modules=[swig],
    py_modules=["anitomy"],
    package_data={"": [str(e) for e in Path().joinpath("anitomy").iterdir() if e.suffix == ".h"]},
    include_package_data=True,
    headers=[str(e) for e in Path().joinpath("anitomy").iterdir() if e.suffix == ".h"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"
    ],
    python_requires='>=3.6'
)
