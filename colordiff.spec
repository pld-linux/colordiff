%include	/usr/lib/rpm/macros.perl
Summary:	Perl script to colorize diffs
Summary(pl.UTF-8):	Skrypt w Perlu do kolorowania diffów
Name:		colordiff
Version:	1.0.6a
Release:	1
License:	GPL v3
Group:		Applications/Text
Source0:	http://colordiff.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	db49d0779a453c96f0859cd20b7b1aa9
URL:		http://colordiff.sourceforge.net/
BuildRequires:	rpm-perlprov
# Required for docs:
#BuildRequires:	xmlto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your diffs.

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
