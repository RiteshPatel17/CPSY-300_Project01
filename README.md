# CPSY-300_Project01

Branch: Aaryan — Tasks 2 & 4
Now, it is time to create the Docker image for the Application.Task 2: Dockerizing the Application.

Created a Dockerfile to containerize the Python 3.9 slim base image on which the data_analysis.py script is based.
Using Docker build to create the image locally
Aran, ran and tested the container to ensure the analysis runs as expected within Docker.
Staged the image to Docker Hub with username “aaryan8888”
Written a docker-compose.yml to mimic cloud deploy locally.

Files: Dockerfile, docker-compose.yml
Screenshots: All Task 2 screenshots with date/time are included in Screens_3_and_4.pdf which include Docker build, Docker run, Docker Hub login, Docker Hub repository, and Docker Compose deployment.

Create a CI/CD Pipeline using GitHub Actions

Created .github/workflows/deploy.yml pipeline
Pipeline automatically starts on each push to the Aaryan branch
Python installs, downloads dependencies, executes data analysis as a test and creates Docker image.
The GitHub Actions pipeline ran successfully with green checkmark.

Files: .github/workflows/deploy.yml
Screenshots: All Task 4 screenshots are captured and documented in Screens_3_and_4.pdf, such as the capture of GitHub secrets configuration and GitHub Actions green pipeline.
