import requests
H = {"User-Agent": "Joel Rajah joelrajah8@gmail.com"}
cik = "0001341439"  # Oracle
facts = requests.get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers=H).json()
for f in facts["facts"]["us-gaap"]["PaymentsToAcquirePropertyPlantAndEquipment"]["units"]["USD"][-4:]:
    acc = f["accn"].replace("-", "")
    print(f["fy"], f["fp"], f["form"], f["val"], f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/")