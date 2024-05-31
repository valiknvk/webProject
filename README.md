# Basic Web Portfolio

## Introduction
Web application with a login functionality. Displays short user account info and "about me" page.  
Developed to demonstrate technical skills for DevOps engineer.  
Can be accessed [here](https://vn.dev-space.co) (Just sign up and test)  

## Tasks
 - [x] Available on the internet webpage with domain and TLS/SSL certs.
 - [x] Possibility of a multi-platform deploy with CI/CD. 

## Technologies
 - Python3 (Flask)
 - Postgresql 
 - GitHub (GitHub Actions)
 - Linux ( ubuntu-22.04 )
 - Docker (Docker-compose, Docker-hub)
 - k8s ( kubeadm cluster )

## Description
Application is a combination of Pyhton3+Flask backend connected to postgresql and simple frontend.  
CI/CD  implemented using GitHub Actions. Current strategy is manual run image build workflow and then automatically deploy and test.  
Can be deployed as:
 - program(service) on Linux ( tested ubuntu-22.04 );
 - build as docker image and
   - run as container ([docker-hub](https://hub.docker.com) public repository - novikva/flasklogin:latest)
   - run on Kubernetes ( tested kubeadm cluster )

## The project status
Active: The project is currently being worked in my spare time.
