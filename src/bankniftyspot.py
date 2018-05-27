import csv
import psycopg2
import sys

con = None
adate = None
def main():
    print ('Started Inserting-->')
    fn = sys.argv[1]
    con = psycopg2.connect("host='localhost' dbname='banknifty' user='postgres' password='postgres'")
    with open(fn, 'rt', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                cur = con.cursor()
                print (row)
                cur.execute("INSERT INTO bankniftyspot (entity, b,c ,d, e,f,g,h,i)"
                            "VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"','"+row[7]+"','"+row[8]+"');")
                con.commit()
            except Exception as e:
                print(e)
           


if __name__ == '__main__':
    main()