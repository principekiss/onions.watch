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
</br>


</br>

This project is a copy of [dark.fail](https://dark.fail) and aims to provide a codebase to allow anyone to create their own information site to assess the uptime of popular [onion services](https://community.torproject.org/onion-services/). <b><i>I solemnly swear that i am up to no dark.</i></b>
</p>


</br>
</br>

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
  

