import data_fetcher

def get_animals_html(animals_data, animal_name):
    output = ""
    if not animals_data:
        output += f"<h2>The animal '{animal_name}' doesnt exist.</h2>"
    else:
        for animal_obj in animals_data:
            output += serialize_animal(animal_obj)
    return output

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


def load_html():
  """ Loads a html file """
  with open("animals_template.html", "r") as fileobj:
      return fileobj.read()


def replace_info(html, animals_info):
    """ Replace the placeholder with real animals info """
    return html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

def write_html(data):
    """ Write a new html """
    with open("animals.html", "w") as fileobj:
        fileobj.write(data)

def main():
    html = load_html()
    animal_name = input("Enter a name of an animal:")
    animals_html = get_animals_html(data_fetcher.fetch_data(animal_name), animal_name)
    new_html = replace_info(html, animals_html)
    write_html(new_html)
    print("Website was successfully generated to the file animals.html")


if __name__ == "__main__":
    main()