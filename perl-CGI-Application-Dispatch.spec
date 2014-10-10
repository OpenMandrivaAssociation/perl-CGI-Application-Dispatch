%define upstream_name    CGI-Application-Dispatch
%define upstream_version 2.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Dispatch requests to CGI::Application based object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Exception::Class::TryCatch)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a way (as a mod_perl handler or running under vanilla CGI)
to look at the path ($r->path_info or $ENV{PATH_INFO}) of the incoming request,
parse off the desired module and it's run mode, create an instance of that
module and run it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes TODO
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.180.0-2mdv2011.0
+ Revision: 656882
- rebuild for updated spec-helper

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.180.0-1mdv2011.0
+ Revision: 628699
- update to new version 2.18

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.170.0-1mdv2011.0
+ Revision: 484370
- update to 2.17

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.160.0-1mdv2010.0
+ Revision: 405770
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.16-1mdv2010.0
+ Revision: 370015
- update to new version 2.16

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.15-1mdv2009.1
+ Revision: 311977
- update to new version 2.15

* Tue Nov 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.14-1mdv2009.1
+ Revision: 299748
- update to new version 2.14

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.13-1mdv2009.1
+ Revision: 292885
- import perl-CGI-Application-Dispatch


* Thu Oct 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.13-1mdv2009.1
- initial mdv release, generated with cpan2dist

