Name:           alex
Version:        2.0.1
Release:        %mkrel 3
License:        BSD-like
Group:          Development/Other
URL:            http://haskell.org/alex/
Source:         http://haskell.org/alex/dist/%{version}/alex-%{version}-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  happy, ghc, docbook-style-xsl, libxslt-proc, libxml2, xmltex
BuildRequires:  gmp-devel
Summary:        The lexer generator for Haskell

%description
Alex is a tool for generating lexical analysers in Haskell, given a
description of the tokens to be recognised in the form of regular
expressions.  It is similar to the tool lex or flex for C/C++.

# the debuginfo subpackage is currently empty anyway, so don't generate it
%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress

%define alexdir %{_libdir}/%{name}-%{version}

%prep
%setup -q

%build
test -f configure || autoreconf
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make
make html

%install
rm -rf ${RPM_BUILD_ROOT}
make install prefix=${RPM_BUILD_ROOT}%{_prefix} libdir=${RPM_BUILD_ROOT}%{alexdir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc alex/ANNOUNCE
%doc alex/LICENSE
%doc alex/README
%doc alex/TODO
%doc alex/doc/alex
%doc alex/examples
%{_bindir}/alex*
%{alexdir}

