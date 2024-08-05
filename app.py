import random
import time

import mesop as me
import mesop.labs as mel


def on_load(e: me.LoadEvent):
  me.set_theme_mode("system")


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/chat",
  title="Mesop Demo Chat",
  on_load=on_load,
)
def page():
  mel.chat(transform, title="Mesop Demo Chat", bot_user="Mesop Bot")


def transform(input: str, history: list[mel.ChatMessage]):
  for line in random.sample(LINES, random.randint(3, len(LINES) - 1)):
    time.sleep(0.3)
    yield line + " "


LINES = [
  "Hello"
]