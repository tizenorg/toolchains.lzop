Name:           lzop
Version:        1.03
Release:        1
License:        GPLv2+
Summary:        lzop
URL:            http://www.lzop.org
Group:          Applications/Text
Source:         %{name}-%{version}.tar.gz
BuildRequires:  lzo
BuildRequires:  lzo-devel


%description
lzop is a file compressor which is very similar to gzip. lzop uses
the LZO data compression library for compression services, and its
main advantages over gzip are much higher compression and
decompression speed (at the cost of some compression ratio).

lzop is copyrighted OpenSource software distributed under the terms
of the GNU General Public License (GPL).

%prep
%setup -q

%build
%configure --disable-nls
make PR_PROGRAM=%{_bindir}/pr

%install
%make_install

%clean
rm -rf %{buildroot}

%docs_package 

%files 
%defattr(-,root,root,-)
%doc NEWS README COPYING
%{_bindir}/*
%{_mandir}/*/*
