====================================
python-anyconfig-configobj-backend
====================================

.. vim:sw=2:ts=2:et:

.. image:: https://img.shields.io/travis/ssato/python-anyconfig-configobj-backend.svg
   :target: https://travis-ci.org/ssato/python-anyconfig-configobj-backend
   :alt: Test status

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-configobj-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-configobj-backend
   :alt: Coverage Status

.. image:: https://landscape.io/github/ssato/python-anyconfig-configobj-backend/master/landscape.png
   :target: https://landscape.io/github/ssato/python-anyconfig-configobj-backend/master
   :alt: Code Health

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

If you're Fedora or Red Hat Enterprise Linux user, try::

  $  python setup.py bdist_rpm --source-only && mock dist/python-anyconfig-*-<ver_dist>.src.rpm
  
or::

  $  python setup.py bdist_rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:
