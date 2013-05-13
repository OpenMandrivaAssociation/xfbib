Summary:	A lightweight BibTeX editor developed for the Xfce desktop environment
Name:		xfbib
Version:	0.0.2
Release:	10
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
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.0.2-9mdv2012.0
+ Revision: 790050
- Rebuild for xfce 4.10

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-8
+ Revision: 633049
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-7mdv2011.0
+ Revision: 579667
- rebuild for new xfce 4.7.0

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-6mdv2010.1
+ Revision: 543287
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.0.2-5mdv2010.0
+ Revision: 445928
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-4mdv2009.1
+ Revision: 349186
- rebuild whole xfce

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-3mdv2009.1
+ Revision: 294936
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.0.2-2mdv2009.0
+ Revision: 269770
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.2-1mdv2009.0
+ Revision: 192380
- new version

* Wed Feb 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.1-1mdv2008.1
+ Revision: 173361
- add missing buildrequires
- add source and spec file
- Created package structure for xfbib.

