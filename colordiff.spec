%include	/usr/lib/rpm/macros.perl
Summary:	Perl script to colorize diffs
Summary(pl):	Skrypt w perlu do kolorowania diff�w
Name:		colordiff
Version:	1.0.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/colordiff/%{name}-%{version}.tar.gz
# Source0-md5:	ccdeeae7555b9fcbb7b8c47b3a92f904
URL:		http://colorize.raszi.hu/
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your diffs.

%description -l pl
Colorize jest kr�tkim skryptem w perlu umo�liwiaj�cym pokolorowanie
diff�w.

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
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
