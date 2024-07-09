from textwrap import dedent
from crewai import Task

class RelatedWorkWriterTasks():
	def research_task(self, agent, topic, number_of_articles):
		return Task(
			description=dedent(f"""\
				Search and find baseline articles on {topic} research area and {number_of_articles} reliable and up-to-date research articles on {topic} , prioritizing sources with high credibility and recent publication dates.
				For each research article, summarize main contributions and used methodologies."""),
			expected_output=dedent("""\
				A comprehensive report detailing the research articles' used methodologies and main contributions along with the bibtext citation of the article."""),
			async_execution=True,
			agent=agent
		)

	def proposed_work_analysis_task(self, agent, topic, proposed_work):
		return Task(
			description=dedent(f"""\
				Analyze the proposed work summary and research article summaries written on {topic}.
                Find out common and different approaches of the porposed work with other research papers.

				Proposed Work Summary: {proposed_work}"""),
			expected_output=dedent("""\
				A comprehensive report that lists differences and common ideas between the proposed work with given research articles."""),
			async_execution=True,
			agent=agent
		)


	def writer_task(self, agent, topic, proposed_work, number_of_articles):
		return Task(
			description=dedent(f"""\
				Write a "Related Work" section of an academic paper about {topic}. First make an introduction by summarizing baseline research artciles. Then summarize {number_of_articles} recent academic papers (provided in context) in 1-2 sentences, and if there are any similarities or differences with my paper, state them academically in 1 sentence. 
    			If the difference in my paper is the same across all papers, you should discuss my paper's differences and similarities in a concluding paragraph instead of mentioning it between the papers.
    
                Research topic: {topic}
				My Paper's Summary: {proposed_work}"""),
			expected_output=dedent("""\
				A well written academical Related Work section consists of 1-2 sentence summary of each academic paper, a 1 sentence academic summary of each paper's similarities or differences with my paper and each other. If the difference in my paper is the same across all papers, a concluding paragraph discussing the differences and similarities of my paper instead of mentioning it between the papers. Papers should be cited in text with latex style and at the end bibtex should be provided."""),
			agent=agent
		)