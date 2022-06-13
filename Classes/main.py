from Controller import Controller
from UiLoader import EventCommunicator, UiLoader


e = EventCommunicator()
v = UiLoader(e)
c = Controller(v)