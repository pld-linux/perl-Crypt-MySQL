#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	MySQL
Summary:	Crypt::MySQL - emulate MySQL PASSWORD() function
Summary(pl.UTF-8):   Crypt::MySQL - emulacja funkcji MySQL PASSWORD()
Name:		perl-Crypt-MySQL
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dfaf418d37f4f690f8e69a2e03e74371
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.32}
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
%dir %{perl_vendorarch}/auto/Crypt/MySQL
%{perl_vendorarch}/auto/Crypt/MySQL/autosplit.ix
%{perl_vendorarch}/auto/Crypt/MySQL/MySQL.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/MySQL/MySQL.so
%{_mandir}/man3/*
