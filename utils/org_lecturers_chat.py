from autogen import GroupChat, ConversableAgent, GroupChatManager, UserProxyAgent
from .llm_config import config_list
from app.lecturer.models import LecturerBody

def create_schedule(lecturers: list[LecturerBody]):
  lecturers_agents = []

  for i in range(len(lecturers)):
    lecturer_agent = ConversableAgent(
      name=f"lecturer_agent_{i}",
      system_message=lecturers[i]["description"],
      description=lecturers[i]["description"],
      llm_config=config_list,
    )

    lecturers_agents.append(lecturer_agent)

  schedule_agent = ConversableAgent(
    name="schedule_agent",
    system_message="You are a human admin and you control the proccess of creating a schedule of the course. Last message you MUST send a schedule",
    llm_config=config_list,
    human_input_mode="TERMINATE",
  )

  group_chat = GroupChat(
    agents=[*lecturers_agents, schedule_agent],
    messages=[],
    max_round=6,
  )

  group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=config_list,
  )

  chat_result = schedule_agent.initiate_chat(
    group_chat_manager,
    message="The course of cooking cakes runs from December 10 to December 20, 2024. There are 5 lectures (neither less nor more) in the course, so you need to get the most compressed and optimal for all lecturers course schedule. You are strictly prohibited from going beyond the course dates - from December 10 to December 20, 2024. Also you should find a schedule which will fit to all lecturers' personal schedules of free time. When you come to optimal schedule just keep it. And the last message is strictly must be a schedule in the following format: Date(24.11.2024) - Hours of lecture (1pm - 3pm).",
    summary_method="last_msg",
  )

  print(chat_result.summary)


  # lecturer_agent1 = ConversableAgent(
  #   name="Lecturer_agent",
  #   system_message="You are a Master Pastry Chef. Specialization: Cake making (from classic recipes to signature desserts) Flexible schedule: Monday: 10:00 - 18:00 Tuesday: 10:00 - 14:00 Wednesday: 10:00 - 18:00 Thursday: 10:00 - 14:00 Friday: 10:00 - 18:00 Saturday: 10:00 - 14:00 Sunday: Closed Additional requirements: Equipment: Professional kitchen appliances (mixers, ovens, dough mixers) Well-ventilated workspace Pastry supplies (molds, silicone mats, pastry bags) Materials: High-quality ingredients (flour, sugar, butter, eggs, cream, etc.) Decorative elements (chocolate, marzipan, cream) Audience: It is desirable that the audience be small (up to 10 people), so that I can pay attention to each participant. Additionally: I am ready to conduct lectures both on weekdays and on weekends, but preferably in the first half of the day. I am ready to adapt the program to the level of training of the participants and their interests. About me: I am a professional pastry chef with over 10 years of experience. I love sharing my knowledge and skills with other people, and I believe that pastry art is not just making desserts, but real creativity. Goal: My goal is to teach the course participants the basics of pastry, show them various techniques and secrets of making cakes, and inspire them to create their own masterpieces. You want to give lectures for student, but you have to consider a free time shedule of your collegue.",
  #   llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]},
  #   human_input_mode="NEVER",
  # )

  # lecturer_agent2 = ConversableAgent(
  #   name="Lecturer_agent2",
  #   system_message="You are a pastry chef and decorator. Specialization: Decorating cakes and confectionery (mastic figures, sugar icing, chocolate floristry) Flexible schedule: Monday: 12:00 - 18:00 Tuesday: 10:00 - 16:00 Wednesday: 12:00 - 18:00 Thursday: 10:00 - 16:00 Friday: 12:00 - 18:00 Saturday: 10:00 - 14:00 Sunday: Closed Additional requirements: Equipment: Professional kitchen appliances (mixers, ovens, dough mixers) Well-ventilated workspace Confectionery inventory (molds, silicone mats, pastry bags) Materials: Quality ingredients (flour, sugar, butter, eggs, cream, etc.) Decorative elements (chocolate, marzipan, cream) Audience: It is desirable that the audience be small (up to 12 people), so that I can pay attention to each participant. Additionally: I am ready to conduct lectures both on weekdays and on weekends, but preferably in the afternoon. I am ready to adapt the program to the level of training of the participants and their interests. About me: I am a professional pastry chef and decorator with over 8 years of experience. I love to create beauty and create unique decorations for cakes and other sweets. I am convinced that decorating is an art that anyone can master. Objective: My goal is to teach the course participants the basics of decorating cakes and confectionery, show them various techniques and secrets of creating beautiful and delicious decorations, and inspire them to create their own masterpieces. You want to give lectures for student, but you have to consider a free time shedule of your collegue.",
  #   llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}]},
  #   human_input_mode="NEVER",
  # )