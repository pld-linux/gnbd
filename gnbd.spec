Summary:	Block device driver to share storage to many machines over a network
Summary(pl):	Sterownik urz±dzenia blokowego do dzielenia pamiêci miêdzy maszynami w sieci
Name:		gnbd
%define	snap	20040627
Version:	0.0.0.%{snap}.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}.tar.gz
# Source0-md5:	e8eba930e01dbf2cb413b82d8301ebef
URL:		http://sources.redhat.com/cluster/gnbd/
BuildRequires:	magma-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sbindir	/sbin

%description
The global network block device (GNBD) driver is similar to other
network block device drivers. Devices exported by GNBD servers can be
used by multiple clients making it suitable for use by a group of GFS
nodes.

%description -l pl
Sterownik GNBS (global network block device) jest podobny do innych
sterownikow sieciowych urz±dzeñ blokowych. Urz±dzenia wyeksportowane
przez serwery GNBD mog± byæ u¿ywane przez wielu klientów, co czyni
sterownik nadaj±cym siê do u¿ywania w grupie wêz³ów GFS.

%prep
%setup -q -n %{name}

%build
./configure \
	--incdir=%{_includedir} \
	--kernel_src=%{_kernelsrcdir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--sbindir=%{_sbindir}
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
