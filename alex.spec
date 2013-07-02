%global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define module alex
Name:           %{module}
Version:        3.0.2
Release:        3
Summary:        Tool for generating lexical analysers in Haskell
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:	happy
BuildRequires:	docbook-style-xsl
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	libxml2
BuildRequires:	xmltex
BuildRequires:	gmp-devel
buildrequires:  haskell(QuickCheck)
BuildRequires:  ghc, ghc-devel, haskell-macros
buildrequires:  xsltproc, dblatex

%description
Alex is a tool for generating lexical analysers in Haskell, given a
description of the tokens to be recognised in the form of regular
expressions.  It is similar to the tool lex or flex for C/C++.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build
cd doc
test -f configure || autoreconf
./configure
make html

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_un

%files
%{_bindir}/%{module}
%{_docdir}/%{module}-%{version}
%{_datadir}/%{module}-%{version}
#% {_libdir}/% {module}-% {version}
%_cabal_rpm_deps_dir
#% _cabal_haddoc_files



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-3mdv2011.0
+ Revision: 609965
- rebuild

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 2.3.1-2mdv2010.1
+ Revision: 503520
- rebuild for new gmp

* Sat Nov 28 2009 Jérôme Brenier <incubusss@mandriva.org> 2.3.1-1mdv2010.1
+ Revision: 470827
- new version 2.3.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Thu Aug 07 2008 Adam Williamson <awilliamson@mandriva.org> 2.2-1mdv2009.0
+ Revision: 266817
- clean spec
- new release 2.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 25 2007 Gaëtan Lehmann <glehmann@mandriva.org> 2.1.0-1mdv2008.0
+ Revision: 71309
- 2.1.0


* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 2.0.1-3mdv2007.0
- rebuild

* Thu Oct 06 2005 Nicolas L�cureuil <neoclust@mandriva.org> 2.0.1-2mdk
- Fix BuildRequires

* Wed Jun 15 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.0.1-1mdk
- initial contrib

* Fri May 06 2005 Jens Petersen <petersen@redhat.com> - 2.0.1-1
- initial packaging for Fedora Haskell based on upstream spec file

