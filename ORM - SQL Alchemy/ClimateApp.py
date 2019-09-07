from flask import Flask, jsonify

import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Mer Manahan's Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<start><br/>"
        f"/api/v1.0/start/end<starts><end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a Dictionary using date as 
       the key and prcp as the value.."""
    # Query the last years data
    last_year_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').all()
    all_data = []
    for date, prcp in last_year_data:
        data_dict = {date:prcp}
        all_data.append(data_dict)

    return jsonify(all_data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    
    # Return a JSON list of stations from the dataset
    stations_query = session.query(Station.station).all()
    list_of_stations=[]
    for station in stations_query:
        list_of_stations.append(station)

    return jsonify(list_of_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """query for the dates and temperature observations from a 
        year from the last data point. 
        Return a JSON list of Temperature Observations (tobs) 
        for the previous year."""

    # query for the dates and temperature observations from a year from the last data point.
    last_year_tobs = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= '2016-08-23').all()

    return jsonify(last_year_tobs)

@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return a JSON list of the minimum temperature, the average temperature, 
        and the max temperature for a given start or start-end range.
        When given the start only, calculate TMIN, TAVG, and TMAX for all 
        dates greater than and equal to the start date."""

    # query for TMIN, TAVG, TMAX for all dates greater than start date
    tobs_list=[]
    after_start_date = session.query(Measurement.tobs).\
            filter(Measurement.date >= start).all()
    for temp in after_start_date:
        tobs_list.append(temp)

    TAVG = np.mean(tobs_list)
    TMIN = np.min(tobs_list)
    TMAX = np.max(tobs_list)

    return jsonify(TMIN,TAVG,TMAX)

@app.route("/api/v1.0/<starts>/<end>")
def start_end(starts, end):
    """Return a JSON list of the minimum temperature, the average temperature, 
        and the max temperature for a given start or start-end range.
        When given the start only, calculate TMIN, TAVG, and TMAX for all 
        dates greater than and equal to the start date."""

    # query for TMIN, TAVG, TMAX for all dates between start and end dates
    tob_list=[]
    start_end_date = session.query(Measurement.tobs).\
            filter(Measurement.date >= starts).\
            filter(Measurement.date <= end).all()
    for temps in start_end_date:
        tob_list.append(temps)

    T_AVG = np.mean(tob_list)
    T_MIN = np.min(tob_list)
    T_MAX = np.max(tob_list)

    return jsonify(T_MIN, T_AVG, T_MAX) 

if __name__ == "__main__":
    app.run(debug=True)
