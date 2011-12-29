# revision 23085
# category TLCore
# catalog-ctan /language/basque
# catalog-date 2009-09-24 15:05:48 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-hyphen-basque
Version:	20090924
Release:	1
Summary:	Basque hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/basque
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-basque.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Basque in T1/EC and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-basque
%_texmf_language_def_d/hyphen-basque
%_texmf_language_lua_d/hyphen-basque

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-basque <<EOF
%% from hyphen-basque:
basque loadhyph-eu.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-basque <<EOF
%% from hyphen-basque:
\addlanguage{basque}{loadhyph-eu.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-basque <<EOF
-- from hyphen-basque:
	['basque'] = {
		loader = 'loadhyph-eu.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-eu.pat.txt',
		hyphenation = '',
	},
EOF
