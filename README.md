
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#systemdesign">System Design</a></li>
      
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
![image](https://github.com/paudelanil/SaralYatra/assets/53502633/26eb5e79-6c6e-475d-89a6-5d967618b696)


Our team worked together on a cool project to make paying for public transportation super easy! We created an
app, which means you can just use your contactless card(NFC card) to hop on a bus 
without dealing with cash. This makes traveling around town much smoother and more convenient for everyone. 
Our goal was to make public transportation more modern and user-friendly, and we're excited about how our
project is making a positive impact on the way people get around. we've developed a user-friendly web app that serves as a terminal in public vehicles. Initially, we've set it up so that mobile phones equipped to accept NFC cards can act as terminals.
Moreover, we've designed a dedicated mobile app for users to easily check schedules, track routes, and stay updated on relevant information.

### Built With

Our MVP is built using follwoing framework and tech stacks
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Flutter](https://flutter.dev/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you can setup your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Clone the repo
  ```sh
  git clone https://github.com/your_username_/Project-Name.git
  ```
* create a virutal environment and activate it
  ```sh
  python -m venv <name of virtual environmnet>
  source <name of virtual environment>/bin/activate
  ```
  * install django
  ```sh
  pip install django
  ```
  * setup django(follow these step-wise.)
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  ```



<!-- USAGE EXAMPLES -->
## Usage

Our terminal app provides an interface to scan a NFC card by passengers. Upon scanning the NFC card, the entry passenger info is displayed for a short time.
In the meantime,  the system records other details like location, entry time of the particular passenger. Our system supports muliple entires and exit events.


The user entry status is automatically recorded and upon the exit, when passenger scans the NFC card, the app shows the total fare cost, destination stop and other details.


## System Design

![Blank_diagram4](https://github.com/paudelanil/SaralYatra/assets/53502633/6c9f5125-bcfc-47f0-97f9-d3c824636a1b)




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>







