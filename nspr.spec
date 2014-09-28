# based on PLD Linux spec git://git.pld-linux.org/packages/.git
Summary:	Netscape Portable Runtime (NSPR)
Name:		nspr
Version:	4.10.7
Release:	1
Epoch:		1
License:	MPL v2.0 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	6e06919e4b56efed501e05d8b45ec10e
Patch0:		%{name}-pc.patch
URL:		http://www.mozilla.org/projects/nspr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries that implement cross-platform runtime services from
Netscape.

%package devel
Summary:	NSPR library header files for development
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for the NSPR library from Netscape.

%prep
%setup -q
%patch0 -p1

%build
cd nspr
%{__autoconf}
%configure \
	--disable-debug	    \
%ifarch %{x8664}
	--enable-64bit	    \
%endif
	--enable-ipv6	    \
	--enable-optimize   \
	--includedir=%{_includedir}/nspr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C nspr install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/{compile-et.pl,prerr.properties}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nspr-config
%{_includedir}/nspr
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

