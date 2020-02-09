#!/usr/bin/env python

t_id = int(input('LeetCode Question ID: >>> '))
diff = input('Difficulty Level: e - Easy, m - Medium, h - Hard >>> ').lower()
name = input('Name >>> ')

if diff == 'e':
    string = '''![#%d](https://img.shields.io/badge/%d-Easy-green.svg?style=flat-square) `%s`''' % (t_id, t_id, name)
elif diff == 'm':
    string = '''![#%d](https://img.shields.io/badge/%d-Medium-yellow.svg?style=flat-square) `%s`''' % (t_id, t_id, name)
elif diff == 'h':
    string = '''![#%d](https://img.shields.io/badge/%d-Hard-red.svg?style=flat-square) `%s`''' % (t_id, t_id, name)
with open('README.TEMPLATE', 'a') as f:
    f.write('\n%s\n' % string)
    f.close()
