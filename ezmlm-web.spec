Summary:	EZLM World Wide Web Interface
Summary(pl):	Interfejs WWW do menad¿era list dyskusyjnych EZMLM
Name:		ezmlm-web
Version:	1.0
Release:	1
Group:		Networking/Daemons
Source0:	ftp://rucus.ru.ac.za/pub/mail/ezmlm/%{name}-%{version}.tar.gz
Source1:	ezmlm-web-setup
Patch:		ezmlm-web.patch
Copyright:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	apache
Requires:	ezmlm-idx
Requires:	perl
Requires:	qmail

%description
EZMLM-WEB is a CGI script that allows users on the web server to easily
create, edit (maintain), and delete mailing lists without having to
"bother" the system administrator.

%description -l pl
EZMLM-WEB to skrypt CGI pozwalaj±cy u¿ytkownikom na ³atwe tworzenie,
zarz±dzanie oraz kasowanie list dyskusyjnych bez zawracania g³owy
administratorowi systemu.

%prep
%setup -q
%patch -p1 -b .orig

%build
cc -s $RPM_OPT_FLAGS index.c -o index

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/httpd/ezmlm
install -d $RPM_BUILD_ROOT/var/state/list
install -d $RPM_BUILD_ROOT%{_bindir}

install	ezmlm-web.cgi	$RPM_BUILD_ROOT/etc/httpd/ezmlm/
install	.htaccess	$RPM_BUILD_ROOT/etc/httpd/ezmlm/ezmlm-web-htaccess
install	index		$RPM_BUILD_ROOT/etc/httpd/ezmlm/ezmlm-web-index.cgi
install %{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}/setup-ezmlm-web

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
%attr(644,root,root)  %doc {CHANGES,README,TODO}.gz
%attr(755,root,root)  %dir /etc/httpd/ezmlm
%attr(755,root,root)  /etc/httpd/ezmlm/ezmlm*
%{_bindir}/*
