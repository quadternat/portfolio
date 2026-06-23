# Portfolio
hello :wave:

---
# Helping others
### guide from github

- echo "# portfolio" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/quadternat/portfolio.git
- git push -u origin main

- if your using this guide from github and as ive experienced struggle getting commits to work from local to github
- steps to doing this:

---
### guide better suited for today
1. go to github
2. profile in the upper right
3. settings
4. scroll on the tabs until developer settings
5. personal access tokens
6. tokens (classic)
7. generate new token
8. allow for repo (all you will need to commit)
9. create
10. copy said token somewhere-notepad somewhere
11. to terminal
12. cd into your directory you want to do
13. git init
14. touch README.md -> nano or whatever you use -> type in it
15. git add README.md
16. git commit -m "<<type what you want here>>" -> personally batman
17. git branch -M main
18. git remote add origin <your github repo>

19. IF all in terminal -> nano / nvim .git/config

you will have (without my specific details)
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://quadternat@github.com/quadternat/portfolio.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main

20. for url -> https://quadternat@github.com/quadternat/portfolio.git
21. you want to change the first username before the @ into your token
22. e.g	url = https://ghp_<<numbers and letters gibberish>>@github.com/quadternat/portfolio.git
23. save
24. back to terminal
25. git push -u main origin

## MAKE NOTE: DISCLAIMER
### This example contains my info for this repo itself, it will be different for anyone else