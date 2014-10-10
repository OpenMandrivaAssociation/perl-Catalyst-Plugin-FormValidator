%define upstream_name    Catalyst-Plugin-FormValidator
%define upstream_version 0.094

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	FormValidator for Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 2.99
BuildRequires:	perl(Data::FormValidator)
BuildArch:	noarch

%description
This plugin uses Data::FormValidator to validate and set up form data
from your request parameters. It's a quite thin wrapper around that
module, so most of the relevant information can be found there.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.94.0-2mdv2011.0
+ Revision: 680734
- mass rebuild

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.94.0-1mdv2011.0
+ Revision: 513471
- update to 0.094

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.92.0-1mdv2010.1
+ Revision: 510072
- update to 0.092
- update to 0.05

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 406262
- rebuild using %%perl_convert_version

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2010.0
+ Revision: 371225
- update to new version 0.03

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-4mdv2009.0
+ Revision: 255553
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-2mdv2008.1
+ Revision: 136677
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2008.0
+ Revision: 86032
- rebuild


* Sun Jan 02 2005 Scott Karns <scott@karnstech.com> 0.02-1mdk
- Initial Mdv RPM

