Summary:	Block device driver to share storage to many machines over a network
Summary(pl.UTF-8):	Sterownik urządzenia blokowego do dzielenia pamięci między maszynami w sieci
Name:		gnbd
Version:	1.03.00
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://sources.redhat.com/pub/cluster/releases/cluster-%{version}.tar.gz
# Source0-md5:	8eea23df70d2007c4fb8c234cfea49cf
URL:		http://sources.redhat.com/cluster/gnbd/
BuildRequires:	magma-devel
BuildRequires:	perl-base
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
install -d %{name}/include/linux
install %{name}-kernel/src/gnbd.h %{name}/include/linux

cd %{name}
%{__perl} -pi -e 's/-Wall/%{rpmcflags} -Wall/' make/defines.mk.input
%{__perl} -pi -e 's/-O2 //' {client,server,tools/gnbd_{export,import}}/Makefile

%build
cd %{name}
./configure \
	--incdir=%{_includedir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--sbindir=%{_sbindir}
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
