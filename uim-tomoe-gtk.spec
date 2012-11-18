Summary:	Tomoe helper for UIM for handwritten input
Summary(pl.UTF-8):	Program pomocniczy UIM tomoe pozwalający na wprowadzanie pisma ręcznego
Name:		uim-tomoe-gtk
Version:	0.6.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tomoe/%{name}-%{version}.tar.gz
# Source0-md5:	2c2573d405b9bf08c618c8dabf3b668a
URL:		http://tomoe.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	tomoe-devel >= %{version}
BuildRequires:	tomoe-gtk-devel >= %{version}
BuildRequires:	uim-devel
Requires:	gtk+2 >= 2:2.4.0
Requires:	tomoe >= %{version}
Requires:	tomoe-gtk >= %{version}
Requires:	uim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uim-tomoe-gtk is an UIM helper program for Tomoe. Tomoe is a
handwriting recognizer which currently supports Japanese.

%description -l pl.UTF-8
uim-tomoe-gtk to program pomocniczy UIM dla Tomoe. Tomoe to system
rozpoznawania pisma ręcznego obsługujący język japoński.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/uim-tomoe-gtk
