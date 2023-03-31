Name:		texlive-crossrefenum
Version:	65016
Release:	2
Summary:	Smart typesetting of enumerated cross-references for various TeX formats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crossrefenum
License:	gpl3+ fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossrefenum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossrefenum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
crossrefenum lets TeX manage the formatting of bunches of
cross-references for you. It features: Automatic collapsing of
references; Support for references by various criteria,
including page and note number, line number in ConTeXt and
edpage and edline when used in conjunction with reledmac
Handling of references combining two criteria (e.g. by page and
note number) Extension mechanisms to add support to other types
of references without modifying the internal macros. Note that
sorting is not supported. I assume that users know in what
order the labels they refer to appear in their document. It is
written in Plain TeX as much as possible in order to make it
compatible with a wide array of formats. For the moment, it
works out of the box with ConTeXt and LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/crossrefenum
%doc %{_texmfdistdir}/doc/generic/crossrefenum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
