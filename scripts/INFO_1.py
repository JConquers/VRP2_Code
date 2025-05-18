import pandas as pd

##############################################################################################
# THE SOLE PURPOSE OF THIS SCRIPT IS TO GET INFORMATION ABOUT HOW MANY QUESTION-ANSWER PAIRS #
# HAVE BEEN GENERATED FOR EACH IMAGE, HOW MANY QUESTIONS FOR WHICH ANSWERS WERE NOT SUPPLIED #
# BY GEMINI API-CALL                                                                         #
##############################################################################################


# Load CSV
df = pd.read_csv('/home/jinesh14/CourseWork/VR_P2/dataset_curated/Sf/Sf_qa_data_cleaned.csv', header=None, names=['a', 'b', 'c'])

# Get frequency count of each unique value in column 'a'
frequency_counts = df['a'].value_counts()
print("Frequency counts in column 'a':")
print(frequency_counts)

# Print number of non-null entries in each column
print(f"\nEntries in column 'a': {df['a'].notnull().sum()}")
print(f"Entries in column 'b': {df['b'].notnull().sum()}")
print(f"Entries in column 'c': {df['c'].notnull().sum()}")

# Find and print rows where column 'c' is missing
missing_c = df[df['c'].isnull() | (df['c'].astype(str).str.strip() == '')]
print(f"\nNumber of rows where column 'c' is missing: {len(missing_c)}")

if not missing_c.empty:
    print("\nRows where column 'c' is missing:")
    print(missing_c['a'])
