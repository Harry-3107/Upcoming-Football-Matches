# Upcoming Football Matches

A full-stack web application that allows users to view upcoming football matches, teams, and leagues using the [Football Data API](https://www.football-data.org/). This project consists of a backend built with Flask to serve API endpoints and frontend files for displaying the data.


## Live Demo

The live working app is available at: [Upcoming Football Matches](https://upcoming-football-matches.onrender.com/)



## Features

- View upcoming football matches from various leagues.
- Select leagues and view associated teams.
- Display matches for selected teams.
- Filter matches based on league and team.
- Full-stack app with Flask for the backend and static frontend served through Flask.



## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (served via Flask)
- **API**: [Football Data API](https://www.football-data.org/)
- **Hosting**: Render (Backend) + Static files served from Flask



## Installation & Setup

1. Clone the repository:

   ### `git clone https://github.com/Harry-3107/Upcoming-Football-Matches.git` <br>
   ### `cd Upcoming-Football-Matches`
  

2. Install the necessary dependencies:
   
   ### `pip install -r requirements.txt`

4. Set up your API key for the [Football Data API](https://www.football-data.org/):
   - Sign up for an API key and place it in the `API_KEY` variable in `app.py`.

5. Run the backend server:

   ###  `python app.py`

   This will start the server at `http://localhost:5000/` by default.

6. Access the application:
   
   - Navigate to `http://localhost:5000/` in your browser to view the application.



## File Structure

Upcoming-Football-Matches/<br>
│<br>
├── backend/<br>
│   ├── app.py <br>
│   ├── requirements.txt  <br>
│<br>
├── frontend/ <br>
│   ├── index.html       <br>



## API Endpoints

### `/api/leagues`
- **GET**: Fetches the list of available football leagues.
  
### `/api/teams/<league_code>`
- **GET**: Fetches the list of teams for a given league.

### `/api/league/<league_code>/matches`
- **GET**: Fetches scheduled matches for a given league.

### `/api/matches/<int:team_id>`
- **GET**: Fetches upcoming matches for a specific team.
