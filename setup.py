import os
from gitversion import __VERSION__

from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext


with open(os.path.join("pyJ2534", "__init__.py"), "w") as f:
    f.write("__VERSION__ = '%s'\n" % __VERSION__)

setup(
    name="pyJ2534",
    version=__VERSION__,
    description="MCU Innovations pyJ2534",
    url="https://github.com/MCU-Innovations/pyJ2534",
    author="Ryan M. Hope",
    author_email="ryan.hope@mcuinnovations.com",
    license="GPL-3",
    ext_modules=cythonize(
        [
            Extension("pyJ2534.Define", ["pyJ2534/Define.pyx"]),
            Extension("pyJ2534.Error", ["pyJ2534/Error.pyx"]),
            Extension("pyJ2534.wrapper", ["pyJ2534/wrapper.pyx"]),
        ],
        build_dir="build",
        compiler_directives=dict(
            always_allow_keywords=True,
            language_level=3,
        ),
    ),
    cmdclass={"build_ext": build_ext},
    packages=["pyJ2534"],
)
