Packer Demo
===

4/8/2016 Round Table

Prerequisites
===

*Please make sure you install the following before the demo, so that you can follow along.*

- Vagrant https://www.vagrantup.com/downloads.html
- VirtualBox https://www.virtualbox.org/wiki/Downloads
- Packer https://www.packer.io/downloads.html
- Ansible http://docs.ansible.com/ansible/intro_installation.html
  - Easiest is just to `sudo pip install ansible --upgrade`

Demo
===

- Clone this repo somewhere to your local box.
  - `git clone git@github.com:ekozlowski/packer_demo.git`

- I will be walking around with a flash drive with more content on it.  The flash drive will contain the Ubuntu ISO file we'll use.  (It's too large to download at the demo.)

What We'll Cover
---

- Creating a Ubuntu packer box from an ISO
- What the preseed.cfg file is, and why you need it
  - How Packer serves the preseed.cfg file
- How to get Packer to build a Vagrant compatible .box file
- What an AMI is
- How to extend Packer so that it builds an AMI for Amazon EC2
  - How to "base" your box on an existing AMI
- Where to go from here
