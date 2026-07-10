%global tl_name arraycols
%global tl_revision 71168

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	New column types for array and tabular environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arraycols
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraycols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraycols.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraycols.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package provides new column types for array and tabular
environments, horizontally and vertically centered, or with adjusted
height for big mathematical expressions. The columns width can be fixed
or calculated like in tabularx environments. Macros for drawing vertical
and horizontal rules of variable thickness are also provided.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/arraycols
%dir %{_datadir}/texmf-dist/source/latex/arraycols
%dir %{_datadir}/texmf-dist/tex/latex/arraycols
%doc %{_datadir}/texmf-dist/doc/latex/arraycols/README.md
%doc %{_datadir}/texmf-dist/doc/latex/arraycols/arraycols.pdf
%doc %{_datadir}/texmf-dist/source/latex/arraycols/arraycols.dtx
%doc %{_datadir}/texmf-dist/source/latex/arraycols/arraycols.ins
%{_datadir}/texmf-dist/tex/latex/arraycols/arraycols.sty
