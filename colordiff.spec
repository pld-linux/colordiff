%include	/usr/lib/rpm/macros.perl
Summary:	Perl script to colorize diffs
Summary(pl):	Skrypt w perlu do kolorowania diffów
Name:		colordiff
Version:	1.0.2
Release:	1
Group:		Applications/Text
License:	GPL
URL:		http://colorize.raszi.hu/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/colordiff/%{name}-%{version}.tar.gz
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your diffs

%description -l pl
Colorize jest krótkim skryptem w perlu który umo¿liwi Ci pokolorowanie
diffów.

%prep
%setup -q

gzip -9v %{name}.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install %{name}.pl $RPM_BUILD_ROOT%{_bindir}/
install %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/
install %{name}rc $RPM_BUILD_ROOT%{_sysconfdir}/%{name}rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README BUGS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
