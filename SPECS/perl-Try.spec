%define _tarball Try
Name:           perl-%{_tarball}
Version:        0.03
Release:        3%{?dist}
Summary:        Try - nicer exception handling syntax

License:        MIT
URL:            https://metacpan.org/pod/Try
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/%{_tarball}-%{version}.tar.gz

#BuildArch:      
BuildRequires:  perl >= 5.14
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Devel::CallParser)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

Requires:  perl >= 5.14
Requires:  perl(Devel::CallParser)
Requires:  perl(Exporter)
Requires:  perl(Try::Tiny)
Requires:  perl(XSLoader)
Requires:  perl(File::Find)
Requires:  perl(File::Temp)
Requires:  perl(Test::More)
Requires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module implements a try/catch/finally statement. It is based heavily on (and mostly implemented via) Try::Tiny. The differences are:

    * It is a statement. my $foo = try { ... } doesn't work anymore, but in return, you don't have to remember the trailing semicolon anymore. eval still works fine if you need an expression (in 5.14+ at least).

    * The blocks are ordered, and only one catch and finally block are supported. try { } finally { } catch { } and try { } catch { } finally { } finally { } do not work with this module, mostly because that's just extra complexity for no real purpose.

    * catch and finally are no longer exported - they are just part of the syntax of the try statement. This is almost certainly not an issue.


%prep
%autosetup -n %{_tarball}-%{version}


%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
# For arch-specific packages: vendorarch
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*


%changelog
* Thu Mar 14 2024 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.03-3
- SPEC file improvements
* Sat Feb 24 2024 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.03-2
- Better Requriements (Perl version is checked now)
* Tue Nov 07 2023 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.03-1
- Basic Perl type package
