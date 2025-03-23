cach = {}

def get_page(url):
    if cach.get(url):
        return cach(url)
    else:
        data = get_data_from_server(url)
        cach(url) = data
        return data
