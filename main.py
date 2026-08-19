import os
import argparse
import json

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key: str = os.environ.get("OPENROUTER_API_KEY")
if not api_key or api_key == None:
    raise RuntimeError("No API Key detected")

def main() -> None:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Userprompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    model: str = "openrouter/free"
    messages: list[dict[str, str]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user","content": args.user_prompt},
    ]
    response = client.chat.completions.create(model=model, messages=messages, tools=available_functions, temperature=0)
    if response.usage == None:
        raise RuntimeError("Usage property of response is None")
    if args.verbose == True:
        print(f"System prompt: {messages[0]["content"]}")
        print(f"User prompt: {messages[1]["content"]}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f" Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    if not message.tool_calls:
        print(response.choices[0].message.content)
    else:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            result_message = call_function(tool_call, args.verbose)
            if not result_message["content"]:
                raise Exception("Error: result_message.content is empty")
            if args.verbose:
                print(f"-> {result_message['content']}")

if __name__ == "__main__":
    main()
