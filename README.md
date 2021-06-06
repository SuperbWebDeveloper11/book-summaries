
### book-summaries    
book-summaries is a django project built for readers to make summaries for each book they read and see other summaries

  
### How users will interact with the app:  
- Anonymous users could display summary list, each summary and download a pdf copy
- Users could login using username and password or create new accounts   
- Logged in users could perform all crud operations 
- Each book instance will have : title, body, category, tags
  
  
### book-summaries is built using:  
- Django   
- django_taggit 
- django-widget-tweaks  
- bootstrap  
- weasyprint 
- Markdown
  

#### here are some screensshot of the book-summaries project:


- The Entity Relationship Diagram for book-summaries:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Book%20Summaries.png)

- This page display summary list along with list of tags and categories:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-10-15.png)

- It is possible to pagingate summary list:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-10-31.png)

- Users could filter summaries by categories:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-10-54.png)

- Users could create summaries (i used bootstrap and django-widget-tweaks), also the 'body' fled use the markdown format:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-11-08.png)

- Using Mardown and custom template filter the user could display summary body in an appropriate way:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-11-29.png)

- At the bottom of the summary detail page 3 buttons are displayed for download pdf copy, edit or delete summary

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-11-41.png)

- If the user is the auther of a summary instance they could 'edit' it:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-11-49.png)

- Anyone could download a pdf copy of the summary without subscription:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-12-25.png)

- If the user is the auther of a summary instance they could 'delete' it:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-12-45.png)

- the messages framework is used to display messages for users:

![screenshot](https://github.com/pedrasfloki/book-summaries/blob/main/screensshot%20for%20the%20project/Screenshot%20from%202021-06-05%2018-12-57.png)

  
Note:
  I took a lot of ideas for the book **Django 2 by Example by Antonio Mele**


