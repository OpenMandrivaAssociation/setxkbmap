Name:		setxkbmap
Version:	1.3.0
Release:	9
Summary:	Set the keyboard using the X Keyboard Extension
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
The setxkbmap command maps the keyboard to use the layout determined by the
options specified on the command line.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1.*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2011.0
+ Revision: 669971
- mass rebuild

* Thu Sep 23 2010 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 580690
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2010.1
+ Revision: 524074
- rebuilt for 2010.1

* Thu Jul 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 393771
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.4-5mdv2009.1
+ Revision: 351523
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-4mdv2009.0
+ Revision: 225436
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-3mdv2008.1
+ Revision: 166417
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2008.1
+ Revision: 156429
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 24 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.4-1mdv2008.0
+ Revision: 55002
- new upstream version: 1.0.4
- minor configure call cleanup (remove unecessary flags)


* Thu Feb 15 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 121457
- new release
- fix description

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

