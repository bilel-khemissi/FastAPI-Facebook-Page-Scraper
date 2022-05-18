<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/bilel-khemissi/FastAPI-Facebook-Page-Scraper">
    <img src="images/coding.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">FastApi Facebook Page Scrapper</h3>

  <p align="center">
    A dockerized facebook scrapping service using fastAPI.
    <br />
    <br />
    ·
    <a href="https://github.com/bilel-khemissi/FastAPI-Facebook-Page-Scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/bilel-khemissi/FastAPI-Facebook-Page-Scraper/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running-the-project">Running the project</a></li>
      </ul>
    </li>
    <li><a href="#running-the-project">Running the project</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#running-tests">Running tests</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#resources">Resources</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

This project is an API service meant to scrap posts from Facebook public pages using page's number then store the posts in a mongo-db database. <br/>
Posts have a unique ID named post_id in the database that help to identify posts in the database, as well as by username field.<br/>
<br/>
The default MongoDB connection was used to simplify the connection to the database (Hostname as "localhost" and port as 27017).

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [FastAPI](https://fastapi.tiangolo.com)
* [MongoDB](https://www.mongodb.com)
* [Python](https://www.python.org)
* [Docker](https://www.docker.com)
* [Facebook_Scraper](https://pypi.org/project/facebook-scraper/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

First, you need to install the packages needed for this project :
* pip
  ```sh
  pip install -r requirements.txt
  ```


## Running the project

To build a docker named “Facebook_Scrapper” for the API please run this command in the same directory as scraper.py, Dockerfile, and requirements.txt (with running mongo ):

```sh
  docker built -t Facebook_Scrapper
  ```

Then you can run the docker container :

```sh
  docker run -p 8000:8000 Facebook_Scrapper
  ```

or with Docker Compose

```sh
  docker-compose up
  ```

An other alternative is to run the project directly on your computer by installing all the requirements then :

```sh
  python -m uvicorn scraper:app --reload
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Run the project
- [x] Test the endpoints with swagger
- [x] Type a page name and its number
- [x] Check the result on the database


<p align="right">(<a href="#top">back to top</a>)</p>


## Running tests
You can run the available test by using Pytest:

```sh
  pytest
  ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

 [Bilel Khemissi](https://www.linkedin.com/in/bilel-khemissi/)

Project Link: [FastAPI Facebook Page Scaper](https://github.com/bilel-khemissi/FastAPI-Facebook-Page-Scraper)

<p align="right">(<a href="#top">back to top</a>)</p>




## Resources

* [FastAPI Documentation](https://fastapi.tiangolo.com)
* [Facebook Scraper Repository](https://github.com/kevinzg/facebook-scraper)
* [Pymongo](https://pymongo.readthedocs.io/en/stable/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-url]: https://www.linkedin.com/in/bilel-khemissi/
[product-screenshot]: images/screenshot.png
