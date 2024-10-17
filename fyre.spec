Name:      fyre
Summary:   Explorer for iterated chaotic functions
Version:   1.0.1
Release:   11
License:   GPLv2+
Group:     Graphics
Source:    http://flapjack.navi.cx/releases/fyre/%{name}-%{version}.tar.bz2
Patch: fyre-1.0.0-datadir.patch
Patch1: fyre-1.0.1-format-strings.patch
URL:       https://fyre.navi.cx
Requires(post): desktop-file-utils shared-mime-info
Requires(postun): desktop-file-utils shared-mime-info
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: OpenEXR-devel
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(gnet-2.0)
BuildRequires: desktop-file-utils shared-mime-info
BuildRequires: automake1.9

%description
Fyre is a tool for producing computational artwork based on histograms
of iterated chaotic functions. At the moment, it implements the Peter
de Jong map in a fixed-function pipeline with an interactive GTK+
frontend and a command line interface for easy and efficient rendering
of high-resolution, high quality images.

%prep
%setup -q
%patch -p1 -b .datadir
%patch1 -p1
aclocal-1.9
autoconf
automake-1.9

%build
%configure2_5x --enable-gnet --enable-openexr
%make

%install
%makeinstall update_xdgmime=true
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

%clean

%post
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor

%postun
%clean_mime_database
%clean_desktop_database
%clean_icon_cache hicolor

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/fyre
%{_datadir}/applications/fyre.desktop
%{_datadir}/fyre/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-fyre-animation.png
%{_datadir}/mime/packages/fyre.xml




%changelog
* Wed Jul 27 2011 Götz Waschk <waschk@mandriva.org> 1.0.1-8mdv2012.0
+ Revision: 691825
- rebuild

* Sat Jul 25 2009 Götz Waschk <waschk@mandriva.org> 1.0.1-7mdv2011.0
+ Revision: 399708
- fix format strings
- update license

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 245586
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.1-4mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 09 2007 Götz Waschk <waschk@mandriva.org> 1.0.1-4mdv2007.0
+ Revision: 118561
- rebuild

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 1.0.1-3mdv2006.0
+ Revision: 63849
- rebuild
- unpack patch
- Import fyre

* Tue Oct 10 2006 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdv2007.1
- update file list
- New version 1.0.1

* Wed Aug 16 2006 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdv2007.0
- initial mdv package

* Fri Mar 04 2005 Mirco Mueller <macslow@bangang.de> 1.0.0-2
- stupid me, I totally forgot to enable gnet2 and OpenEXR support

* Thu Mar 03 2005 Mirco Mueller <macslow@bangang.de> 1.0.0-1
- initial .spec file written for fyre-1.0.0.tar.gz

