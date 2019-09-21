
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
