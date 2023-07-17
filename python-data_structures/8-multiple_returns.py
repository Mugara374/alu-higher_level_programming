#!/usr/bin/python3
def multiple_returns(sentence):
    if not bool(sentence):
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
