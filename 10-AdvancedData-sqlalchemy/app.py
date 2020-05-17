import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f"<a href='/api/v1.0/2016-08-23'>/api/v1.0/2016-08-23</a><br/>"
        f"<a href='/api/v1.0/2016-08-23/2017-08-23'>/api/v1.0/2016-08-23/2017-08-23</a><br/>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation by date"""
    # Query all prcp
    results =  session.query(Measurement.date, Measurement.prcp).all()

    session.close()
    
    # Create a dictionary from the row data and append to a list of all_prcp
    all_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations from the dataset"""
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)
    

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list all temperature observations by date of the most active station for the last year of data"""
    # Query all temperature observations
    results = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.station == 'USC00519281').all()

    session.close()
    
    # Create a dictionary from the row data and append to a list of all_tobs
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["temp observations"] = tobs
        all_tobs.append(tobs_dict)


    return jsonify(all_tobs)

@app.route("/api/v1.0/2016-08-23")
def startdate():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date"""
    # Query all temperature observations
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                filter(Measurement.date >= '2016-08-23').all()

    session.close()    
    
    # Convert list of tuples into normal list
    sdate_tobs = list(np.ravel(results))

    return jsonify(sdate_tobs)

@app.route("/api/v1.0/2016-08-23/2017-08-23")
def startandenddate():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive"""
    # Query all temperature observations
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                filter(Measurement.date >= '2016-08-23').\
                filter(Measurement.date <= '2017-08-23').all()

    session.close()    
    
    # Convert list of tuples into normal list
    sedate_tobs = list(np.ravel(results))

    return jsonify(sedate_tobs)

if __name__ == '__main__':
    app.run(debug=True)
