# Developer Guide
## Table of Contents
<!--ts-->
* **Our Repo**
   * [Coding Standards](#Coding-Standards)
   * [Development Environment](#Development-Environment)

 * **Appendix Tools**
   * [Using the Rileeki AWS Server](#option-1-using-the-rileeki-aws-server)
   * [Installing a Virtual Machine](#option-2-Installing-a-Virtual-Machine)
<!--te-->

## Our Repo
### Coding Standards
- Comment all functions
- Pep standards and lint choice (TBD - devs help me here)
- Most code changes should be done branches with pull requests managed on GitHub
  - creating a new local branch named my-new-branch:
    - `git checkout -b my-new-branch`
  - Push your branch to the remote repository (for the first time)
    - `git push --set-upstream origin my-new-branch`
  - Push updates on your branch to the remote repository
    - `git push origin my-new-branch`
  - When ready, create a pull request

### Development Environment
Using a local IDE of your choice, add the Git repos will need and set up the virtual environment to access helper functions 
 
- (Create a GITHUB account if you have not already - github.com)
- `git clone ssh://git@github.com/orchid-initiative/postpartum-larc` to your IDE
- Create a virtual environment to access shared helper functions
  - Background reading: [VIRTUAL ENVIRONMENTS 1](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/), [VIRTUAL ENVIRONMENTS 2](https://openclassrooms.com/en/courses/6900846-set-up-a-python-environment/6990546-manage-virtual-environments-using-requirements-files)
  - Generate SSH keys on your machine and then add your key to your github account
    - [Generating a SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/you generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    - [Adding your SSH key to github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
  - Run: `$ sudo apt install python3-pip`     (Installs the Python3 version of "pip" on your system, allowing you to easily install and manage Python packages)
  - Run: `$ pip install -r [YOUR REPO PATH]/requirements.txt`
    
## Appendix Tools
### Option 1: Using the Rileeki AWS Server
[Instructions](https://github.com/orchid-initiative/.github-private/blob/main/aws_setup.md)

### Option 2: Installing a Virtual Machine
Even if you use a PC in the general course of business, you may still find it more convenient to code in a unix OS.
A lightweight Linux VM from somewhere like VMware player can be a quick and easy solution.

**(time required: ~30-60 min)**
- Download latest VMware player (free) [LINK](https://www.vmware.com/go/downloadplayer)
- Download a Linux installation to use on the VM (free)
  - Try Mint XFCE first - its lightweight and might be all we need [LINK](https://www.linuxmint.com/edition.php?id=294)
  - Save the iso to a directory of your choice
- Create the VM with the Linux installation
  - Detailed Steps: [LINK](https://thesecmaster.com/step-by-step-procedure-to-install-linux-mint-linux-on-vmware-workstation/)
  - Highlights:
    - “Create a new Virtual Machine” and choose “I will install the operating system later”
    - Select a guest operating system: Linux with version “other linux 5.x kernel 64-bit”
    - Might want at least 100gb of space for your VM filesystem. **the synthea data logs can get big**
      - As an aside - if you ever try to log into your VM and it loops on the login page the likely culprit is low disk space - enter the terminal with "ctr-alt-f1" and login there, then proceed to delete some files to free up space.  Start with the raw /output/fhir/ files from synthea runs.
    - Right click on your new VM in the home menu of VMware workstation and go into settings
      - Allocate more memory - maybe 4gb depending on how much your physical machine has.  I have 32gb RAM and usually only use up to half of it so 4-8 would be fine to allocate when using I think
      - I increased processors to 4 - no idea how important this is
      - Under CD/DVD (IDE) select “use ISO image file” and point to where you put your Mint ISO
      - No further changes to settings
    - Hit “play virtual machine” - it will send you to a welcome screen and auto start linux mint after a 10 sec count down.
    - Once launched and at the desktop screen for linux click “install linux mint” and proceed to step “b” below
  - Go through the install, reboot, and then setup instructions
      - You can safely select “erase disk and install linux mint” this is only referring to the VM disk space you allocated in step 3.a.iii.
    - After the install finishes, restart.
    - Once it boots back up you move onto configuration suggestions - make sure not to enable timeshift - it eats up your disk space and makes it difficult to login ([reference topic discussion](https://forums.linuxmint.com/viewtopic.php?p=2059143))
    - I did the update manager with whatever it suggested.  Select the banner that suggest you “change mirror to a local one” to make this much much faster.  In the popup just click on the two sources and give it a sec to test speeds and select the top speed option for each.
    - Install GIT from the software manager, we will need it later
    - Restart now or after you install your preferred IDE




    
