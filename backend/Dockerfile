# Use an official Python runtime as a parent image
FROM python:3.10-slim-bullseye

# Set the working directory in the container
WORKDIR /usr/src/app

# RUN pip install --no-cache-dir tiktoken langchainhub langchain langgraph tavily-python gpt4all langchain-pinecone
# RUN pip install --no-cache-dir pypdf
# RUN pip install --no-cache-dir langchain-google-genai
RUN pip install --no-cache-dir flask
# RUN pip install --no-cache-dir langchain-community
# RUN pip install --no-cache-dir langchain-openai
# RUN pip install --no-cache-dir langchain-core langchain-mistralai flask

EXPOSE 4000

# Copy the current directory contents into the container at /usr/src/app
COPY ./src .

# Run hello.py when the container launches

CMD [ "python3", "-m" , "flask", "--app", "./service.py", "run", "--host=0.0.0.0", "--port=4000"]