import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page
@APP.route('/')
def index():
    stats = {}
    x = db.execute('SELECT COUNT(*) AS series FROM SERIES').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS actors FROM ACTOR').fetchone()
    stats.update(x)
    logging.info(stats)
    return render_template('index.html',stats=stats)

# series
@APP.route('/series/')
def list_series():
    series = db.execute(
      '''
      SELECT SeriesId, Title, Premiere, Finale
      FROM SERIES
      ORDER BY Title
      ''').fetchall()
    return render_template('SERIES-list.html', series=series)


@APP.route('/series/<int:id>/')
def get_series(id):
  series = db.execute(
      '''
      SELECT SeriesId, Title, Premiere, Finale 
      FROM SERIES 
      WHERE SeriesId = %s
      ''', id).fetchone()

  if series is None:
     abort(404, 'Series id {} does not exist.'.format(id))

  genres = db.execute(
      '''
      SELECT GenreId, Label 
      FROM SERIES NATURAL JOIN GENRE 
      WHERE SeriesId = %s 
      ORDER BY Label
      ''', id).fetchall()

  actors = db.execute(
      '''
      SELECT ActorId, Name
      FROM SERIES NATURAL JOIN ACTOR
      WHERE SeriesId = %s
      ORDER BY Name
      ''', id).fetchall()


@APP.route('/series/search/<expr>/')
def search_series(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  series = db.execute(
      ''' 
      SELECT SeriesId, Title
      FROM SERIES
      WHERE Title LIKE %s
      ''', expr).fetchall()
  return render_template('series-search.html',
           search=search,series=series)

# Actors
@APP.route('/actors/')
def list_actors():
    actors = db.execute('''
      SELECT ActorId, Name 
      FROM Actor
      ORDER BY Name
    ''').fetchall()
    return render_template('actor-list.html', actors=actors)


@APP.route('/actors/<int:id>/')
def view_series_by_actor(id):
  actor = db.execute(
    '''
    SELECT ActorId, Name
    FROM ACTOR 
    WHERE ActorId = %s
    ''', id).fetchone()

  if actor is None:
     abort(404, 'Actor id {} does not exist.'.format(id))

  series = db.execute(
    '''
    SELECT SeriesId, Title
    FROM SERIES NATURAL JOIN ACTOR
    WHERE ActorId = %s
    ORDER BY Title
    ''', id).fetchall()

  return render_template('actor.html', 
           actor=actor, series=series)
 
@APP.route('/actors/search/<expr>/')
def search_actor(expr):
  search = { 'expr': expr }
  # SQL INJECTION POSSIBLE! - avoid this!
  actors = db.execute(
      ' SELECT ActorId, Name'
      ' FROM ACTOR '
      ' WHERE Name LIKE \'%' + expr + '%\''
    ).fetchall()

  return render_template('actor-search.html', 
           search=search,actors=actors)

# Genres
@APP.route('/genres/')
def list_genres():
    genres = db.execute('''
      SELECT GenreId, Label 
      FROM GENRE
      ORDER BY Label
    ''').fetchall()
    return render_template('genre-list.html', genres=genres)

@APP.route('/genres/<int:id>/')
def view_series_by_genre(id):
  genre = db.execute(
    '''
    SELECT GenreId, Label
    FROM GENRE 
    WHERE GenreId = %s
    ''', id).fetchone()

  if genre is None:
     abort(404, 'Genre id {} does not exist.'.format(id))

  series = db.execute(
    '''
    SELECT SeriesId, Title
    FROM SERIES NATURAL JOIN SERIES_GENRE
    WHERE GenreId = %s
    ORDER BY Title
    ''', id).fetchall()

  return render_template('genre.html', 
           genre=genre, series=series)

# Streams
@APP.route('/streams/<int:id>/')
def get_stream(id):
  stream = db.execute(
      '''
      SELECT StreamId, StreamDate, Charge, SeriesId, Title, CustomerId, Name
      FROM STREAM NATURAL JOIN SERIES NATURAL JOIN CUSTOMER 
      WHERE StreamId = %s
      ''', id).fetchone()

  if stream is None:
     abort(404, 'Stream id {} does not exist.'.format(id))

  return render_template('stream.html', stream=stream)


# Staff
@APP.route('/staff/')
def list_staff():
    staff = db.execute('''
      SELECT S1.StaffId AS StaffId, 
             S1.Name AS Name,
             S1.Job AS Job, 
             S1.Supervisor AS Supervisor,
             S2.Name AS SupervisorName
      FROM STAFF S1 LEFT JOIN STAFF S2 ON(S1.Supervisor = S2.StaffId)
      ORDER BY S1.Name
    ''').fetchall()
    return render_template('staff-list.html', staff=staff)

@APP.route('/staff/<int:id>/')
def show_staff(id):
  staff = db.execute(
    '''
    SELECT StaffId, Name, Supervisor, Job
    FROM STAFF
    WHERE staffId = %s
    ''', id).fetchone()

  if staff is None:
     abort(404, 'Staff id {} does not exist.'.format(id))
  superv={}
  if not (staff['Supervisor'] is None):
    superv = db.execute(
      '''
      SELECT Name
      FROM staff
      WHERE staffId = %s
      ''', staff['Supervisor']).fetchone()
  supervisees = []
  supervisees = db.execute(
    '''
      SELECT StaffId, Name from staff
      where Supervisor = %s
      ORDER BY Name
    ''',id).fetchall()

  return render_template('staff.html', 
           staff=staff, superv=superv, supervisees=supervisees)

