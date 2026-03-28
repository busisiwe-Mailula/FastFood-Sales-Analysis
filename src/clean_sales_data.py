import pandas as pd

# in this program i will clean the dataset before analysing it in MySQL

# create a function that inspects the dataset
def inspect_data(df):
    print("First 5 rows:")
    print(df.head())

    print("\nDataset Info:")
    df.info()

    print("\nMissing Values:")
    print(df.isnull().sum())


# load dataset
df = pd.read_csv("data/raw/fastfood_sales_raw.csv")

# call function to inspect dataset
inspect_data(df)


# clean text columns by removing unwanted whitespaces and captitaliing the letter in the text
df['item_name'] = df['item_name'].str.strip().str.title()
df['category'] = df['category'].str.strip().str.title()
df['payment_method'] = df['payment_method'].str.strip().str.title()

# Replace slashes with dashes
df['order_date'] = df['order_date'].str.replace('/', '-')

# Convert to datetime safely
df['order_date'] = pd.to_datetime(
    df['order_date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)
# Check if any dates failed
print("Unparsed dates (if any):")
print(df[df['order_date'].isna()])

# handle missing quantity values by assuming 1 if missing
df['quantity'] = df['quantity'].fillna(1)

# create a new column that shows revenue per row
df['revenue'] = df['price'] * df['quantity']

# change float data type to int
df['quantity'] = df['quantity'].astype(int)

# check cleaned data
inspect_data(df)

# export cleaned data into a new file
df.to_csv("data/cleaned/fastfood_sales_clean.csv", index=False)
