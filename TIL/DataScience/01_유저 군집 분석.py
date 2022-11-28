import os

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors


def load_data(file_path: str, sep: str = None) -> pd.DataFrame:
    return pd.read_csv(file_path, sep=sep)


def check_data(data_frame: pd.DataFrame) -> None:
    print(f'데이터 전체 행 수 : {len(data_frame)}')
    print(f'데이터 컬럼 수 : {len(data_frame.columns)}')
    print(data_frame.info())


if __name__ == '__main__':
    path = 'data'
    file_name = '01_유저 군집 데이터.csv'

    df = load_data(os.path.join(path, file_name), sep="\t")

    check_data(df)

    """
    데이터 컬럼 종류
    People (사람)
        ID: Customer's unique identifier
        Year_Birth: Customer's birth year
        Education: Customer's education level (교육 수준)
        Marital_Status: Customer's marital status (결혼 상태)
        Income: Customer's yearly household income
        Kidhome: Number of children in customer's household (어린 아이의 수)
        Teenhome: Number of teenagers in customer's household (10대 수)
        Dt_Customer: Date of customer's enrollment with the company (서비스 가입 날짜)
        Recency: Number of days since customer's last purchase (마지막으로 구매한 날로부터 얼마가 지났는지)
        Complain: 1 if customer complained in the last 2 years, 0 otherwise
    Products (상품)
        MntWines: Amount spent on wine in last 2 years
        MntFruits: Amount spent on fruits in last 2 years
        MntMeatProducts: Amount spent on meat in last 2 years
        MntFishProducts: Amount spent on fish in last 2 years
        MntSweetProducts: Amount spent on sweets in last 2 years
        MntGoldProds: Amount spent on gold in last 2 years
    Promotion (프로모션)
        NumDealsPurchases: Number of purchases made with a discount (할인 받아 구매한 수)
        AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
        AcceptedCmp2: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
        AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
        AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
        AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
        Response: 1 if customer accepted the offer in the last campaign, 0 otherwise
    Place (구매 장소)
        NumWebPurchases: Number of purchases made through the company’s web site
        NumCatalogPurchases: Number of purchases made using a catalogue
        NumStorePurchases: Number of purchases made directly in stores
        NumWebVisitsMonth: Number of visits to company’s web site in the last month
    """
