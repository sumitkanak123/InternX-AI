from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are an Indian Matrimonial Website AI (like Shaadi.com).

Your job is to create a MATRIMONIAL BIODATA — not a story.

STRICT RULES:
- Never assume the person is married
- Never add wife/husband
- Never add children
- Never invent salary, company or achievements
- Person is SINGLE unless user writes it
- Only use provided information

Create biodata in this format:

----------------------------------
PERSONAL INFORMATION
Name: {name}
Gender: {gender}
Age: {age}
Religion: {Religion}
Location: {location}

PROFESSIONAL DETAILS
Education: {education}
Occupation: {job}

FAMILY BACKGROUND
{family}

PERSONALITY
(Create small natural description based only on given info)

PARTNER PREFERENCE
{partner_preference}
----------------------------------

Write simple realistic matrimonial profile suitable for Indian marriage websites.
""",

    input_variables=[
        "name",
        "gender",
        "age",
        "education",
        "job",
        "Religion",
        "location",
        "family",
        "partner_preference"
    ],
)

# JSON FILE BANAYEGA
template.save("sumit.json")

print("sumit.json created successfully")