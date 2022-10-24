#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_slugify
Version  : 6.1.2
Release  : 46
URL      : https://files.pythonhosted.org/packages/5d/45/915967d7bcc28fd12f36f554e1a64aeca36214f2be9caf87158168b5a575/python-slugify-6.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5d/45/915967d7bcc28fd12f36f554e1a64aeca36214f2be9caf87158168b5a575/python-slugify-6.1.2.tar.gz
Summary  : A Python slugify application that also handles Unicode
Group    : Development/Tools
License  : MIT
Requires: pypi-python_slugify-bin = %{version}-%{release}
Requires: pypi-python_slugify-license = %{version}-%{release}
Requires: pypi-python_slugify-python = %{version}-%{release}
Requires: pypi-python_slugify-python3 = %{version}-%{release}
Requires: pypi(unidecode)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(text_unidecode)

%description
**A Python slugify application that handles unicode**.
        
        [![status-image]][status-link]
        [![version-image]][version-link]
        [![coverage-image]][coverage-link]
        
        # Overview
        
        **Best attempt** to create slugs from unicode strings while keeping it **DRY**.
        
        # Notice

%package bin
Summary: bin components for the pypi-python_slugify package.
Group: Binaries
Requires: pypi-python_slugify-license = %{version}-%{release}

%description bin
bin components for the pypi-python_slugify package.


%package license
Summary: license components for the pypi-python_slugify package.
Group: Default

%description license
license components for the pypi-python_slugify package.


%package python
Summary: python components for the pypi-python_slugify package.
Group: Default
Requires: pypi-python_slugify-python3 = %{version}-%{release}

%description python
python components for the pypi-python_slugify package.


%package python3
Summary: python3 components for the pypi-python_slugify package.
Group: Default
Requires: python3-core
Provides: pypi(python_slugify)
Requires: pypi(text_unidecode)

%description python3
python3 components for the pypi-python_slugify package.


%prep
%setup -q -n python-slugify-6.1.2
cd %{_builddir}/python-slugify-6.1.2
pushd ..
cp -a python-slugify-6.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656402386
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_slugify
cp %{_builddir}/python-slugify-6.1.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_slugify/39348c15454a917e7a44ef76017b198dc3834d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/slugify

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_slugify/39348c15454a917e7a44ef76017b198dc3834d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
