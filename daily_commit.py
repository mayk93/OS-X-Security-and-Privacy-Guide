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
import os
import random
import github
# -----


# Constants
LANGUAGES = ["python", "python", "python", "go", "javascript"]  # More python to increase python probability


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


def main():
    client = github.Github()
    result = client.search_repositories(query=get_query(), sort="stars", order="desc")
    repo_url, repo_name = choose_repo(result)
    clone(repo_url, repo_name)


if __name__ == "__main__":
    main()
