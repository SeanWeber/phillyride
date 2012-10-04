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

from urllib2 import urlopen
import json
import gettext
from gettext import gettext as _
gettext.textdomain('phillyride')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('phillyride')

from phillyride_lib import Window
from phillyride.AboutPhillyrideDialog import AboutPhillyrideDialog
from phillyride.PreferencesPhillyrideDialog import PreferencesPhillyrideDialog

# See phillyride_lib.Window.py for more details about how this class works
class PhillyrideWindow(Window):
    __gtype_name__ = "PhillyrideWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(PhillyrideWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutPhillyrideDialog
        self.PreferencesDialog = PreferencesPhillyrideDialog

        # Code for other initialization actions should be added here.
        
        self.showtrain = self.builder.get_object("showtrain")
        self.infodisplay = self.builder.get_object("infodisplay")
        
        self.startd = self.builder.get_object("startd")
        self.endd = self.builder.get_object("endd")
        self.planbutton = self.builder.get_object("planbutton")
        self.trainnum = self.builder.get_object("trainnum")
        
        
    def on_showtrain_clicked(self, widget):
        trainid = self.trainnum.get_text()
        
        info = urlopen("http://www3.septa.org/hackathon/RRSchedules/" + trainid)
        train = json.load(info)
        self.infodisplay.get_buffer().set_text("")  # Clears previous text
        for item in train:
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "Station: " + item['station'])
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "Time: " + item['sched_tm'])
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "-" * 10)

    def on_planbutton_clicked(self, widget):
        start = self.startd.get_active_text()
        end = self.endd.get_active_text()
        
        query = "http://www3.septa.org/hackathon/NextToArrive/" + start + "/" + end
        results = urlopen(query)
        nextarrivals = json.load(results)
        self.infodisplay.get_buffer().set_text("")
        for item in nextarrivals:
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "Train number: " + item['orig_train'])
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "Depature time: " + item['orig_departure_time'])
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "Arrival time: " + item['orig_arrival_time'])
                    
            if (item['orig_delay'] != "On time"):
                self.infodisplay.get_buffer().insert(
                        self.infodisplay.get_buffer().get_end_iter(),  
                        "\n" + "Delay: " + item['orig_delay'])
                        
            self.infodisplay.get_buffer().insert(
                    self.infodisplay.get_buffer().get_end_iter(),  
                    "\n" + "-" * 10)
