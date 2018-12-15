# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:39:49 2018

@author: laura
"""

#%%
#3. 5 points. Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.


import requests

def add_contact(number, name): 
    request = requests.post('http://127.0.0.1:5000/add_contact/{}/{}'.format(number, name))
    return request.json()


def get_number(name): 
    request = requests.get('http://127.0.0.1:5000/get_number/{}'.format(name))
    return request.json()


def delete_contact(name): 
    request = requests.delete('http://127.0.0.1:5000/delete_contact/{}'.format(name))
    return request.json()

def update_contact(name, number):
    request = requests.put('http://127.0.0.1:5000/update_contact/{}/{}'.format(name, number))
    return request.json()

def get_phonebook(): 
    request = requests.get('http://127.0.0.1:5000/phonebook') 
    return request.json() 