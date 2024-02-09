from dotenv import load_dotenv
from openai import OpenAI

# Load the environment variables from .env file
load_dotenv()

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
