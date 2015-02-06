Summary:	Serial port terminal
Name:		gtkterm
Version:	0.99.6
Release:	3
License:	GPLv2+
Group:		Communications
Url:		http://fedorahosted.org/gtkterm/
Source0:        http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz
Patch2:		gtkterm-0.99.6-scrollback.patch
Patch5:		gtkterm-0.99.6-fix-str-fmt.patch
Patch7:		gtkterm-0.99.6-ubuntu-fixes.patch
BuildRequires:	bison
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(zlib)

%description
Gtkterm is a simple GTK+ terminal used to communicate with a serial port.
It is has fewer features than minicom, but is designed to be as easy to
use as possible.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch2 -p1 -b .scrollback
%patch5 -p0 -b .str
%patch7 -p1 -b .ubuntu

%build
%configure2_5x --disable-rpath

# Hack fix broken Makefile
sed -i 's|@MKINSTALLDIRS@|../mkinstalldirs|g' po/Makefile

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
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

