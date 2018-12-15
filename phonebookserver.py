# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:39:28 2018

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


from flask import Flask, jsonify 

phonebookserver = Flask("phonebook server")


phonebook={"Pepe":"01982201",
           "The Pope":"80192390123",
           "Donald Trump":"2282829",
           "Mom":"82292"
           }

#• add a contact (phone + name)
@phonebookserver.route("/add_contact/<number>/<name>", methods=["POST"])
def add_contact(number, name): 
    if name not in phonebook: 
        phonebook.update({name:number})
        return jsonify("You just added " + name + " with the following number: " + number)
    else: 
        return jsonify("You already have " + name + " in your phonebook.")

#• get a phone by name
@phonebookserver.route("/get_number/<name>")
def get_number(name): 
    if name in phonebook: 
        return jsonify(name + "'s  phone number is: " + phonebook[name])
    else: 
        return jsonify("You don't have " + name + " in your phonebook.")

#• delete a phone by name
@phonebookserver.route("/delete_contact/<name>", methods=["DELETE"])
def delete_contact(name):   
    if name not in phonebook: 
        return jsonify("You don't have " + name + " in your phonebook.")
    else:
        del phonebook[name]
        return jsonify("You just deleted: "+ name + " from your phonebook.")         

#• update a phone by name                
@phonebookserver.route("/update_contact/<name>/<phone>", methods=["PUT"])
def update_contact(name, number): 
    if name not in phonebook: 
        return jsonify("You don't have: "+ name + " in your phonebook.")
    else: 
        phonebook[name] = number
        return jsonify("You just updated: " + name + "'s number to: " + number)
    
  
@phonebookserver.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)
            
phonebookserver.run()





