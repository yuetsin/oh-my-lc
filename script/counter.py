#!/usr/bin/env python

import os
import subprocess

LEETCODE_PROBLEMS_COUNT = 1312

path = os.getcwd() + "/lc-problems/"

folder_counts = 0

for _, dirs, _ in os.walk(path):
    for name in dirs:
        if len(name) == 0 or name[0] == '.':
            continue
        if name.endswith('.rtfd'):
            continue
        print(name)
        folder_counts += 1

"%d / %d Completed" % (
    folder_counts, LEETCODE_PROBLEMS_COUNT)

username = 'yuetsin'
password = os.getenv('GITHUB_PASSWORD_TOKEN')

old_file = open('README.TEMPLATE', 'r')

w_str = ""

svg_link = "https://img.shields.io/badge/Solving%%20Progress-%d%%2F%d%%20Completed-F89F1B?style=flat-square&logo=LeetCode" % (
    folder_counts, LEETCODE_PROBLEMS_COUNT)

badge_str = "\n![LeetCode Progress](%s)" % svg_link
for line in old_file:
    w_str += line
    if line == "## Progress Diagrams\n":
        w_str += badge_str

with open("README.md", 'w') as new_file:
    new_file.write(w_str)
    print("Written new README.md: ")

bash_script = """

echo "Running Bash Script"

git add .

git config --global user.name "LeetCode Bot"

git commit -am "[bot] completed progress (%d/%d)"

git config remote.origin.url https://%s:%s@github.com/%s/oh-my-lc.git

git push origin HEAD:master

echo "Running Bash Script Over"
""" % (folder_counts, LEETCODE_PROBLEMS_COUNT, username, password, username)

with open("push.sh", 'w') as bash_file:

    bash_file.write(bash_script)

rc = subprocess.call("chmod +x ./push.sh; ./push.sh", shell=True)
