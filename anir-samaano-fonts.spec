# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/samaano-fonts
Version:   2.301
Release:   %autorelease

%forgemeta

URL: %{forgeurl}
VCS: git:%{forgeurl}.git
Source0: %{forgesource} 
# https://github.com/mitradranirban/samaano-fonts/archive/v2.301/samaano-fonts-2.301.tar.gz
Source1: https://github.com/mitradranirban/samaanoVF/raw/refs/heads/main/67-0-samaano-fonts.conf

%global foundry        anir
%global fontfamily    samaano        
%global fontlicense    OFL-1.1
%global fontlicenses        OFL.txt
%global fontdocs        README.md   
%global fontdocsex        %{fontlicenses}
%global fontsummary       Fixed Width Multi-Lingual Multi-axis Variable Font
%global fonts            *.ttf
%global fontconfs        %{SOURCE1}
BuildRequires: fontmake
%global fontdescription  %{expand:
Samaano is a variable width, weight, and slant axes fixed width font created 
using mostly rectangular components. It is fully created using open source
tools. It covers a wide range of Latin, Greek and Devanagari based languages.
}

%fontpkg 

%prep
%forgesetup

%build
fontmake -m sources/Samaano.designspace -o ttf
fontmake -m sources/Samaano.designspace -o variable
mv variable_ttf/*.ttf .
mv master_ttf/*.ttf . 

%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
