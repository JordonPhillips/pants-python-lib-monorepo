# Pants for Python Library Monorepos

[Pants](https://www.pantsbuild.org) is a build tool written in Python, but
capable of building projects in multiple languages. While it is capable of doing
a great number of things, my primary interest it is as a monorepo tool for
python packages. Specifically I want to have a set of python packages that will
be published to pypi or some other packaging repository, each of which is
isolated from the others outside of some explictly shared configuration. Each
package should be as close to a typical python package as possible, using standard
configuration files like `pyproject.toml`. In a way, this is similar to Gradle
sub-projects. The following is an example desired repo structure:

```
.
├── packages
│   ├── package-a
│   │   ├── README.md
│   │   ├── package_a
│   │   │   ├── __init__.py
│   │   │   └── module
│   │   │       └── __init__.py
│   │   ├── pyproject.toml
│   │   └── tests
│   │       └── __init__.py
│   └── package-b
│       ├── README.md
│       ├── package_b
│       │   ├── __init__.py
│       │   └── module
│       │       └── __init__.py
│       └── pyproject.toml
└── pants.toml
```

In this example, `package-b` depends on `package-a`. When running tests, it
should use the current state of `package-a` rather than relying on a manually
installed version that may not be up-to-date. When building package
distributions, it should correctly indicate that it depends on `package-a`,
including the specific version.

Unfortunately, I've been unable to find example repos that have a structure
similar to this. The official
[python example repo](https://github.com/pantsbuild/example-python) uses a very
different structure that's presumably meant to showcase the powerful source
filtering capabilities of pants.

This repo then will serve as a minimal testing environment for me to learn how
to achieve this structure, and eventually as an example for others.