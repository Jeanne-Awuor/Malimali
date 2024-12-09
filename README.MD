### MALIMALI BARTER TRADE PLATFORM

An ecommerce platform where users can exchange goods for goods; just like that neighbourhood _MALIMALI_ guy!

This is an experience like no other;view,upload,agree and exchange all under one roof. 

Malimali thrives on the power of trade. Goods for goods, just like in the good old days—no monetary exchange required.

You no longer have to wait for the _MALIMALI_ guy to come around anymore,just go to **Malimali** and exchange your goods instantly.

### Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite


### General Steps followed
1.Created the _**Malimali_** project.<br>
2.Created the store and cart app.<br>
3.For each app: <br>
* Created a url in urls.py 
* Created a function in views.py
* Created a template

### Understanding the code
1.Static folder:Holds the static assets that remain unchanged throughout the entire project e.g CSS
2.Media folder:Contains the images
3.Under the templates folder in the store app:
* base.html-Contains the sections of the page that appear in alot of the pages:Header and Footer,to avoid redundancy in code.
* about.html - Contains a description of the project and it mission statements.
* category.html - Contains the category logic;Ability to be shown the products solely in the chosen category.
* home.html - Contains all the available products and a brief description.
* navbar.html - Contains navigation buttons to various sections of the project.
* product.html - Contains the product logic:Ability to view a single product and its description.
* login.html - Contains the form used to log in existing users.
* register.html -Contains the form to register new users.
