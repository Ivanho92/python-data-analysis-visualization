import os

import config
from src.api.geocode import get_coordinates
from src.store.db import get_content, store_model


def prepare_model():
    content = get_content()

    model = list()
    for row in content:
        country, avg_seizures = row

        try:
            coordinates = get_coordinates(config.API_ENDPOINT, os.environ['API_KEY'], country)
        except Exception as error:
            print('ERROR >> Problem with coordinates\n', error)
            quit()

        model.append({
            'country': country,
            'avg_seizures': avg_seizures,
            'coordinates': coordinates
        })

    store_model(model)
