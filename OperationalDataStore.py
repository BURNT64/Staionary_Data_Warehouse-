'''
Created on 19 December 2022

@author: Will J92908
'''
import pandas as pd


class OperationalDataStore:
    tables = [
        'DimInternetSale'
        'DimCategory',
        'DimSupplier',
        'DimProduct',
        'DimCustomer',
        'DimLocation',
        'DimDate',
        'FactSales']
    
    DimCategory_df = pd.DataFrame(columns = ['CategoryID','CategoryDescription','ParentCatagory'])
    DimSupplier_df = pd.DataFrame(columns = ['SupplierID','SupplierAddress','SupplierCity','SupplierStateProvince',
                                             'SupplierCountry','SupplierPostCode','SupplierPhone'])
    DimProduct_df = pd.DataFrame(columns = ['ProductID','ProductDescription','CategoryID','SupplierPrice',
                                            'ProductPrice','SafetyStockLevel','ReorderPoint','SupplierID'])
    DimCustomer_df = pd.DataFrame(columns = ['CustomerID','CustomerEmail','FirstName','SecondName','CustomerType',
                                              'City','StateProvince','Country','PostalCode'])
    DimLocation_df = pd.DataFrame(columns = ['LocationID','City','Country'])
    DimDate_df = pd.DataFrame(columns = ['DateID','FullDate','Day','Month','Year','Quarter'])
    FactSales_df = pd.DataFrame(columns = ['SalesID','CustomerID','ProductID','CatagoryID','SupplierID','DateOfSale','DateShipped','ShippingType',
                                           'Quantity','SalesAmount','SalesTax','SaleTotal','DateID','LocationID'])
        
        