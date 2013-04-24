#! /bin/bash
set -e

curdir=${0%/*}
topdir=${curdir}/../

if `env | grep -q 'WITH_COVERAGE' 2>/dev/null`; then
    coverage_opts="--with-coverage --cover-tests --cover-inclusive"
fi

which pep8 2>&1 > /dev/null && check_with_pep8=1 || check_with_pep8=0

# Dirty hack! It is very ugly but I don't know how to fix this at once:
setup () {
    moddir=$topdir/anyconfig
    base="https://raw.github.com/ssato/python-anyconfig/master/anyconfig"

    for f in compat.py globals.py mergeabledict.py utils.py; do (cd $moddir && test -f $f || curl -O $base/$f); done
    for f in base.py; do (cd $moddir/backend && test -f $f || curl -O $base/backend/$f); done
}

setup

if test $# -gt 0; then
    test $check_with_pep8 = 1 && (for x in $@; do pep8 ${x%%:*}; done) || :
    PYTHONPATH=$topdir nosetests -c $curdir/nose.cfg ${coverage_opts} $@
else
    # Find out python package dir and run tests for .py files under it.
    for d in ${topdir}/*; do
        if test -d $d -a -f $d/__init__.py; then
            pypkgdir=$d

            for f in $(find ${pypkgdir} -name '*.py'); do
                echo "[Info] Check $f..."
                test $check_with_pep8 = 1 && pep8 $f || :
                PYTHONPATH=$topdir nosetests -c $curdir/nose.cfg \
                        ${coverage_opts} $f
            done

            break
        fi
    done
fi
