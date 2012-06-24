Summary:	LibGTop library
Summary(ja):	LibGTop �饤�֥��
Summary(pl):	Biblioteka LibGTop
Summary(ru):	���������� LibGTop
Summary(uk):	��̦����� LibGTop
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
���Υ饤�֥��ϡ� CPU �����λ���Ψ�������ƥ��֥ץ����ʤɡ�
�¹���Υ����ƥ�ξ�������뤿��Τ�ΤǤ���

Linux �����ƥ�Ǥϡ����ξ����¾�Υץ���ब /dev/kmem �ʤɤ���
���Ф�����������äƤ��� /proc �ե����륷���ƥफ���ɤ߹��ޤ�ޤ���

%description -l pl
LibGTop jest bibliotek� do pozyskiwania informacji o uruchomionych
procesach jak zaj�to�� pami�ci i czasu procesora, aktywnych procesach
itd. Na Linuxie powy�sze informacje s� pozyskiwane bezpo�rednio z
systemu plikowego znajduj�cego si� w /proc, a na innych do pozyskania
powy�szych informacji wykorzystywane jest urz�dzenie /dev/kmem lub
jeszcze w inny spos�b zale�ny od systemu.

%description -l ru
����������, ������� ��������� ���������� � ���������� �������, �����
��� ������������� ������ � ������������� �������, �������� �������� �
��.

�� �������� Linux ��� ���������� ������� �������� �� �������� �������
/proc, ����� ��� �� ������ �������� ������������ ������ ��� ������ ��
����� ���������� ��� /dev/kmem.

%description -l uk
��̦�����, �� ������� �������æ� ��� �������� �������, ���� ��
������������ ����Ԧ �� ������������ ����, �����Φ ������� �� ����.

�� �������� Linux �� �������æ� �������� ������� � ������ϧ �������
/proc, ��Ħ �� �� ����� �������� ����������դ���� ������ ��� ������� �
����� ������ �� /dev/kmem.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Summary(ja):	LibGTop ���ץꥱ�����������Τ���Υ饤�֥�ꡢ���󥯥롼�ɥե�����䤽��¾�ե�����
Summary(pl):	Pliki nag��wkowe dla LibGTop
Summary(ru):	����� ��� ���������� �������� � �������������� LibGTop
Summary(uk):	����� ��� �������� ������� � ������������� LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libgtop1-devel

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l ja
CPU �����λ���Ψ�ʤɤΥ����ƥ����˥����������륢�ץꥱ��������
���������硢���Υѥå������򥤥󥹥ȡ��뤷�Ƥ���������

%description devel -l pl
Pliki nag��wkowe i inne potrzebne do tworzenia program�w opartych o
LibGTop.

%description devel -l ru
����������, ������ � ������ ����� ��� ���������� �������� �
�������������� LibGTop.

%description devel -l uk
��̦�����, ������ �� ��ۦ ����� ��� �������� ������� � �������������
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Summary(ru):	����������� ���������� ��� ���������� �������� � �������������� LibGTop
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� � ������������� LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%description static -l uk
������Φ ¦�̦����� ��� �������� ������� � ������������� LibGTop.

%description static -l ru
����������� ���������� ��� ���������� �������� � ��������������
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
