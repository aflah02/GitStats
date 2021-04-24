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
    ls = []
    for repo in user.get_repos():
        ls.append(str(repo).split('=')[1].split(')')[0].replace('"', ''))
    return ls

# def get_repo_stats(repo_url):


user_id = input('Enter Github Username')
pprint(get_repo_info(user_id))