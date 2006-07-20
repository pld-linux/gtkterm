Summary:	gtkterm - clone of the Hyperterminal
Summary(pl):	gtkterm - klon Hyperterminala
Name:		gtkterm
Version:	0.99.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.jls-info.com/julien/linux/%{name}-%{version}.tar.gz
# Source0-md5:	007ce7810466396b6452dea9c57c5f02
URL:		http://www.jls-info.com/julien/linux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	vte-devel >= 0.10.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a "clone" of the famous Hyperterminal. But it is much more
simple, that is to say, that it can only communicate with a serial
link and that it does not support all the modem protocols.

%description -l pl
Jest to klon s³awnego Hyperterminala. Jednak jest o wile prostszy, to
znaczy mo¿e komunikowaæ siê tylko z portem, ale nie wspiera wszystkich
protoko³ów modemowych

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
