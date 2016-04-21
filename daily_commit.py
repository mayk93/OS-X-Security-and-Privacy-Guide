#!/usr/bin/python
# -*- coding: utf-8 -*-

# Unicode
from __future__ import unicode_literals

import sys
reload(sys)
# -----

# Logging
import logging
logging.basicConfig(level=logging.INFO)
# -----


# Libs
import pymongo
import os
import random
import github
# -----


# Constants
LANGUAGES = ["python", "python", "python", "go", "javascript"]  # More python to increase python probability

def get_token():
    client = pymongo.MongoClient()
    return client.tokendb.token.find_one()["token"]

TOKEN = get_token()
USERNAME = "mayk93"   # Here goes your username
REMOTE_PATH = "git@github.com:" + USERNAME + "/"

'''
git remote rename origin upstream
git remote add origin URL_TO_GITHUB_REPO
git push origin master
'''


def choose_repo(result):
    letter = random.choice("abdefjklnquruvwxyz")
    number = random.choice([i for i in range(10, 100)])
    for index, repo in enumerate(result):
        if index > number and letter in repo.clone_url:
            return repo.clone_url, repo.name
    return result[number].clone_url, result[number].name


def get_query():
    return "language:" + random.choice(LANGUAGES)


def clone(url, name):
    logging.info("Cloning " + name + " from " + url)
    os.system("mkdir ClonedRepos/" + name)
    os.system("cd ClonedRepos/" + name + "; git clone " + url)


def create_repo_on_remote(name):
    os.system("""curl -H "Authorization: token %s" --data '{"name":"%s"}' https://api.github.com/user/repos""" % (TOKEN, name))


def main():
    client = github.Github()
    result = client.search_repositories(query=get_query(), sort="stars", order="desc")
    repo_url, repo_name = choose_repo(result)
    clone(repo_url, repo_name)
    create_repo_on_remote(repo_name)


if __name__ == "__main__":
    main()
