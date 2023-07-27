from setuptools import setup, find_packages

VERSION = "0.0.1"
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
      classifiers = ["Intended Audience :: Education",
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: MIT License",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "Natural Language :: English",
                     "Topic :: Software Development :: Bug Tracking"
                     ]
      )
