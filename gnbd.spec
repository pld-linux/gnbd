Summary:	Block device driver to share storage to many machines over a network
Summary(pl):	Sterownik urz±dzenia blokowego do dzielenia pamiêci miêdzy maszynami w sieci
Name:		gnbd
Version:	1.0
%define	bver	pre13
Release:	0.%{bver}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://people.redhat.com/cfeist/cluster/tgz/%{name}-%{version}-%{bver}.tar.gz
# Source0-md5:	5b740659fd2930ce6da40b2cfe47f7df
# from gnbd-kernel CVS
Source1:	gnbd.h
# NoSource1-md5: f3e7cfe9f6a3c73e314488d6fea0957b (rev. 1.2)
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

%description -l pl
Sterownik GNBS (global network block device) jest podobny do innych
sterowników sieciowych urz±dzeñ blokowych. Urz±dzenia wyeksportowane
przez serwery GNBD mog± byæ u¿ywane przez wielu klientów, co czyni
sterownik nadaj±cym siê do u¿ywania w grupie wêz³ów GFS.

%prep
%setup -q -n %{name}-%{version}-%{bver}

install -d include/linux
cp %{SOURCE1} include/linux

%{__perl} -pi -e 's/-Wall/%{rpmcflags} -Wall/' make/defines.mk.input
%{__perl} -pi -e 's/-O2 //' {client,server,tools/gnbd_{export,import}}/Makefile

%build
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
