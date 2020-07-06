import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="osearch",
    version="0.1.0",
    author="Alex Skov Jensen",
    author_email="pydev@offline.dk",
    description="Search nested lists and dicts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x821938/osearch",
    packages=["osearch"],
    license="MIT",
    keywords=["search", "list", "dictionary", "objects", "pretty", "print", "json"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Bug Tracking ",
        "Topic :: Software Development :: Testing",
        "Topic :: Text Processing :: Filters",
        "Intended Audience :: Developers",
    ],
    project_urls={
        "Documentation": "https://github.com/x821938/osearch",
        "Source": "https://github.com/x821938/osearch",
    },
    install_requires=[],
)
