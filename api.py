import google.generativeai as genai

genai.configure(api_key="your_api_key")

models = genai.list_models(models/gemini-2.5-flash)

print("Available Gemini Models:\n")
for model in models:
    print(model.name)

