#!/usr/local/bin/python

import subprocess

def run_cmd(list):

	run_cmd = subprocess.Popen(list, shell = True)
