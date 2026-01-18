import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal_obj):
    """ Handle a single animal serialization """
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">Name: {animal_obj["name"]}<br/></div>\n'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n"
    output += f"<strong>Location</strong>: {animal_obj["locations"][0]}<br/>\n"
    if "type" in animal_obj.get("characteristics", {}):
        output += f"<strong>Type</strong>: {animal_obj["characteristics"]["type"]}<br/>\n"
    output += '</p>'
    output += '</li>'
    return output


def print_animals():
    """ Returns all the animals info """
    animals_data = load_data("animals_data.json")
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
    animals_info = print_animals()
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