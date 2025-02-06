# GitHub Setup

You will submit your code by pushing it to GitHub. Many actions on GitHub will require authenticating yourself—proving that you have 
access to your repositories—and the best way to do that involves an SSH key, a secret key that defines your identity, and an SSH agent,
a program that remembers the identity so you don’t have to type your password all the time. Here’s how.

## Creating a GitHub account
1. Create a GitHub account if you don’t have one already.
2. Create and/or configure an SSH key using [GitHub’s instructions](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh). Specifically:
    - Create the key (if you don’t have one already) using the `ssh-keygen` program.
    - Add the key to your GitHub account.
    - Test your SSH connection.

**About SSH identities.** An SSH identity is stored in two files, a *public key* with a name like `/Users/yourname/.ssh/id_ed25519.pub` 
and a *private key* with a name like `/Users/yourname/.ssh/id_ed25519`. The private key is kept secret—you should never upload the private 
key to a shared service—while the public key can be uploaded anywhere you like, including your GitHub account. The public and private keys 
are a matched pair. Services like GitHub verify your identity using a mathematical protocol: your computer essentially proves that it has 
access to the private key corresponding to your public key, after which GitHub “knows” that your computer speaks for you.

If you use multiple computers to do your problem sets, you’ll need to configure an identity on each of these computers. You can do this 
either by creating and configuring multiple SSH keys (this is probably a little safer), or by copying the public and private keys between 
the computers (this is probably a little easier, though it’s important to get the file permissions correct).

## Configuring Git

You should also tell your Git installation your name and email, if you haven’t already. This will ensure that you are recorded as the author 
of your code. For the `user.email` configuration, use your email.

```bash
$ git config --global user.name "FIRSTNAME LASTNAME"
$ git config --global user.email "YOUR@EMAIL"
```

> Terminal sessions: A display like this represents a terminal session. To run the commands, you will open a terminal on your computer and 
> then type (or copy and paste) each bold line into the terminal window, one at a time, pressing Return to run each command before going on 
> to the next. The gray $ characters represent shell prompts and should not be copied, and blue lines represent command output.

## Forking this repository

You will want to work on your own personal repository based off of this one. To this, you should fork this repository by hitting the Fork 
button on the top right. This will create your own copy of this repository.

## Working with your own fork

You should now have your own copy of the sw-challenge-fall-2024 repository titled `<username>/sw-challenge-fall-2024`.

**To create a local copy of this repository on your computer**, copy the repository's SSH link by clicking the green Code button. This link 
should look like `git@github.com:<username>/sw-challenge-fall-2024`. Next, clone the repository to your computer:
```bash
$ git clone git@github.com:<username>/sw-challenge-fall-2024.git
```

**Next, add `cardinal-trading-group/sw-challenge-fall-2024` as a remote repository.** This will allow you to fetch future changes we may make. Make sure to 
also disable pushing to the remote.

```bash
$ cd sw-challenge-fall-2024
$ git remote add upstream git@github.com:cardinal-trading-group/sw-challenge-fall-2024
$ git remote set-url --push upstream DISABLE
```

You can list all your remotes with

```bash
$ git remote -v
```

and should see

```bash
origin  git@github.com:<username>/sw-challenge-fall-2024.git (fetch)
origin  git@github.com:<username>/sw-challenge-fall-2024.git (push)
upstream  git@github.com:cardinal-trading-group/sw-challenge-fall-2024.git (fetch)
upstream  DISABLE (push)
```

**To push new changes to your repository**, there are three primary steps:

```bash
$ git add file1 file2
$ git commit -m 'Some helpful message'
$ git push -u origin # After you initially push to origin, you can just type 'git push'
```

**To pull changes from either origin or remote**

```bash
$ git pull upstream main # Pull from cardinal repository
$ git pull # Pulls from origin by default
```

**To view your Git status**

```bash
$ git status
```

## Resources

A lot of this article was pulled (no pun intended) from far better documented resources:

- [CS 61 GitHub setup](https://cs61.seas.harvard.edu/site/2021/SetupGitHub/)
- [CS 165 project page (Starting Code and API tab)](http://daslab.seas.harvard.edu/classes/cs165/project.html)

In addition, these pages might be helpful:

- [CS 61 extended Git docs](https://cs61.seas.harvard.edu/site/ref/git/)
- [SEAS introduction to Git](https://wiki.harvard.edu/confluence/display/USERDOCS/Introduction+To+GIT)
