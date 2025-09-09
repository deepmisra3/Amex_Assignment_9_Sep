Project folder contains the code
to run the docker, please make sure Docker is installed on local system.
In the folder Amex there is file named weather-fastapi.tar which is docker image
Load this file using command in VS Code: docker load -i weather-fastapi.tar

Please Create a .env file with your OpenAI API key
echo "OPENAI_API_KEY=sk-..." > .env

Now you can run the Docker container
docker run -p 8000:8000 --env-file .env weather-fastapi

In case its not working, please use the environment file value in command line and use below command to execute:

docker run -p 8000:8000 -e OPENAI_API_KEY=YOUR_API_KEY weather-fastapi

Replace YOUR_API_KEY with your open AI key which can be generated from https://platform.openai.com/api-keys and it starts from sk

