import pandas as pd
import csv

df1 = pd.read_csv('c:\\Users\\d945607\\Desktop\\Cisco_vuln_advisory\\cisco_vunerability_report1.csv')
df1 = df1.astype(str)

df2 = pd.read_csv('c:\\Users\\d945607\\Desktop\\Cisco_vuln_advisory\\abcswitch_report1.csv')
df2 = df2.astype(str)

with open("c:\\Users\\d945607\\Desktop\\Cisco_vuln_advisory\\abcswitch_model_vunerabilities.csv", \
          "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(("Index2", "IP", "Host_name", "Serial_no", "IOS_ver", "Model", "Index1", \
    "advisoryTitle", "bugIDs", "cves", "sir", "publicationUrl"))
    for index2, row2 in df2.iterrows():
        for index1, row1 in df1.iterrows():
            if row2["IOS_ver"] in row1["productNames"]:
                writer.writerow((index2, row2["IP"], row2["Host_name"], row2["Serial_no"], \
                row2["IOS_ver"], row2["Model"], index1, row1["advisoryTitle"], row1["bugIDs"], \
                row1["cves"], row1["sir"], row1["publicationUrl"]))