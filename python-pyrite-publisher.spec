%define oname pyrite-publisher

Summary: Content Creation Tools for Palm Computing Platform Users
Name: python-%{oname}
Version: 2.1.1
Release: 8
Source0: %{oname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
URL: https://www.pyrite.org/
BuildRequires: python
BuildRequires: python-devel
Requires: python
Obsoletes: txt2pdbdoc
Provides: txt2pdbdoc

%description
Pyrite Publisher is a data converter for Palm Computing Platform
users.  At the moment it is focused on producing e-books for use with
standard document readers.  It has the following features, and maybe
more:

  - converts text and HTML documents to the standard Doc format or the
    new high-compression zTXT format
  - gathers input from local files or from http/ftp URLs
  - produces rich text markup for RichReader or TealDoc
  - detects and reflows paragraphs in text files
  - automatically bookmarks HTML headers and named anchors
  - automatically bookmarks regular expressions in text files
  - supports zTXT annotations and both compression modes
  - annotates and/or footnotes HTML link targets
  - converts between Doc and zTXT while preserving bookmarks
  - converts Doc or zTXT back to text
  - processes Doc or zTXT content as if it is a regular text file
  - most behavior is configurable
  - architecture is extensible to allow addition of more kinds of
    document markup, more input formats, and even handling entirely
    new types of data

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
python setup.py install --root %buildroot

%files
%doc ChangeLog NEWS PKG-INFO README.txt
%{_libdir}/python%{py_ver}/site-packages/*
%{_bindir}/*



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.1.1-6mdv2010.0
+ Revision: 442460
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.1.1-5mdv2009.0
+ Revision: 242462
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 2.1.1-3mdv2008.0
+ Revision: 69372
- use %%mkrel


* Thu Feb 03 2005 Michael Scherer <misc@mandrake.org> 2.1.1-2mdk 
- fix spec file naming

* Wed Sep 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.1.1-1mdk
- 2.1.1

* Tue Aug 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.0-4mdk
- rebuild for new python
- drop Prefix tag

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.0.0-3mdk
- rebuild

* Fri Jul 19 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0.0-2mdk
- fix buildrequires

* Fri Jan 11 2002 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0.0-1mdk
- First release.

