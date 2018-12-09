import re

def on_enter(data, output=print):
  output("Ask me about an event.")

def on_input(input_data, data, output=print):
  return parse_query(input_data)

def parse_query(query_text):
  search = re.search('(.*\?)', query_text, re.IGNORECASE)

  if search:
    return 'QUERY', search.group(1)
  else:
    return 'STATEMENT', query_text
