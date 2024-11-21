from autogen import GroupChat, ConversableAgent, GroupChatManager
import os
from dotenv import load_dotenv

### Load the .env file
load_dotenv()

shedule_agent = ConversableAgent(
  name="Shedule_agent",
  system_message="You return me the shedule i give you.",
  llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]},
  human_input_mode="NEVER",
)

lecturer_agent1 = ConversableAgent(
  name="Lecturer_agent",
  system_message="You are a Master Pastry Chef. Specialization: Cake making (from classic recipes to signature desserts) Flexible schedule: Monday: 10:00 - 18:00 Tuesday: 10:00 - 14:00 Wednesday: 10:00 - 18:00 Thursday: 10:00 - 14:00 Friday: 10:00 - 18:00 Saturday: 10:00 - 14:00 Sunday: Closed Additional requirements: Equipment: Professional kitchen appliances (mixers, ovens, dough mixers) Well-ventilated workspace Pastry supplies (molds, silicone mats, pastry bags) Materials: High-quality ingredients (flour, sugar, butter, eggs, cream, etc.) Decorative elements (chocolate, marzipan, cream) Audience: It is desirable that the audience be small (up to 10 people), so that I can pay attention to each participant. Additionally: I am ready to conduct lectures both on weekdays and on weekends, but preferably in the first half of the day. I am ready to adapt the program to the level of training of the participants and their interests. About me: I am a professional pastry chef with over 10 years of experience. I love sharing my knowledge and skills with other people, and I believe that pastry art is not just making desserts, but real creativity. Goal: My goal is to teach the course participants the basics of pastry, show them various techniques and secrets of making cakes, and inspire them to create their own masterpieces. You want to give lectures for student, but you have to consider a free time shedule of your collegue.",
  llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]},
  human_input_mode="NEVER",
)

lecturer_agent2 = ConversableAgent(
  name="Lecturer_agent2",
  system_message="You are a pastry chef and decorator. Specialization: Decorating cakes and confectionery (mastic figures, sugar icing, chocolate floristry) Flexible schedule: Monday: 12:00 - 18:00 Tuesday: 10:00 - 16:00 Wednesday: 12:00 - 18:00 Thursday: 10:00 - 16:00 Friday: 12:00 - 18:00 Saturday: 10:00 - 14:00 Sunday: Closed Additional requirements: Equipment: Professional kitchen appliances (mixers, ovens, dough mixers) Well-ventilated workspace Confectionery inventory (molds, silicone mats, pastry bags) Materials: Quality ingredients (flour, sugar, butter, eggs, cream, etc.) Decorative elements (chocolate, marzipan, cream) Audience: It is desirable that the audience be small (up to 12 people), so that I can pay attention to each participant. Additionally: I am ready to conduct lectures both on weekdays and on weekends, but preferably in the afternoon. I am ready to adapt the program to the level of training of the participants and their interests. About me: I am a professional pastry chef and decorator with over 8 years of experience. I love to create beauty and create unique decorations for cakes and other sweets. I am convinced that decorating is an art that anyone can master. Objective: My goal is to teach the course participants the basics of decorating cakes and confectionery, show them various techniques and secrets of creating beautiful and delicious decorations, and inspire them to create their own masterpieces. You want to give lectures for student, but you have to consider a free time shedule of your collegue.",
  llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]},
  human_input_mode="NEVER",
)

group_chat = GroupChat(
  agents=[lecturer_agent1, lecturer_agent2, shedule_agent],
  messages=[],
  max_round=6,
)

group_chat_manager = GroupChatManager(
  groupchat=group_chat,
  llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]},
)

chat_result = shedule_agent.initiate_chat(
  group_chat_manager,
  message="The course of cooking cakes runs from December 10 to December 20, 2024. There are 15 lectures in the course, so you need to get the most compressed and optimal for all lecturers course schedule.",
  summary_method="reflection_with_llm",
)

print(chat_result.summary)