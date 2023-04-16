# All-in-Hackathon
All Organize

Application Description: 
Welcome to All Organize, the app for planning and scheduling! This website will assist those finding themselves swamped with deadlines and due dates. Are you tired of manually entering in all of your important information? We are here to help!! 

With our platform, easily link your pdf documents or copy paste the text into our software (text - like a class syllabus) - and our technology will pull out the important information from those documents, for instance, like the assignment due dates off of your class syllabus! Aside from this feature, there is also a to do app which helps you stay committed and focussed on your daily tasks and needs, Try it out today, and experience the benefits for yourself! You will be better able to increase your productivity, and keep track of your due dates and schedule. 

Our code mainly works on the openAI gpt-3.5 model, where it behaves like a chatbot and we use our custom prompt to extract the correct information from it. 


Future Work:
1) Add / delete your tasks dynamically, 
2) Log in 
3) Help create tasks automatically from the homework assignment list into the to do task. 

Feature Extraction (Syllabus -> Assignments Info)
Issues:
1)The Structure of each syllabus file is different, it is difficult to work with such unordered data,
2) There have been research papers done on this, and most of them were on how to tackle unstructured data, to better gain text extraction
Not all the data that you may want , may be present in the syllabus. Example if you want to know what day(Mon-Fri) your homework is due, and the information isnt present in the database, there will not be any values in the column or will have nonsensical values. 
3) The text may not fully be extracted perfectly, since there is no dataset for such a task, it is difficult to fine tune a good model accessible to students without requiring large storage and large compute. 

Future Work:
1) Improving / formatting the syllabus into a more structured format 
2) Building smaller datasets / use few shot learning to fine tuned models for document extraction tasks such as this. 

If you have any other feedback on this project: 
Do leave a comment on devpost or send us a message there! 
Thank you for reading, 
Hopefully more bug fixes coming soon!
Toodalo!

