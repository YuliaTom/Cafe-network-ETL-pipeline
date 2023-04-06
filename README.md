<html>
   <body>
      <img src="https://www.grazitti.com/wp-content/uploads/2019/08/ETL_Bannera.gif"
        width="400" 
        height="150" >
   </body>
</html>

# ETL Data Pipeline

## Table of contents
1. [About the project](https://github.com/YuliaTom/Cafe-network-ETL-pipeline/edit/main/README.md#about-the-project-)
2. [Tech used](https://github.com/YuliaTom/Cafe-network-ETL-pipeline/edit/main/README.md#tech-used)
3. [Getting started](https://github.com/YuliaTom/Cafe-network-ETL-pipeline/edit/main/README.md#getting-started)
   * [Prerequisites](https://github.com/YuliaTom/Cafe-network-ETL-pipeline/edit/main/README.md#prerequisites)
   * [Installation](https://github.com/YuliaTom/Cafe-network-ETL-pipeline/edit/main/README.md#installation)
4. [Usage]()
5. [Testing]()
6. [Appendix]()

## About the project <a name="About the project"></a>

This project succeeds a CLI app, built for a small and independent cafe to track their stock, couriers and customers.
Due to said cafe's unprecedented growth, they have expanded to hundreds of outlets across the country. 
With this demand, comes the need to utilise their sales data to best target new and returning customers, and also to understand which products are selling well.
The cafes are experiecing issues with collating and analysing the data produced at each branch, as their technical setup is limited.

This project solves the problem of providing consultation in what is needed to grow technical offerings, so that the company can continue to accelerate growth.

After a thorough anaylisys of the company's needs, it was decided that the best course of action was to create an ETL pipeline to handle the large volumes of transactional data from the business. The data needs to be centrally stored in a cloud environment so all the stakeholders could quickly access it. 

By being able to easily query the company's data as a whole, the client will drastically increase their ability to identify company-wide trends and insights.

## Tech used

<img src="https://cloudastronautblog.files.wordpress.com/2017/10/aws_logo_smile_1200x630.png"
    width="60"
    height="40"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ89NlVK9G8MUgOHgAGwXayi6Ev-vWq9ZHtRQ&usqp=CAU"
   width="40"
    height="40"> <img src="https://w7.pngwing.com/pngs/167/148/png-transparent-microsoft-azure-sql-database-microsoft-sql-server-database-blue-text-logo-thumbnail.png"
   width="40"
    height="40"> <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
   width="40"
    height="40"> <img src="https://docs.checkmk.com/latest/images/grafana_logo.png"
   width="40"
    height="40">
    
## Getting started

### Prerequisites
+ Any IDE tool for Python code development,
+ AWS Account,
+ GitHub Account with Repository.


### Requirements 
```
boto3==1.24.13
pandas==1.4.2
psycopg2==2.9.3
```
### Installation
1. Clone the repo
 ```
git clone https://github.com/YuliaTom/Cafe-network-ETL-pipeline.git
```
2. Create a virtual environment called `env`

## Usage

## Testing

## Appendix

### Lambda Function

<img src="https://github.com/YuliaTom/Cafe-network-ETL-pipeline/blob/main/appendix/Screenshot%202023-04-06%20at%2016.53.53.png" width="800">

---

### DB Schema

<img src="https://github.com/YuliaTom/Cafe-network-ETL-pipeline/blob/main/appendix/Screenshot%202023-04-06%20at%2016.54.07.png" width="800">

---

### Lambda function testing

<img src="https://github.com/YuliaTom/Cafe-network-ETL-pipeline/blob/main/appendix/Screenshot%202023-04-06%20at%2019.14.54.png" width="800">
