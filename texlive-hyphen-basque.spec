%global tl_name hyphen-basque
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Basque hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/basque
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-basque.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-basque.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Basque in T1/EC and UTF-8 encodings.

