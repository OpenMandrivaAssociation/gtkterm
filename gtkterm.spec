Name:		gtkterm
Version:	0.99.6
Release:	%mkrel 1
Summary:	Serial port terminal
Group:		Communications
License:	GPLv2+
URL:		http://fedorahosted.org/gtkterm/
Source0:        http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz
Patch2:		gtkterm-0.99.6-scrollback.patch
Patch5:		gtkterm-0.99.6-fix-str-fmt.patch
Patch7:		gtkterm-0.99.6-ubuntu-fixes.patch
BuildRequires:	gtk2-devel 
BuildRequires:	gettext 
BuildRequires:	bison 
BuildRequires:	vte-devel 
BuildRequires:	zlib-devel 
BuildRequires:	ncurses-devel

%description
Gtkterm is a simple GTK+ terminal used to communicate with a serial port.
It is has fewer features than minicom, but is designed to be as easy to
use as possible.

%prep
%setup -q
%patch2	-p1 -b .scrollback
%patch5 -p0 -b .str
%patch7 -p1 -b .ubuntu

%build
%configure2_5x --disable-rpath

# Hack fix broken Makefile
sed -i 's|@MKINSTALLDIRS@|../mkinstalldirs|g' po/Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{_real_vendor}-%{name}.desktop <<EOF
[Desktop Entry]
Name=GTKTerm
Comment=Serial port terminal
Exec=%{name}
Icon=terminals_section
Terminal=false
Type=Application
Categories=GTK;RemoteAccess;Network;
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*.desktop


%changelog
* Tue Apr 12 2011 Jani Välimaa <wally@mandriva.org> 0.99.6-1mdv2011.0
+ Revision: 652970
- new version 0.99.6
- sync patches with Fedora
- fix url and source tag
- drop support for old mdv releases
- drop buildroot definition
- clean .spec a bit

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.99.5-8mdv2011.0
+ Revision: 571930
- build with latest vte

* Wed Jun 10 2009 Götz Waschk <waschk@mandriva.org> 0.99.5-8mdv2010.0
+ Revision: 384687
- rebuild for new vte

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.99.5-7mdv2010.0
+ Revision: 382166
- rebuild for new libvte

* Wed May 13 2009 Funda Wang <fwang@mandriva.org> 0.99.5-6mdv2010.0
+ Revision: 375208
- sync with fedora patches to fix bug#50832

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.99.5-5mdv2009.0
+ Revision: 246709
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 05 2007 Funda Wang <fwang@mandriva.org> 0.99.5-3mdv2008.1
+ Revision: 115515
- add missing categories
- add xdg menu entry
- Rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix hardcoded man page extension
    - import gtkterm


* Fri Feb 03 2006 Jerome Soyer <saispo@mandriva.org> 0.99.5-1mdk
- New release 0.99.5

* Fri Dec 16 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.99.4-1mdk 
- First Mandriva release based on fedora spec
