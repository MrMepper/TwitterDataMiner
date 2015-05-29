__author__ = 'Chris'

import Organizer

filename = input("Please enter the filename to organize\n")

json_obj = Organizer.Organizer(filename)

json_obj.organize()