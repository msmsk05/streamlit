

import streamlit as st
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
ımport plotly as plt




html_temp = """
<div style="background-color:white;padding:10px">
<h1 style="color:black;text-align:center;"><b> New Entry/Database Check </b></h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)



html_temp = """
<div style="background-color:red;padding:10px">
<h2 style="color:white;text-align:center;">DQ Project Demo </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

  
@st.cache(allow_output_mutation=True)
def get_query_results(name):

    # Connect to the PostgreSQL database server
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select name, legal_entity_id, organizationz.id, country, city from organizationz inner join organization_address on organization_address.organization_id=organizationz.id inner join address on address.id=organization_address.address_id where lower(Name) like lower('"+name+"%')"

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)
       
        if len(df)>0:
     
            return df
        else:
            name1=name[:5]
            sql="Select name, legal_entity_id, organizationz.id, country, city from organizationz inner join organization_address on organization_address.organization_id=organizationz.id inner join address on address.id=organization_address.address_id where lower(Name) like lower('"+name1+"%')"
            df2 = pd.read_sql(sql, conn, index_col=None)
            
            return df2
        
def get_fuzzy_matches(name):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select * from Organizationz where lower(Name) like lower('%"+name+"%') or lower(Name) like lower('%"+name1+"%') or lower(Name) like lower('%"+name2+"%') or lower(Name) like lower('%"+name3+"%')"

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
        df = df[["id", "legal_entity_id", "name"]]
        if len(df)>0:
            Ratios = process.extract(name,df.name.values)
            values=[a_tuple[0] for a_tuple in Ratios]
            return Ratios, values, df
            
        else:
            name1=name[:5]
            sql="Select * from Organization where lower(Name) like lower('%"+name1+"%')"
            df2 = pd.read_sql(sql, conn, index_col=None)
            df2=df2[["id", "legal_entity_id", "name"]]  
            Ratios = process.extract(name,df2.name.values)
            values=[a_tuple[0] for a_tuple in Ratios]
            return Ratios, values, df


            
def get_difflib_matches(name):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select * from Organizationz where lower(Name) like lower('%"+name+"%') or lower(Name) like lower('%"+name1+"%') or lower(Name) like lower('%"+name2+"%') or lower(Name) like lower('%"+name3+"%') or lower(Name) like lower('%"+name4+"') or lower(Name) like lower('%"+name5+"')"

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)
        
        final=[]
        for i in [name,name1,name2,name3,name4,name5]:
            final.append(difflib.get_close_matches(i, df.name.values,15, cutoff=0.1))
            
        return numpy.unique(final[0])
        #return difflib.get_close_matches(name, df.name.values,10, cutoff=0.1)
            
            
            
def join(name,coun):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select name, legal_entity_id, organizationz.id, country, city from organizationz inner join organization_address on organization_address.organization_id=organizationz.id inner join address on address.id=organization_address.address_id where (lower(Name) like lower('"+name+"%') or lower(Name) like lower('"+name1+"%') or lower(Name) like lower('"+name2+"%') or lower(Name) like lower('%"+name3+"') or lower(Name) like lower('%"+name4+"') or lower(Name) like lower('%"+name5+"')) and lower(country) like lower('%"+coun+"%')"

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
        return df
    
def join2(name,city):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select name, legal_entity_id, organizationz.id, country, city from organizationz inner join organization_address on organization_address.organization_id=organizationz.id inner join address on address.id=organization_address.address_id where (lower(Name) like lower('"+name+"%') or lower(Name) like lower('"+name1+"%') or lower(Name) like lower('"+name2+"%') or lower(Name) like lower('%"+name3+"') or lower(Name) like lower('%"+name4+"') or lower(Name) like lower('%"+name5+"')) and lower(city) like lower('%"+city+"%')"

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
        return df    
    
def individual(name):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select * from individual where (lower(Name) like lower('"+name+"%') or lower(Name) like lower('"+name1+"%') or lower(Name) like lower('"+name2+"%') or lower(Name) like lower('%"+name3+"') or lower(Name) like lower('%"+name4+"') or lower(Name) like lower('%"+name5+"'))"
        df = pd.read_sql(sql, conn, index_col=None)
        matches=process.extract(name,df.name.values,limit=10)
        return matches
    
    
    
    
def id_check(name,legal_id):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select name, legal_entity_id, organizationz.id, country, city from organizationz inner join organization_address on organization_address.organization_id=organizationz.id inner join address on address.id=organization_address.address_id where (lower(Name) like lower('"+name+"%') or lower(Name) like lower('"+name1+"%') or lower(Name) like lower('"+name2+"%') or lower(Name) like lower('%"+name3+"') or lower(Name) like lower('%"+name4+"') or lower(Name) like lower('%"+name5+"')) and legal_entity_id='%s'" %legal_id
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
        return df

def get_id(name):
    df=get_fuzzy_matches(name)[2]
    #legal_ids=df.legal_entity_id.values
    
    return df            
      
def check(name,legal_id):
    name4=name.split()[0]
    name5=name.split()[1]
    y=id_check(name,legal_id)
    if legal_id in y.legal_entity_id.values and y[y.name.str.contains(name,case=False)].shape[0]>0:
        return("Already exist. Inserting this value will cause duplication")
    elif legal_id in y.legal_entity_id.values and name not in y.name.values:
        highest = process.extractOne(name,y.name)[0]
        return("Legal_entity_id matches and there is a partial match for the name. Best match is {}".format(highest))
        
    else:
        return("Not exists, the new value can be saved to the database")  

def check2(name,coun):
    x=join(name,coun)
    if coun in x.country.values and x[x.name.str.contains(name,case=False)].shape[0]>0:
        return("Already exist. Inserting this value will cause duplication")
    elif coun in x.country.values and name not in x.name.values:
        highest = process.extractOne(name,x.name)[0]
        return("Country matches and there is a partial match for the name. Best match is {}".format(highest))
    else:
        return("Not exists, the new value can be saved to the database")  
    
def check3(name,city):
    z=join2(name,city)
    if city in z.city.values and z[z.name.str.contains(name,case=False)].shape[0]>0:
        return("Already exist. Inserting this value will cause duplication")
    elif city in z.city.values and name not in z.name.values:
        highest = process.extractOne(name,z.name)[0]
        return("City matches and there is a partial match for the name. Best match is {}".format(highest))
    else:
        return("Not exists, the new value can be saved to the database")
        
def all_features(name,coun,city,legal_id):
    name1=name[:5]
    name2=name[1:6]
    name3=name[-5:]
    if len(name.split())>1:
        name4=name.split()[0]
        name5=name.split()[1]
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql = "Select name, legal_entity_id, organizationz.id, country, city from organizationz inner join organization_address on organization_address.organization_id=organizationz.id inner join address on address.id=organization_address.address_id where (lower(Name) like lower('"+name+"%') or lower(Name) like lower('"+name1+"%') or lower(Name) like lower('"+name2+"%') or lower(Name) like lower('%"+name3+"') or lower(Name) like lower('"+name4+"%') or lower(Name) like lower('%"+name5+"'))"
        if city:
            sql = sql+ " and city = '%s'" % city
        if coun:
            sql = sql+" and country = '%s'" % coun
        if legal_id:
            sql = sql+" and legal_entity_id = '%s'" % legal_id
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
        return df
    
    
#def check4(name,coun,city,legal_id):
    #b=all_features(all_features(name,coun,city,legal_id)
    #return b           

                   
                   
                   
                   
                   
        
def get_soundex_matches(name):
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql="SELECT * FROM organizationz WHERE soundex(name) = soundex('%s')" %name

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
        df = df[["id", "legal_entity_id", "name"]]    
        return df
    
    
    
def get_levenshtein_matches(name):
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql="SELECT name, levenshtein(name, '%s') FROM organizationz WHERE soundex(name) = soundex('%s') order by levenshtein" % (name,name)
        #sql="select * from organizationz where levenshtein(name, '%s') < 8 and lower(Name)=='%s'" %(name,name)
        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
      
        return df
                
        
def get_difference_matches(name):
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn:
        
        sql="SELECT name FROM organization WHERE difference(name, '%s') = 4" % name
        #sql="SELECT * from organization order by similarity(metaphone(name,10), metaphone('%s',10))" %name

        # Execute query and return results as a pandas dataframe
        df = pd.read_sql(sql, conn, index_col=None)

        # Select necessary columns
          
        return df        
        
        
def get_tables():
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn: 
        sql="SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;"
        df = pd.read_sql(sql, conn, index_col=None)
        return df

def read_table(table_name):
    with psycopg2.connect(host='35.224.7.101',
                          port='5432',
                          database='postgres',
                          user= 'postgres',
                          password= 'FutureLeaders') as conn: 
        sql="select * from %s limit 20" % table_name
        df = pd.read_sql(sql, conn, index_col=None)
        return df

def sentence(text):
    nlp = en_core_web_sm.load()
    doc=nlp(text)
    return([(X.text, X.label_) for X in doc.ents])

    
    
    
def person_query(text):
    nlp = en_core_web_sm.load()
    doc=nlp(text)
    PERSON=[X.text for X in doc.ents if X.label_ in ["PERSON"]]
    conn = psycopg2.connect(database="postgres", user="postgres", password="FutureLeaders", host="35.224.7.101", port="5432")
    if len(PERSON)==1:
        sql = "Select * from individual where lower(Name) like lower('%"+PERSON[0]+"%')"
        df = pd.read_sql(sql, conn, index_col=None)
        if PERSON[0] in df.name.values:
            return (PERSON[0],"exists"), df
        else: return "not exists"
    if len(PERSON)==2:   
        sql = "Select * from individual where lower(Name) like lower('%"+PERSON[0]+"%') or lower(Name) like lower('%"+PERSON[1]+"%')"
        df = pd.read_sql(sql, conn, index_col=None)
        if PERSON[0] and PERSON[1] in df.name.values:
            return "both exists", df
        elif PERSON[0] in df.name.values and PERSON[1] not in df.name.values:
            return PERSON[0],"exists", df[df.name==PERSON[0]]
        elif PERSON[1] in df.name.values and PERSON[0] not in df.name.values:
            return PERSON[1],"exists", df[df.name==PERSON[1]]
        else: return "neither of them exists"
        
def organization_query(text):
    nlp = en_core_web_sm.load()
    doc=nlp(text)
    a,b,c=(X.text for X in doc.ents if X.label_ in ["ORG"])
    conn = psycopg2.connect(database="postgres", user="postgres", password="FutureLeaders", host="35.224.7.101", port="5432")
    
    a1=a.split()[0]
    a2=a.split()[1]
    sql1="Select name from organization where lower(Name) like lower('%"+a1+"%') or lower(Name) like lower('%"+a1+"%')" 
    df1 = pd.read_sql(sql1, conn,index_col=None)
    b1=b.split()[0]
    b2=b.split()[1]
    sql2="Select name from organization where lower(Name) like lower('%"+b+"%') or lower(Name) like lower('%"+b1+"%')" 
    df2 = pd.read_sql(sql2, conn,index_col=None)
    c1=c.split()[0]
    c2=c.split()[1]
    sql3="Select name from organization where lower(Name) like lower('%"+c+"%') or lower(Name) like lower('%"+c1+"%')" 
    df3 = pd.read_sql(sql3, conn,index_col=None)
    df=pd.concat([df1,df2,df3])
    for i in a,b,c:
        if i in df.values:
            return (i, "exists"), process.extract(i,df.values)
        
    
            

        
def button_org(a):
    df=organization_query(text)[0]
    a=organization_query(text)[1]   
    
    
    if a in df.values:
        return (a,"exists")
    else:  
        matches = process.extract(a,df.values)
        return "Not in the DB. Best matches are", matches

            

def save_organization(name):
    #pattern = r'[^a-zA-Z0-9\s]'
    #name = re.sub(pattern, '', name)
    #name=name.title()
    #con = psycopg2.connect(database="postgres", user="postgres", password="FutureLeaders", host="35.224.7.101", port="5432")
    #cur = con.cursor()
        
    #cur.execute("INSERT INTO organizationz (name) VALUES ('%s')" %name)
    #con.commit()
    return"Record inserted successfully"
    #con.close()  
    
def save_individual(name):
    #pattern = r'[^a-zA-Z0-9\s]'
    #name = re.sub(pattern, '', name)
    #name=name.title()
    #con = psycopg2.connect(database="postgres", user="postgres", password="FutureLeaders", host="35.224.7.101", port="5432")
    #cur = con.cursor()
        
    #cur.execute("INSERT INTO individual (name) VALUES ('%s')" %name)
    #con.commit()
    return"Record inserted successfully"
    #con.close()  
        
          
        
        
     
def write():
    """ Writes content to the app """
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox('', ("Choose an option",'Database Info', "Search", 'Match Functions', "Database Check for Matching", "Save to Database"))

    #st.write('You selected:', page)
    #st.title("Get Data from PostgreSQL")
    name=st.sidebar.text_input("Enter the name")
    legal_id=st.sidebar.text_input("Enter legal_id")
    coun=st.sidebar.text_input("Please enter the country")
    city=st.sidebar.text_input("Enter the city")
    
    if page == 'Database Info':
        tool = st.radio('Options',('Tables','Read Tables'))
        if tool == 'Tables':
            st.dataframe(get_tables())
        elif tool == 'Read Tables':
            table_name=st.text_input("Enter the table name")
            if st.button("Read Table"):
                
                st.dataframe(read_table(table_name))
        else:
            st.subheader('Please choose a tool')
        
    if page == 'Search': 
        if st.sidebar.button("Query"):
            st.dataframe(get_query_results(name))
    
    if page == 'Match Functions':
        match_options=st.selectbox('', ("Select a Function",'Fuzzy_Match', "Soundex_Match", 'Levenshtein_Match', "Difference_Match","difflib_Match"))
        if match_options == 'Fuzzy_Match':
            st.dataframe(get_fuzzy_matches(name)[0])
            st.success(get_fuzzy_matches(name)[1])
        
        if match_options == 'Soundex_Match':
            st.info("The soundex algorithm matches similar-sounding names by converting them to the same soundex code. Every soundex code consists of a letter and three numbers, such as W252.")
            st.dataframe(get_soundex_matches(name))
            
        if match_options == 'Levenshtein_Match':
            st.info("The Levenshtein distance between two words is the minimum number of single-character changes (i.e. insertions, deletions, or substitutions) required to change one word into the other. Thus, the smaller the number of edits to transform one word to the other, the closer the words are to each other.")
            st.dataframe(get_levenshtein_matches(name))   
            
        if match_options == 'Difference_Match': 
            st.dataframe(get_difference_matches(name))
            
        if match_options == 'difflib_Match': 
            st.info("diffflib method is a tool that will take in arguments and return the closest matches to the target string.")
            st.dataframe(get_difflib_matches(name))
    
    
    if page == "Database Check for Matching":
        tools = st.selectbox('',("Select a Function",'Option-1: Check with the legal_entity_ids', "Option-2: Check with the Country",'Option-3: Check with the city', 'Option-4: Check with the individual name','Option-5: Check with all features','Option-6: Check with news data'))
        if tools == 'Option-1: Check with the legal_entity_ids':
            if st.sidebar.button("Get IDS"):
                st.dataframe(id_check(name, legal_id))
            
            if st.sidebar.button("Execute Option-1"):  
                st.success(check(name,legal_id))
        if tools == 'Option-2: Check with the Country':
            if st.sidebar.button("Get Country"):
                st.dataframe(join(name,coun))
            
            if st.sidebar.button("Execute Option-2"):    
                st.success(check2(name,coun))
        if tools == 'Option-3: Check with the city':
            if st.sidebar.button("Get City"):
                st.dataframe(join2(name,city))
            
            if st.sidebar.button("Execute Option-3"):
                st.success(check3(name,city))
            
        if tools=='Option-4: Check with the individual name':
            
            if st.sidebar.button("Get individual names"):
                st.dataframe(individual(name))
                
        if tools=='Option-5: Check with all features':
            if st.button("Check with all features"):
                st.dataframe(all_features(name,coun,city,legal_id))
        
        if tools=='Option-6: Check with news data':
            text=st.text_input("Article")
            if st.button("Run NER Model"):
                st.success(sentence(text))
            search_option=st.selectbox('', ("Choose an option",'Person Search', "Organization Search"))
            
            if search_option=='Person Search':
                st.success(person_query(text)[0])
                st.dataframe(person_query(text)[1])
            if search_option=="Organization Search":
                st.success(organization_query(text)[0])
                st.dataframe(organization_query(text)[1])

                    
                    #st.success(button_org(a))   
                    
                    
    if page == 'Save to Database':   
        save_options = st.selectbox('',("Select a Table to Save","Organization","Individual"))
        if save_options=="Organization":
            st.success(save_organization(name))
            
        if save_options=="Individual":
            st.success(save_individual(name))
        
        
        
        
      
if __name__ == "__main__":
    write()   
 


  




 
