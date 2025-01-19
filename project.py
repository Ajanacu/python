import pandas as pd
import numpy as np
import csv
import os
import matplotlib.pyplot as plt

def create_csv(filename,headers,no_rows):
    rows=[]
    for i in range(1,no_rows +1):
        amnt=input("Enter the amount:")
        cat=input("Enter the category:")
        date=input("Enter the date:")
        row=[amnt,cat,date]
        rows.append(row)
        c=input("Do you wish to add another expense?:")
        if c=="no":
            break
    with open(filename,mode='w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

filename="Expense.csv"
headers=["Amount","Category","Date"]


def analyze():
    df=pd.read_csv("Expense.csv")#analyze
    print(df)

    an=pd.DataFrame(df)
    s=df["Amount"].sum()
    print("\nTotal amount:",s)
def visualize():
    d=pd.read_csv("Expense.csv")
    category = d.groupby("Category")["Amount"].sum()
    dateby=d.groupby("Date")["Amount"].sum()
    choice=input("Enter your preferred graph(1.By category 2.By date)")
    if choice == '1':
        x=np.array(category)
        plt.bar(category.index,category.values,label="Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
    elif choice == '2':
        x=np.array(dateby)
        plt.bar(dateby.index,dateby.values,label="Expense by Date")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()
    else:
        print("Wrong choice!!!")
    

while True:
    print("1.Enter expense \n2.Analysis \n3.Visualization \n4.Exit")
    ch=input("Enter your choice:")
    if ch=='1':
        create_csv(filename,headers,1000)
    elif ch=='2':
        analyze()
    elif ch=='3':
        visualize()
    elif ch=='4':
        print("Exiting...")
        break
    else:
        print("Wrong choice!!!")

