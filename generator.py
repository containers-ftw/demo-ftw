#!/usr/bin/env python

from random import (
    choice,
    random
)
import json

choices = ['apple','pear','orange','avocado']
winner = choice(choices)
confidence =  random()

print(json.dumps({"winner":winner,
                  "confidence":confidence}))
