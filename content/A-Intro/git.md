# Git basics for IST769

You won't need to know a lot of git commands for this course, but knowing a few can get you far!

**Cloning the IST769 repository.**  
Cloning means to copy a remote repository locally. The two are then bound by the push / pull operations. To clone IST769, open a terminal window in a folder where you would like the code to live and type:  
```
$ git clone https://github.com/mafudge/ist769
```
This will copy the remote code locally into a folder `ist769`.

**Am I in the right place?**  
Are you in a folder that is a git repository? The easiest way to see that is with:   
```
$ git remote -v
```
This will output the name of the remote repository you cloned. If you see a message like `fatal not a git repository` then you aren't in the correct folder.

Typically the command prompt should match the repository we cloned, in this case `ist769`, try:
```
$ cd ist769
```
to change the current folder to `ist769`. this should be reflected in the command prompt, like this:  
```
ist769$ 
```
Now that you are in the correct place, try:
```
ist769$ git remote -v
```
This will output the repository you cloned.  

**I was fooling around, made changes and now I need to undo them!**  
If you made changes locally and you don't want them you can type the following to reset the repository back to the latest pull:  
```
ist769$ git reset --hard 
```
If you *think* you might need to keep a change around, but still want to reset, I suggest performing a stash instead:
```
ist769$ git stash --include-untracked
```
The stash will store your changes elsewhere and if needed they can always be recovered.

**I need to get updated files from the remote repository!**  
Throughout the semester you might be asked to get updated files that your instructor has posted to github. To do this, execute:
```
ist769$ git fetch --all
ist769$ git reset --hard origin/main 
```

**I really messed things up! Help!**   
Don't fret! You can always delete the current folder and then clone it again, or create a new folder and then `git clone` into that folder instead. For example to clone into a folder called `ist769v2` you type:
```
$ git clone https://github.com/mafudge/ist769 ist769v2
```

**NOTE:** we are no longer in the `ist769` folder: `ist769$ cd ..` to move up a folder.
