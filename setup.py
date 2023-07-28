#
# MIT License
#
# Copyright (c) 2023 Dishant B. (@dishb) <code.dishb@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from setuptools import setup, find_packages

VERSION = "0.0.2"
DESCRIPTION = """A cross-platform CLI to quickly retrieve system information to make issue management easier."""

with open("README.md", "r", encoding = "utf-8") as file:
    LONG_DESCRIPTION = file.read()
    file.close()

with open("requirements.txt", "r", encoding = "utf-8") as file:
    REQUIREMENTS = file.read()
    REQUIREMENTS = REQUIREMENTS.split()
    file.close()

setup(name = "monstera",
      version = VERSION,
      author = "Dishant B. (@dishb)",
      author_email = "code.dishb@gmail.com",
      description = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      long_description_content_type = "text/markdown",
      packages = find_packages(include = ["monstera", "monstera.*"]),
      entry_points = {"console_scripts": ["monstera = monstera.__main__:_main"]},
      install_requires = REQUIREMENTS,
      python_requires = ">=3.9",
      keywords = ["monstera",
                  "bug tracker",
                  "bug tracking",
                  "issue tracker",
                  "issue tracking",
                  "tool",
                  "developers",
                  "developing",
                  "monstera tool",
                  "dependencies",
                  "versions",
                  "file locations",
                  "python",
                  "cross-platform",
                  "python3"
                  ],
      license = "MIT",
      project_urls = {"Documentation": "https://github.com/dishb/monstera/tree/main/docs",
                      "Source": "https://github.com/dishb/monstera/",
                      "Issue Tracker": "https://github.com/dishb/monstera/issues"
                      },
      url = "https://github.com/dishb/monstera",
      classifiers = ["Programming Language :: Python :: 3.9",
                     "Programming Language :: Python :: 3.10",
                     "Programming Language :: Python :: 3.11",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: MIT License",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "Natural Language :: English",
                     "Topic :: Software Development",
                     "Topic :: Software Development :: Bug Tracking",
                     "Topic :: Software Development :: Libraries :: Python Modules"
                     ]
      )
