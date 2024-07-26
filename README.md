# Accuknox DevOps Trainee Hiring Challenge Solution

## Problem Statement 1:

**Title:** Containerisation and Deployment of Wisecow Application on Kubernetes Project Repository: https://github.com/nyrahul/wisecow Wisecow App

**Objective:** To containerize and deploy the Wisecow application, hosted in the above-mentioned GitHub repository, on a Kubernetes environment with secure TLS communication.

**Prerequisites:**

Execute the following commands in order to solve Problem Statement 1

```sh
git clone https://github.com/nyrahul/wisecow.git
sudo apt install fortune-mod cowsay -y
./wisecow.sh
```

Now open your preferred browser and enter this URL: `http://localhost:4499` to get wisecow wisdom

**Requirements:**

- Dockerization:

  - Develop a Dockerfile for creating a container image of the Wisecow application.

  ```Dockerfile
  # use ubuntu as base image
  FROM ubuntu:22.04

  # update, upgrade and install the necessary dependancies
  RUN apt update -y && apt upgrade -y && apt install fortune-mod netcat cowsay -y

  # Set cowsay-app/ as working directory
  WORKDIR /cowsay-app

  # Copy all files from current directory from host machine to WORKDIR
  COPY . .

  # Expose a desired port for the container to be run
  EXPOSE  4499

  # Execute the following command once the container starts
  ENTRYPOINT ["sh","-c","export PATH=$PATH:/usr/games && ./wisecow.sh"]
  ```

- Kubernetes Deployment:
  - Craft Kubernetes manifest files for deploying the Wisecow application in a Kubernetes environment.
    - I am using minikube for implementing the K8s cluster.
    - Take a look at this path for more info about the cowsay-app config -> `/k8s/manifests/deployment.yaml`
  - The Wisecow app must be exposed as a Kubernetes service for accessibility.
    - For exposing and testing the cowsay app I have used `nodePort` as a service type and port-forwarded the response as shown in the screenshot below:
    <img width="987" alt="image" src="https://github.com/user-attachments/assets/e7c5e173-4f8f-403b-b56e-7738bd1d8281">
    <img width="997" alt="image" src="https://github.com/user-attachments/assets/b4bf2a30-4f11-4e7f-8c96-5adca0c41189">
    <img width="1440" alt="image" src="https://github.com/user-attachments
---

## Problem Statement 2:

Please choose any two objectives from the list below and attempt to achieve them using either Bash or Python.

1. **System Health Monitoring Script:**
   Develop a script that monitors the health of a Linux system. It should check CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script should send an alert to the console or a log file.
   
   For solution check `system-health.py` in this repo.

3. **Application Health Checker:**
   Please write a script that can check the uptime of an application and determine if it is functioning correctly or not. The script must accurately assess the application's status by checking HTTP status codes. It should be able to detect if the application is 'up', meaning it is functioning correctly, or 'down', indicating that it is unavailable or not responding.

   For solution check `app-health.py` in this repo.


---
