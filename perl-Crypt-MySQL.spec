#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	MySQL
Summary:	Crypt::MySQL - emulate MySQL PASSWORD() function
Summary(pl.UTF-8):	Crypt::MySQL - emulacja funkcji MySQL PASSWORD()
Name:		perl-Crypt-MySQL
Version:	0.04
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e9a2d1e7f478fe8c90a15c47de37c0ae
URL:		http://search.cpan.org/dist/Crypt-MySQL/
%if %{with tests}
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Test-Simple >= 0.32}
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::MySQL emulates MySQL PASSWORD() SQL function, without
libmysqlclient. You can compare encrypted passwords, without real
MySQL environment.

%description -l pl.UTF-8
Crypt::MySQL emuluje funkcję SQL PASSWORD() z MySQL bez
libmysqlclient. Pozwala porównywać zaszyfrowane hasła bez prawdziwego
środowiska MySQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Crypt/MySQL.pm
%{perl_vendorarch}/Crypt/MySQL.xs
%dir %{perl_vendorarch}/auto/Crypt/MySQL
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/MySQL/MySQL.so
%{_mandir}/man3/*
