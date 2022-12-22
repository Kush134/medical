Project Title: DiagnosX

Contributors: Bree Day 
Contact Information: Breeonad@gmail.com 

Problem Statement addressed: Access to care

Description:

If medical information is not delivered in a manner that a patient can comprehend it, do they actually have access to it? The US and other countries around the world have done a good job at making sure that, at the very least, if someones life is in danger, they can get medical intervention. Where these healthcare systems fall short is making sure these conditions aren't created in the first place or that they don't reach critical levels by thoroughly educating patients on their medical conditions.

Tell us how your entry was the most...

Impactful in solving a real world problem:
People: Since DiagnosX is a web application capable of fully breaking down medical information, patients of all educational levels are empowered with the opportunity to learn details of their diagnosis for better control of their given medical condition. DiagnosX also removed implicit biases so patients of all ethnicities have an equitable experience. It also improves patient outcomes by increasing the accuracy and availability of physician findings, medical details and prognosis. Organization: According to the AAMC, in 12 years the US is expected to have a shortage of 124,000 physicians, during this same time period, the population of the US is expected to grow by 10%. If our current way of diagnosing patients continues, physicians will have to choose between the quality of time with a patient and the quantity of patients they can see. While DiagnosX cannot create more physicians, we can handle the leg work so that quality and quantity of patients interacted with is not compromised.    


Innovative use case of graph:
DiagnosX offers a novel use of the graph by offering patients breadth and depth of information on their medical condition. Most medical applications offer "cookie-cutter" information on a given diagnosis with little to no personalization or consideration of factors niche to the patient. For example, a patient with a history of diabetes treated for a laceration may be discharged home with standard instructions to keep the wound site clean, overlooking that the patient’s healing time may be longer and more prone to infection than non-diabetic patients. DiagnosX on the other hand, will consider all aspects of a patients medical history and give wound care instructions to suit them as an individual.  DiagnosX is also unique in that users can traverse the graph for medical information applicable to them at the time. Since the traversal of the graph has thousands of permutations, new questions can be answered each visit for a less artificial experience.

Ambitious and complex graph:
Currently the graph for DiagnosX is constructed using data from 21 different CSV files with over 50 different relationship types and the potential for hundreds more. DiagnosX can potentially be expanded to give more information on insurance coverage, and statistics on: physical exam findings, vitals, family history, and lab results for comparison to a given population. In the future, DiagnosX could also scale to include data on the thousands of chemicals found in medications both prescription and over the counter. This information could then be render into 3D modeling of the compounds and how the drug impacts your body to treat an ailment, or model why drugs have negative side effects when mixed.     

Applicable graph solution:
In the doctor’s office use case for DiagnosX, patient information from the physicians charting portal used for billing and medical record purposes is all that is needed for adoption. One adoption for DiagnosX is modeling the development cycle of a baby while in the womb. Parents can get a 3D model of how their baby is currently developing all they would need to give is the last day of menstruation and or due date. If their doctor diagnoses the fetus with any abnormalities, DiagnosX can give model how the fetus is developing with that abnormality and what the outcome may look like for the baby.


Other additions:
DiagnosX can be applied to any industry someone is trying to learn from. Even further applications could include data and 3D models of concerning symptoms for pets and how certain foods affect them i.e. chocolate for dogs. 3D modeling of car parts could also aid mechanics in explaining diagnostics on vehicles and how certain parts of a car affect it.


Data: located in the Tigergraph file in the DiagnosX repository.

Technology Stack: DiagnosX was written in Javascript in conjunction with the Three.js and GSAP libraries for rendering and animation of 3D models. A Tigergraph schema and graph database was created for establishing connections of data files and rendering data on the backend. There were a number of issues with linking the front end and the backend as well as getting the exact data needed when querying the database. For better visualization of the application, data was hardcoded in and the schema and graph database created for DiagnosX was included for implementation once those kinks are worked out. 

Visuals:  https://docs.google.com/document/d/1pVyHKQYpDJ3bLIF2hdZ97ZyHch90CmGprHHvusuqoGA/edit


Dependencies: Three.js and GSAP libraries. The are included in the packages.json file. 


Installation: run:
		npm install
		npm run dev	

Clone repository: https://github.com/BreeDay/DiagnosX

Install dependencies: three.js and gsap libraries. In package.json file

Access data: All data files for tigergraph schema and graph database are included in the Tigergraph folder.  

Steps to build/run project: npm install
				npm run dev


Known Issues and Future Improvements: 
Front end and back end function independently but are not connected. There were issues with getting correct data back when querying database. 

Explain known limitations within the project and potential next steps: 
Creating or purchasing 3D models. It takes me about a week to create 1 model or I could pay $10-20 for a model from a creator. There are a number of models currently available for the body systems, however, if I need more specific models, the creators take about 2-3 days to create them. 

Reflections:
The code and database connections are not as ironed out as I wanted the to be but I am proud that the idea for an application of this magnitude is out of my head and into the world to help millions of people achieve equitable access of healthcare and understanding of their medical condition. This was my first time putting together a graph database and the limitless ability to scale data makes DiagnosX an agile program with limitless applications. 

Review the steps you took to create this project and the resources you were provided. Feel free to indicate room for improvement and general reflections:
The youtube tutorials were great for helping a beginner like myself use a powerful technology like tigergraph. I also got a number of questions answered over the 4-5 sessions of office hours I attended. For future hackathons, replication of common bugs or errors users run into and how to fix them would be extremely valuable.  

References:
Design inspiration for the front end: Bruno Simon- Three.js rendering of 3D models 
						Jonas Schleberman- landing page design
Backend: Tigergraph youtube videos 	
