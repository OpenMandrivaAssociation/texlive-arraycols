Name:		texlive-arraycols
Version:	61719
Release:	1
Summary:	New column types for array and tabular environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arraycols
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arraycols.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arraycols.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arraycols.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package provides new column types for array and
tabular environments, horizontally and vertically centered, or
with adjusted height for big mathematical expressions. The
columns width can be fixed or calculated like in tabularx
environments. Macros for drawing vertical and horizontal rules
of variable thickness are also provided.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/arraycols
%{_texmfdistdir}/tex/latex/arraycols
%doc %{_texmfdistdir}/doc/latex/arraycols

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
