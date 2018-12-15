# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 18:51:15 2018

@author: laura
"""

#%%
#2. 3 points. Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its name, number
#of stars, main language, and url.
             
import requests

def description_repository(user):
    url="https://api.github.com/users/{}/repos".format(user)
    
    repositories = requests.get(url).json()
    repository_list=[]
    for repository in repositories:
        repo={"name of repository":repository["name"], 
               "main_language":repository["language"],
               "number_of_stars":repository["stargazers_count"],
               "url":repository["url"]}
        repository_list.append(repo)
    return repository_list
    
