Summary:	LibGTop library
Summary(pl):	Biblioteka LibGTop
Name:		libgtop
Version:	1.0.3
Release:	2
Serial:		1
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.home-of-linux.org/pub/%{name}-%{version}.tar.gz
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	ORBit-devel
BuildRequires:	guile-devel
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	gdbm-devel
BuildRequires:	zlib-devel
BuildRequires:	gnome-libs-devel
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	libgtop-examples

%define		_prefix	/usr/X11R6

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc.

On Linux systems, these information are taken directly from the /proc
filesystem while on other systems a server is used to read those
information from /dev/kmem or whatever. 

%description -l pl
LibGTop jest bibliotek± do pozyskiwania informacji o uruchomionych procesach
jak zajêto¶æ pamiêci i czasu procesora, aktywnych procesach itd.

Na Linuxie powy¿sze informacje s± pozyskiwane bezpo¶rednio z systemu
plikowego znajduj±cego siê w /proc, a na innych do pozyskania powy¿szych
informacji wykorzystywane jest urz±dzenie /dev/kmem lub jeszcze w inny
sposób zale¿ny od systemu.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(pl):	Pliki nag³ówkowe dla LibGTop
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-linux-table \
	--with-libgtop-inodedb
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf src/inodedb/README.inodedb \
	RELNOTES* AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc src/inodedb/README.inodedb.gz

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/file_by_inode
%attr(755,root,root) %{_bindir}/libgtop_daemon
%attr(755,root,root) %{_bindir}/mkinodedb

%{_libdir}/libgtop-features.def

%files devel
%defattr(644,root,root,755)
%doc {RELNOTES*,AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/libgtop-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/*.la

%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
