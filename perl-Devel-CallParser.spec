Name:           perl-Devel-CallParser
Version:        0.002
Release:        1%{?dist}
Summary:        Devel::CallParser - custom parsing attached to subroutines

License:        perl_5
URL:            https://metacpan.org/pod/Devel::CallParser
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Devel-CallParser-%{version}.tar.gz

#BuildArch:      
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Devel::CallChecker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(CPAN)

Requires:  perl(Devel::CallChecker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a C API, for XS modules, concerned with custom parsing. It is centred around the function cv_set_call_parser, which allows XS code to attach a magical annotation to a Perl subroutine, resulting in resolvable calls to that subroutine having their arguments parsed by arbitrary C code. (This is a more conveniently structured facility than the core's PL_keyword_plugin API.) This module makes cv_set_call_parser and several supporting functions available.

This module provides the implementation of the functions at runtime. It also, at compile time, supplies the C header file and link library which provide access to the functions. In normal use, "callparser0_h"/"callparser1_h" and "callparser_linkable" should be called at build time (not authoring time) for the module that wishes to use the C functions.

%prep
%autosetup -n Devel-CallParser-%{version}


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
* Tue Nov 07 2023 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.002
- Basic Perl type package
