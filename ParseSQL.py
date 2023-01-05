'''
Created on 23 December 2022

@author: Will J92908
'''
import pyodbc
import pandas as pd
from OperationalDataStore import OperationalDataStore

class ParseSQL:
    def __init__(self):
        print("Building Parse SQL via constructor")
        connectionString = "DRIVER={SQL Server};SERVER=sql2016.fse.network;DATABASE=db_2111421_stationery;UID=user_db_2111421_stationery;PWD=Che20030407"
        self.conn = pyodbc.connect(connectionString)
        self.cursor = self.conn.cursor()
        
    def ParseSQL(self):
        print("Parsing SQL")
        self.parseDates()
        self.parseLocation()
        self.parseCustomer()
        self.parseProduct()
        self.parseCategory()
        self.parseSupplier()
        self.parseSales()
        
    def parseDates(self):
        print("\t Parsing SQL Dates")
        dates_df = pd.read_sql_query("SELECT DateOfSale FROM InternetSale", self.conn)
        dates_df['FullDate'] = pd.to_datetime(dates_df['DateOfSale'])
        dates_df['DateID'] = dates_df['FullDate'].dt.strftime('%Y%m%d')
        dates_df['Day'] = dates_df['FullDate'].dt.strftime('%A') 
        dates_df['Month'] = dates_df['FullDate'].dt.strftime('%B')       
        dates_df['Year'] = dates_df['FullDate'].dt.strftime('%Y')
        dates_df['Quarter'] = dates_df['FullDate'].dt.quarter
        dates_df = dates_df.drop(columns=['DateOfSale'])
        OperationalDataStore.DimDate_df = OperationalDataStore.DimDate_df.append(dates_df)
        OperationalDataStore.DimDate_df.drop_duplicates(subset='DateID', keep='first',inplace=True)
        print(OperationalDataStore.DimDate_df.to_string())
        
    def parseLocation(self):
        print("\t parsing SQL Location")
        locations_df = pd.read_sql_query("SELECT PostalCode as LocationID, City, Country FROM Customer", self.conn)
        OperationalDataStore.DimLocation_df = OperationalDataStore.DimLocation_df.append(locations_df)
        OperationalDataStore.DimLocation_df.drop_duplicates(subset='LocationID', keep='first',inplace=True)
        print(OperationalDataStore.DimLocation_df.to_string())
         
    def parseCustomer(self):
        print("\t parsing SQL Customer")
        customer_df = pd.read_sql_query("SELECT * FROM Customer", self.conn)
        OperationalDataStore.DimCustomer_df = OperationalDataStore.DimCustomer_df.append(customer_df)
        print(customer_df.to_string())
        
    def parseInternetSale(self):
        print("\t parsing SQL InternetSale")
        internetSale = pd.read_sql_query("SELECT * FROM InternetSale", self.conn)
        customer_df = pd.read_sql_query("SELECT * FROM Customer", self.conn)
        OperationalDataStore.DiminternetSale_df = OperationalDataStore.DiminternetSale_df.append(customer_df)
        print(customer_df.to_string())
        
    def parseProduct(self):
        print("\t parsing SQL Product")
        product_df = pd.read_sql_query("SELECT * FROM Product", self.conn)
        OperationalDataStore.DimProduct_df = OperationalDataStore.DimProduct_df.append(product_df)
        print(product_df.to_string())
        
    def parseCategory(self):
        print("\t parsing SQL Category")
        category_df = pd.read_sql_query("SELECT * FROM Category", self.conn)
        OperationalDataStore.DimCategory_df = OperationalDataStore.DimCategory_df.append(category_df)
        print(category_df.to_string())
        
    def parseSupplier(self):
        print("\t parsing SQL Supplier")
        supplier_df = pd.read_sql_query("SELECT * FROM Supplier", self.conn)
        OperationalDataStore.DimSupplier_df = OperationalDataStore.DimSupplier_df.append(supplier_df)
        print(supplier_df.to_string())
        
        
    def parseSales(self):
        print("\t parsing SQL Sales")
        sales_df = pd.read_sql_query("SELECT * FROM InternetSale", self.conn)
        sales_df['DateOfSale'] = pd.to_datetime(sales_df['DateOfSale'])
        sales_df['DateID'] = sales_df['DateOfSale'].dt.strftime('%Y-%m-%d')
        sales_df = sales_df.drop(columns=['DateOfSale'])
        sales_df = pd.merge(sales_df,OperationalDataStore.DimCustomer_df[['CustomerID','PostalCode']], left_on='CustomerID', right_on='CustomerID', how ='left')
        sales_df = sales_df.rename(columns = {'PostalCode':'LocationID'})
        OperationalDataStore.FactSales_df = OperationalDataStore.FactSales_df.append(sales_df)
        print(OperationalDataStore.FactSales_df.to_string())
        
        
        
        