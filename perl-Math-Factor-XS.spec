#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Factor-XS
Summary:	Math::Factor::XS - Factorize numbers and calculate matching multiplications
Name:		perl-Math-Factor-XS
Version:	0.40
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fec7d1291fd9fecebe316d57f2a16cd3
URL:		http://search.cpan.org/dist/Math-Factor-XS/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-boolean
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Factor::XS factorizes numbers by applying trial divisions.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%dir %{perl_vendorarch}/Math/Factor
%{perl_vendorarch}/Math/Factor/XS.pm
%dir %{perl_vendorarch}/auto/Math/Factor
%dir %{perl_vendorarch}/auto/Math/Factor/XS
%{perl_vendorarch}/auto/Math/Factor/XS/XS.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Factor/XS/XS.so
%{_mandir}/man3/*
