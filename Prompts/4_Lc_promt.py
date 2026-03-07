from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Write a {style} literature on the topic "{topic}" 
in {language} language within {number_of_lines} lines.
""",
    input_variables=["style","number_of_lines","topic","language"],
)

template.save("sumit.json")
print("sumit.json created successfully")