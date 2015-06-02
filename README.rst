===================================
python-anyconfig-configobj-backend
===================================

*This repo was suspended as this module was merged into anyconfig itself and is now maintained in it.* [https://github.com/ssato/python-anyconfig/commit/83b6f9820b62bb4143da68c6063e478d5e1a588b]

This is a backend module for anyconfig to support configobj library.

* Author: Satoru SATOH <ssato@redhat.com>
* License: MIT

SEE ALSO:

* anyconfig: https://pypi.python.org/pypi/anyconfig
* configobj: http://www.voidspace.org.uk/python/configobj.html

Build & Install
================

If you're Fedora or Red Hat Enterprise Linux user, try::

  $ python setup.py srpm && mock dist/SRPMS/python-anyconfig-configobj-backend-<ver_dist>.src.rpm
  
or::

  $ python setup.py rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

Test Status
=============

.. image:: https://api.travis-ci.org/ssato/python-anyconfig-configobj-backend.png?branch=master
   :target: https://travis-ci.org/ssato/python-anyconfig-configobj-backend
   :alt: Test status

.. vim:sw=2:ts=2:et:
