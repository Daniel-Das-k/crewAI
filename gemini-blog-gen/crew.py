from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher, news_writer

crew = Crew(
    agents = [news_researcher,news_writer],
    tasks = [research_task,write_task],
    process = Process.sequential,
)

result = crew.kickoff(inputs = {'topic':"AI in Augmented Reality (AR) and Virtual Reality (VR)"})
print(result)