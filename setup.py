import os
import platform
from pathlib import Path

from Cython.Build import cythonize
from numpy import get_include
from setuptools import Extension, setup

SYSTEM = platform.system()
LINK = "static"
SDK = Path("sdk") / SYSTEM / LINK
LIB = SDK / "lib"
INCLUDE = SDK / "include"
CYTHON_TRACE = bool(os.getenv("CYTHON_TRACE", "0") not in ("0", "False"))

# os.environ["MACOSX_DEPLOYMENT_TARGET"] = "11.0"

nd2file = Extension(
    name="nd2._nd2file",
    sources=["nd2/_nd2file.pyx"],
    libraries=["nd2readsdk-static"],
    library_dirs=[str(LIB)],
    include_dirs=[str(INCLUDE), get_include()],
    extra_objects=[str(x) for x in LIB.glob("*")],
    define_macros=[("LX_STATIC_LINKING", None), ("CYTHON_TRACE", int(CYTHON_TRACE))],
)


setup(
    use_scm_version={"write_to": "nd2/_version.py"},
    ext_modules=cythonize(
        [nd2file],
        language_level="3",
        compiler_directives={"linetrace": CYTHON_TRACE, "c_string_encoding": "utf-8"},
    ),
)
