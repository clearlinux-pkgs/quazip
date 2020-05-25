#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : quazip
Version  : 0.9.1
Release  : 4
URL      : https://github.com/stachenov/quazip/archive/v0.9.1/quazip-0.9.1.tar.gz
Source0  : https://github.com/stachenov/quazip/archive/v0.9.1/quazip-0.9.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: quazip-lib = %{version}-%{release}
Requires: quazip-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkg-config
BuildRequires : qtbase-dev
BuildRequires : zlib-dev

%description
QuaZIP is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package
(AKA Minizip) using Trolltech's Qt library.

%package dev
Summary: dev components for the quazip package.
Group: Development
Requires: quazip-lib = %{version}-%{release}
Provides: quazip-devel = %{version}-%{release}
Requires: quazip = %{version}-%{release}

%description dev
dev components for the quazip package.


%package lib
Summary: lib components for the quazip package.
Group: Libraries
Requires: quazip-license = %{version}-%{release}

%description lib
lib components for the quazip package.


%package license
Summary: license components for the quazip package.
Group: Default

%description license
license components for the quazip package.


%prep
%setup -q -n quazip-0.9.1
cd %{_builddir}/quazip-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590373239
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1590373239
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/quazip
cp %{_builddir}/quazip-0.9.1/COPYING %{buildroot}/usr/share/package-licenses/quazip/0d1e2b456373e26a124bae1dfa4a798519b97364
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/quazip5/JlCompress.h
/usr/include/quazip5/ioapi.h
/usr/include/quazip5/minizip_crypt.h
/usr/include/quazip5/quaadler32.h
/usr/include/quazip5/quachecksum32.h
/usr/include/quazip5/quacrc32.h
/usr/include/quazip5/quagzipfile.h
/usr/include/quazip5/quaziodevice.h
/usr/include/quazip5/quazip.h
/usr/include/quazip5/quazip_global.h
/usr/include/quazip5/quazipdir.h
/usr/include/quazip5/quazipfile.h
/usr/include/quazip5/quazipfileinfo.h
/usr/include/quazip5/quazipnewinfo.h
/usr/include/quazip5/unzip.h
/usr/include/quazip5/zip.h
/usr/lib64/cmake/QuaZip5/QuaZip5Config.cmake
/usr/lib64/libquazip5.so
/usr/lib64/pkgconfig/quazip.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libquazip5.so.1
/usr/lib64/libquazip5.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/quazip/0d1e2b456373e26a124bae1dfa4a798519b97364
