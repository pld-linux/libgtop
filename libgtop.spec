Summary:	LibGTop library
Summary(ja):	LibGTop ライブラリ
Summary(pl):	Biblioteka LibGTop
Summary(ru):	睇駄貧堙冒 LibGTop
Summary(uk):	皃駄ο堙冒 LibGTop
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
このライブラリは、 CPU やメモリの使用率、アクティブプロセスなど、
実行中のシステムの情報を得るためのものです。

Linux システムでは、この情報は他のプログラムが /dev/kmem などから
取り出した情報の入っている /proc ファイルシステムから読み込まれます。

%description -l pl
LibGTop jest bibliotek� do pozyskiwania informacji o uruchomionych
procesach jak zaj�to倶 pami�ci i czasu procesora, aktywnych procesach
itd. Na Linuxie powy�sze informacje s� pozyskiwane bezpo�rednio z
systemu plikowego znajduj�cego si� w /proc, a na innych do pozyskania
powy�szych informacji wykorzystywane jest urz�dzenie /dev/kmem lub
jeszcze w inny spos�b zale�ny od systemu.

%description -l ru
睇駄貧堙冒, 墨塹卅� 冨很屠租� 瀕届厖礎廟 � 卅堆堊摂妬 喇嘖斗�, 堊釦�
冒� 瓶佻蒙斛彖良� 仭用塢 � 侑話途嗜厠惑� 徠斗杜�, 阻塢徇拇 侑話途噎 �
漬.

鄙 喇嘖斗組 Linux 榑� 瀕届厖礎頻 妥凖墫� 料侑冤媽 冨 徳別�從� 喇嘖斗�
/proc, 塹把� 冒� 料 漬嫻蛭 喇嘖斗組 瓶佻蒙旁都嗔 單叟賭 通� 湟杜頻 冨
堊防� 瓶塹淮彬�� 冒� /dev/kmem.

%description -l uk
皃駄ο堙冒, 殤 掴怠彖� ξ届厖礎�� 侑� 侑礎誓渾 喇嘖斗�, 堊釦 冕
徂墨夘嘖僧倫 仭用圖 堊 侑話途碗力馬 涸嗾, 阻塢徇� 侑話途� 堊 ξ枦.

鄙 喇嘖斗組 Linux 恥 ξ届厖礎ρ 妥凖墮嗔 料侑冤� � 徳別�從� 喇嘖斗�
/proc, 塹彫 冕 料 ξ柯� 喇嘖斗組 徂墨夘嘖�徼ぴ慯� 單叟賭 通� 淺堊領� �
堊防� 綴賭徒 冕 /dev/kmem.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(ja):	LibGTop アプリケーション作成のためのライブラリ、インクルードファイルやその他ファイル
Summary(pl):	Pliki nag鞄wkowe dla LibGTop
Summary(ru):	譱別� 通� 卅斷疎�塰� 侑惑卅様 � 瓶佻蒙斛彖良斗 LibGTop
Summary(uk):	譱別� 通� 厦斷和防 侑惑卅� � 徂墨夘嘖僧倫� LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libgtop1-devel

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l ja
CPU やメモリの使用率などのシステム情報にアクセスするアプリケーションを
作成する場合、このパッケージをインストールしてください。

%description devel -l pl
Pliki nag鞄wkowe i inne potrzebne do tworzenia program�w opartych o
LibGTop.

%description devel -l ru
睇駄貧堙防, 氾津燮 � 漬嫻錨 徳別� 通� 卅斷疎�塰� 侑惑卅様 �
瓶佻蒙斛彖良斗 LibGTop.

%description devel -l uk
皃駄ο堙防, 氾津夘 堊 ξ昿 徳別� 通� 厦斷和防 侑惑卅� � 徂墨夘嘖僧倫�
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Summary(ru):	黌壮扶途防� 舵駄貧堙防 通� 卅斷疎�塰� 侑惑卅様 � 瓶佻蒙斛彖良斗 LibGTop
Summary(uk):	黌壮扶陸 側駄ο堙防 通� 厦斷和防 侑惑卅� � 徂墨夘嘖僧倫� LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%description static -l uk
黌壮扶陸 側駄ο堙防 通� 厦斷和防 侑惑卅� � 徂墨夘嘖僧倫� LibGTop.

%description static -l ru
黌壮扶途防� 舵駄貧堙防 通� 卅斷疎�塰� 侑惑卅様 � 瓶佻蒙斛彖良斗
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
