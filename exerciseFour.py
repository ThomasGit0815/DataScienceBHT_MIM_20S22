import pandas as pd
import io
import requests

def exerciseFour():
    print('Start exercise...')

    print('read countries.csv...')
    url = "https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv"
    s = requests.get(url).content

    data = pd.read_csv(io.StringIO(s.decode('utf-8')), ',')    
    print(data.head())

    # Display some basic information as rows, columns and some basic statistical info.
    print('\nDisplay some basic information as rows, columns and some basic statistical info.')
    print(data.describe())
    

    # show the last 4 rows of the data frame.
    print('\nShow the last 4 rows of the data frame.')
    print(data[len(data)-4:])

    # Show all the row of countries who have the EURO
    print('\nShow all the row of countries who have the EURO')
    print(data.query('Currency == "EUR"'))

    # Show only name and Currency in a new data frame
    print('\nShow only name and Currency in a new data frame')
    data2 = data[["Name", "Currency"]]
    print(data2)

    # Show only the rows/countries that have more than 2000 BIP (it is in Milliarden USD Bruttoinlandsprodukt)
    print('\nShow only the rows/countries that have more than 2000 BIP (it is in Milliarden USD Bruttoinlandsprodukt)')
    print(data.query('BIP > 2000')["Name"])

    # Select all countries where with inhabitants between 50 and 150 Mio
    print('\nSelect all countries where with inhabitants between 50 and 150 Mio')
    print(data.query('People > 50000000 and People < 150000000'))

    # Change BIP to Bip
    print('\nChange BIP to Bip')
    print(data.rename(columns={"BIP": "Bip"}))

    # Calculate the Bip sum
    print('\nCalculate the Bip sum')
    print("Summe vom BIP: "+str(data.rename(columns={"BIP": "Bip"})['Bip'].sum()))

    # Calculate the average people of all countries
    print('\nCalculate the average people of all countries')
    print("Bei der Auswertung von " +  str(len(data)) + " Datensätzen, ergibt sich einen durchschnittliche Anzahl von : " + str(data['People'].mean()) + " Menschen pro Land.")

    # Sort by name alphabetically
    print('\nSort by name alphabetically')
    print(data.sort_values(by='Name', ascending=True))

    # Create a new data frame from the original where the area is changed as follows: all countries with
    # > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced!
    print('\nCreate a new data frame from the original where the area is changed as follows:')
    print('all countries with > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced!')
    data3 = data.copy()
    data3.loc[data['Area'] > 1000000, 'Area'] = "BIG"
    data3.loc[data['Area'] <= 1000000, 'Area'] = "SMALL"
    print(data3) 
    
exerciseFour()
