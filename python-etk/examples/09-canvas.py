#!/usr/bin/python

import etk
import ecore

c = etk.Canvas()


w = etk.Window(title="Button", size_request=(200, 200), child=c)
w.show_all()

evas = c.toplevel_evas_get()
r = evas.Rectangle(color="#ff0000", size=(50,50))
r.show()
c.object_add(r)

def mover(obj):
    (x, y) = obj.center
    obj.center = (x+1, y+1)
    return True

ecore.animator_add(mover, r)

def quit(obj):
    etk.main_quit()
w.on_destroyed(quit)

etk.main()