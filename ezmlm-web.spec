Summary:	EZLM World Wide Web interface
Summary(pl):	Interfejs WWW do zarz�dcy list dyskusyjnych EZMLM
Name:		ezmlm-web
Version:	2.1
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	http://ftp.rucus.ru.ac.za/pub/mail/ezmlm/%{name}-%{version}.tar.gz
# Source0-md5:	41d701bc509c1a7fbec42f954e3e4171
Patch0:		%{name}.patch
Requires:	apache
Requires:	ezmlm-idx
Requires:	perl
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EZMLM-WEB is a CGI script that allows users on the web server to
easily create, edit (maintain), and delete mailing lists without
having to "bother" the system administrator.

%description -l pl
EZMLM-WEB to skrypt CGI pozwalaj�cy u�ytkownikom na �atwe tworzenie,
zarz�dzanie oraz kasowanie list dyskusyjnych bez zawracania g�owy
administratorowi systemu.

%prep
%setup -q
%patch -p1

%build
%{__cc} %{rpmldflags} %{rpmcflags} index.c -o index

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/srv/httpd/html/ezmlm}

install ezmlm-web.cgi	$RPM_BUILD_ROOT/srv/httpd/html/ezmlm
install .htaccess	$RPM_BUILD_ROOT/srv/httpd/html/ezmlm/.htaccess
install index		$RPM_BUILD_ROOT/srv/httpd/html/ezmml/ezmlm-web-index.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%dir /srv/httpd/html/ezmlm
/srv/httpd/html/ezmlm/.htaccess
%attr(755,root,root) /srv/httpd/html/ezmlm/*.cgi
