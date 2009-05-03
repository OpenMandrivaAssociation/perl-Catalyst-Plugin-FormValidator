%define realname Catalyst-Plugin-FormValidator
%define name	perl-%{realname}
%define version 0.03
%define release %mkrel 1

Summary:	FormValidator for Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(Data::FormValidator)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This plugin uses Data::FormValidator to validate and set up form data
from your request parameters. It's a quite thin wrapper around that
module, so most of the relevant information can be found there.


%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst/*

%clean
rm -rf $RPM_BUILD_ROOT

