"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
# from home.pages import routes
from home.base_state import State
from home.pages import index

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


# Add state and page to the app.
app = pc.App(state=State)

# Add the pages to the app.
# for route in routes:
#     app.add_page(
#         route.component,
#         route.path,
#         route.title,
#         description="Write web apps in pure Python. Deploy in minutes.",
#         image="preview.png",
#     )
app.add_page(index)
app.compile()