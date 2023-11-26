![](https://i.imgur.com/pe1O565.png)
Medisight.co
=======================

**Live Demo**: [Link](http:127.0.0.1:5000)

A boilerplate for **flask** web applications.

When we started this project, our primary focus was on **simplicity** and **accessibility**. We stripped away all the features that only contribute to complexity. As a result, our service is very easy to install and use. It also means that it's very easy to contribute new features to this project. If you are interested in contributing, please make a pull request and we will review it as soon as possible.

<h4 align="center">Infobip API Example</h4>

![](https://i.imgur.com/REXf28X.png)

Table of Contents
-----------------

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Obtaining API Keys](#obtaining-api-keys)
- [Project Structure](#project-structure)
- [List of Packages](#list-of-packages)
- [Useful Tools and Resources](#useful-tools-and-resources)
- [Recommended Design Resources](#recommended-design-resources)
- [Contributing](#contributing)
- [License](#license)

Features
--------
- Login
- **Local Authentication** using Email and hashed Password
- **API Examples**
	- Infobip, Google Cloud, gCloud SQL, Github, OpenAI, MayoClinic, Postgresql 
- **Meetings**
    - Create, Edit, Delete, Join, Leave, View
- **Medical Form**
    - Create, Edit, Delete, View

Prerequisites
-------------

- PostgreSQL (local install OR hosted (like on gCloud))
  - Local Install: [PostgreSQL](http://www.postgresql.org/download/))
  - Hosted: No need to install, see the Google Cloud SQL DB section

- [Flask 3+](https://flask.palletsprojects.com/en/3.0.x/)
- Command Line Tools
 - <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Apple_logo_grey.svg" height="17">&nbsp;**Mac OS X:** [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) (or **OS X 10.9+**: `xcode-select --install`)
 - <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg" height="17">&nbsp;**Windows:** [Visual Studio Code](https://code.visualstudio.com) + [Windows Subsystem for Linux - Ubuntu](https://docs.microsoft.com/en-us/windows/wsl/install-win10) OR [Visual Studio](https://www.visualstudio.com/products/visual-studio-community-vs)
 - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/UbuntuCoF.svg/512px-UbuntuCoF.svg.png?20120210072525" height="17">&nbsp;**Ubuntu** / <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Linux_Mint_logo_without_wordmark.svg" height="17">&nbsp;**Linux Mint:** `sudo apt-get install build-essential`
 - <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Fedora_logo.svg" height="17">&nbsp;**Fedora**: `sudo dnf groupinstall "Development Tools"`
 - <img src="https://en.opensuse.org/images/b/be/Logo-geeko_head.png" height="17">&nbsp;**OpenSUSE:** `sudo zypper install --type pattern devel_basis`

**Note:** If you are new to Flask, you may find [Python Flask Tutorial: Full-Featured Web App series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) helpful for learning the basics of Flask and networking. Alternatively, here is another great tutorial for complete beginners - [Flask Tutorial by Tech with Tim](https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX).

Getting Started
---------------

**Step 1:** The easiest way to get started is to clone the repository:

```zsh
# Get the latest snapshot
git clone https://github.com/harishuthaya/hackwestern.git

# Change directory
cd hackwestern

# Install NPM dependencies
pip3 install -r requirements.txt

# Then simply start your app
flask run
```

**Note:** I highly recommend installing [theFuck](https://github.com/nvbn/thefuck). It allows you to have a much smoother experience within the terminal. During debugging or development, on the off chance that you mess up a terminal command, simply typing `fuck` afterwards will correct the command and allow you to run it again.

**Step 2:** Obtain API Keys and change configs if needed
After completing step 1 and locally installing Postgresql, you should be able to access the application through a web browser (at 127.0.0.1:5000) and use local user accounts after changing the database connection information. However, certain functions like API integrations may not function correctly until you obtain specific keys from service providers. The keys provided in the project serve as placeholders, and you can retain them for features you are not currently utilizing. To incorporate the acquired keys into the application, you have two options:
   
1.  Set environment variables in your console session: Alternatively, you can set the keys as environment variables directly through the command prompt. For instance, in bash, you can use the `export` command like this: `export API_KEY=xxxxxx`. This method is considered a better practice as it reduces the risk of accidentally including your secrets in a code repository.
2. Replace the keys in the `.env` file: Open the `.env` file and update the placeholder keys with the newly acquired ones. This method has the risk of accidental checking-in of your secrets to code repos, however makes it easier to collaborate on multiple systems.
    
*What to get and configure:*

- API keys for service providers in the API Examples if you are planning to use them.

- PostgreSQL
	- If you are using PostgreSQL on Google Cloud SQL instead of a local db, allow connections from your local public ips on the networking tab. Otherwise your connection will be denied.

**Step 3:** Develop your application and customize the experience

**Step 4:** Optional - deploy to production
See:
- [Deployment](#deployment)

# Obtaining API Keys
You will need to obtain appropriate credentials (Client ID, Client Secret, API Key) for API and service provides which you need (Infobip, OpenAI, Metered). See Step 2 in the Getting started section for more info.

<hr>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1000px-Google_2015_logo.svg.png" width="200">

- Visit <a href="https://cloud.google.com/console/project" target="_blank">Google Cloud Console</a>
- Click on the **Create Project** button
- Enter *Project Name*, then click on **Create** button
- Then click on *APIs & auth* in the sidebar and select *API* tab
- Click on **Google SQL API** under *SQL*, then click **Enable API**
 - **Application Type**: Web Application
 - **Authorized Flask origins**: set to your BASE_URL value (i.e. `http://localhost:8080`, etc)

<hr>

Project Structure
-----------------

| Name                               | Description                                                  |
| ---------------------------------- | ------------------------------------------------------------ |
| **flaskr**/__init__.py             | Flask webserver running on 127.0.0.1:5000                    |
| **static**/api.js                  | Controller for /api route and all login api examples.        |
| **static**/image1.png              | Medical practitioner image.                                  |
| **static**/image2.png              | Computer image.                                              |
| **static**/image3.png              | Web meeting graphic.                                         |
| **static**/image4.png              | Medical practitioners discussing image.                      |
| **templates**/navbar.html          | Navbar html file and structure.                              |
| **templates**/index.html           | Index page html structure.                                   |  
| **templates**/layout.html          | Layout html & css for landing page.                          |  
| **templates**/login.html           | Login webpage with login form.                               |  
| **templates**/signup.html          | Sign-up webpage with sign-up form.                           |             
| .env                               | Environment variables & API keys.                            |
| app.py                             | Folder and files ignored by docker usage.                    |
| auth.py                            | Your API keys, tokens, passwords and database URI.           |
| diagnos.py                         | Rules for eslint linter.                                     |
| infobip.py                         | Folder and files ignored by git.                             |
| webRTC.py                          | The main application file.                                   |
| README.md                          | Docker compose configuration file.                           |


**Note:** There is no preference for how you name or structure your views.
You could place all your templates in a top-level `views` directory without
having a nested folder structure if that makes things easier for you.
Just don't forget to corresponding `render_template()` paths in __init__.py.

List of Packages
----------------

| Package                         | Description                                                             |
| ------------------------------- | ------------------------------------------------------------------------|
| Flask                           | Webserver library (backend)                                             |
| OpenAI                          | OpenAI SDK API (medical ai)                                             |
| psycopg2 / psycopg2_binary      | Postgresql library                                                      |
| requests                        | POST / GET requests library                                             |
| rich                            | Rich format within cli                                                  |

Useful Tools and Resources
--------------------------
- [RealPython](https://realpython.com/python-sql-libraries/) - Database of Python SQL Libraries
- [Awesome Python](https://github.com/vinta/awesome-python) - A curated list of awesome Python frameworks, libraries, software and resources
- [git - the simple guide](https://rogerdudler.github.io/git-guide/) - just a simple guide for getting started with git. no deep shit
- [sentdex](https://www.youtube.com/user/sentdex/videos) - Python Programming tutorials, going further than just the basics

Recommended Design Resources
----------------------------
- [Code Guide](http://codeguide.co/) - Standards for developing flexible, durable, and sustainable HTML and CSS.
- [Bootstrap Zero](https://www.bootstrapzero.com) - Free Bootstrap templates themes.
- [Google Bootstrap](http://todc.github.io/todc-bootstrap/) - Google-styled theme for Bootstrap.
- [Font Awesome Icons](https://fontawesome.com) - Awesome font library .
- [Colors](http://clrs.cc) - A nicer color palette for the web.
- [Medium Scroll Effect](http://codepen.io/andreasstorm/pen/pyjEh) - Fade in/out header background image as you scroll.
- [GeoPattern](https://github.com/btmills/geopattern) - SVG background pattern generator.
- [Figma](https://www.figma.com/) - Amazing prototyping tool.

<hr>

Contributing
------------

If something is unclear, confusing, or needs to be refactored, please let me know.
Pull requests are always welcome, but due to the opinionated nature of this project, I cannot accept every pull request. Please open an issue before submitting a pull request.

License
-------

The MIT License (MIT)

Copyright (c) 2023-2023 Medisight.co

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
