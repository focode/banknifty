import csv
import psycopg2
import sys

con = None
adate = None
def main():
    print ('Strated Inserting-->')
    fn = sys.argv[1]
    con = psycopg2.connect("host='localhost' dbname='banknifty' user='postgres' password='postgres'")
    with open(fn, 'rt', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                cur = con.cursor()
                var = row[1].split('/')
                adate = var[2]+"-"+var[1]+"-"+var[0]+" "+row[2]
                print ("adate: "+adate)
                cur.execute("INSERT INTO master (ticker, associateddate ,datetime,  open, high,low,close,volume,openinterest,indexprice) "
                            "VALUES ('"+row[0]+"', '2017-04-06', '"+adate+"', '"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"','"+row[7]+"','"+row[8]+"','18500');")
                con.commit()
            except Exception as e:
                print("Uh oh, can't connect. Invalid dbname, user or password?")
                print(e)
            print ("Row Inserted: "+row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])


if __name__ == '__main__':
    main()