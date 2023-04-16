# All-ganize (All-in-Hackathon)
Optimize your success through All-ganize, a tool we ALL can use to improve our productivity and organization!

Welcome to All Organize, the application for planning and scheduling! This website will assist those finding themselves swamped with deadlines and due dates. Are you tired of manually entering in all of your important information? We are here to help!!

## Inspiration: 
We wanted to create an application that students could use to stay motivated, and to increase their organization and productivity, and use to allow themselves to be on track with their learning objectives. The application comes with several different features - including the feature that extracts important information from syllabi, customizable 'Goals' and 'To Do' list trackers - and a motivational board with inspirational quotes to keep students going towards accomplishing their aspirations.

## What it does: 
The web application is separated into three separate pages. In the homepage, With our platform, easily link your pdf documents or copy paste the text into our software (text - like a class syllabus) - and our technology will pull out the important information from those documents, for instance, like the assignment due dates off of your class syllabus! Our application is then designed to display the extracted information to the users. 

Aside from this feature, there is also a second page, which houses a customizable ‘goals’ list, as well as a ‘To-do’ application which helps users stay committed. and focused on their daily tasks and needs. In the third page of the website, we created a motivational moodboard, with some of our favorite motivational quotes to inspire students to get started on persevering and accomplishing their goals. 


## How we built it:
The entirety of this website uses tools, frameworks, and languages including - HTML/CSS (for website design), Javascript (for the functionality of the ‘Goals’ and To do Lists’, as well as Python and Flask. Our homepage uses OpenAI gpt-3.5 model, where it behaves like a chatbot and we use our custom prompt to extract the correct information from the syllabi that are uploaded to the website.

## Regarding the Extraction Feature (Syllabus → Assignments Information; Homepage) 
The Structure of each syllabus file is different, it is difficult to work with such unordered data,
There have been research papers done on this, and most of them were on how to tackle unstructured data, to better gain text extraction
The text may not fully be extracted perfectly, since there is no dataset for such a task, it is difficult to fine tune a good model accessible to students without requiring large storage and large compute.

## Accomplishments that we are proud of: 
We were able to dive deeper into the world of productivity, and brainstorm efficient tools that would help users (especially students) be able to tackle their goals. We are able to extract the data from the syllabi and display the information in a table, using Flask and OpenAI; this is a first for us, so it was difficult to initially set up. 

## What we learned: 
We learned about OpenAI usage within applications, and how to dive deeper into using it within the backend of our Homepage. Some of us also had learned to use Flask for the first time, and we learned a lot about web development in 24 hours. 
 
## What is next for All-ganize: 
1. The ability to be able to Add / delete your tasks dynamically. 
2. Log in feature: We will work with User Authentication to find a way to create specific user profiles. Users will be able to log into their profiles, and view their saved ‘Goals’ and ‘To Do’ list. 
3. Help create tasks automatically from the homework assignment list into the to do task.

## Future Work includes: 
1. Improving / formatting the syllabus into a more structured format
2. Building smaller datasets / use few shot learning to fine tuned models for document extraction tasks such as this.
3. Currently extraction takes 5 - 10 seconds to accomplish. We would like to find a way to further reduce the time that it takes to extract information from syllabi. 


We are hoping to fix additional issues or bugs with our application.
Here are example links that you can try with the application :
https://www.cs.cornell.edu/courses/cs2110/2023sp/schedule.html
https://www.cs.princeton.edu/courses/archive/spr23/cos126/schedule/

References (sources for code): 
To do list, and goals list: 
https://www.w3schools.com/howto/howto_js_todolist.asp
