# NOTE: obsolete, for 3rd generation cluster see cluster.spec
Summary:	Block device driver to share storage to many machines over a network
Summary(pl.UTF-8):	Sterownik urządzenia blokowego do dzielenia pamięci między maszynami w sieci
Name:		gnbd
Version:	2.03.11
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://sources.redhat.com/pub/cluster/releases/cluster-%{version}.tar.gz
# Source0-md5:	712b9f583472d1de614641bc0f4a0aaf
Patch0:		cluster-kernel.patch
URL:		http://sources.redhat.com/cluster/gnbd/
BuildRequires:	cman-devel >= 2.03.10
BuildRequires:	perl-base
Requires:	cman-libs >= 2.03.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The global network block device (GNBD) driver is similar to other
network block device drivers. Devices exported by GNBD servers can be
used by multiple clients making it suitable for use by a group of GFS
nodes.

%description -l pl.UTF-8
Sterownik GNBS (global network block device) jest podobny do innych
sterowników sieciowych urządzeń blokowych. Urządzenia wyeksportowane
przez serwery GNBD mogą być używane przez wielu klientów, co czyni
sterownik nadającym się do używania w grupie węzłów GFS.

%prep
%setup -q -n cluster-%{version}
%patch -P0 -p1

%build
./configure \
	--cc="%{__cc}" \
	--cflags="%{rpmcflags} -Wall" \
	--ldflags="%{rpmldflags}" \
	--incdir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--sbindir=%{_sbindir} \
	--without_gfs \
	--without_gfs2 \
	--without_kernel_modules
%{__make} -C %{name}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C %{name} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/gnbd_*
%{_mandir}/man8/gnbd*.8*
