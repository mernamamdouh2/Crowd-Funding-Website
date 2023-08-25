# Crowd-Funding-WebApp

<h1 align="center">
  <br>
  <a href=""><img src="https://www.iti.gov.eg/assets/images/iti-logo.png" alt="ITI" width="200"></a>
  <br>
  ITI
  <br>
</h1>

<h4 align="center">This is a web platform for starting fundraising projects in Egypt. It allows users to create fundraising campaigns, donate to projects, and rate and comment on projects.
.</h4>

![screenshot](https://www.educative.io/cdn-cgi/image/f=auto,fit=contain,w=1200/api/page/4851104629129216/image/download/5817722754564096)


---------------------------------------------------------------

## How to run
---------------------------------------------------------------
pip install virtualenv
----------------------------------------------------------------
virtualenv my_env_name
----------------------------------------------------------------
virtualenv my_env_name to create a new environment
----------------------------------------------------------------
source my_env_name/bin/activate to activate the new environment
----------------------------------------------------------------
pip install -r requirements.txt
----------------------------------------------------------------
python manage.py migrate
----------------------------------------------------------------
python manage.py createsuperuser
----------------------------------------------------------------
python manage.py runserver
----------------------------------------------------------------
The web app should now be accessible at http://localhost:8000.


---------------------------------------------------------------
Project Structure
The project is structured as follows:
<div>
  <ul>
    <li><strong>crowdfunding/</strong>
      <ul>
        <li>settings.py</li>
        <li>urls.py</li>
        <li>wsgi.py</li>
        <li>asgi.py</li>
      </ul>
    </li>
    <li><strong>users/</strong>
      <ul>
        <li>urls.py</li>
        <li>views.py</li>
        <li>models.py</li>
        <li>forms.py</li>
      </ul>
    </li>
    <li><strong>indexapp/</strong>
      <ul>
        <li>urls.py</li>
        <li>views.py</li>
        <li>models.py</li>
        <li>forms.py</li>
      </ul>
    </li>
    <li><strong>projectsapp/</strong>
      <ul>
        <li>urls.py</li>
        <li>views.py</li>
        <li>models.py</li>
        <li>forms.py</li>
      </ul>
    </li>
  </ul>
</div>


## Created By

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/bedaba">
        <img src="https://avatars.githubusercontent.com/u/21156712?v=4" width="100px" alt="Bedaba Edward">
      </a>
      <br>
      <a href="https://github.com/bedaba">Bedaba Edward</a>
    </td>
    <td align="center">
      <a href="https://github.com/mohamedsto7y">
        <img src="https://avatars.githubusercontent.com/u/34280108?v=4" width="100px" alt="Second User">
      </a>
      <br>
      <a href="https://github.com/mohamedsto7y">Mohamed Elsayed</a>
    </td>
    <td align="center">
      <a href="https://github.com/Ahmed-AbdElRhman">
        <img src="https://avatars.githubusercontent.com/u/43652872?v=4" width="100px" alt="Third User">
      </a>
      <br>
      <a href="https://github.com/Ahmed-AbdElRhman"> Ahmed AbdElRhman </a>
    </td>
    <td align="center">
      <a href="https://github.com/mernamamdouh2">
        <img src="https://avatars.githubusercontent.com/u/74082044?v=4" width="100px" alt="Fourth User">
      </a>
      <br>
      <a href="https://github.com/mernamamdouh2">Merna Mamdouh</a>
    </td>
     <td align="center">
      <a href="https://github.com/ayahassanali96">
        <img src="https://avatars.githubusercontent.com/u/111661698?v=4" width="100px" alt="Fourth User">
      </a>
      <br>
      <a href="https://github.com/ayahassanali96"> Aya Hassan </a>
    </td>
  </tr>
</table>


## [License](https://github.com/Cooperate-IT-Projects-Python/Crowd-Funding-WebApp/blob/main/LICENSE)

MIT
