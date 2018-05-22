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
                print (row)
                var = row[1].split('/')
                adate = var[2]+"-"+var[1]+"-"+var[0]

                var1 = row[0].split('.')
                firstPart = var1[0]
                entity = firstPart[0:9]
                print ("Entity name= "+entity)



                expirydate = firstPart[9:16]
                print ("Expiry Date = "+expirydate)
                actual_expiry_date1 = expirydate[0:2]
                actual_expiry_date2 = expirydate[2:5]
                actual_expiry_date3 = expirydate[5:7]
                print ("actual_expiry_date ="+actual_expiry_date1 +"-"+ actual_expiry_date2 +"-"+ actual_expiry_date3)
                actual_expiry_date = actual_expiry_date1 +"-"+ actual_expiry_date2 +"-"+ actual_expiry_date3

                strikeprice = firstPart[16:21]
                print ("strikeprice = "+expirydate)

                type = firstPart[21:23]



                print ("adate: "+adate)
                cur.execute("INSERT INTO banknifty1 (type, expirydate,strikeprice ,striktime, d,e,f,g,h,i,entity)"
                            "VALUES ('"+type+"', '"+actual_expiry_date+"', '"+strikeprice+"','"+row[2]+"', '"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"','"+row[7]+"','"+row[8]+"','"+entity+"');")
                con.commit()
            except Exception as e:
                print(e)
           


if __name__ == '__main__':
    main()