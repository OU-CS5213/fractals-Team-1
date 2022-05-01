---
marp: true
title: Python with GCP
paginate: true
theme: uncover
---
# Python project using serverless services(Cloud Function and Cloud Run) from GCP

**Sai Siddhardha Maguluri**
**Gnaneswar Kolla**
**Venkat Narra**

---
# Project Description
Restful APIs to render fractal images using serverless services like Cloud Function and Cloud Run from Google cloud Platform.
[Cloud Function URL](https://us-central1-sep-5213.cloudfunctions.net/getfractals)
[Cloud Run URL](https://fractal-service-jlmbmkr2aa-uc.a.run.app/)

---
# Cloud Function
1. Select or create a Google Cloud project and make sure that correct billing account is enabled for the project.
2. Create a Google Cloud Storage Bucket to hold the fractal images from [Tashfeen's](https://tashfeen.org/fractalsetc/build/index.html) project.
3. Give the bucket a name, select where to store data, select a default storage class, and select how to control object access and how to protect object data.
4. Finally, click create.
---
5. After creating the bucket, upload six images(Each fractal's image with its high and low resolution) and add principals **allusers** and role as **Cloud Functions Invoker**.
6. Each image uploaded to the bucket will have an URL which can be accessed from the browser.
7. Enable the following APIs.
    - Cloud Shell
    - Cloud Functions
    - Cloud Build
8. Open cloud functions page and create a function with 1st gen as Environment with suitable region.
---
9. Give the function a name, select HTTP as Trigger field and select allow unauthenticated invocations in the Authentication field.
10. Click save and next to go to Code tab and use the Runtime dropdown to select Python as desired language.
11. Change the code in the `main.py` file as required for the fractal project.
12. Create index.html and get image url  from the bucket to render html page.
---
13. Finally click deploy at the bottom of the page.
14. Similarly, create a cloud functions for each fractal image and resolutions(i.e total of 6)
---
# Cloud Run
1. Open cloud shell and create a directory fractal and open in editor. 
2. Create the following project structure with required files.
    ![Project Structure](https://user-images.githubusercontent.com/98314862/166159465-9a85fcc1-6481-4df2-bb3b-446ab5e9a186.png)
---
- `app.py` : contains code for the Flask application to the Fractal project.
- `requirements.txt` : contains dependency packages required for the project. 
- `Dockerfile` : contains all the commands to assemble an image.
- **Templates** folder contains html files.
        - `index.html` : contains REST API endpoints URL of fractal images.
        - `fractal.html` : contains code to render different images in different resolutions(low/high).
---
3. The following command is used to build container image.
    >gcloud builds submit --tag gcr.io/sep-5213/fractal:1.0.0 .
4. To deploy the container, the following command is used.
    >gcloud run deploy --image=gcr.io/sep-5213/fractal:1.0.0 --platform=managed --max-instances=1
---
**Thank You**

