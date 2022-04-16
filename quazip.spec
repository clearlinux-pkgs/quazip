#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : quazip
Version  : 1.3
Release  : 7
URL      : https://github.com/stachenov/quazip/archive/v1.3/quazip-1.3.tar.gz
Source0  : https://github.com/stachenov/quazip/archive/v1.3/quazip-1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: quazip-lib = %{version}-%{release}
Requires: quazip-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : zlib-dev

%description
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package
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
%setup -q -n quazip-1.3
cd %{_builddir}/quazip-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650126921
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1650126921
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/quazip
cp %{_builddir}/quazip-1.3/COPYING %{buildroot}/usr/share/package-licenses/quazip/ed6a355236b9e20b1e5d2f8f5798f45f3baace8a
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QuaZip-Qt5-1.3/quazip/JlCompress.h
/usr/include/QuaZip-Qt5-1.3/quazip/ioapi.h
/usr/include/QuaZip-Qt5-1.3/quazip/minizip_crypt.h
/usr/include/QuaZip-Qt5-1.3/quazip/quaadler32.h
/usr/include/QuaZip-Qt5-1.3/quazip/quachecksum32.h
/usr/include/QuaZip-Qt5-1.3/quazip/quacrc32.h
/usr/include/QuaZip-Qt5-1.3/quazip/quagzipfile.h
/usr/include/QuaZip-Qt5-1.3/quazip/quaziodevice.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazip.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazip_global.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazip_qt_compat.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazipdir.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazipfile.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazipfileinfo.h
/usr/include/QuaZip-Qt5-1.3/quazip/quazipnewinfo.h
/usr/include/QuaZip-Qt5-1.3/quazip/unzip.h
/usr/include/QuaZip-Qt5-1.3/quazip/zip.h
/usr/lib64/cmake/QuaZip-Qt5-1.3/QuaZip-Qt5Config.cmake
/usr/lib64/cmake/QuaZip-Qt5-1.3/QuaZip-Qt5ConfigVersion.cmake
/usr/lib64/cmake/QuaZip-Qt5-1.3/QuaZip-Qt5_SharedTargets-relwithdebinfo.cmake
/usr/lib64/cmake/QuaZip-Qt5-1.3/QuaZip-Qt5_SharedTargets.cmake
/usr/lib64/libquazip1-qt5.so
/usr/lib64/pkgconfig/quazip1-qt5.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libquazip1-qt5.so.1.3
/usr/lib64/libquazip1-qt5.so.1.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/quazip/ed6a355236b9e20b1e5d2f8f5798f45f3baace8a
