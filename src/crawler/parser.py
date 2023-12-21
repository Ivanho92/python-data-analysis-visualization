def parse_data(soup, table_id):
    table = soup.find(id=table_id)
    rows = table.find_all('tr')

    data_dict = {
        'headers': list(),
        'data': dict()
    }
    for row in rows:
        if row.find('th'):
            row_headers = row.find_all('th')
            data_dict['headers'] = [row_header.get_text() for row_header in row_headers[1:]]
            continue

        row_classes = row.get('class')
        if row_classes is None: continue
        for row_class in row_classes:
            if row_class is not None and row_class in ['odd', 'even']:
                row_data = row.find_all('td')
                country = row_data[0].get_text()
                data_dict['data'][country] = dict()
                data_dict['data'][country]['data'] = [row_data_item.get_text() for row_data_item in row_data[1:]]
                continue

    return data_dict
