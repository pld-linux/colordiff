Summary:	Perl script to colorize diffs
Summary(hu.UTF-8):	Egy Perl szkript, amely a diff kimenetét teszi színessé
Summary(pl.UTF-8):	Skrypt w Perlu do kolorowania diffów
Name:		colordiff
Version:	1.0.10
Release:	1
License:	GPL v3
Group:		Applications/Text
Source0:	http://colordiff.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	e3e86e2837deb884e43eacdc96a67baa
URL:		http://colordiff.sourceforge.net/
BuildRequires:	rpm-perlprov
# Required for docs:
#BuildRequires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your diffs.

%description -l hu.UTF-8
Ez a rövidke perl szkript a diff parancs kimenetét teszi színek
segítségével olvashatóbbá.

%description -l pl.UTF-8
Colorize jest krótkim skryptem w Perlu umożliwiającym pokolorowanie
diffów.

%prep
%setup -q

%build
# fails right now
#%{__make} -j1 doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install %{name}.pl $RPM_BUILD_ROOT%{_bindir}/colordiff
install cdiff.sh $RPM_BUILD_ROOT%{_bindir}/cdiff
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}rc $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man1/*
