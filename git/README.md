# Git Base setup 

## Start with  installation
    - [Install the git in your machine] (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    -  open git bash and setup the git config
    -  git clone from github - any newly created project or create a repo in local and add the remote url of gitup repo
## Git basic commands 
    -  git config
    -  git init
    -  git add <file name or . to add all the files from unstaging area to staging area>
    -  git clone
    -  git checkout <branch name>
    -  git commit
    -  git push
    -  git pull
    -  git merge
    -  git rebase
    -  git blame
    -  git log
    -  git tag
    -  git branch
## Do you know :
    - Every object in Git has its own SHA1 and SHA1s are unique in the universe.
    - git is persistent map
    - Git obeject model - fun to understand this
    - Blobs, trees, commit and tags
    - git saves branches details in refs/head
    - .git/HEAD file have current branch details
    - when you merge your branches and there is one conflict , you  need to resolved conflicts and there is new commit and taht commit have 2 have 2 heads.
    - Deattched head situation when you checkout a commit and do some changes. How to resolve it - create a branch for latest commit and then merge it to your working branch.
    - Git 3 major rule -
      - The current branch tracks new commit 
      - when you move to another commit , Git updates you working directory
      - Unreachable objects are garbage collected(Example - when commit something on undetachhed head and move your current head without tagging/branching these changes)
    - When to merge, when to rebase?
      - Merge - preserve the history (merges never lie) so when in doubt- MERGE
      - Rebase - refator history(distructive option)
      - Never rebase shared commits
    - Tags - A tag is like a branch that head dose'nt.match. Saved in .git/refs/tags
      - Annonated tags - With a message
      - Non - Annonated tags - light weight tags , no msg nothing , simple tagging on commit
    - Distributed Version Control
      - .git/config - have base configs when we clone the repos
      - like a local branch , remote branch is reference of a commit
    - Synchronization of repos local to remote
      - when we push latest commits then local and remote both the branches are in sync
    - Synchronization of remote to local
      - git fetch - get the latest objects from remote
      - you "fetch" and "merge", then you "push" or git pull and push
  
  
  





