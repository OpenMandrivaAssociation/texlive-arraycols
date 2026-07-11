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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package provides new column types for array and tabular
environments, horizontally and vertically centered, or with adjusted
height for big mathematical expressions. The columns width can be fixed
or calculated like in tabularx environments. Macros for drawing vertical
and horizontal rules of variable thickness are also provided.

