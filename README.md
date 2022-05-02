# P10 Pur Beurre

### Context
Pur Beurre is a Django web application previously developped and deployed on a PAAS.<br>
👉 You can find it [here](https://github.com/Blankxx420/P8-Healty-choice).

In this project, we are deploying this app on an IAAS.

This project is part of my Python Developer training at [Openclassrooms](https://openclassrooms.com/fr/).

### General informations
HTTP server : Nginx<br>
HTTP Python server for Unix : Gunicorn<br>
CI pipeline with Travis CI<br>
Sentry monitoring
### Checklist 📝
- [x] Deploy on an IAAS
- [x] Setting up the Continuous Integration with Travis CI
- [x] Monitoring with Sentry
- [x] Add Cron job to automate a task : update OpenFoodFacts data once a week

Example of cron job:

```0 0 * * 0 /home/user/path/to/virtualenv/python /home/user/path/to/project/manage.py db_customized_command >> /tmp/myfile.log 2>&1```

### Author 📝
[BRICE GUICHOU](https://github.com/Blankxx420)