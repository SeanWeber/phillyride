# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
''' 
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
''' 

import gettext
from gettext import gettext as _
gettext.textdomain('phillyride')

import logging
logger = logging.getLogger('phillyride')

from phillyride_lib.AboutDialog import AboutDialog

# See phillyride_lib.AboutDialog.py for more details about how this class works.
class AboutPhillyrideDialog(AboutDialog):
    __gtype_name__ = "AboutPhillyrideDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutPhillyrideDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

