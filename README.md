# GREAT JOB RESUME BUILDER
## Description:
This website was created with a personal touch, born from the perspective of someone standing at the threshold of a job application. While exploring existing resume builder sites, I quickly realized that they often fell short in providing comprehensive guidance on resume sections. Many offered little more than templates, leaving job seekers searching for tips, examples, and insights across various tabs as they meticulously constructed their resumes.
Additionally, I noticed that the online resources available for resume building were often overly detailed, causing information overload. This realization drove me to embark on a mission: to create a resume builder site that not only offers beautifully designed templates but also serves as a wellspring of advice, best practices, and real-world examples for each resume section.
In the pursuit of simplicity and effectiveness, I designed the tips to be concise and to the point, streamlining the resume-building process. This website is the culmination of that vision, aiming to empower job seekers with the tools they need to craft the perfect resume, ensuring that their unique skills and experiences shine through effortlessly.
## Python Files
### 'app.py':
In this python file is the core of the Flask web application. It handles various routes and corresponding functions to render different pages, such as the main index, resume templates, and individual resume sections. It also controls the selection of resume templates and redirects users to their chosen templates.
## HTML Files
### 'layout.html':
This HTML file serves as the backbone of the entire website, providing a consistent and user-friendly layout. There is a navigation bar that provides easy access to different sections. A bootstrap CSS file (**bootstrap.css**) that I've made extensions is also attached.
### 'index.html':
This serves as the welcoming gateway to the website. It offers visitors a succinct introduction to the platform, providing a clear understanding of its purpose and functionality.
### 'tips.html':
This page showcases three resume examples for both students/intermediates and senior professionals. To enhance user interactivity, I've implemented image maps, allowing users to click on specific sections of interest. With a simple click, users are seamlessly redirected to the corresponding HTML file, where they can delve deeper into specific resume sections, uncovering important tips and examples.
### 'achievements.html', 'certifications.html', 'conferences.html', 'contact.html', 'education.html', 'experience.html', 'expertise.html', 'hobbies.html', 'languages.html', 'organizations.html', 'picture.html', 'projects.html', 'publications.html', 'references.html', 'skills.html', 'summary.html':
These HTML pages provide brief explanations and examples for various sections commonly found in resumes, making it easier for users to understand and create their resumes confidently.
### 'get_started.html':
This HTML page presents users where they can kickstart their resume-building process. It offers a choice between two distinct resume templates via a simple form. I've tried to make the templates to address different needs while both of them contain the most essential parts of a resume.
### 'template_1.html' and 'template_2.html':
These two HTML files are the heart of my resume builder. Each page is uniquely styled with custom CSS (**template1.css and template2.css**) and features a user-friendly interface. At the top, a navigation bar provides easy access to the home page. The centerpiece of these pages is a dynamic form where users can input all the necessary information for their resumes. The form updates the resume preview in real-time as users fill it out, eliminating the need for a submission step.
Towards the end of the form, there's a preview section that displays the final resume, giving users a glimpse of how their information is presented. Lastly, both templates include a print button that allows users to generate and download their resume as a PDF.
### 'about.html':
This file contains the references, websites that inspired and helped me, and my deep gratitude to the whole CS50x team.
## JavaScript Files
### 'app.js' and 'app2.js':
These JavaScript files are responsible for managing client-side functionality and user input validation. It defines various regular expressions for form field validation, such as validating names, emails, phone numbers, and more. The script interacts with the HTML forms, capturing user inputs and ensuring they meet specific validation criteria. Additionally, it includes functions to display and print the generated resume based on the user's input. Overall, app.js and app2.js play a crucial role in providing a smooth user experience by validating data and rendering the resume preview.
### 'script.js':
This file is responsible for managing the form repeater functionality in my web application. It uses the jQuery library to handle form field repetition. This script enhances my web application's form handling capabilities by allowing users to dynamically add and remove form field sets. It also triggers the generateCV() function to update the CV preview whenever a field is added or removed.

#### Video Demo:  <https://youtu.be/CKHfE0mrEoo>
