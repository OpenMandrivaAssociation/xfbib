Summary:	A lightweight BibTeX editor developed for the Xfce desktop environment
Name:		xfbib
Version:	0.0.2
Release:	13
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	bison
BuildRequires:	flex

%description
Xfbib is a lightweight BibTeX editor developed for the Xfce.
The intentions of Xfbib is to provide an easy and efficient 
way of editing BibTeX files.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
