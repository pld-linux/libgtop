Summary:     LibGTop library
Summary(pl): Biblioteka LibGTop
Name:        libgtop
Version:     0.26.0
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.home-of-linux.org/pub/%{name}-%{version}.tar.gz
URL:         http://www.home-of-linux.org/gnome/libgtop/
BuildRoot:   /tmp/%{name}-%{version}-root

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
Summary:     Header files and etc for develop LibGTop applications
Summary(pl): Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o LibGTop
Group:       X11/libraries
Requires:    %{name} = %{version}

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o LibGTop.

%package static
Summary:     Static LibGTop libraries
Summary(pl): Biblioteki statyczne LibGTop
Group:       X11/libraries
Requires:    %{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%package examples
Summary:     Examples for LibGTop
Summary(pl): Przyk³ady do biblioteki LibGTop
Group:       X11/libraries
Requires:    %{name} = %{version}

%description examples
Examples for LibGTop.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 \
	--without-linux-table \
	--with-libgtop-inodedb
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/libexec

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

# Move all examples to /usr/X11R6/libexec/libgtop
mv $RPM_BUILD_ROOT/usr/X11R6/libexec $RPM_BUILD_ROOT/usr/X11R6/libgtop
mv $RPM_BUILD_ROOT/usr/X11R6/libgtop $RPM_BUILD_ROOT/usr/X11R6/libexec

strip $RPM_BUILD_ROOT/usr/X11R6/{libexec/*,bin/*,lib/lib*so.*.*} || :

rm -fr $RPM_BUILD_ROOT/usr/X11R6/include/libgtop

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc src/inodedb/README.inodedb
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
%attr(755, root, root) /usr/X11R6/bin/file_by_inode
%attr(755, root, root) /usr/X11R6/bin/libgtop_daemon
%attr(755, root, root) /usr/X11R6/bin/mkinodedb

%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/libgtop.mo

%files devel
%defattr(644, root, root, 755)
%doc RELNOTES* AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/X11R6/bin/libgtop-config
/usr/X11R6/lib/lib*.so
/usr/X11R6/lib/*.sh
/usr/X11R6/include/*

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%files examples
%attr(755, root, root) /usr/X11R6/libexec/*

%changelog
* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.26.0-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- removed "Prereq: /sbin/install-info" from main package,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  and examples subpackages,
- added full %attr description in %files,
- removed copyright.txt from %doc (copyright statment is in Copyright
  field),
- some %doc moved to devel,
- added pl translation,
- removed Packager field (thi must be in private ~/.rpmrc),
- addes triping binaries and shared libtaries,
- changed prefix to /usr/X11R6,
- added striping shared libraries.

* Tue Aug 19 1998 Martin Baulig <martin@home-of-linux.org>
- released LibGTop 0.25.0

* Sun Aug 16 1998 Martin Baulig <martin@home-of-linux.org>
- first version of the RPM
