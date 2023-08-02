# How to use FlumeAI to log your openAI calls

## Vanilla OpenAI (python)
If you are using openAI APIs directly, following the following steps

#### (1) Set the openAI base url to flumeAI

```python
openai.api_base = "https://flume-proxy.pankhudi.workers.dev/v1
```

#### (2) Pass Flume API key as a header param to openAI API. 

```python
headers={
        "Flume-API-Key": "f40133ec-6e37-40fd-b8a0-272d56d6aaa9",
        }
```

#### (3) Optional - How to pass tags 

#### (4) Optional - How to pass properties 
