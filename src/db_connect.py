import psycopg2
import boto3


# CREATING A DATABASE CONNECTION

def setup_db_connection():
    """fuction to setup a connetion, no args needed"""
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(
        Name='alternative-team4-pass', WithDecryption=True)
    mypassword = parameter['Parameter']['Value']

    return psycopg2.connect(dbname="dev_delon6_team4",
                            host="redshiftcluster-8pp4d8ute2ly.cfahydnz3hic.eu-west-1.redshift.amazonaws.com",
                            port="5439",
                            user="awsuser",
                            password=mypassword)


db = setup_db_connection()
db.set_session(autocommit=True)
cursor = db.cursor()
