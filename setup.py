from __future__ import absolute_import

import os
import setuptools
import setuptools.command.bdist_rpm


# For daily snapshot versioning mode:
RELEASE = "1%{?dist}"
if os.environ.get("_SNAPSHOT_BUILD", None) is not None:
    import datetime
    RELEASE = RELEASE.replace('1',
                              datetime.datetime.now().strftime("%Y%m%d"))


class bdist_rpm(setuptools.command.bdist_rpm.bdist_rpm):
    """Override the default content of the RPM SPEC.
    """
    spec_tmpl = os.path.join(os.path.abspath(os.curdir),
                             "pkg/package.spec.in")

    def _replace(self, line, rpmver):
        """Replace some strings in the RPM SPEC template"""
        if "@VERSION@" in line:
            return line.replace("@VERSION@", rpmver)

        if "@RELEASE@" in line:
            return line.replace("@RELEASE@", RELEASE)

        if "Source0:" in line:  # Dirty hack
            return "Source0: %{pkgname}-%{version}.tar.gz"

        return line

    def _make_spec_file(self):
        version = self.distribution.get_version()
        rpmver = version.replace('-', '_')

        return [self._replace(l.rstrip(), rpmver) for l
                in open(self.spec_tmpl).readlines()]


setuptools.setup(cmdclass=dict(bdist_rpm=bdist_rpm))

# vim:sw=4:ts=4:et:
