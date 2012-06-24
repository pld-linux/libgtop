Summary:	LibGTop library
Summary(pl):	Biblioteka LibGTop
Name:		libgtop
Version:	1.0.1
Release:	2
Copyright:	LGPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.home-of-linux.org/pub/%{name}-%{version}.tar.gz
Patch:		libgtop-DESTDIR.patch
Requires:	glib = 1.2.1
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
LibGTop jest bibliotek� do pozyskiwania informacji o uruchomionych procesach
jak zaj�to�� pami�ci i czasu procesora, aktywnych procesach itd.

Na Linuxie powy�sze informacje s� pozyskiwane bezpo�rednio z systemu
plikowego znajduj�cego si� w /proc, a na innych do pozyskania powy�szych
informacji wykorzystywane jest urz�dzenie /dev/kmem lub jeszcze w inny
spos�b zale�ny od systemu.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(pl):	Pliki nag��wkowe dla LibGTop
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l pl
Pliki nag��wkowe i inne potrzebne do tworzenia program�w opartych o LibGTop.

%package	static
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
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--without-linux-table \
	--with-libgtop-inodedb
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

gzip -9nf src/inodedb/README.inodedb
gzip -9nf RELNOTES* AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc src/inodedb/README.inodedb.gz

%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*
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
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/libgtop.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/libgtop.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/libgtop.mo

%files devel
%defattr(644,root,root,755)
%doc {RELNOTES*,AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) /usr/X11R6/bin/libgtop-config
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/lib/*.sh

/usr/X11R6/include/*

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Sun Mar 14 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [1.0.1-2]
- gzipping documentation (instead bzipping)

* Thu Mar 11 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.1-1]
- changed Group in devel and static to X11/Development/Libraries,
- updated Requires (gnome-libs = 1.0.2, glib = 1.2.0),
- more locales (ja).

* Mon Jan 04 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99.1-1]
- added LDFLAGS="-s" to ./configure enviroment,
- removed examples subpackage (added to Obsoletes),
- more locales (de, es, es_DO, es_GT, es_HN, es_MX, es_PA,
  es_PE, es_SV, ko, no),

  by Wojtek �lusarczyk <wojtek@shadow.eu.org>

- build against GNU libc-2.1,
- compressed documentation,
- patch against empty macros.

* Fri Sep 25 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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
