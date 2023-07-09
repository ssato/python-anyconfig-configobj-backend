====================================
python-anyconfig-configobj-backend
====================================

.. vim:sw=2:ts=2:et:

.. image:: https://img.shields.io/pypi/pyversions/anyconfig-configobj-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-configobj-backend/
   :alt: [Python versions]

.. image:: https://img.shields.io/pypi/l/anyconfig-configobj-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-configobj-backend/
   :alt: MIT License

.. image:: https://github.com/ssato/python-anyconfig-configobj-backend/workflows/Tests/badge.svg
   :target: https://github.com/ssato/python-anyconfig-configobj-backend/actions?query=workflow%3ATests
   :alt: [Github Actions: Test status]

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-configobj-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-configobj-backend
   :alt: Coverage Status

.. image:: https://codecov.io/gh/ssato/python-anyconfig-configobj-backend/branch/next/graph/badge.svg?token=CEHaIGm60z
   :target: https://codecov.io/gh/ssato/python-anyconfig-configobj-backend
   :alt: [Codecov Status]

.. image:: https://readthedocs.org/projects/python-anyconfig-configobj-backend/badge/?version=latest
   :target: http://python-anyconfig-configobj-backend.readthedocs.io/en/latest/?badge=latest
   :alt: Doc Status

.. vim:sw=2:ts=2:et:

This is a backend module for python-anyconfig to load and dump configuration
data configobj supports.

- Author: Satoru SATOH <ssato@redhat.com>
- License: MIT

SEE ALSO:

- python-anyconfig: https://pypi.python.org/pypi/anyconfig
- configobj: http://www.voidspace.org.uk/python/configobj.html

.. - Download:

..   - PyPI: https://pypi.python.org/pypi/anyconfig-configobj-backend
  - Copr RPM repos: https://copr.fedoraproject.org/coprs/ssato/python-anyconfig/

.. vim:sw=2:ts=2:et:

Build & Install
================

There is a couple of ways to install this package:

- Binary RPMs: if you want to install the latest version, optionally, you can enable my copr repo, http://copr.fedoraproject.org/coprs/ssato/python-anyconfig/ .

- PyPI: You can install this package from PyPI with using pip:

  .. code-block:: console

    $ pip3 install anyconfig-configobj-backend

- pip from git repo:

  .. code-block:: console

     $ pip3 install git+https://github.com/ssato/python-anyconfig-configobj-backend/

- Build RPMs from source: It's easy to build python-anyconfig with using rpm-build and mock:

  .. code-block:: console

    # Build Source RPM first and then build it with using mock (better way)
    $ python3 setup.py bdist_rpm --source-only && mock dist/python3-anyconfig-configobj-backend-<ver_dist>.src.rpm

  or

  .. code-block:: console

    # Build Binary RPM to install
    $ python3 setup.py bdist_rpm

  and install RPMs built.

- Build from source: Of course you can build and/or install python modules in usual way such like 'python setup.py bdist'.

.. vim:sw=2:ts=2:et:
