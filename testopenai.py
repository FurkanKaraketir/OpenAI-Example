import openai

openai.api_key = "YOUR API KEY"
response = ""
while True:
    answer = input()
    try:
        prompt = response[0].get("text") + "\n" + answer
    except:
        prompt = response + "\n" + answer

    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        temperature=0.7,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response = response.get("choices")

    print(response[0].get("text"))
