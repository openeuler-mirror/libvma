Name:               libvma
Version:            8.9.4
Release:            13
Summary:            A library that boosts performance for message-based and streaming applications
License:            GPLv2 or BSD
URL:                https://github.com/Mellanox/libvma
Source:             https://github.com/Mellanox/libvma/archive/%{version}.tar.gz
Patch0000:          Resolve-gcc-9.x-issues.patch
Patch0001:          0001-Remove-ExecReload-that-is-not-supported.patch
Patch0002:          fix-build-error-with-glibc-2.34.patch
Patch0003:          fix-clang.patch
Patch0004:          fix-arm.patch
Patch0005:          add-riscv64-support.patch
ExcludeArch:        %{arm}
Requires:           pam
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
BuildRequires:      rdma-core-devel libnl3-devel automake autoconf libtool g++
Provides:           %{name}-utils = %{version}-%{release}
Obsoletes:          %{name}-utils < %{version}-%{release}

%description
Mellanox's Messaging Accelerator (VMA) is dynamically linked user space Linux
library for transparently enhancing the performance of networking-heavy
applications. It boosts performance for message-based and streaming applications
such as those found in financial services market data environments and Web2.0
clusters.

%package            devel
Summary:            Header files for libvma
Requires:           %{name} = %{version}-%{release}

%description        devel
Headers files for libvma.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%if "%toolchain"=="clang"
%ifarch x86_64
export CXXFLAGS+="$CXXFLAGS -Werror  -Wno-deprecated-register -Wno-non-c-typedef-for-linkage -Wno-unused-but-set-variable -Wno-gnu-variable-sized-type-not-at-end"
export CFLAGS+="$CFLAGS -Werror  -Wno-deprecated-register -Wno-non-c-typedef-for-linkage -Wno-unused-but-set-variable -Wno-gnu-variable-sized-type-not-at-end"
%endif
%ifarch aarch64
export CXXFLAGS+="$CXXFLAGS -Wall -Wno-error -Wno-invalid-pp-token -Wno-deprecated-register -Wno-gnu-variable-sized-type-not-at-end"
export CFLAGS+="$CFLAGS  -Wno-invalid-pp-token -Wno-deprecated-register -Wno-gnu-variable-sized-type-not-at-end"
%endif
%ifarch riscv64
export CXXFLAGS+="$CXXFLAGS -Werror -Wnon-c-typedef-for-linkage -Wno-deprecated-register -Wno-gnu-variable-sized-type-not-at-end"
export CFLAGS+="$CFLAGS  -Werror -Wnon-c-typedef-for-linkage -Wno-deprecated-register -Wno-gnu-variable-sized-type-not-at-end"
%endif
%endif
./autogen.sh
%configure
%make_build V=1

%install
%make_install
%delete_la

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc README.md README.txt journal.txt VMA_VERSION.in
%license COPYING LICENSE
%config(noreplace) %{_sysconfdir}/libvma.conf
%config(noreplace) %{_sysconfdir}/security/limits.d/30-libvma-limits.conf
%{_bindir}/vma_stats
%{_libdir}/%{name}.so
%{_libdir}/%{name}*.so.*
%{_sbindir}/vmad
%{_sbindir}/vma
%{_unitdir}/vma.service

%files devel
%defattr(-,root,root)
%{_includedir}/*

%files help
%defattr(-,root,root)
%{_pkgdocdir}/README.txt
%{_pkgdocdir}/journal.txt
%{_pkgdocdir}/VMA_VERSION

%changelog
* Fri Jul 7 2023 zhangxiang <zhangxiang@iscas.ac.cn> - 8.9.4-13
- fix clang build error & add riscv64 support

* Tue Aug 10 2021 wangyue <wangyue92@huawei.com> - 8.9.4-12
- fix build error with glibc-2.34

* Tue Jun 08 2021 wulei <wulei80@huawei.com> - 8.9.4-11
- fixes failed: g++: No such file or directory

* Wed Mar 10 2021 maminjie <maminjie1@huawei.com> - 8.9.4-10
- Remove ExecReload that is not supported

* Thu Sep 3 2020 zhaowei<zhaowei23@huawei.com> - 8.9.4-9
-update source URL

* Thu May 21 2020 yanan li <liyanan032@huawei.com> - 8.9.4-8
- Slove the problem of pointer value misalignment caused by gcc 9.x enabling verification.

* Sun Jan 19 2020 lijin Yang <yanglijin@huawei.com> - 8.9.4-7
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: update the tar package

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.0.1-6
- Package init
