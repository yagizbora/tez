import openai

with open('api.txt') as file:
    openai.api_key = file.read()
    
def get_api_response(prompt: str) -> str | None:
    text: str | None = None 
    
    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,   
            stop=['Human','AI:']
        )
        
        
        choices: dict = response.get('choices')[0]
        
        print(response)
    except Exception as e:
        print('ERROR',e)

prompt = "The following  is a conversation with an AI assistant. The assistant helpful,creative,clever and very friendly\n\n\n\nHuman:Who are you?\nAI: I am an created by OpenAI. How can i help you today?\nHuman:Hello again!\nAI: Hi there, what can I do for you?\nHuman:"
get_api_response(prompt)