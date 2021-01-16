#!/usr/bin/python3
import os

# This script uses green.svg and generates the following files from it:
#
# aqua.svg
# blue.svg
# brown.svg
# grey.svg
# orange.svg
# pink.svg
# purple.svg
# red.svg
# sand.svg
# teal.svg
# arc.svg

# It uses the following color table to do so:
COLORS = {}
COLORS["aqua"] = "66a8cb"
COLORS["blue"] = "5972c3"
COLORS["brown"] = "997052"
COLORS["grey"] = "999999"
COLORS["orange"] = "cc823f"
COLORS["pink"] = "ce6ca2"
COLORS["purple"] = "8463c5"
COLORS["red"] = "b74c4a"
COLORS["sand"] = "c4a660"
COLORS["teal"] = "59c3ad"
COLORS["yellow"] = "e7bc0d"
COLORS["arc"] = "6ba4e7"
COLORS["spring-rain"] = "ad93ba"
COLORS["faux-royal-red"] = "931636"


GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
