import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merge_df=pd.merge(prices,units_sold,on="product_id",how="left")
    merge_df["units"].fillna(0,inplace=True)
    merge_df["purchase_date"] = merge_df["purchase_date"].fillna(pd.Timestamp("1900-01-01"))
    filter_df=merge_df[(merge_df["start_date"]<=merge_df["purchase_date"]) & (merge_df["purchase_date"]<=merge_df["end_date"]) | (merge_df["units"]==0)]
    filter_df["Total Price"]=filter_df["price"]*filter_df["units"]
    print(filter_df.head())
    group_df=filter_df.groupby("product_id")["Total Price"].sum().reset_index(name="sum_price")
    group_df2=filter_df.groupby("product_id")["units"].sum().reset_index(name="total_units")
    group_df["average_price"]=round(group_df["sum_price"]/group_df2["total_units"].replace(0, pd.NA),2)
    group_df["average_price"].fillna(0,inplace=True)
    return group_df[["product_id","average_price"]]
    
    