# Gendiff

[![Maintainability](https://api.codeclimate.com/v1/badges/edc0ee50d88cb1a411ad/maintainability)](https://codeclimate.com/github/vetalpaprotsky/gendiff/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/edc0ee50d88cb1a411ad/test_coverage)](https://codeclimate.com/github/vetalpaprotsky/gendiff/test_coverage)
![Python CI](https://github.com/vetalpaprotsky/gendiff/workflows/Python%20CI/badge.svg)

## Installation
Gendiff can be installed using pip. The package is published on [TestPyPI](https://test.pypi.org/) repository(not [PyPI](https://pypi.org/), as usually) so, you need to pass additional parameters to `pip install` command to make pip search for the package on [TestPyPI](https://test.pypi.org/) instead of [PyPI](https://pypi.org/). Note that the name of the package is actually vetalpaprotsky-gendiff. Here's the installation command:

```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ vetalpaprotsky-gendiff
```

To verify that the installation was successful, run `gendiff -h` command in the terminal. If you're not getting any errors, then everything went well.

Here's how the installation process looks like:
[![asciicast](https://asciinema.org/a/cSzpo7BhLYCHX17rvPmSKEXg1.svg)](https://asciinema.org/a/cSzpo7BhLYCHX17rvPmSKEXg1)

## File types & output formats
Gendiff knows how to work with JSON and YAML files. The difference between files can be outputted in three different formats: stylish, plain, json.

### JSON files
[![asciicast](https://asciinema.org/a/ekaHAH1C9GNfNC3ERpWyeSpq1.svg)](https://asciinema.org/a/ekaHAH1C9GNfNC3ERpWyeSpq1)

### YAML files
[![asciicast](https://asciinema.org/a/jKFePrvbGx7dUhr5AR6QZHOKf.svg)](https://asciinema.org/a/jKFePrvbGx7dUhr5AR6QZHOKf)
