# number_fact_alexa_skill
Number fact alexa skill. Choose a specific number or let alexa pick a random number for you. 

To run:
1. Run flask app: `python numbergeek.py`
2. Open a secure tunnel to localhost and expose that tunnel behind an http endpoint: `./ngrok http 5000`
3. Paste https endpoint in appropriate field on amazon developer site.
4. Prompt alexa with skill invocation name: "Alexa, start Johnny's Number Facts."
