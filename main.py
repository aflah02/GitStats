from bs4 import BeautifulSoup
import requests
from pprint import pprint
import base64
from github import Github
import pandas as pd
import numpy as np
import matplotlib as plt

def get_user_data(user_id):
    profile_url = f'https://api.github.com/users/{user_id}'
    user_data = requests.get(profile_url).json()
    return (user_data)

def get_repo_info(user_id):
    g = Github()
    user = g.get_user(user_id)
    ls_repos = []
    for repo in user.get_repos():
        ls_repos.append(str(repo).split('=')[1].split(')')[0].replace('"', ''))
    return ls_repos

def get_repo_langs(user_id):
    ls_repos = get_repo_info(user_id)
    base_url = f'https://api.github.com/repos/{user_id}/'
    ls_repo_data = []
    for repo in ls_repos:
        print(requests.get(base_url+repo+'/languages'))
        ls_repo_data.append(requests.get(base_url+repo+'/languages'))
    return ls_repo_data



# print(requests.get('https://api.github.com/repos/aflah02/Digital-Clock/languages'))
user_id = input('Enter Github Username: ')
pprint(get_user_data(user_id))