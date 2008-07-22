Name:           alex
Version:        2.1.0
Release:        %mkrel 3
License:        BSD-like
Group:          Development/Other
URL:            http://haskell.org/alex/
Source:         http://haskell.org/alex/dist/%{version}/alex-%{version}.tar.gz
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

%define alexdir %{_datadir}/%{name}-%{version}

%prep
%setup -q

%build
runhaskell Setup.lhs configure --prefix=%{_prefix}
runhaskell Setup.lhs build
cd doc
test -f configure || autoreconf
./configure
make html

%install
rm -rf ${RPM_BUILD_ROOT}

runhaskell Setup.lhs copy --destdir=${RPM_BUILD_ROOT}


%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc ANNOUNCE  LICENSE  README  Setup.lhs  TODO examples
%{_bindir}/alex*
%{alexdir}

