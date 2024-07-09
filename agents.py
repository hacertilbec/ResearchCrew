from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
import os

class RelatedWorkWriterAgents:
    def __init__(self):
        self.llm = ChatOpenAI(model='gpt-4o',
                                 api_key=os.environ["OPENAI-API-KEY"])
        
    def researcher_agent(self):
        return Agent(
            role="Research paper founder",
            backstory=dedent(f"""As an Academic Research Specialist, your mission is to find baseline articles and latest research papers on the given topic.
                             These research papers should be reliable. You should learn title, publication date, publication source and the summary of papers."""),
            goal=dedent(f"""Reliable and latest research papers on the given topic."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
        

        
    def proposed_work_comparer(self):
        return Agent(
            role="Proposed work comparer",
            backstory=dedent(f"""As an Academic Research Specialist, your mission is to get a related work of the topic and proposed work then find out common and different approaches of the porposed work with given research papers.
                             You should list differences and common ideas between the proposed work and each research paper."""),
            goal=dedent(f"""Understand different and common aspects of the proposed work with researh papers"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
        
    def related_work_writer(self):
        return Agent(
            role="Related Work Writer",
            backstory=dedent(f"""As an Academic Writer, your mission is to get a related academic articles of the topic and proposed work then write a Related Work section of the academic paper. Related Work should not contain subtitles, it should be a one combined section with several paragraphs if needed."""),
            goal=dedent(f"""Write the Related work section of the paper."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )