import requests

headers = {
    'X-Api-Key' : '4UX4iKpH5Bi99WT5BsZNxOBkQKNlCCMTgGHkgdqp'
}

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  request_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  animals_data = requests.get(request_url, headers=headers).json()
  return animals_data
