Name:      fyre
Summary:   Explorer for iterated chaotic functions
Version:   1.0.1
Release:   %mkrel 4
License:   GPL
Group:     Graphics
Source:    http://flapjack.navi.cx/releases/fyre/%{name}-%{version}.tar.bz2
Patch: fyre-1.0.0-datadir.patch
URL:       http://fyre.navi.cx
BuildRoot: %_tmppath/%name-%version-%release
Requires(post): desktop-file-utils shared-mime-info
Requires(postun): desktop-file-utils shared-mime-info
BuildRequires: gtk2-devel OpenEXR-devel
BuildRequires: libglade2.0-devel
BuildRequires: libgnet2-devel
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
aclocal-1.9
autoconf
automake-1.9

%build
%configure2_5x --enable-gnet --enable-openexr
%make

%install
rm -rf %buildroot
%makeinstall update_xdgmime=true
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -f %buildroot%{_datadir}/icons/hicolor/icon-theme.cache

%clean
rm -rf %buildroot

%post
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor

%postun
%clean_mime_database
%clean_desktop_database
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/fyre
%{_datadir}/applications/fyre.desktop
%{_datadir}/fyre/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-fyre-animation.png
%{_datadir}/mime/packages/fyre.xml


