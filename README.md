<p align="center">
 <img src="static/onions.svg">
</p>

<p align="center">
  <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/tuxicorn/onions.watch" />
  <img alt="Github License" src="https://img.shields.io/github/license/tuxicorn/onions.watch" />
 <img alt="PR friendly" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat" />
 <img alt="Python Version" src="https://img.shields.io/github/pipenv/locked/python-version/tuxicorn/onions.watch" />
 <img alt="Flask Version" src="https://img.shields.io/github/pipenv/locked/dependency-version/tuxicorn/onions.watch/flask/master" />
 <img alt="Requests Version" src="https://img.shields.io/github/pipenv/locked/dependency-version/tuxicorn/onions.watch/requests/master" />
 <img alt="Reddit" src="https://img.shields.io/reddit/user-karma/combined/principekiss?style=social" />
 
 
</p>

<p align="center">
<i>Learn how to use Tor hidden services safely. Check whether a darknet site is online, view the uptime history of popular darknet sites and their mirrors.</i>
</p>

This project is a copy of [dark.fail](https://dark.fail) and aims to provide a codebase to allow anyone to create their own [onion services](https://community.torproject.org/onion-services/) informational website as well.


Install Vagrant and VirtualBox in [this tutorial](https://www.bogotobogo.com/DevOps/Vagrant/Vagrant_VirtualBox.php)

Install Ansible

```sh 
sudo apt-get update
```

```sh 
sudo apt-get install ansible
```

Create a Virtual Environement

```sh
pipenv shell
```

```sh
pipenv install
```
  
```sh
python app.py
```

Create the VM and to provision it in one go

```sh
vagrant up
```

Destroy the VM
```sh
vagrant destroy
```
  

