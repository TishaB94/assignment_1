#total amount spent in each category

SELECT 
    Category, SUM(Amount_Paid) AS Sum_Amount
FROM
    expense_tracker.monthly_expense
GROUP BY Category
ORDER BY Sum_Amount  desc;

#total amount spent using each payment mode

SELECT 
    Payment_Mode, round((SUM(Amount_Paid)),2) AS Payment_Sum_Amount
FROM
    expense_tracker.monthly_expense
GROUP BY Payment_Mode
ORDER BY Payment_Sum_Amount  desc;

#total cashback received across all transactions

select sum(Cashback) AS Sum_Cashback from expense_tracker.monthly_expense;

#top 5 most expensive categories in terms of spending

SELECT 
    Category, SUM(Amount_Paid) AS Sum_Amount
FROM
    expense_tracker.monthly_expense
GROUP BY Category
LIMIT 5;

#spent on transportation using different payment modes

SELECT 
    Category, Payment_Mode, SUM(Amount_Paid) AS Sum_Amount
FROM
    expense_tracker.monthly_expense
WHERE
    Category = 'Transport'
GROUP BY Payment_Mode
ORDER BY Sum_Amount DESC;


#transactions resulted in cashback

SELECT 
    *
FROM
    expense_tracker.monthly_expense
WHERE
    Cashback != 0;
    
    
    
    #total spending in each month of the year
    
SELECT 
    MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
    SUM(Amount_Paid) AS sum_amount
FROM
    expense_tracker.monthly_expense
GROUP BY expense_month
ORDER BY expense_month;

#Which months have the highest spending in categories like "Travel," "Entertainment," or "Gifts"?


SELECT 
    MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
    SUM(Amount_Paid) AS sum_amount,
    Category
FROM
    expense_tracker.monthly_expense
WHERE Category = 'Travel'        
GROUP BY expense_month
ORDER BY sum_amount DESC;

#Are there any recurring expenses that occur during specific months of the year (e.g., insurance premiums, property taxes)?

#How much cashback or rewards were earned in each month?

SELECT 
    MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
    SUM(Cashback) AS monthly_cashback
FROM
    expense_tracker.monthly_expense
GROUP BY expense_month
ORDER BY monthly_cashback DESC;

#How has your overall spending changed over time (e.g., increasing, decreasing, remaining stable)?

SELECT 
    MONTH(STR_TO_DATE(Date, '%d-%m-%Y')) AS expense_month,
    SUM(Amount_Paid) AS sum_amount
FROM
    expense_tracker.monthly_expense
GROUP BY expense_month
ORDER BY expense_month ;

#What are the typical costs associated with different types of travel (e.g., flights, accommodation, transportation)?


#Are there any patterns in grocery spending (e.g., higher spending on weekends, increased spending during specific seasons)?

SELECT 
    DAY(STR_TO_DATE(Date, '%d-%m-%Y')) AS days,
    SUM(Amount_Paid) AS Sum_Amount
FROM
    expense_tracker.monthly_expense
WHERE
    Category = 'Groceries'
GROUP BY days
ORDER BY Sum_Amount;

# Define High and Low Priority Categories

SELECT 
    Category, SUM(Amount_Paid) AS Sum_Amount
FROM
    expense_tracker.monthly_expense
GROUP BY Category
ORDER BY Sum_Amount DESC;


#Which category contributes the highest percentage of the total spending?

SELECT 
    Category,
    (SUM(Amount_Paid) / (SELECT 
            SUM(Amount_Paid)
        FROM
            expense_tracker.monthly_expense) * 100) AS Category_Percentage
FROM
    expense_tracker.monthly_expense
GROUP BY Category
ORDER BY Category_percentage DESC;









