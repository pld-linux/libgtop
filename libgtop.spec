Summary:	LibGTop library
Summary(ja):	LibGTop ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka LibGTop
Summary(ru):	âÉÂÌÉÏÔÅËÁ LibGTop
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ LibGTop
Name:		libgtop
Version:	1.0.13
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libgtop/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-amfix.patch
Patch2:		%{name}-ovflw.patch
Patch3:		%{name}-isdn.patch
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	gdbm-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	guile-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtop-examples
Obsoletes:	libgtop1

%define		_prefix		/usr/X11R6

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc. On Linux systems, these
information are taken directly from the /proc filesystem while on
other systems a server is used to read those information from
/dev/kmem or whatever.

%description -l ja
¤³¤Î¥é¥¤¥Ö¥é¥ê¤Ï¡¢ CPU ¤ä¥á¥â¥ê¤Î»ÈÍÑÎ¨¡¢¥¢¥¯¥Æ¥£¥Ö¥×¥í¥»¥¹¤Ê¤É¡¢
¼Â¹ÔÃæ¤Î¥·¥¹¥Æ¥à¤Î¾ðÊó¤òÆÀ¤ë¤¿¤á¤Î¤â¤Î¤Ç¤¹¡£

Linux ¥·¥¹¥Æ¥à¤Ç¤Ï¡¢¤³¤Î¾ðÊó¤ÏÂ¾¤Î¥×¥í¥°¥é¥à¤¬ /dev/kmem ¤Ê¤É¤«¤é
¼è¤ê½Ð¤·¤¿¾ðÊó¤ÎÆþ¤Ã¤Æ¤¤¤ë /proc ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤«¤éÆÉ¤ß¹þ¤Þ¤ì¤Þ¤¹¡£

%description -l pl
LibGTop jest bibliotek± do pozyskiwania informacji o uruchomionych
procesach jak zajêto¶æ pamiêci i czasu procesora, aktywnych procesach
itd. Na Linuxie powy¿sze informacje s± pozyskiwane bezpo¶rednio z
systemu plikowego znajduj±cego siê w /proc, a na innych do pozyskania
powy¿szych informacji wykorzystywane jest urz±dzenie /dev/kmem lub
jeszcze w inny sposób zale¿ny od systemu.

%description -l ru
âÉÂÌÉÏÔÅËÁ, ËÏÔÏÒÁÑ ÉÚ×ÌÅËÁÅÔ ÉÎÆÏÒÍÁÃÉÀ Ï ÒÁÂÏÔÁÀÝÅÊ ÓÉÓÔÅÍÅ, ÔÁËÕÀ
ËÁË ÉÓÐÏÌØÚÏ×ÁÎÉÅ ÐÁÍÑÔÉ É ÐÒÏÃÅÓÓÏÒÎÏÇÏ ×ÒÅÍÅÎÉ, ÁËÔÉ×ÎÙÅ ÐÒÏÃÅÓÓÙ É
ÄÒ.

îÁ ÓÉÓÔÅÍÁÈ Linux ÜÔÁ ÉÎÆÏÒÍÁÃÉÑ ÂÅÒÅÔÓÑ ÎÁÐÒÑÍÕÀ ÉÚ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÙ
/proc, ÔÏÇÄÁ ËÁË ÎÁ ÄÒÕÇÉÈ ÓÉÓÔÅÍÁÈ ÉÓÐÏÌØÚÕÅÔÓÑ ÓÅÒ×ÅÒ ÄÌÑ ÞÔÅÎÉÑ ÉÚ
ÔÁËÉÈ ÉÓÔÏÞÎÉËÏ× ËÁË /dev/kmem.

%description -l uk
â¦ÂÌ¦ÏÔÅËÁ, ÝÏ ÄÏÂÕ×Á¤ ¦ÎÆÏÒÍÁÃ¦À ÐÒÏ ÐÒÁÃÀÀÞÕ ÓÉÓÔÅÍÕ, ÔÁËÕ ÑË
×ÉËÏÒÉÓÔÁÎÎÑ ÐÁÍÑÔ¦ ÔÁ ÐÒÏÃÅÓÏÒÎÏÇÏ ÞÁÓÕ, ÁËÔÉ×Î¦ ÐÒÏÃÅÓÉ ÔÁ ¦ÎÛÅ.

îÁ ÓÉÓÔÅÍÁÈ Linux ÃÑ ¦ÎÆÏÒÍÁÃ¦Ñ ÂÅÒÅÔØÓÑ ÎÁÐÒÑÍÕ Ú ÆÁÊÌÏ×Ï§ ÓÉÓÔÅÍÉ
/proc, ÔÏÄ¦ ÑË ÎÁ ¦ÎÛÉÈ ÓÉÓÔÅÍÁÈ ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÓÅÒ×ÅÒ ÄÌÑ ÞÉÔÁÎÎÑ Ú
ÔÁËÉÈ ÄÖÅÒÅÌ ÑË /dev/kmem.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(ja):	LibGTop ¥¢¥×¥ê¥±¡¼¥·¥ç¥óºîÀ®¤Î¤¿¤á¤Î¥é¥¤¥Ö¥é¥ê¡¢¥¤¥ó¥¯¥ë¡¼¥É¥Õ¥¡¥¤¥ë¤ä¤½¤ÎÂ¾¥Õ¥¡¥¤¥ë
Summary(pl):	Pliki nag³ówkowe dla LibGTop
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ LibGTop
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libgtop1-devel

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l ja
CPU ¤ä¥á¥â¥ê¤Î»ÈÍÑÎ¨¤Ê¤É¤Î¥·¥¹¥Æ¥à¾ðÊó¤Ë¥¢¥¯¥»¥¹¤¹¤ë¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤ò
ºîÀ®¤¹¤ë¾ì¹ç¡¢¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Æ¤¯¤À¤µ¤¤¡£

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o
LibGTop.

%description devel -l ru
âÉÂÌÉÏÔÅËÉ, ÈÅÄÅÒÙ É ÄÒÕÇÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ LibGTop.

%description devel -l uk
â¦ÂÌ¦ÏÔÅËÉ, ÈÅÄÅÒÉ ÔÁ ¦ÎÛ¦ ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ LibGTop
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ LibGTop.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ
LibGTop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cd src/daemon
sed -e 's/.*-static//' Makefile.am > Makefile.am.tmp
mv -f Makefile.am.tmp Makefile.am

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros -I .
autoconf
automake -a -c -f
%configure \
	--without-linux-table \
	--with-libgtop-inodedb \
	--with-libgtop-smp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf src/inodedb/README.inodedb \
	RELNOTES* AUTHORS ChangeLog NEWS README

%find_lang %{name}

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
%{_infodir}/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
