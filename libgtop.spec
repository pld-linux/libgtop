Summary:	LibGTop library
Summary(es):	Biblioteca libgtop
Summary(ja):	LibGTop �饤�֥��
Summary(pl):	Biblioteka LibGTop
Summary(pt_BR):	Biblioteca libgtop
Summary(ru):	���������� LibGTop
Summary(uk):	��̦����� LibGTop
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
Una biblioteca que obtiene informaci�n sobre el sistema como cpu y uso
de la memoria, procesos activos, etc. En sistemas Linux esta
informaci�n se obtiene directamente del sistema de archivos /proc.

%description -l ja
���Υ饤�֥��ϡ� CPU �����λ���Ψ�������ƥ��֥ץ����ʤɡ�
�¹���Υ����ƥ�ξ�������뤿��Τ�ΤǤ���

Linux �����ƥ�Ǥϡ����ξ����¾�Υץ���ब /dev/kmem �ʤɤ���
���Ф�����������äƤ��� /proc �ե����륷���ƥफ���ɤ߹��ޤ�ޤ���

%description -l pl
LibGTop jest bibliotek� do pozyskiwania informacji o uruchomionych
procesach jak zaj�to�� pami�ci i czasu procesora, aktywnych procesach
itd. Na Linuksie powy�sze informacje s� pozyskiwane bezpo�rednio z
systemu plikowego znajduj�cego si� w /proc, a na innych do pozyskania
powy�szych informacji wykorzystywane jest urz�dzenie /dev/kmem lub
jeszcze w inny spos�b zale�ny od systemu.

%description -l pt_BR
Uma biblioteca que obt�m informa��es sobre o sistema como cpu e uso da
mem�ria, processos ativos, etc. Em sistemas Linux estas informa��es
s�o obtidas diretamente do sistema de arquivos /proc.

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
Summary(es):	Bibliotecas e archivos de inclusi�n para desarrollar aplicaciones libgtop
Summary(ja):	LibGTop ���ץꥱ�����������Τ���Υ饤�֥�ꡢ���󥯥롼�ɥե�����䤽��¾�ե�����
Summary(pl):	Pliki nag��wkowe dla LibGTop
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolver aplica��es com a libgtop
Summary(ru):	����� ��� ���������� �������� � �������������� LibGTop
Summary(uk):	����� ��� �������� ������� � ������������� LibGTop
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gdbm-devel >= 1.8.3
Requires:	glib2-devel >= 1:2.6.2
Obsoletes:	libgtop1-devel

%description devel
Header files and etc for develop LibGTop applications.

%description devel -l es
Bibliotecas e archivos de inclusi�n para desarrollar aplicaciones
libgtop.

%description devel -l ja
CPU �����λ���Ψ�ʤɤΥ����ƥ����˥����������륢�ץꥱ��������
���������硢���Υѥå������򥤥󥹥ȡ��뤷�Ƥ���������

%description devel -l pl
Pliki nag��wkowe i inne potrzebne do tworzenia program�w opartych o
LibGTop.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolver aplica��es com a
libgtop.

%description devel -l ru
����������, ������ � ������ ����� ��� ���������� �������� �
�������������� LibGTop.

%description devel -l uk
��̦�����, ������ �� ��ۦ ����� ��� �������� ������� � �������������
LibGTop.

%package static
Summary:	Static LibGTop libraries
Summary(pl):	Biblioteki statyczne LibGTop
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libgtop
Summary(ru):	����������� ���������� ��� ���������� �������� � �������������� LibGTop
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� � ������������� LibGTop
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static LibGTop libraries.

%description static -l pl
Biblioteki statyczne LibGTop.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libgtop.

%description static -l uk
������Φ ¦�̦����� ��� �������� ������� � ������������� LibGTop.

%description static -l ru
����������� ���������� ��� ���������� �������� � ��������������
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
