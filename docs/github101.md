# Github 101
This page starts with some background on version control and github. Click [here](#hands-on) to skip to the hands-on part of the tutorial.

!!! note
    This page is under development, and wide open for comments and contributions. There is a [forum for discussion here](https://github.com/phawthorne/ki-tutorials/discussions).


## What is version control?
* A system for tracking line-by-line changes in your work in batches called "commits". Additional features include viewable histories of changes, ability to seamlessly switch between committed versions of the code, maintaining distinct working versions and assisting with merging them, and ability to sync updates from one machine to another.
* Version control can be done without Github. There is a software tool called `git`, among others, that allows you to do version control on your computer. Github, Gitlab, etc... are services that take `git` to the cloud. 
* Version control is generally used at the project level. Sometimes there may be more than one "repository" as part of a project, but this is a more advanced case. 

## What is Github?
* Github is a website/service provider that helps with version control and sharing/collaboration.
* It acts as a remote host for your projects so that they are accessible from the internet.
* It can serve project webpages through a service called github-pages. 
* Provides both public and private repositories.
* Provides a host of collaboration-focused tools (issue boards, pull requests, teams/organizations, ...).


## Why is version control important for scientific work?
These are some brief points on the value of version control in science. For more, see the section on [best practices for reproducible research](rst-guidelines)

* Collaboration - having your code on github makes it easy to share with a collaborator. Just add them to the project, or send a link if the repo is public. They will be able to keep up to date with all of your changes and contribute their own additions. 
* Work history and versioning for results - each commit has a unique ID and can be assigned a label ("tag"). You can record the ID or assign a label to the commit used to generate a specific set of results, a manuscript, or a report, rather than needing to keep multiple versions of a file around, like "analysis_results_jan_05_final_edits_FINAL_v3.py"
* Reproducibility - When it gets to be time to share the project with the wider world as part of publication, having project code in a well-organized repository makes it much easier for users to access, understand, and test. 
* Journal requirement compliance - as more journals require that your code be accessible, having it ready to go on github makes this an easy box to check off. 
* Branching and merging during development - you can create "branches" of your project to add new functionality or restructure your code while keeping the main version untouched, then "merge" the branch into the main version when it's ready to go. `Git` makes it easy to switch back and forth between versions. 


# Setting up a repository - the actual tutorial<a name="hands-on"></a>

In this tutorial, we'll go through the basics of setting up a github repository, making some changes on your local computer, and pushing them back to github. 


## Step 0: Get set up with git and a github account:

* If you don't have an account on [github.com](https://github.com), please register for one.
* Macs should have a version of git installed already, and I'm not sure about Windows. Downloads are available from here: [https://git-scm.com/downloads](https://git-scm.com/downloads).

## Step 1: Make a new repository on github:

On your github homepage, click the green "New" button in the upper left. 

* Pick a name for the repository, like "ki-github-tutorial". It doesn't matter if other people have repositories with the same name. 
* You can choose to make the repository public or private. If it's private, you can later grant access to specific people, or change it to public. 
* Add a README file. You can skip the .gitignore file and license for now, but it's a good idea to add licenses to projects you intend to make public (topic for another time). 
* Click "Create repository" at the bottom of the page.

!!! note
    Git historically names the main branch in the repository `master`, but there is a push to switch to `main`. When you create the repository, there will probably be a message that says "This will set `______` as the default branch. Change the default name in your settings". Feel free to change to `main` if it isn't already. You may need to restart the new repository process.

After you click the button, you'll be taken to the repository's page. There's a lot more on there than is needed for most uses. The main things to notice now are:
* The text of the README.md file is rendered on this page, making a useful landing page for information about what the project is about, contact info, etc...
* The bright green button that contains the link to download the code.
* The "settings" menu right above the green button.

## Step 2: Create a local copy and make some changes
* On Mac, open the terminal (find Terminal.app if you haven't used it)
* Create the folder you want the project folder to go into (when you clone the repository, it will make a new folder with the same name as the repository).
* Navigate to that folder in the terminal (e.g. type `cd /full/path/to/folder`).
* Click the green button on the repository's page, and copy the HTTPS URL in the popup.
* In the terminal, type `git clone [repository-url-here]`. This will download a copy of the repository to your computer.
* At this point, things can differ depending on what editor you like to use. Some editors, like Visual Studio Code, have git and a number of helper utilities built-in or accessible as extensions. We're going to stick with the command line/terminal for now.
* Open up README.md (this is a "Markdown" file). Underneath the title line, add some text describing the repository, then save and close the repo.
* In the terminal, run `git status`. This will show you that README.md has been modified since the last "commit"
* Run `git add README.md`, then `git commit -m "updating README"`. These commands tell git that we want README.md included in this commit, and then make the commit with a short message. 
* Finally type `git push` to send these changes back to github. 
* Reload the repository page on github to see the changes. 

## Step 3: Create a repository for a project you've already started

## Next Steps:
* .gitignore files
* Set up a project gh-pages to serve a webpage

## Version control/github terms
+ Repository
+ Clone
+ Commit
+ Push/Pull
+ Branch
+ Merge
+ Pull Request