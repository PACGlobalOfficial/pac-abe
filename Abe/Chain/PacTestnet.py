# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .X11Chain import X11Chain

class PacTestnet(X11Chain):
    def __init__(chain, **kwargs):
        chain.name = 'PacTestnet'
        chain.code3 = 'tPAC'
        chain.address_version = '\x8c'
        chain.script_addr_vers = '\x13'
        chain.magic = '\x23\x45\x67\x89'
        X11Chain.__init__(chain, **kwargs)

    datadir_conf_file_name = 'pacglobal.conf'
    datadir_rpcport = 19998
    datadir_p2pport = 29999
