URL = "https://en.wikipeida.org/wiki/List_of_world_records_in_swimming"

import gazpacho
html = gazpacho.get(URL)
len(html)