import setuptools
from setuptools.command.build_ext import build_ext as build_ext_orig


with open("README.md", "r") as fh:
    long_description = fh.read()

class build_ext(build_ext_orig):
    
    def get_ext_filename(self, fullname):
        return fullname+".so"


extension = setuptools.Extension("libmcp", ["src/mcp_com.c"])

setuptools.setup(
    name="pynpoint", # Replace with your own username
    version="0.0.1",
    author="Felix Grzelka",
    description="A python wrapper around some mcp lib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sirexeclp/pynpoint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    ext_modules=[
        extension
    ],
    cmdclass={'build_ext': build_ext},
)