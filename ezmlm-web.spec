Summary:	EZLM World Wide Web interface
Summary(pl):	Interfejs WWW do zarz±dcy list dyskusyjnych EZMLM
Name:		ezmlm-web
Version:	1.0
Release:	2
Group:		Networking/Daemons
Source0:	ftp://rucus.ru.ac.za/pub/mail/ezmlm/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	apache
Requires:	ezmlm-idx
Requires:	perl
Requires:	qmail

%description
EZMLM-WEB is a CGI script that allows users on the web server to
easily create, edit (maintain), and delete mailing lists without
having to "bother" the system administrator.

%description -l pl
EZMLM-WEB to skrypt CGI pozwalaj±cy u¿ytkownikom na ³atwe tworzenie,
zarz±dzanie oraz kasowanie list dyskusyjnych bez zawracania g³owy
administratorowi systemu.

%prep
%setup -q
%patch -p1
%build
%{__cc} %{rpmldflags} %{rpmcflags} index.c -o index

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/home/httpd/html/ezmlm}

install ezmlm-web.cgi	$RPM_BUILD_ROOT/home/httpd/html/ezmlm/
install .htaccess	$RPM_BUILD_ROOT/home/httpd/html/ezmlm/.htaccess
install index		$RPM_BUILD_ROOT/home/httpd/html/ezmml/ezmlm-web-index.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %dir /home/httpd/html/ezmlm
%attr(644,root,root) /home/httpd/html/ezmlm/.htaccess
%attr(755,root,root) /home/httpd/html/ezmlm/*.cgi
