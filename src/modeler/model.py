import json


def clean_data(data):
    print(json.dumps(data, indent=4))

    for country in data['data']:
        raw_data = data['data'][country]['data']
        filtered_data = list(filter(lambda item: item != '', raw_data))
        print('raw data:', country, raw_data)
        print('filtered data:', country, filtered_data)

        if len(filtered_data) > 1:
            data['data'][country]['data'] = filtered_data

    print(json.dumps(data, indent=4))

    return data
