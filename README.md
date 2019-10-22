# DevOps-coding-challenge
Coding challenge for full stack Engineer/Senior/Lead/Architect - DevOps/Cloud. The challenge is categories in two sections as junior and senior full stack DevOps positions but you are free to takeup any challenge.

# Goal

The goal of this exercise is to access your familiarity with DevOps concepts, tools, cloud platforms and your programming/scripting skills.

# Rules
- Solve any one from the respective sections listed below
- Clone this repo and create your branch for implementing the solution and upon completion push the Branch to remote
- Complete the challenge within 5 days, mention time spent in hours explicitly took for solving the challenge
- Your solution should be clean, readable, maintainable and implemented with emphasize on DevOps methodologies
- You are free to use the programming language, tools and cloud platform of your choice
- Provide a description, execution steps and testing steps in plain text file (EXECUTION-STEPS.txt)
- We are absolutely not looking for completion or perfection, we expect trade-offs to be made
- Submit all the codebase, diagrams and documents
- Bonus points: For the solutions built with best security practice
- Bonus points: For the solutions built with out of box approach

# Prerequisites
You might need an AWS/Azure/GCP account. Create one if you do not own one already. You can use free-tier resources for this test.

# Challenges
Full Stack Engineer - DevOps/Cloud  (junior)
------------
| #No  |   Problem statement|
| ------------ | ------------ |
|  1 |Implement rest layer application in golang/python/nodeJS (any one of your choice) that should listen on port 9097 and should ask for name and upon submitting should return "Hello [entered name]" string <br> E.g. If you submit "Cognologix" the returning string will be "Hello Cognologix". In case no name is provided it should return "Hello stranger"<br> Dockerize the above implemented application.<br>|
| 2  | Use Infrastructure as code (IaC) tool of your choice (ansible/terraform/cloudformation/python etc) and cloud of your choice (AWS/Azure/GCP). Create VM auto scaling group of 1 to 3 VMs with at least 1 VM always running and should meet following elastic criteria<br> a) Keep adding VM when CPU utilization goes above 80%<br> b) Terminate the VM when CPU utilization reduces to 30%<br>Provide your testing method/codes/scripts along with the IaC codebase |
|3   |  Implement simple MEAN stack application to perform user registration by asking users to provide the information like Name, Age, Address, Phone and Blood group. The registration entries should be available in to the DB and can be fetched later for analytics.<br>-  Dockerize the application<br>- Implement Docker compose to configure and run the application with services |
| 4 | A Linux server is hosted with IMAP service. All the IMAP member mail directory is configured under specific domain directory e.g */home/domain/member/mail*. Customer requested for a simple backup solution using bash script.<br>- Implement the script that will find all the files present in the mail directory between specific date & time e.g. from 01 september 10 am to 02 september 9 am.<br>- Copy all the files to remote passive IMAP server under the same domain/user directory structure|


Full Stack Senior/Lead/Architect - DevOps/Cloud (senior)
------------
|  #No |  Problem statement |
| ------------ | ------------ |
| 1  |  Implement CI pipeline for https://github.com/elastic/elasticsearch on Jenkins or GitLab |
|2   |  Use any IaC tool of your choice (ansible/Terraform/Python etc) and deploy https://github.com/scotch-io/node-todo on aws or gcp or azure |
| 3  |  Implement kubernetes deployment for https://github.com/codeworksio/docker-streaming-server |
|  4 |  A tech startup working on a project involving 10 members of team. The project comprises 3 modules and they want to follow git multi repo based approach. On each module team of 2 developers and 1 QA are suppose to work with 1 manager looking out on entire project. Their goal is to have continuous product release strategy. To achieve their goal<br> - What will be the git branching strategy, elaborate why & why not with pros and cons<br>- Which tool you will consider for CI/CD<br>- What will be your build promotion plans (Dev - QA - Prod)<br>- Provide CI/CD implementation plans with stages<br>- How will you manage module version dependencies |
|  5 |  A tech startup implementing food waste sharing application and wanted to make the application go live publically with an estimated user sharing workflow hit through app close to 10 millions. The technology stack includes hybrid frontend and business logic implemented using Java with a DB for persisting workflow details.<br>- Propose cloud of your choice for IaaS and PaaS usage<br>- Which all cloud managed services you want to propose to host and manage this application on cloud<br>- Architect the cloud infrastructure for the same<br>- Use draw.io or any other tool of your choice and send us deployment architecture diagram along with the above mentioned proposal |
|  6|Customer running workloads on the production systems. The production environment is made highly available and scalable so assume that the application is running on N number of Linux VMs. After launching the application on production one of the QA members reported service impacting bug and should be fixed on priority. Development team worked and fixed the bug. The fixed is into a config file named location.properties. As a DevOps Engineer you need to replace existing */etc/location.property* file on all the N VMs with this new file provided by developer.<br>- Implement a solution to distribute location.property file on all N VMs<br>- Report the number of VMs on which the file is successfully distributed<br>- Report the number of VMs on which the file is failed to transfer<br>Use your choice of language to implement this solution. Document the approach, thought and methodology used for this solution. |




