Summary:	LibGTop library
Summary(es):	Biblioteca libgtop
Summary(ja):	LibGTop ¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka LibGTop
Summary(pt_BR):	Biblioteca libgtop
Summary(ru):	âÉÂÌÉÏÔÅËÁ LibGTop
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ LibGTop
Name:		libgtop
Version:	2.12.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgtop/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	050e0d7834a3e73f693895e0a3130917
Patch0:		%{name}-configure.patch
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	texinfo
Obsoletes:	libgtop-examples
Obsoletes:	libgtop1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc. On Linux systems, these
information are taken directly from the /proc filesystem while on
other systems a server is used to read those information from
/dev/kmem or whatever.

%description -l es
Una biblioteca que obtiene información sobre el sistema como cpu y uso
de la memoria, procesos activos, etc. En sistemas Linux esta
información se obtiene directamente del sistema de archivos /proc.

%description -l ja
¤³¤Î¥é¥¤¥Ö¥é¥ê¤Ï¡¢ CPU ¤ä¥á¥â¥ê¤Î»ÈÍÑÎ¨¡¢¥¢¥¯¥Æ¥£¥Ö¥×¥í¥»¥¹¤Ê¤É¡¢
¼Â¹ÔÃæ¤Î¥·¥¹¥Æ¥à¤Î¾ðÊó¤òÆÀ¤ë¤¿¤á¤Î¤â¤Î¤Ç¤¹¡£

Linux ¥·¥¹¥Æ¥à¤Ç¤Ï¡¢¤³¤Î¾ðÊó¤ÏÂ¾¤Î¥×¥í¥°¥é¥à¤¬ /dev/kmem ¤Ê¤É¤«¤é
¼è¤ê½Ð¤·¤¿¾ðÊó¤ÎÆþ¤Ã¤Æ¤¤¤ë /proc ¥Õ¥¡¥¤¥ë¥·¥¹¥Æ¥à¤«¤éÆÉ¤ß¹þ¤Þ¤ì¤Þ¤¹¡£

%description -l pl
LibGTop jest bibliotek± do pozyskiwania informacji o uruchomionych
procesach jak zajêto¶æ pamiêci i czasu procesora, aktywnych procesach
itd. Na Linuksie powy¿sze informacje s± pozyskiwane bezpo¶rednio z
systemu plikowego znajduj±cego siê w /proc, a na innych do pozyskania
powy¿szych informacji wykorzystywane jest urz±dzenie /dev/kmem lub
jeszcze w inny sposób zale¿ny od systemu.

%description -l pt_BR
Uma biblioteca que obtém informações sobre o sistema como cpu e uso da
memória, processos ativos, etc. Em sistemas Linux estas informações
são obtidas diretamente do sistema de arquivos /proc.

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
Summary(es):	Bibliotecas e archivos de inclusión para desarrollar aplicaciones libgtop
Summary(ja):	LibGTop ¥¢¥×¥ê¥±¡¼¥·¥ç¥óºîÀ®¤Î¤¿¤á¤Î¥é¥¤¥Ö¥é¥ê¡¢¥¤¥ó¥¯¥ë¡¼¥É¥Õ¥¡¥¤¥ë¤ä¤½¤ÎÂ¾¥Õ¥¡¥¤¥ë
Summary(pl):	Pliki nag³ówkowe dla LibGTop
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolver aplicações com a libgtop
Summary(ru):	æÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ LibGTop
Summary(uk):	æÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gdbm-devel >= 1.8.3
Requires:	glib2-devel >= 1:2.6.2
Obsoletes:	libgtop1-devel

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l es
Bibliotecas e archivos de inclusión para desarrollar aplicaciones
libgtop.

%description devel -l ja
CPU ¤ä¥á¥â¥ê¤Î»ÈÍÑÎ¨¤Ê¤É¤Î¥·¥¹¥Æ¥à¾ðÊó¤Ë¥¢¥¯¥»¥¹¤¹¤ë¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤ò
ºîÀ®¤¹¤ë¾ì¹ç¡¢¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Æ¤¯¤À¤µ¤¤¡£

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o
LibGTop.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolver aplicações com a
libgtop.

%description devel -l ru
âÉÂÌÉÏÔÅËÉ, ÈÅÄÅÒÙ É ÄÒÕÇÉÅ ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó
ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ LibGTop.

%description devel -l uk
â¦ÂÌ¦ÏÔÅËÉ, ÈÅÄÅÒÉ ÔÁ ¦ÎÛ¦ ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libgtop
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ LibGTop
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libgtop.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ LibGTop.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ
LibGTop.

%prep
%setup -q
%patch0 -p1

cd src/daemon
sed -e 's/.*-static//' Makefile.am > Makefile.am.tmp
mv -f Makefile.am.tmp Makefile.am
cd ../../examples
sed -e 's/.*-static//' Makefile.am > Makefile.am.tmp
mv -f Makefile.am.tmp Makefile.am

%build
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-linux-table=no \
	--with-libgtop-inodedb \
	--with-libgtop-smp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove bogus es_ES locale (empty while there is non-empty es)
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README src/inodedb/README.inodedb
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/file_by_inode2
%attr(755,root,root) %{_bindir}/mkinodedb2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libgtop-2.0
%{_infodir}/*info*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
