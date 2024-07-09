from dotenv import load_dotenv
load_dotenv(dotenv_path = ".env", override=True)

from crewai import Crew

from tasks import RelatedWorkWriterTasks
from agents import RelatedWorkWriterAgents


def crew(proposed_work, topic, number_of_articles):
	tasks = RelatedWorkWriterTasks()
	agents = RelatedWorkWriterAgents()
	objective = "Write the related work section of my academic research paper.\n"
 
	# Create Agents
	researcher_agent = agents.researcher_agent()
	proposed_work_comparer = agents.proposed_work_comparer()
	related_work_writer = agents.related_work_writer()

	# Create Tasks
	research = tasks.research_task(researcher_agent, topic, number_of_articles)
	proposed_work_analysis = tasks.proposed_work_analysis_task(proposed_work_comparer, topic, proposed_work)
	related_work = tasks.writer_task(related_work_writer, topic, proposed_work, number_of_articles)

	proposed_work_analysis.context = [research]
	related_work.context = [research, proposed_work_analysis]

	# Create Crew responsible for Copy
	crew = Crew(
		agents=[
			researcher_agent,
			proposed_work_comparer,
			related_work_writer
		],
		tasks=[
			research,
			proposed_work_analysis,
			related_work
		]
	)

	result = crew.kickoff()
	return result