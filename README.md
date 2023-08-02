# How to use FlumeAI to log your openAI calls

## Vanilla OpenAI (python)
If you are using openAI APIs directly, following the following steps

#### (1) Set the openAI base url to flumeAI

```python
openai.api_base = "https://flume-proxy.pankhudi.workers.dev/v1
```

#### (2) Pass Flume API key as a header param to openAI API. 

<normal>You should find the api key in the apps tab of your FlumeAI dashboard.</normal>

```python
headers={
        "Flume-API-Key": "f40133ec-6e37-40fd-b8a0-272d56d6aaa9",
}
```

#### (3) Optional - How to pass tags 

<normal>You can choose to identify you openAI with some tags. These tags will show alongside each API request on the requests tab of your FlumeAI dashbaord. You will be able to filter via these tags.</normal>

#### (4) Optional - How to pass properties 

<normal>You can set pass specific identifiers such as sessionId, conversationId, etc, by passing them to FlumeAI. These properties will show alongside each API request on the requests tab of your FlumeAI dashboard. This will allow to you filter by specific property values.</normal>
