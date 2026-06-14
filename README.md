# The Unofficial Guide

*AI201: Project No.1*

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

**Research Labs, clubs, and people for Undergraduates at Florida International University**

*This knowledge is not the easiest to find becaus eof how unmanaged and segmented the research scene is at FIU, such that undergraduates do not have the smoothest pipeline. Outdated webpages and isolated pages add insult to injury.*

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
1200 characters

**Overlap:**
Size of 200 characters as overlap for better meshing

**Reasoning:**
This is my first time doing this so there is not much of a reason besides that the pages I linked have good paragraphs that hold information someone may search for. I want overlaps possible, assuming this helps the model retrieve related chuncks for responding.

**Why these choices fit your documents:**
This ended working perfectly since parapgraphs are usually around 850 characters

**Final chunk count:**
140

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
bge-small-en-v1.5 (from sentence-transformers)

**Production tradeoff reflection:**
I am not entirely sure about tradefoffs since I did not try other models and draw up unit tests to compare effectiveness. I think this model is a great fit for this guide.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
The LLM is given a set of 4 rules that describe how to behave. I asked for it to follow these strictly:

1. ONLY use details explicitly stated in the context blocks below. Do not make up facts, external URLs, names, or general knowledge.
2. If the context does not contain enough concrete information to answer the user query completely, state explicitly: "I do not have enough specific retrieved information to answer that completely based on available documentation."
3. When referencing a fact, attach inline citations using the exact Source number provided in the context format (e.g., [Source #1]).
4. Keep your tone expressive, helpful, and highly clear for an academic environment.

**How source attribution is surfaced in the response:**
After each piece of "quoted" text a source is cited, and a list of references are appended to the end fo the response.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What sorts of labs does FIU have in its engineering college? | Florida International Universiy (FIU) has labs such as [list of labs] | According to the provided context, FIU's College of Engineering has several labs, including 1. Fluid Structure Interaction (FSI) Lab, 2. Interdisciplinary Microfluidics Lab, 3. Mechatronics Laboratory, 4. Corrosion Lab, 5. Engineering Manufacturing Center. These are in the CEC. | Relevant | Accurate |
| 2 | What research does FIU have in physics? | At FIU, there is research being done ine [list of some research topics]. Here are some of FIU's research pages: [links to research pages]. | I do not have anough information to answer that completely based on available documentation [Source #1]. My provided context blocks do not explicitly mention physics. They mention research in various fields such as ocean preservation, [names other fields], but not do not provide info on physics research. | Relevant | Partially Accurate |
| 3 | Is there any recent research news at FIU, and where can I find it? | Recent news from FIU is [most recent news article from FIU]. More can be found at [link to FIU news]. | Yes there is recent news at FIU. According to [Source #18], Fiu researchers are pioneering the science needed to fight illegal wildfire trafficking, and the university is also conducting research on heart disease, extreeme storm resilience, and conservation efforts in the Amazon River... You can find more information about FIU's research news on the FIU Research website. | Relevant | Accurate |
| 4 | Are there any clubs at FIU that have roots in projects and research in science and technology? | There are plenty of clubs at FIU. Ones that meet your criteria may be [list of techincal project/research clubs from CEC]. Ask again with a subject area if these are not what you are searching for? | Yes, there are clubs at FIU that have roots in projects and research in science and technology. According to [Source #13], the CEC is home to many student organizations including professional associations and student clubs. | Relevant | Accurate |
| 5 | How can undergraduates at FIU get there research seen and/or published from the university? | Undergraduates at FIU can publish their work in the Undergraduate Research Journal (URJ). Steps include: [list of steps]. Here is a link to the publishing process information: [link to FIU URJ publishing process page] | Undergraduates at FIU can get their research seen and/or published through the Florida International University Undergraduate Research Journal (FIUURJ) [Source #8]. FIUURJ is an interdisciplinary, peer-reviewed journal that publishes promising undergraduate research and provides professional development opportunities for undergrads. | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
What research does FIU have in physics?

**What the system returned:**

I do not have enough specific retrieved information to answer that completely based on available documentation. The provided context blocks do not explicitly mention research in physics at FIU [Source #14, Source #18, Source #6]. They discuss research in various fields such as ocean preservation, spaceflight, environmental resilience, wildlife trafficking, heart disease, and mathematics and statistics, but do not provide information on physics research.

📚 SOURCE ATTRIBUTIONS USED FOR VALIDATION:
 * Source #6: https://case.fiu.edu/mathstat/
 * Source #14: https://www.fiu.edu/research/index.html
 * Source #18: https://news.fiu.edu/research-magazine/

**Root cause (tied to a specific pipeline stage):**
The main and only casue was not including a resource that covered the information to answer the question. The cause is at the resource collection and chunking stage

**What you would change to fix it:**
I would go online and find the FIU page that lists the research conducted in the physics section of the College of Arts, Science, and Education. I would do the same with all other colleges to help mediate this same issue across similar questions, aiming for this guide to be of use to undergarduates will all and any questions about research and clubs at any college at Florida International University. ✌🏾

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec was super helpful for (1) getting my idea, sources, and methods fleshed out and (2) collecting my plan to ask an LLM for implementation aid. 

**One way your implementation diverged from the spec, and why:**
My spec never went into details, so I suppose the way of implementation diverged. I have testing files for each step. Besides this, things were pretty on point. I had about 3 hiccups in total since my queries to Gemini for specific and breadth-y.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
**My planning.md and requirements.txt files**
- *What it produced:*
**Recommendations for embeddding models that fit my chunking size and domain.**
- *What I changed or overrode:*
**I used what was recommeneded switching from a chunk size of words to chunk size of characters.**

**Instance 2**

- *What I gave the AI:*
**output from one of my tests, where there was an issue with the chunking process.**
- *What it produced:*
**An explanation of why I was getting my output**
- *What I changed or overrode:*
**The erroe was due to a spelling error so I changed seperator to separator and the chunking worked, though I had another chunking hiccup before coming to my current complete implementation.**
