py-learn
========

sample python codes for begginers
I think git is better than python

how to commit / upload a new file to github repository


[jayaram@localhost py-learn]$ git pull  https://github.com/sanjaycal/py-learn.git
remote: Counting objects: 2, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 2 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (2/2), done.
From https://github.com/sanjaycal/py-learn
 * branch            HEAD       -> FETCH_HEAD
Updating dfd8721..34cdfe8
Fast-forward
 python cube a number code. => cube.py | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename python cube a number code. => cube.py (100%)
[jayaram@localhost py-learn]$ ls
cube.py  n2.py  README.md


[jayaram@localhost py-learn]$ git add n2.py
[jayaram@localhost py-learn]$ git commit n2.py
[master ce03d5e] added by sanjay
 1 file changed, 4 insertions(+)
 create mode 100644 n2.py
[jayaram@localhost py-learn]$ git push  https://github.com/sanjaycal/py-learn.git
warning: push.default is unset; its implicit value is changing in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the current behavior after the default changes, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': sanjaycal
Password for 'https://sanjaycal@github.com': 
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 405 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/sanjaycal/py-learn.git
   34cdfe8..ce03d5e  master -> master

