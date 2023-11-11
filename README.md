<normal>FlumeAI is an observability solution for Generative AI apps, kinda like datadog/sentry is for regular apps. We help you log and track your openAI API requests and uncover potential issues with your responses. We support Langchain. To get access, email pankhudi@gmail.com</normal>

# How to use FlumeAI to log your openAI calls

#### (1) Set the openAI base url to flumeAI
<normal> You can see this in app.py. </normal>

```python
openai.api_base = "https://oai.flumeai.workers.dev/v1"
```

#### (2) Pass Flume API key as a header param to openAI API. 

<normal>You should find the api key in the apps tab of your FlumeAI dashboard. Pass this API key in the headers. You can find relevant examples in app.py</normal>

```python
headers={
        "Flume-API-Key": "xxxx33ec-6e37-40fd-b8a0-272d56d6xxxx",
}
```

#### (3) Optional - How to log tags

<normal>You can choose to identify you openAI with some tags. These tags will show alongside each API request on the requests tab of your FlumeAI dashbaord. You will be able to filter via these tags. You can pass these tags in the headers. See examples in app.py.</normal>

#### (4) Optional - How to log properties

<normal>You can set pass specific identifiers such as sessionId, conversationId, etc, by passing them to FlumeAI. These properties will show alongside each API request on the requests tab of your FlumeAI dashboard. This will allow to you filter by specific property values. You can pass properties via headers. See examples in app.py.</normal>

#### (5) How to run examples in this repo.

<normal>First clone this repo and add your openAI API key in .env file. In the main directory, start up Python VM, install requirements and start Flask server as shown below. Once the server is running at 5000, use the respective endpoints in app.py to test different use cases. 

```python
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
flask run
flask run --port xxxx  //to run on a specific port 
```
