import pandas as pd
import ast


def transform_data(data):
    df = pd.DataFrame(data)
    # df['analytics'] = df['analytics'].apply(ast.literal_eval)
    df = df.join(df['analytics'].apply(pd.Series)).drop(columns='analytics')
    df = (df.join(df['flights'].apply(pd.Series)).rename(columns={'score': 'flight score'})
          .join(df['travelers'].apply(pd.Series)).rename(columns={'score': 'traveler score'}).drop(
        columns=['travelers', 'flights']))
    df['Total_Score'] = df['flight score'] + df['traveler score']
    df = df.sort_values(by=['Total_Score'], ascending=[False]).drop(
        columns=['flight score', 'traveler score']).reset_index(drop=True)

    return df.to_dict(orient="records")




if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    df = pd.read_csv("test_flights_most_traveled.csv")
    df['analytics'] = df['analytics'].apply(ast.literal_eval)
    df = df.join(df['analytics'].apply(pd.Series)).drop(columns='analytics')
    df = (df.join(df['flights'].apply(pd.Series)).rename(columns={'score':'flight score'})
          .join(df['travelers'].apply(pd.Series)).rename(columns={'score': 'traveler score'}).drop(columns=['travelers', 'flights']))
    df['Total Score'] = df['flight score'] + df['traveler score']
    df = df.sort_values(by=['Total_Score'], ascending=[False]).drop(columns=['flight score', 'traveler score']).reset_index(drop=True)
    print(df.to_dict(orient="records"))