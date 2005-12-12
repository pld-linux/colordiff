%include	/usr/lib/rpm/macros.perl
Summary:	Perl script to colorize diffs
Summary(pl):	Skrypt w Perlu do kolorowania diffów
Name:		colordiff
Version:	1.0.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/colordiff/%{name}-%{version}.tar.gz
# Source0-md5:	b8ef81a80dfa8a4c001915d03a73f7d1
URL:		http://colordiff.sourceforge.net/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your diffs.

%description -l pl
Colorize jest krótkim skryptem w Perlu umo¿liwiaj±cym pokolorowanie
diffów.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install %{name}.pl $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}rc $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README BUGS TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man1/*
