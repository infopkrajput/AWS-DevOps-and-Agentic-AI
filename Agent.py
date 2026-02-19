from strands import Agent

# Strands Agent will automatically read from AWS_BEARER_TOKEN_BEDROCK environment variable
agent = Agent()

response = agent("Hello, how are you doing today?")
print(response)