Name:               libvma
Version:            8.9.4
Release:            8
Summary:            A library that boosts performance for message-based and streaming applications
License:            GPLv2 or BSD
URL:                https://github.com/Mellanox/libvma
Source:             https://github.com/Mellanox/libvma/archive/%{version}.tar.gz
ExcludeArch:        %{arm}
Requires:           pam
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
BuildRequires:      rdma-core-devel libnl3-devel automake autoconf libtool
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
* Thu Sep 3 2020 zhaowei<zhaowei23@huawei.com> - 8.9.4-8
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: update source URL

* Sun Jan 19 2020 lijin Yang <yanglijin@huawei.com> - 8.9.4-7
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: update the tar package

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.0.1-6
- Package init
