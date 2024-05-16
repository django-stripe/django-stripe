# django-stripe

[![PyPI](https://img.shields.io/pypi/v/ kiecutter.project_name }}.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/django-stripe.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/django-stripe)][pypi status]
[![License](https://img.shields.io/pypi/l/django-stripe)][license]

[![Read the documentation at https://django-stripe.readthedocs.io/](https://img.shields.io/readthedocs/django-stripe/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/django-stripe/django-stripe/actions/workflows/tests.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/django-stripe/django-stripe/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/django-stripe/
[read the docs]: https://django-stripe.readthedocs.io/
[tests]: https://github.com/abe-101/django-stripe/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/abe-101/django-stripe
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

Stripe is a fast moving target, and while maintaining a handful
of django project that relies on stripe, I found myself repeatedly
writing code to handle stripe webhooks, and storing stripe data in
the database.
This package aims to provide a simple way to handle
stripe webhooks and store stripe data in the database.


## Requirements

- TODO

## Installation

You can install _django-stripe_ via [pip] from [PyPI]:

```console
$ pip install django_stripe
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_django-stripe_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@OmenApps]'s [Cookiecutter Django Package] template.

[@omenapps]: https://github.com/OmenApps
[pypi]: https://pypi.org/
[cookiecutter django package]: https://github.com/OmenApps/cookiecutter-django-package
[file an issue]: https://github.com/abe-101/django-stripe/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/abe-101/django-stripe/blob/main/LICENSE
[contributor guide]: https://github.com/abe-101/django-stripe/blob/main/CONTRIBUTING.md
[command-line reference]: https://django-stripe.readthedocs.io/en/latest/usage.html
