# raritan-rpc
This collection is to configure Raritan and ServerTech rack PDUs that are PRO2X/PX2 or newer.

## Usage
To use this collection, there is a spreadsheet in the listed files titled 'DEVICES.csv' in which the required items to list are username & password (if PDU is not new and has been previously setup), IP address, intended device name, and device location.

There is also an .env file to add the appropriate values for PDU login username and password, and the SNMPv3 username, auth-pass, and priv-pass.

After the csv file is completed with all intended devices, and the .env file has the appropriate credentials, the main.py script can be ran.
