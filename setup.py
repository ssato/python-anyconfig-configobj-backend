from setuptools import setup, Command

import datetime
import os
import subprocess


# Ugly, but necessary to avoid extra dependency on build time.
# from anyconfig_configobj_backend.globals import PACKAGE, VERSION
PACKAGE = "anyconfig-configobj-backend"
VERSION = "0.0.3"

# For daily snapshot versioning mode:
if os.environ.get("_SNAPSHOT_BUILD", None) is not None:
    import datetime
    VERSION = VERSION + datetime.datetime.now().strftime(".%Y%m%d")


class SrpmCommand(Command):

    user_options = []
    build_stage = "s"

    curdir = os.path.abspath(os.curdir)
    rpmspec = os.path.join(curdir, "pkg/package.spec")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.pre_sdist()
        self.run_command('sdist')
        self.build_rpm()

    def pre_sdist(self):
        c = open(self.rpmspec + ".in").read()
        open(self.rpmspec, "w").write(c.replace("@VERSION@", VERSION))

    def build_rpm(self):
        rpmbuild = os.path.join(self.curdir, "pkg/rpmbuild-wrapper.sh")
        workdir = os.path.join(self.curdir, "dist")

        cmd_s = "%s -w %s -s %s %s" % (rpmbuild, workdir, self.build_stage,
                                       self.rpmspec)
        subprocess.check_call(cmd_s, shell=True)


class RpmCommand(SrpmCommand):

    build_stage = "b"


_CLASSIFIERS = ["Development Status :: 4 - Beta",
                "Intended Audience :: Developers",
                "Programming Language :: Python",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 2.7",
                "Programming Language :: Python :: 3.3",
                "Programming Language :: Python :: 3.4",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6",
                "Operating System :: OS Independent",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "Topic :: Text Processing :: Markup",
                "Topic :: Utilities",
                "License :: OSI Approved :: MIT License"]


def _parse_requirements_txt(filepath="pkg/requirements.txt"):
    return [l.rstrip() for l in open(filepath).readlines()
            if l and not l.startswith('#')]


setup(name=PACKAGE,
      version=VERSION,
      description="Backend module for python-anyconfig to load and dump Configobj data",
      long_description=open("README.rst").read(),
      author="Satoru SATOH",
      author_email="ssato@redhat.com",
      license="MIT",
      url="https://github.com/ssato/python-anyconfig-configobj-backend",
      classifiers=_CLASSIFIERS,
      install_require=_parse_requirements_txt(),
      tests_require=_parse_requirements_txt("pkg/test_requirements.txt"),
      packages=["anyconfig_configobj_backend"],
      include_package_data=True,
      cmdclass=dict(srpm=SrpmCommand, rpm=RpmCommand),
      entry_points=open(os.path.join(os.curdir,
                                     "pkg/entry_points.txt")).read(),
)

# vim:sw=4:ts=4:et:
