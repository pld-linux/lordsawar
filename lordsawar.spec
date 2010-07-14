Summary:	Turn-based strategy game
Summary(pl.UTF-8):	Turowa gra strategiczna
Name:		lordsawar
Version:	0.1.9
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://download.savannah.gnu.org/releases-noredirect/lordsawar/%{name}-%{version}.tar.gz
# Source0-md5:	f6e6b6c05c4494b5029402eb0e5535e0
Source1:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.nongnu.org/lordsawar/
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	glibmm-devel >= 2.4
BuildRequires:	gnet-devel >= 2.0
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtar-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LordsAWar! is a free, turn-based strategy game where up to 8 players
strive for control of as many cities as possible. Produce new armies
in cities to conquer nearby cities. Using the income from those
cities, make more armies to take more cities. Send a hero to a temple
to get a quest, or maybe search a nearby ruin instead. Play with
others or against the computer.

%description -l pl.UTF-8
LordsAWar! jest darmową, turową grą strategiczną, w której maksymalnie
do 8 graczy usiłuje zdobyć jak najwięcej miast. Gracze budują nowe
armie w zdobytch już miastach, aby zdobywać kolejne miasta. Miasta
przynoszą zysk, który wykorzystywany jest do budowy nowych armii,
które z służą z kolei do zajęcia większej ilości miast. Wysyłając
bohatera do świątyni, otrzymuje się zadania, można też zwiedzać
pobliskie ruiny. W grze istnieje możliwość gry z innymi żywymi
graczami lub przeciwko komputerowi.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/*.txt
%attr(755,root,root) %{_bindir}/lordsawar*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/gtkrc
%dir %{_datadir}/%{name}/army
%{_datadir}/%{name}/army/*.lwa
%dir %{_datadir}/%{name}/citysets
%{_datadir}/%{name}/citysets/*.lwc
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/*.ui
%dir %{_datadir}/%{name}/glade/editor
%{_datadir}/%{name}/glade/editor/*.ui
%dir %{_datadir}/%{name}/map
%{_datadir}/%{name}/map/*.map
%dir %{_datadir}/%{name}/music
%{_datadir}/%{name}/music/*.ogg
%{_datadir}/%{name}/music/*.xml
%dir %{_datadir}/%{name}/shield
%{_datadir}/%{name}/shield/*.lws
%dir %{_datadir}/%{name}/tilesets
%{_datadir}/%{name}/tilesets/*.lwt
%dir %{_datadir}/%{name}/various
%{_datadir}/%{name}/various/*.bmp
%{_datadir}/%{name}/various/*.jpg
%{_datadir}/%{name}/various/*.png
%dir %{_datadir}/%{name}/various/editor
%{_datadir}/%{name}/various/editor/*.png
%dir %{_datadir}/%{name}/various/items
%{_datadir}/%{name}/various/items/*.xml
%{_desktopdir}/lordsawar.desktop
%{_pixmapsdir}/lordsawar.png
