#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : munch
Version  : 2.3.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/68/f4/260ec98ea840757a0da09e0ed8135333d59b8dfebe9752a365b04857660a/munch-2.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/f4/260ec98ea840757a0da09e0ed8135333d59b8dfebe9752a365b04857660a/munch-2.3.2.tar.gz
Summary  : A dot-accessible dictionary (a la JavaScript objects).
Group    : Development/Tools
License  : MIT
Requires: munch-python3
Requires: munch-license
Requires: munch-python
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
[![Build Status](https://travis-ci.org/Infinidat/munch.svg?branch=master)](https://travis-ci.org/Infinidat/munch)
[![Latest Version](https://img.shields.io/pypi/v/munch.svg)](https://pypi.python.org/pypi/munch/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/munch.svg)](https://pypi.python.org/pypi/munch/)
[![Downloads](https://img.shields.io/pypi/dm/munch.svg)](https://pypi.python.org/pypi/munch/)

%package license
Summary: license components for the munch package.
Group: Default

%description license
license components for the munch package.


%package python
Summary: python components for the munch package.
Group: Default
Requires: munch-python3

%description python
python components for the munch package.


%package python3
Summary: python3 components for the munch package.
Group: Default
Requires: python3-core

%description python3
python3 components for the munch package.


%prep
%setup -q -n munch-2.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533784432
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/munch
cp LICENSE.txt %{buildroot}/usr/share/doc/munch/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/munch/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
