Name:		alex
Summary:	The lexer generator for Haskell
Version:	2.2
Release:	%mkrel 3
License:	BSD
Group:		Development/Other
URL:		http://haskell.org/alex/
Source0:	http://haskell.org/alex/dist/%{version}/alex-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	happy
BuildRequires:	ghc
BuildRequires:	docbook-style-xsl
BuildRequires:	libxslt-proc
BuildRequires:	libxml2
BuildRequires:	xmltex
BuildRequires:	gmp-devel

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
rm -rf %{buildroot}

runhaskell Setup.lhs copy --destdir=%{buildroot}

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ANNOUNCE  LICENSE  README  Setup.lhs  TODO examples
%{_bindir}/alex*
%{alexdir}

