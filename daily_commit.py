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
import random
import github
# -----


# Constants
LANGUAGES = ["python", "python", "python", "go", "javascript"]


def choose_repo(result):
    letter = random.choice("abdefjklnquruvwxyz")
    number = random.choice([i for i in range(10, 100)])
    for index, repo in enumerate(result):
        if index > number and letter in repo.clone_url:
            return repo.clone_url
    return result[number].clone_url


def get_query():
    return "language:" + random.choice(LANGUAGES)


def main():
    client = github.Github()
    result = client.search_repositories(query=get_query(), sort="stars", order="desc")
    repo_url = choose_repo(result)
    logging.info("Now cloning: " + unicode(repo_url))

if __name__ == "__main__":
    main()
