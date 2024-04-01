# Project Description:

## Market research on top local online retailers - ParknShop / Wellcome

- Aim at developing automated web scraping solutions using Selenium tools as a technical web scraper.
- Focused on extracting data related to wines and alcohol goods from ParknShop and Wellcome.
- Find out and analyze the business model in a specific category. In this case: Alcohol goods.
- Get a comprehensive understanding and provide valuable insights to end-users.

## Project management tool - Trello Kanban

This is a tool that inclines the Agile development approach which is similar to Taskboard but an online version.
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/a53976df-80ef-48ee-a9cf-40771248ed97)

# Table of contents
- [Brainstorm on research and design workflow](#Brainstorm-on-research-and-design-workflow)
- [Conduct web scraping initiatives](#Conduct-web-scraping-initiatives)
- [Maintain a database](#Maintain-a-database)
- [Provide valuable insights](#Provide-valuable-insights) 
- [Conclusion](#Conclusion)
  
<a name="Brainstorm-on-research-and-design-workflow"></a>
# 1. Brainstorm on research and design workflow

- My teammates and I conducted research by testing some e-stores using web scraping techniques.
- Determine the suitability of the online shop for web scraping.
- Assess if the website provides comparable product details, such as product ID, brand, volume, etc.
- Analyze the database structure, including the number of tables and the specific information to be stored.
- Address any analytical questions or provide solutions that arise from this project.

<a name="Conduct-web-scraping-initiatives"></a>
# 2. Conduct web scraping initiatives
## Main technical library
Selenium

```shell
pip install -r requirement.txt
```

More in [requirement.txt](requirement.txt)

## ParknShop DataFrame
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/9232e9cb-c68e-47c7-bef9-69190745dabc)

## Wellcome DataFrame
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/daa031da-66a8-4a5e-865a-28fa672b8ce4)
<a name="Maintain-a-database"></a>
# 3. Maintain a database

## Connect to database (PostgreSQL)
### Psycopg2

```shell
def connect(host="localhost", database="blue", user="postgres", password="1234"):
    print('Connecting to the database...')
    try:
        connection = psycopg2.connect(
            user=user, 
            password=password, 
            host=host, 
            port="5432", 
            database=database)
        print("Successfully connected to the database")
        return connection
    except psycopg2.Error as ero:
        print("Failed to connect to the database:", ero)
        return None
```

### There are three tables we created: 

## supermarket_list
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/86a8c24f-9009-4195-a84b-ec8dd42be6f3)

## product_table (Unchanged value)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/f1714b83-3e2d-45cf-8572-59fda2e72bcc)

## daily_table (Frequently changed)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/b412b011-b3fa-4d25-8075-8c3e862b1eee)

<a name="Provide-valuable-insights"></a>
# 4. Provide valuable insights 
In the end, some charts deliver business insights for end-users:
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/39a95157-59c4-4178-8481-931da92727c1)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/8685b6ec-c79e-4ae7-a0a5-edc33f42977c)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/dd961690-9eaa-4cd1-8f35-bdf719b1cd04)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/795aa473-54aa-4ead-b2c1-d909bdfa1d7d)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/6003f455-4fad-4ee1-bb50-969b0ed53299)
![image](https://github.com/StevenLuk18/mid_project/assets/158287260/003945e2-b62c-45fc-8ecd-d4e2adbcf287)

# Conclusion
## Wellcome
- Selling more high-end alcohols.
- Tend to sell with box or bulk.
- More expensive if a customer only buys a single one.

More types of one particular alcohol
- Attract brand-loyal customers to come.

## ParknShop
- Selling more economic alcohols.
- Tend to encourage to buy a single one.
- Small profit but rapid turnover

More unique brands for the customers
- Attract newcomers to try something new.
