# Set your Hugging Face API token
huggingfacehub_api_token = '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'

# Create a prompt template from the template string
template = "You are an artificial intelligence assistant, answer the question. {question}"
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create a chain to integrate the prompt template and LLM
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "How does LangChain make LLM application development easier?"
print(llm_chain.run(question))
