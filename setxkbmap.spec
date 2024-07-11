Name:		setxkbmap
Version:	1.3.4
Release:	2
Summary:	Set the keyboard using the X Keyboard Extension
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xorg-macros)

%description
The setxkbmap command maps the keyboard to use the layout determined by the
options specified on the command line.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/setxkbmap
%doc %{_mandir}/man1/setxkbmap.1.*
