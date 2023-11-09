# ekg-interpretation
Project for Human Computer Interaction class where myself and Nick Landers design a web app that takes CSV data that represent an EKG reading and returns a statistical analysis of the results to the nurse.

Tech stack:

    Frontend:
        Tailwind CSS
            https://tailwindcss.com/docs/installation
            https://tailwindcss.com/docs/configuration
    Backend:
        Python with Flask
            https://flask.palletsprojects.com/en/3.0.x/installation/
            https://flask.palletsprojects.com/en/3.0.x/quickstart/
    Database:
        Do we really need this? To be discussed.


To run the web app:
First execute '. .venv/bin/activate'
Next, run 'flask --app demo run'

Also, the 'ecg.csv' file is one I found online here:
https://www.kaggle.com/datasets/devavratatripathy/ecg-dataset/
Each row corresponds to a patient - 
I would like to have the UI show the user a HR/time graph between the "upload EKG" button and the first
section that will be showing likely conditions. Let me know what you think