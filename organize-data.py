__author__ = 'Chris'

import Organizer

#Uses JSON to organizer data from text that is sent in by Listener object

filename = input("Please enter the filename to organize\n")

json_obj = Organizer.Organizer(filename)

json_obj.organize()