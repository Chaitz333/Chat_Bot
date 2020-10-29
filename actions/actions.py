# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []









'''
        if date_var+'$'+time not in slots:
            slots[date_var+'$'+time]= 1
            dispatcher.utter_message(text="Slot Booked!")
        else:
            dispatcher.utter_message(text="Hi The Slot is not available! Please try for some other slots")


        '''
Booking_IDs = {}
import time as timer
slots = {}
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World! from Action")

         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_confirm_just_booking"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         #print(dir(dispatcher), 'Dispatcher')
         #rint(dir(tracker),'Tracker')
         #print(domain, 'Domain')

         date_var = tracker.get_slot('date')
         
         time = tracker.get_slot('time')
         #print('date :',date_var,' Person : ',person,' Time: ',time)
         if date_var+'$'+time not in slots:
            slots[date_var+'$'+time]= 1
            t = timer.time()
            i = int(t)
            Booking_IDs[i]=1
            dispatcher.utter_message(text="Slot Booked! Please Note down your Bookig ID : "+str(i))
         else:
            dispatcher.utter_message(text="Hi The Slot is not available! Please try for some other slots")
        
         dispatcher.utter_message(text='action_confirm_just_booking')

         return []


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_confirm_Day_Time_Given"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         #print(dir(dispatcher), 'Dispatcher')
         #rint(dir(tracker),'Tracker')
         #print(domain, 'Domain')

         date_var = tracker.get_slot('date')
         
         time = tracker.get_slot('time')
         #print('date :'+date_var+' Person : '+person+' Time: '+time)
         if date_var+'$'+time not in slots:

            slots[date_var+'$'+time]= 1
            dispatcher.utter_message(text="Slot Booked!" + date_var+'$'+time)
         else:
            dispatcher.utter_message(text="Hi The Slot is not available! Please try for some other slots")
       
         dispatcher.utter_message(text='action_confirm_Day_Time_Given')
         return []

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_delete_res"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         id_ = tracker.get_slot('id')
         
         if int(id_) in Booking_IDs:
            Booking_IDs.pop(id_,0)
            dispatcher.utter_message(text="Slot Deleted!")
         else:
            #print(id_,type(id_), Booking_IDs)
            dispatcher.utter_message(text="Invalid booking ID")
         
         dispatcher.utter_message(text='action_confirm_Day_Time_Given')
         return []