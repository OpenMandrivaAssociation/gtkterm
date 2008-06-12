Name:           gtkterm
Version:        0.99.5
Release:        %mkrel 3
Summary:        Serial port terminal
Group:          Communications
License:        GPLv2+
URL:            http://www.jls-info.com/julien/linux
Source0:        http://www.jls-info.com/julien/linux/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot 

BuildRequires:  gtk2-devel 
BuildRequires:  gettext 
BuildRequires:  bison 
BuildRequires:  vte-devel 
BuildRequires:  zlib-devel 
BuildRequires:  ncurses-devel

%description
Simple GUI terminal used to communicate with the serial port.
Similar to minicom or hyperterminal.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%{name}.desktop <<EOF
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
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*.desktop
