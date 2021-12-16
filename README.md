![onion.watch](static/onions.png)

- [x] Install Vagrant and VirtualBox in [this tutorial](https://www.bogotobogo.com/DevOps/Vagrant/Vagrant_VirtualBox.php)

- [x] Install Ansible

  `s sudo apt-get update`

  `$ sudo apt-get install ansible`

- [x] Create a Virtual Environement

  `$ python3 -m vnv pyenv`

  `$ source pyenv/bin/activate`

  `$ pip install -r requirements.txt`

  `$ cd deep.dive-flask`
  
  `$ python app.py`

- [x] Create the VM and to provision it in one go

  `$ vagrant up`
  
:bulb: To destroy the VM, run:
  `$ vagrant destroy` 
  After it's destroyed, type vagrant up to recreate the VM and to provision it
  
- [x] SSH into the VM and run the following to get the server up:

  `$ vagrant ssh`
  
:bulb: To stop the server run **CTRL + C**

- [x] Since you already installed gunicorn via requirements.txt file, we should be able to run the following:
  
  `$ gunicorn --bind 0.0.0.0:8000 app:app` 

