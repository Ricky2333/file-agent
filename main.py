from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv
from prompt_toolkit import prompt
import tools
import os

load_dotenv() # Load environment variables from .env file

# Configure the language model
MODEL = 'DEEPSEEK'
# MODEL = 'QWEN'

if MODEL == 'DEEPSEEK':
    model_name = "deepseek-chat"
    api_key=os.getenv('DEEPSEEK_API_KEY')
    base_url="https://api.deepseek.com"
elif MODEL == 'QWEN':
    model_name = "qwen-plus"
    api_key=os.getenv('DASHSCOPE_API_KEY')
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"

# Ensure API key is available
if not api_key:
    print("Please set your API key in the .env file")
    exit()

# Initialize the language model provider
model = OpenAIModel(
    model_name=model_name,
    provider=OpenAIProvider(
        api_key=api_key,
        base_url=base_url,
    )
)

# Initialize the file agent with available tools
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
    """Main function to run the interactive agent."""
    history = [] # Store conversation history
    while True:
        try:
            user_input = prompt("[User]: ")
            if user_input.lower() == "exit":
                break

            # Run the agent with user input and history
            resp = fileagent.run_sync(user_prompt=user_input, message_history=history)
            history = list(resp.all_messages()) # Update history
            print("[Agent]:", resp.output, '\\n')
        except KeyboardInterrupt:
            # Allow graceful exit on Ctrl+C
            break


if __name__ == "__main__":
    main()