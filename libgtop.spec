Summary:	LibGTop library
Summary(es.UTF-8):	Biblioteca LibGTop
Summary(ja.UTF-8):	LibGTop ライブラリ
Summary(pl.UTF-8):	Biblioteka LibGTop
Summary(pt_BR.UTF-8):	Biblioteca LibGTop
Summary(ru.UTF-8):	Библиотека LibGTop
Summary(uk.UTF-8):	Бібліотека LibGTop
Name:		libgtop
Version:	2.22.3
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtop/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	57764ad246ceb959f601505aa2364f1f
Patch0:		%{name}-configure.patch
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libXau-devel
Obsoletes:	libgtop1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc. On Linux systems, these
information are taken directly from the /proc filesystem while on
other systems a server is used to read those information from
/dev/kmem or whatever.

%description -l es.UTF-8
Una biblioteca que obtiene información sobre el sistema como cpu y uso
de la memoria, procesos activos, etc. En sistemas Linux esta
información se obtiene directamente del sistema de archivos /proc.

%description -l ja.UTF-8
このライブラリは、 CPU やメモリの使用率、アクティブプロセスなど、
実行中のシステムの情報を得るためのものです。

Linux システムでは、この情報は他のプログラムが /dev/kmem などから
取り出した情報の入っている /proc ファイルシステムから読み込まれます。

%description -l pl.UTF-8
LibGTop jest biblioteką do pozyskiwania informacji o uruchomionych
procesach jak zajętość pamięci i czasu procesora, aktywnych procesach
itd. Na Linuksie powyższe informacje są pozyskiwane bezpośrednio z
systemu plikowego znajdującego się w /proc, a na innych do pozyskania
powyższych informacji wykorzystywane jest urządzenie /dev/kmem lub
jeszcze w inny sposób zależny od systemu.

%description -l pt_BR.UTF-8
Uma biblioteca que obtém informações sobre o sistema como cpu e uso da
memória, processos ativos, etc. Em sistemas Linux estas informações
são obtidas diretamente do sistema de arquivos /proc.

%description -l ru.UTF-8
Библиотека, которая извлекает информацию о работающей системе, такую
как использование памяти и процессорного времени, активные процессы и
др.

На системах Linux эта информация берется напрямую из файловой системы
/proc, тогда как на других системах используется сервер для чтения из
таких источников как /dev/kmem.

%description -l uk.UTF-8
Бібліотека, що добуває інформацію про працюючу систему, таку як
використання памяті та процесорного часу, активні процеси та інше.

На системах Linux ця інформація береться напряму з файлової системи
/proc, тоді як на інших системах використовується сервер для читання з
таких джерел як /dev/kmem.

%package apidocs
Summary:	LibGTop API documentation
Summary(pl.UTF-8):	Dokumentacja API LibGTop
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
LibGTop API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API LibGTop.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(es.UTF-8):	Bibliotecas e archivos de inclusión para desarrollar aplicaciones LibGTop
Summary(ja.UTF-8):	LibGTop アプリケーション作成のためのライブラリ、インクルードファイルやその他ファイル
Summary(pl.UTF-8):	Pliki nagłówkowe dla LibGTop
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolver aplicações com a LibGTop
Summary(ru.UTF-8):	Файлы для разработки программ с использованием LibGTop
Summary(uk.UTF-8):	Файли для розробки програм з використанням LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gdbm-devel >= 1.8.3
Requires:	glib2-devel >= 1:2.16.0
Requires:	xorg-lib-libXau-devel
Obsoletes:	libgtop1-devel

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l es.UTF-8
Bibliotecas e archivos de inclusión para desarrollar aplicaciones
LibGTop.

%description devel -l ja.UTF-8
CPU やメモリの使用率などのシステム情報にアクセスするアプリケーションを
作成する場合、このパッケージをインストールしてください。

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne potrzebne do tworzenia programów opartych o
LibGTop.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolver aplicações com a
LibGTop.

%description devel -l ru.UTF-8
Библиотеки, хедеры и другие файлы для разработки программ с
использованием LibGTop.

%description devel -l uk.UTF-8
Бібліотеки, хедери та інші файли для розробки програм з використанням
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl.UTF-8):	Biblioteki statyczne LibGTop
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com LibGTop
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с использованием LibGTop
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з використанням LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static LibGTop libraries.

%description static -l pl.UTF-8
Biblioteki statyczne LibGTop.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com LibGTop.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм з використанням LibGTop.

%description static -l ru.UTF-8
Статические библиотеки для разработки программ с использованием
LibGTop.

%package examples
Summary:	LibGTop - example programs
Summary(pl.UTF-8):	LibGTop - przykładowe programy
Group:		X11/Development/Libraries

%description examples
LibGTop - example programs.

%description examples -l pl.UTF-8
LibGTop - przykładowe programy.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-linux-table=no \
	--with-libgtop-inodedb \
	--with-libgtop-smp \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtop-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtop-2.0.so.7

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtop-2.0.so
%{_libdir}/libgtop-2.0.la
%{_includedir}/libgtop-2.0
%{_infodir}/*info*
%{_pkgconfigdir}/libgtop-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtop-2.0.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
