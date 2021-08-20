import requests
from geopy.units import radians
from api.address import Address


# function to search the given address
def search_address(address: str) -> list:
    arr = []
    parameters = {
        "apikey": "8ef38655-abbc-4679-9073-4e4f89d1773f",
        "format": "json",
        "lang": "en_US",
        "geocode": address,
        "results": 1
    }
    # to check if the result exists
    try:
        response = requests.get(
            "https://geocode-maps.yandex.ru/1.x/?", params=parameters)
        data = response.json()
        print("lo que quiero ver es: ", data.get("resoponse").get(
            "GeoObjectCollection").get("featureMember"))
    except:
        try:

            for i in (data.get('response').get('GeoObjectCollection').get(
                    'featureMember')):
                # name of each result
                name = (i.get('GeoObject').get('metaDataProperty').get(
                    'GeocoderMetaData').get('text'))
                # store coordinates
                coord = (i.get('GeoObject').get('Point').get('pos'))
                coord2 = coord.split(" ")
                # store longitude and latitude
                lon = coord2[0]
                lat = coord2[1]
                # create the address object to store the info and add it to array.
                address_object = Address(name, lat, lon)
                arr.append(address_object)

            return arr

        except:
            return ["There was an error. Send the request again."]
    return arr

# result = search_address(false)
# print(search_address(false))
# print(len(result))
# for elem in result:
#     print(elem)
