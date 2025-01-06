import os


def main():
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        print("OPENAI_API_KEY is not set")
    else:
        print("OPENAI_API_KEY is set")
        print(api_key)

if __name__ == "__main__":
    main()
        