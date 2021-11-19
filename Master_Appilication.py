#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Libarires

from flask import *
import sys
import pandas as pd
import json
import operator as op
import smtplib
from email.message import  EmailMessage
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, render_template, request


# In[2]:


#Object_Detection

def Object_Detection():
    obj = ['Food','Garden Leaves','Milk Covers','Ghee/Oil Packets']
    return obj


# In[3]:


#Binary_Classification

list1 = ['Vegetable Peels','Fruit Peels','Rotten Vegetables','Rotten Fruits','Left over food','Mango Seeds','Used Tea Bags',
         'Used Coffee Powder from Filter','Egg Shells','Rotten Eggs','Coconut Shells','Tender Coconut Shells',
         'Used Leaves & Flowers','Spoiled Spices','Floor Sweeping Dust','Meat & Non-Veg Food Remains','Bones','Food Packagings',
         'Nails','Hair','Food','Garden Leaves','Weeds','Dried Flowers','Used Oils','potato peels','tomato','cabbage',
         'paper plates','disposables','green leaves','onion peels','tortilas','packed boxes','flower waste','chips',
        'rubber bands','eatables','peels','banana peels','apples','Vegetable','Fruits','Water cans','water bottles',
         'oranges','carrot','grains']
list2 = ['Mop Stick','Used Mop Cloth','Toilet Cleaning Brush','Brush & Scrubs used for Cleaning','Used & Dirty Floor Mats',
         'Bottles & Container of Pesticides','Used Tooth Brush','Soap Covers','Chocolate Wrappers',
         'Butter Paper (Wrapping for Butter)','Milk Covers','Ghee/Oil Packets','Batter Packets','Oil Cans',
         'Expired Food Packages','Newspaper','Broken Stationary','Used Razor Blades','Empty Shampoo bottles','Empty Perfume bottles',
         'Thermocol','Broken Glass','Broken Household','Aluminium Cans','Old Brooms','Tissue Paper','Thermocol Balls','Small Broken Toys',
         'Used bottles, tubes, cans of shaving cream','Leather','Rexine','Furniture','Used bottles', 'tubes', 'cans of Deodrant',
         'creams','Wrapper','pen','colour','Batteries','CD''s','Printer Cartridges','Broken Watch Electronics',
         'Broken/Damaged Computer Peripherals','Broken/Damaged Television','Broken/Damaged Radios','Expired Medicines',
         'Tablets Covers','Medicine Syrup Bottle','Injection Bottles','Other Medicinal Discards','CFL', 'Tube Light',
         'Broken Thermometer','Old Paints','Bottles','Cans of Insecticide Sprays','Bottles or Cans of Room Freshners',
         'stationary','cloths','Polyethene','packets','cups','chocolates','notebooks','copies']

def Binary_Classification():
    items = Object_Detection()
    final_list = []
    for x in items:
        if x in list1:
            i = "wet"
            final_list.append(i)
        if x in list2:
            j = "dry"
            final_list.append(j)
    return final_list


# In[4]:


#Alert_Notification

def email_alerts(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = 'smartbin.alerts@gmail.com'
    password = 'avcddhmefereapun'
    msg['from'] = user
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

def action(bin_type,items):
    if bin_type == "dry":
        if "wet" in items:
            return True
        else : 
            return False
    elif bin_type == "wet":
        if "dry" in items:
            return True
        else : 
            return False
   
def Alert_Notification():
    bin_type = request.form['bin_type']
    items = Binary_Classification()
    user_name = request.form['user_name']
    out = action(bin_type,items)
    if out:
        subject1 = "SmartBin Alert Notification"
        body1 = f"Wrong item is put into {bin_type} bin"
        to1 = user_name
        email_alerts(subject1,body1,to1)
    return {'Output': out}


# In[5]:


#Master_App

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Object_Detection':
            Object_Detection_Model = Object_Detection()
            return "Objects inside the bin are detected"
        elif  request.form.get('action2') == 'Binary_Classification':
            Binary_Classification_Model = Binary_Classification()
            return "Binary Classification is performed and Items are classified"
        elif request.form.get('action3') == 'Go_Smart_Bin':
            App = Alert_Notification()
            return "Smart Inspection is Completed"
        else:
            pass
    elif request.method == 'GET':
        return render_template('Testing1.html')
    return render_template("Testing1.html")
if __name__ == '__main__':
    app.run()


# In[ ]:




