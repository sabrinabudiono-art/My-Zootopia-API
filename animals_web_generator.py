import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def print_animals():
    animals_data = load_data("animals_data.json")
    output = ""
    for animal in animals_data:
        output += f"Name: {animal["name"]}\n"
        output += f"Diet: {animal["characteristics"]["diet"]}\n"
        output += f"Location: {animal["locations"][0]}\n"
        if "type" in animal.get("characteristics", {}):
            output += f"Type: {animal["characteristics"]["type"]}\n"
        output += "\n"
    return output


def load_html():
  """ Loads a html file """
  with open("animals_template.html", "r") as fileobj:
      return fileobj.read()


def replace_info(html):
    animals_info = print_animals()
    return html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

def write_html(data):
    with open("animals.html", "w") as fileobj:
        fileobj.write(data)

def main():
    html = load_html()
    new_html = replace_info(html)
    write_html(new_html)


if __name__ == "__main__":
    main()