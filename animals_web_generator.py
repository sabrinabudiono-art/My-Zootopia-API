import json
import requests

headers = {
    'X-Api-Key' : '4UX4iKpH5Bi99WT5BsZNxOBkQKNlCCMTgGHkgdqp'
}

REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name=fox"
OUTPUT_FILE_NAME ="output.html"

def serialize_animal(animal_obj):
    """ Handle a single animal serialization """
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">Name: {animal_obj["name"]}</div>\n'
    output += '<div class="card__text">'
    output += '<ul>'
    if "diet" in animal_obj.get("characteristics", {}):
        output += f"<li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n"
    output += f"<li><strong>Location</strong>: {animal_obj["locations"][0]}</li>\n"
    if "type" in animal_obj.get("characteristics", {}):
        output += f"<li><strong>Type</strong>: {animal_obj["characteristics"]["type"]}</li>\n"
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def get_animals():
    """ Returns all the animals info """
    animals_data = requests.get(REQUEST_URL, headers=headers).json()
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def load_html():
  """ Loads a html file """
  with open("animals_template.html", "r") as fileobj:
      return fileobj.read()


def replace_info(html):
    """ Replace the placeholder with real animals info """
    animals_info = get_animals()
    return html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

def write_html(data):
    """ Write a new html """
    with open("animals.html", "w") as fileobj:
        fileobj.write(data)

def main():
    html = load_html()
    new_html = replace_info(html)
    write_html(new_html)


if __name__ == "__main__":
    main()