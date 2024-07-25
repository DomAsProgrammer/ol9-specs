%define _tarball Variable-Alias
Name:           perl-%{_tarball}
Version:        0.01
Release:        3%{?dist}
Summary:        Variable::Alias - Alias any variable to any other variable

License:        unknown
URL:            https://metacpan.org/release/BRENTDAX/Variable-Alias-0.01/view/Alias.pm
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRENTDAX/%{_tarball}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl-generators
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Switch)
BuildRequires:  perl(Test::More)

Requires:  perl >= 5.8.0
Requires:  perl(Switch)
Requires:  perl(Test::More)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
There are various ways to alias one variable to another in Perl. The most popular is by assigning to typeglobs. This is quite efective, but only works with globals. Another method is to use a module like Lexical::Alias or Devel::LexAlias, but as their names suggest, these only work with lexicals. There's no way to alias an element of an array or hash.

Variable::Alias changes all that. It uses a tie to provide One True Way to alias a variable.

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
# For noarch packages: vendorlib
%{perl_vendorlib}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*


%changelog
* Thu Mar 14 2024 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.01-3
- SPEC file improvements
* Sat Feb 24 2024 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.01-2
- Better Requriements (Perl version is checked now)
* Tue Nov 07 2023 Dominik Bernhardt <domasprogrammer@gmail.com> - 0.01-1
- Basic Perl type package
