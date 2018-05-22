# banknifty

Its python script to insert historical data of banknifty in postgres sql

Input file should be in csv format

Please use below command to run : py src\start.py D:\data\banknifty\src\Bnf03042017.csv


INSERT INTO master (ticker, associateddate ,date,  open, high,low,close,volume,openinterest,indexprice) 
VALUES ('BANKNIFTY', '2017-04-06', '2017-04-03 11:55:59','0.35','0.35','0.35','0.35','40','0','18500');
