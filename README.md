# CPSY-300_Project01

Branch: Ritesh — Tasks 1 & 3
Task 1: Dataset Analysis

Analysed All_Diets.csv (7,806 recipes, 5 diet types)
The average macronutrient for each diet type was calculated.
Found Keto has highest average protein
Produced a bar chart, heatmap and scatter diagram graphics.

The files are as follows: data_analysis.py, All_Diets.csv and visualizations/.
Screenshots: All task 1 screenshots showing date/time are documented in the Visualizations.pdf with a bar chart, heatmap, scatter plot and terminal output.

Task 3: Serverless Function with Azurite

The local Azure Blob Storage emulator is ran as Azure "Azure Azurite".The local Azure Blob Storage emulator is: Azure Azurite.
Create a serverless function to read, process and store data
The simulated_nosql/results.json file is updated with results.

Files: lambda_function.py, simulated_nosql/results.json
Screenshots: All 3 screenshots that include a date and time are documented in the Visualizations.pdf file and include output from Azurite running, output from the lambda function, and output of results.json.


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
