# library imports
from flask import jsonify, Flask, request
from geopy.distance import geodesic
import logging

# flask settings
app = Flask(__name__)
app.config["DEBUG"] = True

# logging settings
logging.basicConfig(filename="logs.log", level=logging.INFO)


# location the Moscow Ring Road
def moscow_ring_road_location():
    return "55.690943504922814, 37.413014159169926"


# assignment for distance calculation
def distance_location(your_distance):
    # verifies if in fact correct data is coming
    try:
        return geodesic(moscow_ring_road_location(), your_distance).miles
    except:
        return None


# endpoint to calculate distance
@app.route(...)
def calculate_distance(your_distance):
    your_distance = request.args.get('your_distance')
    # "try catch" to handle any errors that arrive
    try:
        distance = distance_location(your_distance)

        # condition for checking the distance between the person and the destination
        if distance == 0:
            # if the person is already at the destination
            message_result = 'You are already at Moscow Ring Road'
            # registered log
            logging.info('The person is in Moscow Ring Road')
        else:
            # if the person is not on the Moscow ring road, then show the distance to get there
            message_result = f'Your distance to Moscow Ring Road is: {distance:.5f} Miles'

            # registered log
            logging.info(f'The person is {distance:.5f} miles away')

        return jsonify(
            status_code=200,
            message=message_result
        )

    except:
        # registered log error
        logging.error("Error API - Request failed due to incorrect or correlated data")
        return jsonify(
            status_code=400,
            message="Error - Request failed due to incorrect or correlated data"
        )


# execute application
app.run()
