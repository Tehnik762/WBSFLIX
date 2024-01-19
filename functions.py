def search_movies(data, query):
    query = query.lower()
    results = data[data['title'].str.lower().str.contains(query)]
    return results

