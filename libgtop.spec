Summary:	LibGTop library
Summary(pl):	Biblioteka LibGTop
Name:		libgtop
Version:	0.99.1
Release:	1d
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.home-of-linux.org/pub/%{name}-%{version}.tar.gz
Patch0:		libgtop-DESTDIR.patch
Patch1:		libgtop-mountlist.patch
Requires:	gnome-libs = 0.99.2
Requires:	glib = 1.1.15
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	libgtop-examples

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc.

On Linux systems, these information are taken directly from the /proc
filesystem while on other systems a server is used to read those
information from /dev/kmem or whatever. 

%description -l pl
LibGTop jest bibliotek± pozyskiwania informacje o uruchomionych procesach
jak zajêto¶æ pamiêci i czasu procesora, aktywnych procesach itd.

Na Linuxie powy¿sze informacje s± pozyskiwane bezpo¶rednio z systemu
plikowego znajduj±cego siê w /proc, a na innych do pozyskania powy¿szych
informacji wykorzystywane jest urz±dzenie /dev/kmem lub jeszcze w inny
sposób zale¿ny od systemu.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(pl):	Pliki nag³ówkowe dla LibGTop
Group:		X11/libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o LibGTop.

%package	static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Group:		X11/libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--without-linux-table \
	--with-libgtop-inodedb
make

bzip2 -9 src/inodedb/README.inodedb
bzip2 -9 RELNOTES* AUTHORS ChangeLog NEWS README

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc src/inodedb/README.inodedb.bz2

%attr(755,root,root) /usr/X11R6/lib/lib*.so.*
%attr(755,root,root) /usr/X11R6/bin/file_by_inode
%attr(755,root,root) /usr/X11R6/bin/libgtop_daemon
%attr(755,root,root) /usr/X11R6/bin/mkinodedb

/usr/X11R6/lib/libgtop-features.def

%lang(de)    /usr/X11R6/share/locale/de/LC_MESSAGES/libgtop.mo
%lang(es)    /usr/X11R6/share/locale/es/LC_MESSAGES/libgtop.mo
%lang(es_DO) /usr/X11R6/share/locale/es_DO/LC_MESSAGES/libgtop.mo
%lang(es_GT) /usr/X11R6/share/locale/es_GT/LC_MESSAGES/libgtop.mo
%lang(es_HN) /usr/X11R6/share/locale/es_HN/LC_MESSAGES/libgtop.mo
%lang(es_MX) /usr/X11R6/share/locale/es_MX/LC_MESSAGES/libgtop.mo
%lang(es_PA) /usr/X11R6/share/locale/es_PA/LC_MESSAGES/libgtop.mo
%lang(es_PE) /usr/X11R6/share/locale/es_PE/LC_MESSAGES/libgtop.mo
%lang(es_SV) /usr/X11R6/share/locale/es_SV/LC_MESSAGES/libgtop.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/libgtop.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/libgtop.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/libgtop.mo

%files devel
%defattr(644,root,root,755)
%doc RELNOTES* AUTHORS.bz2 ChangeLog.bz2 NEWS.bz2 README.bz2

%attr(755,root,root) /usr/X11R6/bin/libgtop-config

/usr/X11R6/lib/lib*.so

%attr(755,root,root) /usr/X11R6/lib/*.sh

/usr/X11R6/include/*

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.1-1]
- added LDFLAGS="-s" to ./configure enviroment,
- removed examples subpackage (added to Obsoletes),
- more locales (de, es, es_DO, es_GT, es_HN, es_MX, es_PA,
  es_PE, es_SV, ko, no),

  by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>

- build against GNU libc-2.1,
- compressed documentation,
- patch against empty macros.

* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.26.0-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- removed "Prereq: /sbin/install-info" from main package,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  and examples subpackages,
- added full %attr description in %files,
- removed copyright.txt from %doc (copyright statment is in Copyright
  field),
- some %doc moved to devel,
- added pl translation,
- removed Packager field (thi must be in private ~/.rpmrc),
- addes triping binaries and shared libtaries,
- changed prefix to /usr/X11R6,
- added stripping shared libraries.

* Tue Aug 19 1998 Martin Baulig <martin@home-of-linux.org>
- released LibGTop 0.25.0

* Sun Aug 16 1998 Martin Baulig <martin@home-of-linux.org>
- first version of the RPM
