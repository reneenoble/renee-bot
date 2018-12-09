from . import no_query

import re

def on_enter(query, output=print):
  # Don't repeat back any @user mentions!
  query = re.sub('<@.*> ', '', query)

  output(f"{query}... I haven't heard that one before.")
  output(f"What a good question! Ask me another!")

def on_input(input_data, question, output=print):
  return no_query.on_input(input_data, None, output)
