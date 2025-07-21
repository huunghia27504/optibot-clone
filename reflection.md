# Short Project Reflection

**1. Overall Concept Understanding**  
The goal of this assignment was to build an automated pipeline that fetches help articles, converts them to Markdown, uploads them to OpenAI's vector store via API, and creates an Assistant that answers support questions based only on those documents.

---

**2. Approach & Solution**  
I used Python to implement the following:

- Fetch articles via Zendesk Help Center API  
- Convert HTML content to clean Markdown format  
- Detect changes using file comparison to only upload deltas  
- Upload Markdown files to OpenAI Vector Store using API  
- Programmatically create an Assistant with the required system prompt  

All logic is wrapped in a single `main.py` script that runs once and exits cleanly. A Dockerfile is included for easy deployment.

---

**3. Learning New Concepts**  
This was my first time building a project with Python.  
I learned quickly through AI tools to understand syntax and use libraries like `requests`, `dotenv`, `markdownify`, and `openai`.  
By breaking the problem into smaller steps, I was able to complete the assignment on time.

---

**4. Suggestions & Thoughts on OptiBot**  
I think this Assistant could be very helpful if integrated into the OptiSigns website.  
Limiting answers to uploaded docs helps ensure accuracy and consistency.  
As a potential next step, categorizing or tagging the articles could improve search and user experience.
