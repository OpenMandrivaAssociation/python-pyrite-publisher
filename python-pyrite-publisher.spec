%define oname pyrite-publisher
%define version 2.1.1
%define release %mkrel 5

Summary: Content Creation Tools for Palm Computing Platform Users
Name: python-%{oname}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
URL: http://www.pyrite.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: python libpython-devel >= %{py_ver}
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
rm -rf %buildroot
python setup.py install --root %buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog NEWS PKG-INFO README.txt
%{_libdir}/python%{pyver}/site-packages/*
%{_bindir}/*

