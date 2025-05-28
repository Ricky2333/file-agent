from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv
import tools
import os

load_dotenv()  # take environment variables

model = OpenAIModel(
    model_name="deepseek-chat",
    provider=OpenAIProvider(
        api_key=os.getenv('OPENAI_API_KEY'),
        base_url="https://api.deepseek.com",
    )
)

fileagent = Agent(
    model=model,
    name="File Agent",
    system_prompt="A specialized agent designed to manage files and directories",
    tools=[
        tools.list_files,
        tools.delete_file,
        tools.rename_file,
        tools.move_file,
        tools.create_file,
        tools.append_to_file,
        tools.show_file_content,
        tools.create_folder,
        tools.copy_file,
    ]
)

def main():
    history = []
    while True:
        user_input = input("[User]: ")
        if user_input.lower() == "exit":
            break

        resp = fileagent.run_sync(user_prompt=user_input, message_history=history)
        history=list(resp.all_messages())
        print("[Agent]:", resp.output, '\n')


if __name__ == "__main__":
    main()