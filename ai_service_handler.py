def get_store_recommendations(...):
    ...
    stores_as_dicts = [
        {  
            'id': store.get('id'),  
            'name': store.get('name'),  
            'lat': store.get('lat', ''),  
            'lng': store.get('lng', ''),  
            ...
        }
        for store in stores
    ]
    ...
    main_screen_categories = [
        MainScreenCategoryList(
            id=store.get('id'),
            name=store.get('name'),
            lat=store.get('lat', ''),
            lng=store.get('lng', ''),
            ...
        )
        for store in stores
    ]
    ...