import os

import pandas as pd
import warnings
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


def data_cleaning(data_frame: pd.DataFrame) -> None:
    print(f"결측값 제거 전 데이터 수 - {len(data_frame)}")
    data_frame = data_frame.dropna()
    print(f"결측값 제거 후 데이터 수 - {len(data_frame)}")

    data_frame["Dt_Customer"] = pd.to_datetime(data_frame["Dt_Customer"])

    customer_dates = [customer_date_time.date() for customer_date_time in data_frame["Dt_Customer"]]
    recent_register_date = max(customer_dates)
    print(f"가장 최근 가입 날짜 - {recent_register_date} | 가장 오래된 가입 날짜 - {min(customer_dates)}")

    data_frame["Customer_For"] = [recent_register_date - register_date for register_date in customer_dates]
    data_frame["Customer_For"] = pd.to_numeric(data_frame["Customer_For"], errors="raise")

    print(data_frame["Marital_Status"].value_counts())
    print(data_frame["Education"].value_counts())

    # Marital_Status 데이터 전처리 -> 파트너와 같이 사는지, 독신인지 분류
    data_frame["Living_With"] = (
        data_frame["Marital_Status"].replace({
            "Married": "Partner",
            "Together": "Partner",
            "Single": "Alone",
            "Divorced": "Alone",
            "Widow": "Alone",
            "Alone": "Alone",
            "Absurd": "Alone",
            "YOLO": "Alone"
        })
    )

    # kidhome, teenhome을 분류하지 않고 미성년자 자녀 여부를 저장하는 데이터 생성
    data_frame["Children"] = data_frame["Kidhome"] + data_frame["Teenhome"]

    # 해당 데이터를 통해 가족 사이즈를 구함
    data_frame["Family_Size"] = (
        data_frame["Living_With"].replace({"Alone": 1, "Partner": 2}) + data_frame["Children"]
    )

    data_frame["Is_Parent"] = np.where(data_frame.Children > 0, 1, 0)

    # 학력 상태 정리
    data_frame["Education"] = data_frame["Education"].replace({
        "Basic": "Undergraduate",
        "2n Cycle": "Undergraduate",
        "Graduation": "Graduate",
        "Master": "Postgraduate",
        "PhD": "Postgraduate"
    })

    # 생년 월일을 통해 나이를 구할 수 있다.
    data_frame["Age"] = 2022 - data_frame["Year_Birth"]

    # 다양한 잡화 구매를 더해서 총 사용한 비용 Spent 를 구한다.
    data_frame["Spent"] = data_frame["MntWines"] + data_frame["MntFruits"] + data_frame["MntMeatProducts"] + data_frame[
        "MntFishProducts"] + data_frame["MntSweetProducts"] + data_frame["MntGoldProds"]

    # 컬럼명 짧게 변경
    data_frame = data_frame.rename(
        columns={"MntWines": "Wines", "MntFruits": "Fruits", "MntMeatProducts": "Meat", "MntFishProducts": "Fish",
                 "MntSweetProducts": "Sweets", "MntGoldProds": "Gold"})

    # 중복되거나 필요없는 컬럼 제거
    drop_column_list = ["Marital_Status", "Dt_Customer", "Z_CostContact", "Z_Revenue", "Year_Birth", "ID"]
    data_frame = data_frame.drop(drop_column_list, axis=1)

    # 색상 지정
    sns.set(rc={"axes.facecolor": "#FFF9ED", "figure.facecolor": "#FFF9ED"})

    # 아래의 정해진 컬럼들 사이의 상관관계를 그래프로 확인해 본다.
    To_Plot = ["Income", "Recency", "Customer_For", "Age", "Spent", "Is_Parent"]
    print("Reletive Plot Of Some Selected Features: A Data Subset")
    sns.pairplot(data_frame[To_Plot], hue="Is_Parent", palette=(["#682F2F", "#F3AB60"]))

    # Outlier 데이터 제거
    data_frame = data_frame[(data_frame["Age"] < 90)]
    data_frame = data_frame[(data_frame["Income"] < 600000)]
    print("Outlier 제거 후 데이터 row 수:", len(data_frame))

    return data_frame


if __name__ == '__main__':
    warnings.filterwarnings('ignore')

    path = 'data'
    file_name = '01_유저 군집 데이터.csv'

    df = load_data(os.path.join(path, file_name), sep="\t")

    # 데이터 확인
    check_data(df)

    # 데이터 전처리
    data_cleaning(df)
    print(df.describe())

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
