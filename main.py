import streamlit as st
import os


import google.generativeai as genai
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv() ##load all the environment variables .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

# def get_conversational_chain():
#     prompt_template = """
#     Autism Focus I specialize in providing information about autism. I'll do my best to answer your questions thoughtfully and accurately. If I don't have sufficient knowledge, I'll let you know.

#     Question: \n{question}\n

#     Answer:
#     """
#     model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    
#     prompt = PromptTemplate(template=prompt_template,input_variables=["question"])
#     chain = load_qa_chain(model,chain_type="stuff",prompt=prompt)
#     return chain

# def op_processing(user_question):
    
#     chain = get_conversational_chain()
    
#     response = chain(
#         {"question":user_question},
#         return_only_outputs=True)
    
#     return response["output_text"]
    

##initialize  streamlit app

st.set_page_config(page_title="Autism Q&A Bot")
st.header("Autism Q&A Bot")

#Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input = st.text_input("Input : (I only give information as per the information I am trained , do not consider my advice as a final advice)",key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append("You: ")
    st.session_state['chat_history'].append(input)
    st.session_state['chat_history'].append("Bot :")
    st.subheader("The Response 🩺 :")
    for chunk in response:
        st.write(chunk.text)
        # st.session_state['chat_history'].append("Bot :")
        st.session_state['chat_history'].append(chunk.text)
        
st.subheader("The Chat history is")

for text in st.session_state['chat_history']:
    st.write(f"{text}")
