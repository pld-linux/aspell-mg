Summary:	Malagasy dictionary for aspell
Summary(pl):	S³ownik malgaski dla aspella
Name:		aspell-mg
Version:	0.03
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/mg/aspell5-mg-%{version}-%{subv}.tar.bz2
# Source0-md5:	f75e3b51a6935cd4be19c1ea452217a1
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Malagasy dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik malgaski (lista s³ów) dla aspella.

%prep
%setup -q -n aspell5-mg-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
