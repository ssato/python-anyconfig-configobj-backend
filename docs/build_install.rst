
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
