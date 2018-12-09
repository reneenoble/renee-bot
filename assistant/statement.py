from . import no_query

import re

def on_enter(statement, output=print):
  # Don't repeat back any @user mentions!
  statement = re.sub('<@.*> ?', '', statement)

  statement = statement.replace('@ncssbot ', '')
  output(f"'{statement}' is a statement. Try again.")

def on_input(input_data, question, output=print):
  return no_query.on_input(input_data, None, output)
