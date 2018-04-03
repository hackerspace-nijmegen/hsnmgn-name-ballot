#!/usr/bin/env python

from pyvotecore.schulze_method import SchulzeMethod
from pyvotecore.condorcet import CondorcetHelper
from allvotes import ballots
from pprint import pprint

pprint(SchulzeMethod(ballots, ballot_notation = CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict())
