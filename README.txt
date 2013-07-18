
FUSION Project Objective as Stated in Original Application:

The main objective is to develop a tool, ‘ReCAP’, for capturing the requirements of any warehousing operation and in so doing to semi-automate the production of customer-specific process flow diagrams, text for the Customer Scoping Document and configuration of In-DEX switches. The detailed objectives are to:
•	Establish the functional and usability requirements for ReCAP.
•	Research, identify and agree the most appropriate software development framework and tools for ReCAP
•	Develop and test ReCAP Software Modules. This will involve functional and usability testing for each of the 4 software modules that will comprise ReCAP to ensure correct and reliable operation.
•	Test and optimise the final design implementation of the 4 modules for correct operation, robustness and maintainability.
•	Develop and approve user manuals and online user training and support materials.

The purpose of the FUSION project was to develop online software (‘ReCAP’) that would (1) assist with Requirements Capture and calculate a quotation during a PSL customer site visit. (2) transform the requirements to semi-automate (a) process flow diagrams in MS Visio, (b) In-DEX configuration settings (‘switches’) and (c) the Customer Scoping Document. 

The functional and usability requirements were captured by (a) a highly detailed review of the business logic and In-DEX software, (b) in-house mentoring to develop a detailed knowledge of the warehousing business, as the project developed and (c) observations / suggestions / evident needs arising from interaction with and observation of prospective customers.

The Python programming language and a No-SQL database were adopted as the most appropriate software development tools. They are widely used in industry and are conducive to high programmer productivity. It was also decided at an early stage that jQuery, which can support menus, toolbars, drag and drop features, etc., would be used to support ReCAP’s ease of use in the browser.

As of early July, ReCAP is close to product release. The database has been repeatedly enhanced during its development to reflect the emerging needs of the requirements capture phase and to ensure efficient performance. The web interface software has similarly undergone a number of iterative improvements, not least as a result from using the prototype during customer site visits, and it is now appropriately flexible and intuitive to use. During the development of ReCAP, with research and a reassessment of what would be necessary during an initial site visit, it was decided that an on-line tool, such as ‘Creately’ or ‘lucidchart’ could be used to produce adequate process flow diagrams.

During the project, it became evident that automatically generating In-DEX configuration settings could only be achieved to a limited extent and the focus on accurate requirements capture was correspondingly increased.

The sales team put a major effort into revising the customer template scoping document, and provided the graduate with a version in Word. With input from a related undergraduate project at Ulster, a mechanism to generate a tailored version largely by automated means has now been developed and tested, taking output directly from the requirements capture component and using it to replace relevant text and numeric fields in the template. Additionally, the generated document includes an appendix that details the customer’s responses to questions asked during the site visit.  



useful notes:


This is  an application to gather sales data for Warehouse management Implementation

mongoexport -d recap -c users -o users.txt


mongoimport --db recap --collection users --file users.txt


Run sonar / start

then sonar-runner in recap folder

git add -u

scp test.txt ubuntu@54.228.195.27:recap

STEPS BEFORE UPLOAD:
remmeber to set root path for static files on ubuntu server

turn off debugging.


sudo newrelic-admin run-python recap_questionaire_module.py

