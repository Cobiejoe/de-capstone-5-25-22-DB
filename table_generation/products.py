import pandas as pd
from web_scrape import webscrape_product_data


product_url_list = ['https://us.speedo.com/women/one-piece-swimwear.list',
                    'https://us.speedo.com/men/elite-competition-swimwear.list',
                    'https://us.speedo.com/men/briefs.list',
                    'https://us.speedo.com/women/elite-competition-swimwear.list',
                    'https://us.speedo.com/gear/bags-backpacks.list',
                    'https://us.speedo.com/gear/swim-caps.list',
                    'https://us.speedo.com/goggles/racing-swimming-goggles.list',
                    'https://us.speedo.com/goggles/recreation-swimming-goggles.list',
                    'https://us.speedo.com/gear/floatation.list',
                    'https://us.speedo.com/gear/training-fins.list',
                    'https://us.speedo.com/men/jammers.list',
                    'https://us.speedo.com/women/bikinis-separates.list']


def create_product_df(data_list):

    df = pd.DataFrame(data=data_list,
                      columns=['product_id','product_category','product_name','product_price','stock_quantity'])
    df['product_price'] = df['product_price'].str.replace('$', '').astype(float)
    df[['product_category', 'product_name', 'product_price']] = df[['product_category', 'product_name', 'product_price']]. \
        apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    return df


product_df = create_product_df(webscrape_product_data(product_url_list))

product_table = product_df.to_csv('../csv_folders/product_table.csv', index=False)
