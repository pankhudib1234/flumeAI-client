import os
from dotenv import load_dotenv
import openai

from flask import Flask, jsonify, request
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts import (
    PromptTemplate,
)
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain

from langchain.schema import (
    HumanMessage,
    SystemMessage
)

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
print(os.getenv("FLASK_APP"))

# add following line to start logging your openAI requests using Flume
openai.api_base = "https://oai.flumeai.workers.dev/v1"

@app.route("/", methods=["GET"])
def index():
    return jsonify("Not implemented. Check app.py for valid routes.")

# vanilla open AI single shot example
@app.route("/flume/simple", methods=["GET"])
def get_completion_simple():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="I want a short childen's story about a boy who goes to the moon.",
        temperature=0.2,
        headers={
            "Flume-API-Key": "ADD_YOUR_FLUME_API_KEY_HERE",
            "Flume-Metadata-Session": "session-simple",
            "Flume-Metadata-Conversation": "conversation-simple",
            "Flume-Tags": "promptchain1-simple,openAI-vanilla",
        },
    )
    return jsonify(response)

# simple one short example using langchain 
@app.route("/flume/langchain/simple", methods=["GET"])
def get_completion_langchain_simple():
    llm = OpenAI(temperature=0.6,
                 n=1,
                 headers={
                     "Flume-API-Key": "ADD_YOUR_FLUME_API_KEY_HERE",
                     "Flume-Metadata-Session": "session-langchain-simple",
                     "Flume-Metadata-Conversation": "conversation-langchain-simple",
                     "Flume-Tags": "promptchain-langchain",
                 })

    prompt = PromptTemplate(
        input_variables=["pet"],
        template="Give me one name for a small {pet}?",
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run("dog")
    return jsonify(response)

# langchain chat example
@app.route("/flume/langchain/chat2", methods=["GET"])
def get_completion_langchain_chat2():
    chat = ChatOpenAI(temperature=0.6,
                 headers={
                     "Flume-API-Key": "ADD_YOUR_FLUME_API_KEY_HERE",
                     "Flume-Metadata-Session": "session-1234-chat2",
                     "Flume-Metadata-Conversation": "issue2345-chat2",
                     "Flume-Tags": "promptchain1-chat2,production-chat2",
                 })

    batch_messages = [
    [
        SystemMessage(content="You are a helpful assistant that translates English to Spanish."),
        HumanMessage(content="I love programming.")
    ],
    [
        SystemMessage(content="You are a helpful assistant that translates English to Flemish."),
        HumanMessage(content="I love artificial intelligence.")
    ],
]
    result = chat.generate(batch_messages)
    print(result)
    return jsonify({"result": "check console"})

# langchain example with sequential chains
@app.route("/flume/langchain/seq", methods=["GET"])
def get_completion_langchain_seq():
    llm = OpenAI(temperature=0.9,
                 headers={
                     "Flume-API-Key": "ADD_YOUR_FLUME_API_KEY_HERE",
                     "Flume-Metadata-Session": "session-langchain-seq",
                     "Flume-Metadata-Conversation": "conversation-langchain-seq",
                     "Flume-Tags": "promptchain-seq,production-seq",
                 })

    prompt1 = PromptTemplate(
        input_variables=["animal"],
        template="Give me one name for {animal}?",
    )

    prompt2 = PromptTemplate(
        input_variables=["name"],
        template="Write a sonnet for this {name}?",
    )

    chain1 = LLMChain(llm=llm, prompt=prompt1)
    chain2 = LLMChain(llm=llm, prompt=prompt2)
    overall_chain = SimpleSequentialChain(
        chains=[chain1, chain2], verbose=True)
    response = overall_chain.run("dog")
    return jsonify(response)


# langchain example for chat
@app.route("/flume/langchain/chat", methods=["GET"])
def get_completion_langchain_chat():
    llm = OpenAI(temperature=0.9, headers={
                     "Flume-API-Key": "ADD_YOUR_FLUME_API_KEY_HERE",
                     "Flume-Metadata-Session": "session-langchain-seq-chat",
                     "Flume-Metadata-Conversation": "conversation-langchain-seq-chat",
                     "Flume-Tags": "promptchain-seq-chat,production-seq-chat",
    })

    template = "You are a helpful assistant that translates English to French.\n' \
                {history}\n' \
                Human: {human_input}\n' \
                Assistant:"

    prompt = PromptTemplate(
        input_variables=["history", "human_input"],
        template=template,
    )
    chatgpt_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2),
    )
    o = chatgpt_chain.predict(human_input="Hello, how are you?")
    print(o)
    return jsonify(o)


# langchain example for agent 
@app.route("/flume/langchain/agent", methods=["GET"])
def get_completion_langchain_agent():
    llm = OpenAI(temperature=0, headers={
        "Flume-API-Key": "ADD_YOUR_FLUME_API_KEY_HERE",
        "Flume-Metadata-Session": "session-langchain-agent",
        "Flume-Tags": "promptchain-agent,production-agent",
    })
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    output = agent.run(
        "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")
    return jsonify(output)
