# TODO:
# fix autoconf (LIBOBJS issuse)
Summary:	LibGTop library
Summary(pl):	Biblioteka LibGTop
Name:		libgtop
Version:	2.0.0
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-ac.patch
#Patch1:		%{name}-amfix.patch
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRequires:	ORBit2-devel >= 2.4.0
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	gettext-devel
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	guile-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtop-examples

%define		_prefix		/usr/X11R6

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc. On Linux systems, these
information are taken directly from the /proc filesystem while on
other systems a server is used to read those information from
/dev/kmem or whatever.

%description -l pl
LibGTop jest bibliotek± do pozyskiwania informacji o uruchomionych
procesach jak zajêto¶æ pamiêci i czasu procesora, aktywnych procesach
itd. Na Linuxie powy¿sze informacje s± pozyskiwane bezpo¶rednio z
systemu plikowego znajduj±cego siê w /proc, a na innych do pozyskania
powy¿szych informacji wykorzystywane jest urz±dzenie /dev/kmem lub
jeszcze w inny sposób zale¿ny od systemu.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(pl):	Pliki nag³ówkowe dla LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
cd src/daemon
sed -e 's/.*-static//' Makefile.am > Makefile.am.tmp
mv -f Makefile.am.tmp Makefile.am

%build
libtoolize --copy --force
glib-gettextize --copy --force
aclocal 
%{__autoconf}
%{__automake}
%configure \
	--with-linux-table=no \
	--with-libgtop-inodedb \
	--with-libgtop-guile \
	--with-libgtop-smp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf src/inodedb/README.inodedb \
	RELNOTES* AUTHORS ChangeLog NEWS README

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc src/inodedb/README.inodedb.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/file_by_inode2
%attr(755,root,root) %{_bindir}/libgtop_daemon2
%attr(755,root,root) %{_bindir}/mkinodedb2

%files devel
%defattr(644,root,root,755)
%doc {RELNOTES*,AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/lib*.??
%{_libdir}/libgtop
%{_includedir}/libgtop-2.0
%{_pkgconfigdir}/*.pc
%{_infodir}/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
