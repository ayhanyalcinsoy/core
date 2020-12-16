#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

LIBDIR = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"
bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-jit \
                         --libdir=%s \
                         --bindir=%s \
                         --enable-pcretest-libreadline \
                         --enable-pcre32 \
                         --enable-pcre16 \
                         --enable-utf \
                         --enable-unicode-properties \
                         --enable-cpp \
                         --docdir=/%s/%s \
                         --disable-static" % (LIBDIR, bindir, get.docDIR(), get.srcNAME()))
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    if get.buildTYPE() == "emul32":
        pass
    else:
        autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return
    
