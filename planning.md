# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

**Research Labs, clubs, and people for Undergraduates at Florida International University**

*This knowledge is not the easiest to find becaus eof how unmanaged and segmented the research scene is at FIU, such that undergraduates do not have the smoothest pipeline. Outdated webpages and isolated pages add insult to injury.*

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source  | Description | URL or location |
|---|---------|-------------|-----------------|
| 1 | FIU CEC | FIU College of Engineering & Computing's research labs page | https://cec.fiu.edu/about/schools-departments/mechanical-materials-engineering/research-industry/centers-labs/index.html |
| 2 | FIU Subreddit | Subreddit page used by FIU students | https://www.reddit.com/r/FIU/ |
| 3 | FIU CIS | FIU Knight Foundation Schools's Research page for Computing and Inofrmation Sciences | https://www.cis.fiu.edu/research/ |
| 4 | Solid Lab |  | https://solid.cs.fiu.edu/ |
| 5 | FIU CASE Physics | Research overview page for Physics at FIU's College of Arts, Education, and Science | https://case.fiu.edu/physics/research/index.html |
| 6 | FIU Math | Mathematics and Satistics at FIU's College of Arts, Education, and Science | https://case.fiu.edu/mathstat/ |
| 7 | FIU News: Science & Technology | Science and tech news from internal research and external research | https://news.fiu.edu/science-and-technology/ |
| 8 | FIU URJ | FIU Undergraduate Reasearch Journal Homepage | https://fiuurj.fiu.edu/ |
| 9 | FIU URJ: Volume 1 | Volume 1 of FIU's Undergraduate Research Journal | https://digitalcommons.fiu.edu/search?c=FIUURJ+Volume+1%2C+Issue+1+%282023%29&cc=FIUURJ+Volume+1%2C+Issue+1+%282023%29&ln=en|
| 10 | FIU URJ: Volume 2 | Volume  of FIU's Undergraduate Research Journal | https://digitalcommons.fiu.edu/search?c=FIUURJ+Volume+2%2C+Issue+1+%282024%29&cc=FIUURJ+Volume+2%2C+Issue+1+%282024%29&ln=en |
| 11 | FIU URJ: Volume 3 | Volume 1 of FIU's Undergraduate Research Journal | https://digitalcommons.fiu.edu/search?c=FIUURJ+Volume+3%2C+Issue+1+%282025%29&cc=FIUURJ+Volume+3%2C+Issue+1+%282025%29&ln=en |
| 12 | FIU News: Medicine & Health Sciences | Medicine and Heath news from FIU students, researchers, and professors | https://news.fiu.edu/medicine-and-health-sciences/ |
| 13 | FIU CEC: Student Orgs | Student organizations under FIU's College of Computing and Engineering | https://cec.fiu.edu/students/student-organizations/index.html |
| 14 | FIU Research | Research news page on FIU's main domain | https://www.fiu.edu/research/index.html |
| 15 | FIU CDSSEC | FIU's Center for Development, Support, and Success in Engineering and computing Homepage | https://cdssec.fiu.edu/ |
| 16 | Cheng-Yu Lai's Advanced Functional Material Lab | Dr. Lai's material lab page at FIU | https://lai-afm.fiu.edu/ |
| 17 | Nano-Bio Research Lab | Lab page for a Dr. Jinhe's Nanobiotechology lab at FIU | https://faculty.fiu.edu/~jinhe/ |
| 18 | FIU Magazine | Procured research and news from students and professionals tied to FIU | https://news.fiu.edu/research-magazine/ |
| 19 | FIU URJ: Publishing Process | Explanation of how FIU undergraduates can publish their work/research in FIU's Undergraduate Research Journal (URJ) | https://fiuurj.fiu.edu/publishing-process/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
2 Paragraphs (~1000–1500 characters)

**Overlap:**
Size of 200 characters as overlap for better meshing

**Reasoning:**
This is my first time doing this so there is not much of a reason besides that the pages I linked have good paragraphs that hold information someone may search for. I want overlaps possible, assuming this helps the model retrieve related chuncks for responding.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
bge-small-en-v1.5

**Top-k:**
5-10

**Production tradeoff reflection:**
Multilingual support and accuracy would be more considered with more time and money if needed.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What sorts of labs does FIU have in its engineering college? | Florida International Universiy (FIU) has labs such as [list of labs] |
| 2 | What research does FIU have in physics? | At FIU, there is research being done ine [list of some research topics]. Here are some of FIU's research pages: [links to research pages]. |
| 3 | Is there any recent research news at FIU, and where can I find it? | Recent news from FIU is [most recent news article from FIU]. More can be found at [link to FIU news]. |
| 4 | Are there any clubs at FIU that have roots in projects and research in science and technology? | There are plenty of clubs at FIU. Ones that meet your criteria may be [list of techincal project/research clubs from CEC]. Ask again with a subject area if these are not what you are searching for? |
| 5 | How can undergraduates at FIU get there research seen and/or published from the university? | Undergraduates at FIU can publish their work in the Undergraduate Research Journal (URJ). Steps include: [list of steps]. Here is a link to the publishing process information: [link to FIU URJ publishing process page] |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Perhaps there is not enough information from my chunks to answer a question. My domain suggests that the chatbot is able to retrieve all information pertaining to clubs, people, and research for undergraduates looking to get into more rigorous topics at FIU.

2. I chose a chunk size for the first time, so I am thinking that I may need to enlargen the chunk size or maybe keep the size and simplly shift where a chunk starts and ends.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

[Live URLs/Markdown Files]
     -> (Requests + BeautifulSoup Ingestion)
[Raw Text Extraction]
     -> (REcursive Character Splitting: 1200 char size / 200 char overlap)
[Text Chunks]
     -> (Sentence-Transformers: bge-small-en-v1.5)
[Chroma Vector Database]
     -> (Similarity Search Vector Query : Topk=5)
[Context Chunks + User Query]
     -> (Groq API LLM Generation)
[Clear UI / Terminal Response]

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

I am going to give gemini my entire planning.md and ask "is my plan sound? If not exactly, where could I possibly improve. This file is my plan for an "Unofficial guide" with a domain of Research Labs, clubs, and people for Undergraduates at Florida International University."

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
