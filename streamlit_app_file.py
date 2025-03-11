import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kingshuk@13",
        database="expense_tracker"
    )
    return conn

# Function to execute query and return DataFrame
def execute_query(query):
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def main():
    st.title("Expense Tracker Dashboard")
    
    # Query 1: Total amount spent in each category
    st.header("Total Amount Spent in Each Category")
    query1 = """
    SELECT Category, SUM(Amount_Paid) AS Sum_Amount
    FROM expense_tracker.monthly_expense
    GROUP BY Category
    ORDER BY Sum_Amount DESC;
    """
    df1 = execute_query(query1)
    st.bar_chart(df1.set_index("Category"))

    # Query 2: Total amount spent using each payment mode
    st.header("Total Amount Spent Using Each Payment Mode")
    query2 = """
    SELECT Payment_Mode, SUM(Amount_Paid) AS Payment_Sum_Amount
    FROM expense_tracker.monthly_expense
    GROUP BY Payment_Mode
    ORDER BY Payment_Sum_Amount DESC;
    """
    df2 = execute_query(query2)
    st.bar_chart(df2.set_index("Payment_Mode"))

    # Query 3: Total cashback received across all transactions
    st.header("Total Cashback Received")
    query3 = """
    SELECT SUM(Cashback) AS Sum_Cashback FROM expense_tracker.monthly_expense;
    """
    df3 = execute_query(query3)
    st.write(f"Total Cashback: ${df3['Sum_Cashback'][0]:.2f}")

    # Query 4: Top 5 most expensive categories in terms of spending
    st.header("Top 5 Most Expensive Categories")
    query4 = """
    SELECT Category, SUM(Amount_Paid) AS Sum_Amount
    FROM expense_tracker.monthly_expense
    GROUP BY Category
    ORDER BY Sum_Amount DESC
    LIMIT 5;
    """
    df4 = execute_query(query4)
    st.bar_chart(df4.set_index("Category"))

    # Query 5: Spent on transportation using different payment modes
    st.header("Spent on Transportation Using Different Payment Modes")
    query5 = """
    SELECT Payment_Mode, SUM(Amount_Paid) AS Sum_Amount
    FROM expense_tracker.monthly_expense
    WHERE Category = 'Transport'
    GROUP BY Payment_Mode
    ORDER BY Sum_Amount DESC;
    """
    df5 = execute_query(query5)
    st.bar_chart(df5.set_index("Payment_Mode"))

    # Query 6: Transactions resulted in cashback
    st.header("Transactions Resulted in Cashback")
    query6 = """
    SELECT * FROM expense_tracker.monthly_expense WHERE Cashback != 0;
    """
    df6 = execute_query(query6)
    st.write(df6)

    # Query 7: Total spending in each month of the year
    st.header("Total Spending in Each Month of the Year")
    query7 = """
    SELECT MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
           SUM(Amount_Paid) AS sum_amount
    FROM expense_tracker.monthly_expense
    GROUP BY expense_month
    ORDER BY expense_month;
    """
    df7 = execute_query(query7)
    st.line_chart(df7.set_index("expense_month"))

    # Query 8: Months with the highest spending in categories like "Travel," "Entertainment," or "Gifts"
    st.header("Months with Highest Spending in Specific Categories")
    query8 = """
    SELECT MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
           SUM(Amount_Paid) AS sum_amount,
           Category
    FROM expense_tracker.monthly_expense
    WHERE Category IN ('Travel', 'Entertainment', 'Gifts')
    GROUP BY expense_month, Category
    ORDER BY sum_amount DESC;
    """
    df8 = execute_query(query8)
    st.bar_chart(df8.set_index("expense_month"))

    # Query 9: Recurring expenses during specific months
    st.header("Recurring Expenses During Specific Months")
    query9 = """
    SELECT MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
           SUM(Amount_Paid) AS sum_amount
    FROM expense_tracker.monthly_expense
    WHERE Category IN ('Insurance', 'Property Taxes')
    GROUP BY expense_month
    ORDER BY expense_month;
    """
    df9 = execute_query(query9)
    st.line_chart(df9.set_index("expense_month"))

    # Query 10: Cashback or rewards earned in each month
    st.header("Cashback or Rewards Earned in Each Month")
    query10 = """
    SELECT MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
           SUM(Cashback) AS monthly_cashback
    FROM expense_tracker.monthly_expense
    GROUP BY expense_month
    ORDER BY monthly_cashback DESC;
    """
    df10 = execute_query(query10)
    st.bar_chart(df10.set_index("expense_month"))

    import matplotlib.pyplot as plt

#  Query 11: Overall spending change over time
    st.header("Overall Spending Change Over Time")
    query11 = """
    SELECT 
        MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
        SUM(Amount_Paid) AS sum_amount
    FROM 
        expense_tracker.monthly_expense
    GROUP BY 
        expense_month
    ORDER BY 
        expense_month;
    """
    df11 = execute_query(query11)

    # Plot using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(df11["expense_month"], df11["sum_amount"], marker='o', linestyle='-', color='b')
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Spending")
    ax.set_title("Overall Spending Change Over Time")
    ax.set_ylim(200000, 250000)  # Set y-axis range
    ax.set_xticks(df11["expense_month"])  # Set x-axis ticks to match months
    ax.grid(True)

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Query 12: Patterns in grocery spending
    st.header("Patterns in Grocery Spending")
    query12 = """
    SELECT DAY(STR_TO_DATE(Date, '%d-%m-%Y')) AS days,
           SUM(Amount_Paid) AS Sum_Amount
    FROM expense_tracker.monthly_expense
    WHERE Category = 'Groceries'
    GROUP BY days
    ORDER BY Sum_Amount;
    """
    df12 = execute_query(query12)
    st.bar_chart(df12.set_index("days"))

    # Query 13: High and Low Priority Categories
    st.header("High and Low Priority Categories")
    query13 = """
    SELECT Category, SUM(Amount_Paid) AS Sum_Amount
    FROM expense_tracker.monthly_expense
    GROUP BY Category
    ORDER BY Sum_Amount DESC;
    """
    df13 = execute_query(query13)
    st.bar_chart(df13.set_index("Category"))



    # Query 14: Category contributing the highest percentage of total spending
st.header("Category Contributing the Highest Percentage of Total Spending")
query14 = """
SELECT 
    Category,
    (SUM(Amount_Paid) / (SELECT SUM(Amount_Paid) FROM expense_tracker.monthly_expense) * 100) AS Category_Percentage
FROM 
    expense_tracker.monthly_expense
GROUP BY 
    Category
ORDER BY 
    (SUM(Amount_Paid) / (SELECT SUM(Amount_Paid) FROM expense_tracker.monthly_expense) * 100) DESC;
"""
df14 = execute_query(query14)
st.bar_chart(df14.set_index("Category"))

if __name__ == "__main__":
    main()

