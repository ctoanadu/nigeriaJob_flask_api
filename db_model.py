from web_scrapper import create_dict
import pandas as pd 
from sqlalchemy import create_engine

#Initial SQLalchemy engine to interact with database 
engine = create_engine('postgresql://user_new:Password1@localhost:5432/beekin_db')


def main():

    #create a database table to from datagrame
    df = pd.DataFrame(create_dict())
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)

    # Create a dataframe for technologies to unnest the technology column
    df_technologies = df.explode('technologies').reset_index(drop=True)
    df_technologies.rename(columns={'technologies': 'technology'}, inplace=True)

    # Create a dataframe for locations to unnest the location column 
    df_locations = df.explode('location').reset_index(drop=True)
    df_locations.rename(columns={'location': 'location_name'}, inplace=True)

    #drop unnecessary columns
    df_locations=df_locations.drop('technologies',axis=1)
    df_technologies=df_technologies.drop('location',axis=1)

    #Normalize the data by joining the two dataframe 
    df_final = pd.merge(df_technologies, df_locations, how='inner')

    #rename column 
    df_final.rename(columns={'row_num': 'id'}, inplace=True)

    #Save create table in postgres and export dataframe table.
    df_final.to_sql('beekin_job', engine,if_exists='replace')  

    return df_final
print(main())

if __name__=='__main__':
    main()



