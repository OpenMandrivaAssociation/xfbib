Summary:	A lightweight BibTeX editor developed for the Xfce desktop environment
Name:		xfbib
Version:	0.1.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	https://git.xfce.org/archive/xfbib/snapshot/xfbib-%{version}.tar.gz
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:  xfce4-dev-tools 
BuildRequires:  libtool

%description
Xfbib is a lightweight BibTeX editor developed for the Xfce.
The intentions of Xfbib is to provide an easy and efficient 
way of editing BibTeX files.

%prep
%setup -q

%build
xdt-autogen
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
