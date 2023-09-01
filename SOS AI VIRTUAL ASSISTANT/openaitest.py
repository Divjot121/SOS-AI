import os
import openai
from config import api_key
import random


def ai(prompt):
  openai.api_key = api_key
  text = f"Open AI Response for Prompt: {prompt} \n ***********************\n\n"

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
  )
  print(response["choices"][0]["text"])
  text += response["choices"][0]["text"]
  if not os.path.exists("Openai"):
    os.mkdir("Openai")

    with open(f"Openai/prompt- {random.randint(1, 23455967380)}", "w") as f:
      f.write(text)

{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-7tz1KXxj5oGZvp9B44Bqk7qvwkZh5",
  "object": "text_completion",
  "created": 1693576958,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject: Resignation from Position\n\nDear [Name of Boss],\n\nI am writing to inform you of my intention to resign from my position as [Position Title] with [Company Name] effective [date]. I have greatly enjoyed my time here and have grown professionally over the past [number of years], but I have decided to pursue other opportunities.\n\nI would like to thank you for the opportunity to work at [Company Name] and for your guidance and support over the years. I am confident that my experience here will help me in my future endeavors.\n\nIf there is anything I can do to help make the transition smoother, please let me know.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 150,
    "total_tokens": 159
  }
}
